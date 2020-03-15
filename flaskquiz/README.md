# Lib
pip install python-dotenv  (for .env)

# Flask  Quiz  sample


##  Components
First, let’s go over the basics of how most web apps are broken down.

* Model: This is the main Python backend logic of your app. All your classes, functions, etc. live here. 
Our model is currently contained in model.py, though in other places you may see a folder containing multiple Python classes and files.

* View: This is our beautiful HTML/CSS interface — what the user sees. 
Our views are currently contained in the templates folder, which contains two empty HTML files: index.html and result.html. 
There is also the static folder, which contains assets such as our style.css file.

* Controller: The controller goes between the model and view, calling on the model for backend computations and delivering results to the view.
 Our controller lives in server.py.