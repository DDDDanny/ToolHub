from flask import Flask

from FakerData.FakerDataBlue import faker

app = Flask(__name__)

# app注册蓝图
app.register_blueprint(faker)


@app.route('/')
def homepage():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
