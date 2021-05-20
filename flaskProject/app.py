from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('mainPage.html')


@app.route('/cv')
def cv():
    return render_template('cv.html')


@app.route('/contactList')
def contactlist():
    return render_template('contactList.html')


@app.route('/message')
def message():
    return render_template('Message.html')


@app.route('/assignment8')
def assignment8():
    return render_template('assignment8.html')


@app.route('/hobbies')
def hobbies():
    currentUser = 'barak'
    return render_template('assignment8.html',
                           name=currentUser,
                           travel={'South Island', 'New Zealand', 'Paris'},
                           sport={'basketball', 'soccer', 'tennis'},
                           movie={'titanic', 'superman'})


@app.route('/block')
def block():
    currentUser = 'barak'
    return render_template('block.html',
                           name=currentUser,
                           travel={'South Island', 'New Zealand', 'Paris'},
                           sport={'basketball', 'soccer', 'tennis'},
                           movie={'titanic', 'superman'})


if __name__ == '__main__':
    app.run(debug=True)
