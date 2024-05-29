from flask import Flask
from flask_bcrypt import Bcrypt


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "e2b341cbbefda9007f17c097fb08b3380fa2786184d3c779544b46f21eb7cf35"