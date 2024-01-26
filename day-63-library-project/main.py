from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String

app = Flask(__name__)

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[str] = mapped_column(String(5), nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = list(db.session.execute(db.select(Book).order_by(Book.title)).scalars())
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        # book = {
        #     "title": request.form.get("title"),
        #     "author": request.form.get("author"),
        #     "rating": request.form.get("rating")
        # }
        # all_books.append(book)
        new_book = Book(
                title=request.form.get("title"),
                author=request.form.get("author"),
                rating=request.form.get("rating")
                )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit/<int:book_id>", methods=["POST", "GET"])
def edit_rating(book_id):
    query_book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    if request.method == "POST":
        query_book.rating = request.form.get("new_rating")
        db.session.commit() 
        return redirect(url_for('home'))
    return render_template("edit.html", book=query_book)


@app.route("/delete/<int:book_id>")
def delete(book_id):
    query_book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(query_book)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

