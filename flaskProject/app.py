from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = '123'


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


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    username = ''
    MyUsers = [
        {'id': 1, 'email': "michael.lawson@reqres.in", 'firstname': "Michael", 'lastname': "Lawson"},
        {'id': 2, 'email': "lindsay.ferguson@reqres.in", 'firstname': "Lindsay", 'lastname': "Ferguson"},
        {'id': 3, 'email': "tobias.funke@reqres.in", 'firstname': "Tobias", 'lastname': "Funke"},
        {'id': 4, 'email': "byron.fields@reqres.in", 'firstname': "Byron", 'lastname': "Fields"},
        {'id': 5, 'email': "george.edwards@reqres.in", 'firstname': "George", 'lastname': "Edwards"},
        {'id': 6, 'email': "rachel.howell@reqres.in", 'firstname': "Rachel", 'lastname': "Howell"}
    ]
    firstname = ''
    if request.method == 'GET':
        if 'firstname' in request.args:
            firstname = request.args['firstname']
    elif request.method == 'POST':
        if 'username' in request.form:
            username = request.form['username']
            session['LoggedIn'] = True
            session['username'] = username
        else:
            session['LoggedIn'] = False
            session['username'] = ''
            username = ''
    return render_template('assignment9.html',
                           MyUsers=MyUsers,
                           username=username,
                           firstname=firstname,
                           request_method=request.method)


@app.route('/my_Hobbies')
def my_Hobbies():
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
