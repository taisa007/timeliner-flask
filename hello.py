from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_workld():
    return "hello world"

if __name__ == '__main__':
    app.run()
