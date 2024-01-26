from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(12)
Bootstrap(app)

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-movie-collection.db"
db.init_app(app)

load_dotenv()

class MovieTable(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    year: Mapped[str] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[str] = mapped_column(String(5), nullable=False)
    ranking: Mapped[str] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

class RateMovieForm(FlaskForm):
    new_rating = StringField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    new_review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")

class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    movie_list = list(db.session.execute(db.select(MovieTable).order_by(MovieTable.rating)).scalars())
    for i in range(len(movie_list)):
        movie_list[i].ranking = len(movie_list) - i
    db.session.commit()
    return render_template("index.html", movie_list=movie_list)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    rate_form = RateMovieForm()
    movie_id = request.args.get("id")
    if rate_form.validate_on_submit():
        record = db.session.execute(db.select(MovieTable).where(MovieTable.id == movie_id)).scalar()
        record.rating = float(request.form['new_rating'])
        record.review = request.form['new_review']
        db.session.commit()
        return redirect(url_for('home'))
    if db.session.execute(db.select(MovieTable).where(MovieTable.id == movie_id)).scalar() is None:
        res = requests.get(url=f"{os.environ['API_GET']}/{movie_id}", params={"api_key": os.environ["API_KEY"]})
        res.raise_for_status()
        data = res.json()
        new_movie = MovieTable(
            id=data['id'],
            title=data['original_title'],
            year=data['release_date'],
            description=data['overview'],
            img_url=f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()
        return render_template("edit.html", form=rate_form, movie_title=data['original_title'])
    else:
        record = db.session.execute(db.select(MovieTable).where(MovieTable.id == movie_id)).scalar()
        return render_template("edit.html", form=rate_form, movie_title=record.title)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    record = db.session.execute(db.select(MovieTable).where(MovieTable.id == movie_id)).scalar()
    db.session.delete(record)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddMovieForm()
    if add_form.validate_on_submit():
        params = {
            "api_key": os.environ["API_KEY"],
            "language": "en-US",
            "query": request.form["title"]
        }
        res = requests.get(url=os.environ['API_SEARCH'], params=params)
        res.raise_for_status()
        data = res.json()['results']
        return render_template("select.html", movies=data)
    return render_template("add.html", form=add_form)


if __name__ == '__main__':
    app.run(debug=True)
