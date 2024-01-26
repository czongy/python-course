from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import choice

app = Flask(__name__)

class Base(DeclarativeBase):
  pass

##Connect to Database
db = SQLAlchemy(model_class=Base)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random")
def random():
    cafes = list(db.session.execute(db.select(Cafe)).scalars())
    random_cafe = choice(cafes)
    # return jsonify(cafe={
    #     'name': random_cafe.name,
    #     'map_url': random_cafe.map_url,
    #     'img_url': random_cafe.img_url,
    #     'location': random_cafe.location,
    #     'seats': random_cafe.seats,
    #     'has_toilet': random_cafe.has_toilet,
    #     'has_wifi': random_cafe.has_wifi,
    #     'has_sockets': random_cafe.has_sockets,
    #     'can_take_calls': random_cafe.can_take_calls,
    #     'coffee_price': random_cafe.coffee_price,
    # })
    return jsonify(cafe=random_cafe.to_dict())


@app.route('/all')
def all_cafe():
    cafes = db.session.execute(db.select(Cafe)).scalars()
    cafe_list = []
    for cafe in cafes:
        cafe_list.append(cafe.to_dict())
    return jsonify(cafe=cafe_list)


@app.route('/search')
def search():
    loc = request.args.get("loc").title()
    get_cafe = db.session.execute(db.select(Cafe).filter_by(location=loc)).scalars()
    cafe_list = []
    for cafe in get_cafe:
        cafe_list.append(cafe.to_dict())
    if not cafe_list:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
    return jsonify(cafe=cafe_list)


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form["name"],
        map_url=request.form["map_url"],
        img_url=request.form["img_url"],
        location=request.form["location"],
        seats=request.form["seats"],
        has_toilet=bool(request.form["has_toilet"]),
        has_wifi=bool(request.form["has_wifi"]),
        has_sockets=bool(request.form["has_sockets"]),
        can_take_calls=bool(request.form["can_take_calls"]),
        coffee_price=request.form["coffee_price"],
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={'Success': 'Successfully added the new cafe.'})

## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update(cafe_id):
    new_price = request.args.get("new_price")
    get_cafe = db.session.execute(db.select(Cafe).filter_by(id=cafe_id)).scalar()
    if not get_cafe:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})
    else:
        get_cafe.coffee_price = new_price
        db.session.commit()
        return jsonify({"Success": "Successfully updated the price."})

## HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>")
def delete(cafe_id):
    api_key = request.args.get("api_key")
    if api_key == "TopSecretAPIKey":
        get_cafe = db.session.execute(db.select(Cafe).filter_by(id=cafe_id)).scalar()
        db.session.delete(get_cafe)
        db.session.commit()
        return jsonify({"Success": "Successfully deleted the cafe."})
    else:
        return jsonify({"error": "Sorry, that's not allowed. Make sure you have the correct api_key."})


if __name__ == '__main__':
    app.run(debug=True)
