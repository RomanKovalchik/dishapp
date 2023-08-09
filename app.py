# DONE BY Roman Kovalchyk
# Connection to database is added_ version 2
# Getting data from the database for /menu endpoint
from flask import Flask
import sqlite3

app = Flask(__name__)


@app.route('/')
def start_page():  # put application's code here
    forms = """<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
  <input type="submit" value="Submit">
</form> """
    return '<h1>Welcome to our order food app!</h1>' + forms


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


@app.route('/user/register', methods=['POST'])
def user_reg():
    return '<h1>User/register endpoint</h1>'


@app.route('/user/signin', methods=['POST'])
def user_signin():
    return '<h1>User/signin endpoint</h1>'


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
@app.route('/menu', methods=['GET'])
def menu():
    con = sqlite3.connect("dish.db")
    cursor = con.cursor()
    res = cursor.execute("SELECT * FROM Dishes")
    results = res.fetchall()
    return results


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


if __name__ == '__main__':
    app.run()


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