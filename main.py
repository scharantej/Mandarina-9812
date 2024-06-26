
from flask import Flask, render_template

app = Flask(__name__)

LESSONS = {
    'lesson1': {
        'title': 'Lesson 1: Getting Started',
        'image': 'path/to/image1.jpg',
        'content': 'Lesson 1 content...'
    },
    'lesson2': {
        'title': 'Lesson 2: Basic Grammar',
        'image': 'path/to/image2.jpg',
        'content': 'Lesson 2 content...'
    },
    # ... More lessons
}

@app.route('/')
def index():
    return render_template('index.html', lessons=LESSONS)

@app.route('/lessons/<lesson_name>')
def lesson(lesson_name):
    lesson = LESSONS.get(lesson_name)
    if lesson is None:
        return render_template('error.html'), 404
    return render_template('lesson.html', lesson=lesson)

if __name__ == '__main__':
    app.run(debug=True)
