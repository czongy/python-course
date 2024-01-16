from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests
import smtplib
import os

app = Flask(__name__)
load_dotenv()

res = requests.get(url="https://api.npoint.io/88c2c1f644ef334058be")
blog_posts = res.json()

@app.route("/")
def home():
    return render_template("index.html", blog_posts=blog_posts)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        send_email(name, email, phone, message)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route("/post/<id_num>")
def post_page(id_num):
    return render_template("post.html", indiv_post=blog_posts[int(id_num)-1])

def send_email(name, email, phone, message):
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=os.environ['USER'], password=os.environ['PASS'])
    connection.sendmail(from_addr=os.environ['USER'],
                        to_addrs=os.environ['TO_EMAIL'],
                        msg=f"Subject:Message\n\n{name}\n{email}\n{phone}\n{message}")

if __name__ == "__main__":
    app.run(debug=True)

