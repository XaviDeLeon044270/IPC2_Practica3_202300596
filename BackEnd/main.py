from flask import Flask

class MyFlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def hello_world():
            return 'Hola mundo'

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    my_app = MyFlaskApp()
    my_app.run()