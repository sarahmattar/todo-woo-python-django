# todo-woo-python-django

This is a Todo app written in Python using the Django framework.

## Why did I code this?

This was a coursework project for Nick Walter's UDEMY course about
[creating Python and Django applications](https://www.udemy.com/course/django-3-make-websites-with-python-tutorial-beginner-learn-bootstrap/).

## What I learned From This

In terms of app functionality, I learned how to display tasks assigned to a user
and update their state (from no given priority level to Important) and mark them
as Completed.

Conditional rendering of the data, based on the boolean value of Completed,
shows each task on their own respective path (`/current` and `/completed`).

### Django

I've gotten pretty good at creating views, querying data from an SQL database,
and passing that data into a Dictionary for rendering the view. For the UI, I
created Template files and passed logic into them. Most of this was based on
conditionally rendering data based on user authentication, and I found that more
things than you realize need to be buried in form submissions to trigger a POST
request (looking at you, logout button!).

### UI/Front End Styling

Styling for the site was done in [Bootstrap 4](https://getbootstrap.com/), so
this has really given me a chance to beef up my Bootstrap skills (especially the
parts of it that don't inherently make sense). I used one of the Bootstrap
examples for creating a cover page and tailored the CSS to fit the image chosen
for the cover image.

### Deployment/DevOps

On my own, I learned how to deploy a Django/Python app to Heroku, and set
environment variables so that my secret key was secure and other
environment-specific information for the development or production environments.
You can visit the deployed app
[here](https://whispering-bayou-34998.herokuapp.com/).

## Installation

Installation requires you to have Python 3.8 and Django 3 installed.

Install and create a virtual environment using virtualenv:

`pip install virtualenv `

`virtualenv todowoo-env`

(If, for some reason, your virtual environment doesn't get activated when it is
created, or you get interrupted/close terminal windows/etc., you can run
`source todowoo-env/bin/activate` from the same command line to reactivate it.)

Once inside the virtual environement, to deactivate it, simply type
`deactivate`.

Install the requirements:

`pip install -r requirements.txt`

You should be good to go!
