from flask import Flask, render_template
import requests

app = Flask(__name__)

res = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
posts = res.json()


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/<id_num>')
def blog_post(id_num):
    return render_template("post.html", post=posts[int(id_num)-1])


if __name__ == "__main__":
    app.run(debug=True)
