HarvardX CS50W: Web Programming with Python and JavaScript

This project is a multilingual and multi-currency e-commerce Python Djnago web project.
The project's video: 

Justification
I consider that this project meets all the expectations raised in the assignment of the final project, as it is a web platform that implements most of the concepts and techniques taught in the course.

The whole application is based on the Django framework, which allowed managing user authentication, database models, http requests, static files and the html page rendering.

On the other hand, user interface was designed with bootstrap, along with additional javascript libraries

This project took me longer than I expected, between figuring out how to do things and, well, life. I tried to implement everything I learned that I could use, but I also found other ways or new ways just investigating and searching how to make the ideas I had. I'm pretty satisfied with what I made overall, but I see many ways of improvement.

Final project
My final project is E-commerce website. Users are able to register, add items to cart, subscribe to emails and send emails, write comments. They can also search using the search bar.

The project was built using Django as a backend framework and JavaScript/HTML/CSS as a frontend programming language. All generated information are saved in database (SQLite by default).

All webpages of the project are mobile-responsive.

Before running this project you need intall below list apps and packages
Installation:
Install Python 3.7 or above -> https://www.python.org/

Install project dependencies by running pip install -r requirements.txt. Dependencies include Django and Pillow module that allows Django to work with images.
Make and apply migrations by running python manage.py makemigrations and python manage.py migrate.
Create superuser with python manage.py createsuperuser. This step is optional.
Go to website address and register an account.
Web Template of this prpoject:  https://colorlib.com/wp/template/e-shop/
 
Files and directories:
mysite - main application directory.
home/static/contains all static content.
    /css contains compiled CSS file and its map.
    /js - all JavaScript files used in project.
    /img - all base pictures of the project
    /fonts - all fonts
home/templates - contains all application templates.
admin.py - admin classes and re-registered User model.
models.py contains all models that have been used in the project. 
urls.py - all application URLs.
views.py respectively, contains all application views.
media - pictures of items are stored here after bein uploaded

Requirements
The final project is your opportunity to design and implement a dynamic website of your own. So long as your final project draws upon this course’s lessons, the nature of your website will be entirely up to you, albeit subject to the staff’s approval.

In this project, you are asked to build a web application of your own. The nature of the application is up to you, subject to a few requirements:

*Your web application must utilize at least two of Python, JavaScript, and SQL.
*Your web application must be mobile-responsive.
*In README.md, include a short writeup describing your project, what’s contained in each file you created or modified, and (optionally) any other additional information the staff should know about your project.
*If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to requirements.txt!
*Beyond these requirements, the design, look, and feel of the website are up to you!