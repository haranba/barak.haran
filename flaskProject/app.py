from flask import Flask, render_template, request, session, Blueprint, flash, redirect
import mysql.connector

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

assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         static_url_path='/assignment10',
                         template_folder='templates')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='barak123',
                                         database='assigment10')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@app.route('/assignment10', methods=['GET', 'POST'])
def assignment10():
    return render_template('InsertUpdateDelete.html')


@app.route('/users', methods=['GET', 'POST'])
def users():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)


@app.route('/INSERT', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        email = request.form['email']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        query = "INSERT INTO users(email, firstname, lastname) VALUES ('%s', '%s', '%s')" % (
            email, firstname, lastname)
        interact_db(query=query, query_type='commit')
        return redirect('/users')
    return render_template('assignment10.html', req_method=request.method)


@app.route('/DELETE', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'GET':
        id2 = request.args['id']
        query = "DELETE FROM users Where id='%s';" % id2
        interact_db(query=query, query_type='commit')
        return redirect('/users')
    return render_template('assignment10.html', req_method=request.method)


@app.route('/UPDATE', methods=['GET', 'POST'])
def update_user():
    if request.method == 'GET':
        email = request.form['email']
        id2 = request.args['id']
        query = "UPDATE users SET email = %s WHERE id= %s" % (email, id2)
        interact_db(query=query, query_type='commit')
        return redirect('/users')
    return render_template('assignment10.html', req_method=request.method)
