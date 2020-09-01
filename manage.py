from flask import Flask
from flask_cors import *

from Menu.MenuBlue import menu
from FakerData.FakerDataBlue import faker
from SecretCode.SecretCodeBlue import secretCode
from Calculate.CalculateBlue import calc

app = Flask(__name__)

CORS(app, supports_credentials=True)

# app注册蓝图
app.register_blueprint(menu, url_prefix='/api/v1')
app.register_blueprint(faker, url_prefix='/api/v1')
app.register_blueprint(secretCode, url_prefix='/api/v1')
app.register_blueprint(calc, url_prefix='/api/v1')


@app.route('/')
def homepage():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
