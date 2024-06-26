## Flask Application Design

### HTML Files

**index.html:**
- Main page of the website.
- Displays various Mandarin lessons with images and text descriptions.
- Includes navigation links to other pages.

**lessons/<lesson_name>.html:**
- Individual lesson pages.
- Provides in-depth explanations of each Mandarin lesson, including grammar points, vocabulary, and exercises.
- Contains interactive exercises using images to reinforce learning.
- Includes links to previous and next lessons.

### Routes

**@app.route('/')**
- Home page route.
- Renders the index.html template, displaying the main page of the website.

**@app.route('/lessons/<lesson_name>')**
- Lesson page route.
- Renders the template for the specified lesson, displaying its content and exercises.
- Dynamically generates the URL based on the lesson name, allowing for easy navigation between lessons.