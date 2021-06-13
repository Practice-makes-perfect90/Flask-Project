from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/josephlopez/Desktop/flask_blog-master/blog.db'

db = SQLAlchemy(app)
##################################################Classes###############################################################
class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)

    #this is a test I might have to make a new class and database 
    #email = db.Column(db.String(50))
    #name = dbColumn(db.String(50))
#maybe change this 
#class emailList(db.Model):
class email_list(db.Model):
    email = db.Column(db.String(50), primary_key=True)
    name  = db.Column(db.String(50))
########################################################################################################################
@app.route('/')
def index():
    # Posts is getting it's infromation from the Blogpost class and ordering the information by date posted
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()

    return render_template('index.html', posts=posts)


@app.route('/jinjaPractice')
# This is for me to practice my jinja skills 
def jinjaPractice():
   

    my_name = "Joseph"

    age = 30

    langs = ["Python","JavaScript","Bash"]

    return render_template('jinjaPractice.html',my_name=my_name,langs=langs,age=age)



@app.route('/about')
def about():
    #Links to the about page
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/addpost', methods=['POST'])
def addpost():
    # This function is utilizing the request extension 
    # And it is getting the information from the add.html html post form
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/register')
def register():

    return render_template('register.html')
# FINISH THIS 
@app.route('/registerUser', methods=['POST'])
def registerUser():
    #This function is very similar to add post but instead it will register a list of names and email to a blog
    name = request.form['name']
    email = request.form['email']
    
    # maybe change this back V 
    #user = emailList(name=name,email=email)
    user= email_list(name=name,email=email)
    db.session.add(user)
    db.session.commit()

    return render_template('register.html')
    
if __name__ == '__main__':
    db.create_all()
    app.run(port=9999,debug=True,host="127.0.0.1")

