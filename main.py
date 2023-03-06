from flask import Flask, url_for,render_template, jsonify
import datetime
app = Flask(__name__)

category = ['For You', 'Politics', 'National', 'International'
            ]
blogs = [
    {'image': 'static/image/images.jpg',
     'post_title': 'Post 01',
     'post_des': 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Iste molestiae voluptatem voluptate totam quod adipisci porro perferendis doloribus, distinctio inventore.',
     'id': 1,
     'link': "#"
     },
    {'image': 'static/image/images.jpg',
     'post_title': 'Post 02',
     'post_des': 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Iste molestiae voluptatem voluptate totam quod adipisci porro perferendis doloribus, distinctio inventore.',
     'id': 2,
     'link': "#"
     },
    {'image': 'static/image/images.jpg',
     'post_title': 'Post 03',
     'post_des': 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Iste molestiae voluptatem voluptate totam quod adipisci porro perferendis doloribus, distinctio inventore.',
     'id': 3,
     'link': "#"
     },
    {'image': 'static/image/images.jpg',
     'post_title': 'Post 04',
     'post_des': 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Iste molestiae voluptatem voluptate totam quod adipisci porro perferendis doloribus, distinctio inventore.',
     'id': 4,
     'link': "#"
     }
]




@app.route("/api/blogs")
def blog_home():
    return jsonify(blogs)

@app.route("/")
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html", blogs=blogs, category=category,current_year=current_year)
@app.route("/write")
def write():
    return render_template('write_form.html')
app.run(debug=True)
