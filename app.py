from flask import Flask, request, render_template
from stories import Story
from flask_debugtoolbar import DebugToolbarExtension

print(Story)
app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Shows Madlibs form"""
    return render_template("home.html")

@app.route('/story')
def complte_story():
    """Shows story with blanks filled in"""
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]
    return render_template("story.html", place=place, noun=noun, verb=verb, adjective=adjective,
        plural_noun=plural_noun)