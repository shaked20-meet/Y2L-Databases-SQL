from model import Base, Product


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

def edit_product(id, price):
	product_object = session.query(Product).filter_by(id = id).first()
	product_object.price = price
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


######################################################
#add_product("Pink Macaron", 5, "/static/pink.jpg", "___")
#print(del_product(1))
#product_list = return_all_products()
#print(product_list[0].price)
edit_product(3, 5609)