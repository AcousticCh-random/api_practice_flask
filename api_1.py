#!/usr/bin/env python3
from flask import Flask, url_for, render_template
#import Flask Class from flask module
from markupsafe import escape 
#escapes user provided values in the html to prevent injection attacks

app = Flask(__name__)
#application object/flask instance

@app.route("/")
def index():
	return render_template("contactme.html")
	
@app.route("/contact/")
def contactme():
	return render_template("contactme.html")
#with name  escaped the user cant inject <script> into html

@app.route("/user/<username>", methods = ["GET", "POST"])
def show_user_profile(username):
	return f"Welcome to your account profile {escape(username)}!"
	
@app.route("/post/<int:post_id>")
def show_post(post_id):
	return f"Post {post_id}"
	
@app.route("/path/<path:subpath>")
def show_subpath(subpath):
	return f"subpath {escape(subpath)}"
	
with app.test_request_context():
	print(url_for("index"))
	print(url_for("contactme"))
	print(url_for("show_user_profile", username = "random"))
	print(url_for("show_post", post_id = "7777"))
	print(url_for("show_subpath", subpath = "thisPath"))

app.run()
