from flask import Flask, url_for, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

def cv():
    return redirect('cv.html')



