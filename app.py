# DONE BY Roman Kovalchyk
# Connection to database is added_ version 2
# Getting data from the database for /menu endpoint
import json

from flask import Flask

from fanctions import SQLiteDB

app = Flask(__name__)


@app.route('/')
def start_page():  # put application's code here

    return '<h1>Welcome to our order food app!</h1>'


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    return '<h1>Cart endpoint</h1>'


@app.route('/art', methods=['POST'])
def cart_ord():
    return '<h1>Hi</h1>'


@app.route('/cart/order', methods=['GET', 'POST'])
def cart_order():
    return '<h1>Cart/order endpoint</h1>'


@app.route('/cart/add', methods=['PUT', 'POST'])
def cart_add():
    return '<h1>Cart/add endpoint</h1>'


@app.route('/user', methods=['GET', 'PUT', 'POST', 'DELETE'])
def user():  # put application's code here
    return '<h1>User endpoint</h1>'


@app.route('/user/register', methods=['GET', 'POST'])
def user_reg():
    with SQLiteDB("dish.db") as db:
        from flask import request
        if request.method == 'POST':
            data = request.form.to_dict()
            db.insert_into('User', data)
        data = db.select_from('User', ['*'])

        html_forms = f""" 
           <form method='POST'>
           <input type="text" name="Phone" placeholder="phone"/>
           <input type="text" name="Email" placeholder="email"/>
           <input type="text" name="Password" placeholder="password"/>
           <input type="text" name="Tg" placeholder="telegram"/>
           <input type="text" name="Type" placeholder="type"/>
           <input type="submit" value="submit"/>
           </form>
           <br/> 
           {str(data)}
           """

    return html_forms


@app.route('/user/signin', methods=['GET', 'POST'])
def user_signin():
    with SQLiteDB("dish.db") as db:
        from flask import request
        message = "Please, enter your e-mail and password!"
        if request.method == 'POST':
            #data = request.form.to_dict()
            info = request.form.to_dict()
            email = info.get('Email')
            password = info.get('Password')

            data = db.select_from('User', ['*'], {'Email': email, 'Password': password})
            if not data:
                message = "No users found! Please, check your date or register!"
            else:
                message = "Welcome to our food delivery service!"
        html_forms = f""" 
           <form method='POST'>
          {str(message)}
          <br/>
          <br/>
           <input type="text" name="Email" placeholder="email"/>
           <input type="text" name="Password" placeholder="password"/>
          
           <input type="submit" value="sign in"/>
           </form>
           <br/> 
           
           """

    return html_forms


@app.route('/user/logout', methods=['POST', 'GET'])
def logout():
    return '<h1>user/logout endpoint</h1>'


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
        from flask import request
        if request.method == 'POST':
            data = request.form.to_dict()
            db.insert_into('Dishes', data)
        data = db.select_from('Dishes', ['*'])
        html_forms = f""" 
        <form method='POST'>
        <input type="text" name="Dish_name" placeholder="name"/>
        <input type="text" name="Price" placeholder="price"/>
        <input type="text" name="Description" placeholder="description"/>
        <input type="text" name="Available" placeholder="available"/>
        <input type="text" name="Category" placeholder="category"/>
        <input type="text" name="Photo" placeholder="photo"/>
        <input type="text" name="Calory" placeholder="calory"/>
        <input type="text" name="Protein" placeholder="protein"/>
        <input type="text" name="Fat" placeholder="fat"/>
        <input type="text" name="Carbs" placeholder="carbs"/>
        <input type="submit" value="submit"/>
        </form>
        <br/>
        {str(data)}
        """

    return html_forms


@app.route('/menu/<cat_name>/', methods=['GET'])
def cat_name(cat_name: int):
    return f'<h1>menu/{cat_name} endpoint</h1>'


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


# print("Hi")
# db = SQLiteDB("dish.db")
# print(db.select_from("Dishes", ['Dish_name', "Description"]))

if __name__ == '__main__':
    app.run()
