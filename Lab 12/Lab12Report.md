Lab: Creating HTML Interfaces with Flask 

1.  Install Flask and create a first simple application. 

Run Flask in debug mode. This means you will access your local server at 127.0.0.1
Create a single route for “/”.
Respond to a request for this route by outputting “Welcome to {your name}’s web site!”

# Create a simple HTML Flask application that displays a welcome message
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return ("Welcome to Kazman's really boring web page")

if __name__ == '__main__':
    app.run(debug=True)

2. When creating HTML pages in the Flask framework, they need to be put in a “templates” subdirectory.
Create an index.html page that allows a user to select a link that takes them to a login page.
Create a login.html page--a simple form with a text field for a username, a password field for a password, and a submit button. Create a route for /login. The function for login should present the form.
When this form is submitted, process the data and take the user to a success page. You can hard-code a dictionary of userIDs and passwords such as:

USERS = {"port": "port123",
        	  "kazman": "kazman123"}

ON YOUR OWN: 3. Create a simple Flask application to retrieve memes from https://meme-api.com/gimme/wholesomememes.  To get the memes you will need to issue a requests.request("GET", url) command.

Present the meme and the meme source (subreddit) to the user. Refresh the meme every 10 seconds.  You can accomplish this by including the following <meta> tags in the <head> of your HTML page.
<head>
   <title>Memes'R'Us</title>
   <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=0.8">
   <meta http-equiv="refresh" content="10; url=http://127.0.0.1:5000" />
</head>


# Application that allows a user to login.  If login credentials are correct,
# the user is welcomed.  If not, an error message is displayed.
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userid = request.form['username']
        password = request.form['password']
        # Replace this with your actual authentication logic
        if USERS.get(userid) == password:
            return redirect(url_for('success', username=userid))
        else:
            return "Sorry bud.  Try again."
    else:
        return render_template('login.html')

@app.route('/success/<username>')
def success(username):
    return render_template('success.html', username=username)

USERS = {"port": "port123",
        "kazman": "kazman123"}


if __name__ == '__main__':
    app.run(debug=True, port=5001)

ON YOUR OWN: 4. Create a “skeleton” of your quiz game using Flask. There are several approaches to this:
i.  Create “mock up” pages for your quiz game and modify Ex 2 above to navigate to all these pages (e.g. index.html links to “take the quiz” page). 
ii. Another approach  is to ask AI “create a skeleton for a Flask application for a quiz game” and adapt this to your vision of the game. 
iii. Another approach is to give AI your quiz.py from Assignment 1 and prompt “create a Flask application for this quiz game <add your quiz.py code here>”

What are the benefits and disadvantages of using a skeleton? 
Discuss the pros and cons of the approach you used (i,ii,iii) and ultimately if it was better than creating the initial quiz game web application from scratch.

