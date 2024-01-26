from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # all_data = db.session.execute(db.select(User)).scalars()
    # for data in all_data:
    #     db.session.delete(data)
    #     db.session.commit()
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        check_email = db.session.execute(db.select(User).filter_by(email=request.form["email"])).scalar()
        if not check_email:
            new_user = User(
                email=request.form["email"],
                password=generate_password_hash(request.form["password"], method="pbkdf2:sha256", salt_length=8),
                name=request.form["name"]
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("secrets"))
        else:
            flash("You've signed up with that email. Login instead.")
            return redirect(url_for("login"))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = db.session.execute(db.select(User).filter_by(email=request.form["email"])).scalar()
        check_password = request.form["password"]
        if not user or not check_password_hash(user.password, check_password):
            flash('Please check your login details and try again.')
            return redirect(url_for("login"))
        else:
            login_user(user)
            return redirect(url_for("secrets"))
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", user_name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
def download():
    if not current_user.is_authenticated:
        return login_manager.unauthorized()
    return send_from_directory("static/files/", "cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
