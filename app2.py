from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *
from model import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

##### Code here ######
@app.route('/')
def home():
	return render_template("home.html")

@app.route('/store', methods = ['GET', 'POST'])
def store():
	products_list = return_all_products()
	return render_template("store.html", products_list = products_list)

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/cart', methods = ['GET', 'POST'])
def cart():
	products_list = []
	if request.method == 'POST':
		product_id = request.form["product_info"]
		add_to_cart(product_id)

	cart_items_id = return_cart()
	for item in cart_items_id:
		product = return_product(item.productID)
		products_list.append(product)

	return render_template("cart.html", products_list = products_list)

@app.route('/log_in', methods = ['GET','POST'])
def log_in():
	return render_template("log in.html")

@app.route('/admin_portal', methods = ['GET', 'POST'])
def portal():
	if request.method == 'POST':
		username = request.form["Username"]
		password = request.form["Password"]
		if username == "shaked20-meet" and password == "meetyr20":
			return render_template("portal.html")
	return render_template("log in.html")
if __name__ == '__main__':
    app.run(debug=True)