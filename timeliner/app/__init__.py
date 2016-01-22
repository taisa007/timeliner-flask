from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/hello', methods=['GET'])
def hello_view():
    username = request.form['username']
    # username = 'test'
    return render_template('hello.html', username=username)

if __name__ == '__main__':
    app.run()
