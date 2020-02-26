from flask import Flask, render_template, flash, redirect, url_for, session, request,logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from data import Articles
from flaskext.mysql import MySQL


# start app here 

app1 = Flask(__name__)

app1.debug = True

Articles = Articles()
mysql = MySQL()
mysql.init_app(app1)

@app1.route('/')
def index():
    return render_template('home.html')

@app1.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app1.route('/article/<string:id>/')
def article(id):    
    return render_template("article.html", id=id)



@app1.route("/about")
def about():
    return render_template("about-us.html")




#Here Form Register 

class RegisterForm(Form):
    name = StringField('Name',[validators.Length(min=1,max=50)])
    username = StringField('Username',[validators.Length(min=4,max=25)])
    email = StringField('Email',[validators.Length(min=4,max=25)])
    password = PasswordField('Password', [ validators.DataRequired(),validators.EqualTo('confirm',message ='passwords do not match')])
    confirm = PasswordField('Confirm password')

if __name__=="__main__":
    app1.run()


