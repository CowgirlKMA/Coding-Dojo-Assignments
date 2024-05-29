
from flask_app import app
#flask_app is a package what we are doing here is importing the app

from flask_app.controllers import dojos
#remember to import your controller files here
from flask_app.controllers import ninjas

if __name__ == "__main__":
    app.run(debug=True)