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
		product = return_product(request.form["product_id"])
		edit_product(product.id, request.form["name"], request.form["price"], request.form["description"], request.form["pic_link"])
		return render_template("edit.html", product = product)
	return render_template("edit.html")
# @app.route('/delete')
# def delete():
# 	products_list = return_all_products()


if __name__ == '__main__':
    app.run(debug=True)