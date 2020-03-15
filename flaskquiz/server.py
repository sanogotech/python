from flask import Flask
from flask import render_template
from flask import request
import model
from os import environ


app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

@app.route("/")
def home():
  return render_template("index.html")

@app.route('/result', methods=['GET', 'POST'])
def result():
  if request.method == 'POST' and len(dict(request.form)) > 0:
    userdata = dict(request.form)
    print(userdata)
    book = userdata["book"]
    print("Book Info",book)
    character = model.get_character(book)
    print("Character ",character)
    gif_url = model.get_gif(character)
    print("gifurl ",gif_url)
    return render_template("result.html", character=character, gif_url=gif_url)
  else:
    return "Sorry, there was an error."

@app.route('/verify')
def verify():
    secretmessage = str(app.config['SECRET_KEY'])

    return  '<p>' + secretmessage + '</p>'

  
if __name__ == "__main__":
  app.run()
