from model import Base, Product, Cart


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, price, picture_link, description):
	product_object = Product(
		name = name,
		price = price,
 		picture_link = picture_link,
		description = description)
	session.add(product_object)
	session.commit()

def edit_product(id, name, price, description, picture_link):
	product_object = session.query(Product).filter_by(id = id).first()
	product_object.name = name
	product_object.price = price
	product_object.picture_link = picture_link
	product_object.description = description
	session.commit()

def del_product(id):
	session.query(Product).filter_by(id = id).delete()
	session.commit()

def return_all_products():
	products = session.query(Product).all()
	return products

def return_product(id):
	product = session.query(Product).filter_by(id = id).first()
	return product

def add_to_cart(productID):
	productID_object = Cart(productID = productID)
	session.add(productID_object)
	session.commit()
def return_cart():
	items = session.query(Cart).all()
	return items

def remove_from_cart(productID):
	session.query(Cart).filter_by(productID = productID).delete()
	session.commit()

######################################################

# cart_list = return_cart()
# print(cart_list)
# remove_from_cart(cart_list[0].productID)
# print(cart_list)
