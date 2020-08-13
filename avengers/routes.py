from avengers import app
from flask import render_template, request, redirect, url_for

from july_blog.forms import UserInfoForm, BlogPostFrom, LoginFrom

#import form route
from avengers.forms import UserInfoForm, BlogPostFrom

# home route
@app.route('/')
def home():
    name = "Avenger"

    return render_template("a_home.html", name=name)


# register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserInfoForm()
    if request.method == 'POST' and form.validate():
        # Get information from 'POST' request
        username = form.username.data
        password = form.password.data 
        email = form.email.data 
        phone = form.phone.data
        print("\n", username, password, email, phone)

    return render_template("a_register.html", form=form)

# creat post route
@app.route('/createposts', methods=['GET', "POST"])
def createposts():
    form = BlogPostFrom()
    if request.method == 'POST' and form.validate():
        title = form.title.data
        content = form.content.data
        print("\n", title, content)
    return render_template('a_createposts.html', form=form)