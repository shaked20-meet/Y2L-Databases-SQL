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
	product_list = []
	if request.method == 'POST':
		product_id = request.form["product_info"]
		add_to_cart(product_id)

	cart_items_id = return_cart()
	for item in cart_items_id:
		product = return_product(item.productID)
		product_list.append(product)

	return render_template("cart.html", product_list = product_list)

@app.route('/log_in')
def log_in():
	return render_template("log in.html")

@app.route('/admin_portal', methods = ['GET', 'POST'])
def portal():
	if request.method == 'POST':
		products_list = return_all_products()
		username = request.form["Username"]
		password = request.form["Password"]
		if username == "shaked20-meet" and password == "meetyr20":
			return render_template("portal.html", products_list = products_list)
	return render_template("log in.html")

@app.route('/edit', methods = ['GET', 'POST'])
def edit():
	if request.method == 'POST':
		product_id = request.form["id"]
		product = return_product(product_id)
		return render_template("edit.html", product = product)

@app.route('/edit_form', methods = ['GET','POST'])
def edit_form():
	if request.method == 'POST':
		product_id = request.form["product_id"]
		name = request.form["name"]
		price = request.form["price"]
		description = request.form["description"]
		pic_link = request.form["pic_link"]
		edit_product(product_id, name, price, description, pic_link)
		products_list = return_all_products()
		return render_template("portal.html", products_list = products_list)
	return render_template("home.html")

@app.route('/delete', methods = ['POST'])
def delete():
	product_id = request.form["del_id"]
	del_product(product_id)
	products_list = return_all_products()
	return render_template("portal.html", products_list = products_list)

@app.route('/add_form', methods = ['GET','POST'])
def add_form():
	if request.method == 'POST':
		name = request.form["add_name"]
		price = request.form["add_price"]
		description = request.form["add_description"]
		pic_link = request.form["add_pic_link"]
		add_product(name, price, description, pic_link)
		products_list = return_all_products()
		return render_template("portal.html", products_list = products_list)
	return render_template("add.html")

if __name__ == '__main__':
    app.run(debug=True)