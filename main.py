from flask import Flask, redirect, url_for, session, request, render_template
from settings import *
from db_scripts import *



app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = getUser()
    return render_template('about.html', user=user)

@app.route('/post/category/<category_name>', methods=['POST', 'GET'])
def postCategory(category_name):
    category_id = getIdByCategory(category_name)
    
    if request.method == 'GET':
        posts = getPostsByCategory(category_name)
        
    if request.method == 'POST':
        addPost(request.form['category_id'], request.form['post'])
        posts = getPostsByCategory(category_name)

    return render_template('post_category.html', category_name=category_name, posts=posts, category_id=category_id)

@app.route('/post/view')
def postView():
    return '<h1>post View</h1>'

@app.route('/about')
def about():
    return '<h1>About</h1>'


# app.add_url_rule('/', 'index', index)
# app.add_url_rule('/index', 'index', index)

# app.add_url_rule('/post/category', 'postCategory', postCategory)
# app.add_url_rule('/post/view', 'postView', postView)

# app.add_url_rule('/about', 'about')

app.config['SECRET_KEY'] = 'VeryStrongKey'

if __name__ == '__main__':
    app.run(debug=True, port=5000)