from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author':'Corey',
        'title':'Blog Post 1',
        'content':'First Post content',
        'date_posted':'March 29, 2022'
    },
    {   'author':'jim',
        'title':'Blog Post 2',
        'content':'Second Post content',
        'date_posted':'March 30, 2022'
    }
    ]

@app.route("/index")
def index():
    return render_template('index.html', posts=posts)

@app.route("/aboutus")
def about():
    return render_template('aboutus.html',title='About')



if __name__== '__main__':
     app.run(debug=True)


