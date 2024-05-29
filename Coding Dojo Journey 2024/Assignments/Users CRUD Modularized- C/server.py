from flask_app import app
#flask_app is a package, it lives in the __init__.py file, what we are doing here is importing the app

from flask_app.controllers import user_controller
#remember to import your controllers here

if __name__ == "__main__":
    app.run(debug=True)
