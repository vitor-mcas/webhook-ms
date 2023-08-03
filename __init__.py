import os

from flask import Flask, request

# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return 'Hello, Docker!'
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'webhook-ms.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def first_msg():
        return 'Hello, World!'
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    @app.route('/faceme', methods=['POST'])
    def receive():
        if request.method == 'POST':
            try:
                print(request.data)
            except:
                return 'Something wrong'
            return 'OK'
    
    return app

#http://10.10.10.203:5000