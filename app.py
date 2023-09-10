# DONE BY Roman Kovalchyk
# Connection to database is added_ version 2
# Getting data from the database for /menu endpoint
import json

from flask import Flask, request, session, redirect, url_for, render_template
from flask import request
from fanctions import SQLiteDB
from fanctions import dict_factory
app = Flask(__name__)
app.secret_key = 'f23419!hj'


@app.route('/')
def start_page():  # put application's code here
    if 'user' in session:
        return f'<h1>Hello, {session["user"]}</h1>'
    return f'<h1>Welcome to our order food app! Please, login!</h1>'




@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if 'user' in session:
        user_id = session.get("user")
        order_status = 0
        list_of_orders = []
        with SQLiteDB("dish.db") as db:
            orders = db.select_from('Orders', ['*'], {'user':user_id, 'Status':order_status})
            for i in range(0, len(orders)):
                order = orders[i]
                dishes = db.db_row_query(f'select * from ordered_dishes join Dishes on ordered_dishes.Dish_id = Dishes.id where ordered_dishes.ordid = {order["order_id"]}', fetch_all=False)
                list_of_orders.append(dishes)
    return render_template('cart.html', user=session["user"], orders=list_of_orders)





@app.route('/cart/order', methods=['GET', 'POST'])
def cart_order():
    return '<h1>Cart/order endpoint</h1>'


@app.route('/cart/add', methods=['PUT', 'POST'])
def cart_add():
    form_data = request.form.get('dish_id')
    with SQLiteDB("dish.db") as db:
        #db.update_row('Dishes', {'Status': 0}, {'id': 1})
        db.update_row('Dishes', {'Status': 0}, {'id': form_data})


    return f'<h1>Cart/add endpoint {form_data}</h1>'


@app.route('/user', methods=['GET', 'PUT', 'POST', 'DELETE'])
def user():  # put application's code here
    return '<h1>User endpoint</h1>'


@app.route('/user/register', methods=['GET', 'POST'])
def user_reg():
    with SQLiteDB("dish.db") as db:
        if request.method == 'POST':
            data = request.form.to_dict()
            db.insert_into('User', data)
        data = db.select_from('User', ['*'])


    return render_template('register.html', info=str(data))


@app.route('/user/signin', methods=['GET', 'POST'])
def user_signin():
    with SQLiteDB("dish.db") as db:
        message = "Please, enter your e-mail and password!"
        if request.method == 'POST':
            info = request.form.to_dict()
            username = info.get('Username')
            password = info.get('Password')

            data = db.select_from('User', ['*'], {'Username': username, 'Password': password})
            if not data:
                message = "No users found! Please, check your date or register!"
            else:
                session['user'] = username
                return redirect(url_for('start_page'))

    return render_template('signin.html', msg=str(message))


@app.route('/user/logout', methods=['POST', 'GET'])
def logout():
    if request.method == 'POST':
        if request.form.get("btn1"):
            #removing the session
            session.clear()


    return render_template('logout.html')


@app.route('/user/restore', methods=['POST', 'GET'])
def restore_pass():
    return '<h1>user/restore endpoint</h1>'


@app.route('/user/orders/', methods=['GET'])
def orders():
    return '<h1>user/orders endpoint</h1>'


@app.route('/user/orders/<order_id>', methods=['GET'])
def order_id(order_id: int):
    return f'<h1>user/orders endpoint with {order_id}</h1>'


@app.route('/user/address', methods=['GET', 'POST'])
def user_address():
    return '<h1>user/address endpoint</h1>'


@app.route('/user/address/<id>', methods=['GET', 'PUT'])
def user_addr(id: int):
    return f'<h1>user/address of {id} user endpoint</h1>'


# Connection for database
@app.route('/menu', methods=['GET', 'POST'])
def menu():
    with SQLiteDB("dish.db") as db:
        if request.method == 'POST':
            data = request.form.to_dict()
            db.insert_into('Dishes', data)
        data = db.select_from('Dishes', ['*'])

    return render_template('menu.html', info=str(data))


@app.route('/menu/<cat_name>/', methods=['GET'])
def cat_name(cat_name: int):
    with SQLiteDB("dish.db") as db:
        #if request.method == 'POST':
           #data = request.form.to_dict()
            #db.insert_into('Category', data)
        data = db.select_from('Dishes', ['*'], {'Category': cat_name})
        #html_forms = f"""

           #{str(data)}
          # """

    return render_template('first_course.html', info=data)



@app.route('/menu/<cat_name>/<dish>', methods=['GET'])
def dish(cat_name: str, dish: str):
    return f'<h1>menu/{cat_name} and {dish} endpoint</h1>'


@app.route('/menu/<cat_name>/<dish>/review', methods=['POST'])
def dish_review(cat_name: str, dish: str):
    return f'<h1>menu/{cat_name} and {dish} and review endpoint</h1>'


@app.route('/menu/search', methods=['GET', 'POST'])
def menu_search():
    return '<h1>menu/search endpoint</h1>'


# endpoints for Admin pannel
# admin [GET]
@app.route('/admin', methods=['GET'])
def admin():
    return '<h1>admin endpoint</h1>'


# admin/dishes [GET, POST]

@app.route('/admin/dishes', methods=['GET', 'POST'])
def admin_dishes():
    return '<h1>admin/dishes endpoint</h1>'


# admin/categories [GET, PUT, POST]
@app.route('/admin/categories', methods=['GET', 'POST', 'PUT'])
def admin_categs():
    return '<h1>admin/categories endpoint</h1>'


# admin/categories/<category_id> [GET, PUT, DELETE, POST]
@app.route('/admin/categories/<category_id>/', methods=['GET', 'PUT', 'DELETE', 'POST'])
def admin_cat_id(category_id: int):
    return f'<h1>admin/categories/{category_id} endpoint</h1>'


# admin/orders [GET]
@app.route('/admin/orders', methods=['GET'])
def admin_orders():
    return '<h1>admin/orders endpoint</h1>'


# admin/orders/<order_id> [GET, PUT]
@app.route('/menu/<order_id>/', methods=['GET', 'PUT'])
def menu_order(order_id: int):
    return f'<h1>menu/order_id{order_id} endpoint</h1>'


# admin/search [GET]
@app.route('/admin/search', methods=['GET'])
def admin_search():
    return '<h1>admin/search endpoint</h1>'




if __name__ == '__main__':
    app.run(debug=True)
