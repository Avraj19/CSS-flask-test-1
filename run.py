# First import flack
from flask import Flask, render_template


app = Flask(__name__)



@app.route("/")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

# This runs the app (if in main)
# (debug=True) is there for devs making change
# So when a change is made is happen immediately
# So you don't have to constantly restart your server
if __name__ == "__main__":
    app.run(debug=True)
