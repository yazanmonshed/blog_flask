from flask import Flask, render_template
from data import Articles
# start app here 

app1 = Flask(__name__)

app1.debug = True
Articles = Articles()


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


if __name__=="__main__":
    app1.run()


