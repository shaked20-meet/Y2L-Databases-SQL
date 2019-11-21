# The Online Shop - Lab (Part 2); Databases 
<br/>
Today, we are continuing creating <b>our awesome online shop!</b>
I don't want to see the <b>creativity</b> stop here. Keep it going!
<br/>
<br/>
We will be working in the Y2L-Flask-Routing folder from last lab. If you didn't clone the last lab, do so now.
<br/>
<br/>
You can also use Today's lecture as reference if you forgot certain lines - https://tinyurl.com/y2-databases



## Part 1: Setting Up
1. Create 2 new empty files and save them as "model.py" and "databases.py"

## Part 2: Creating Our Table
1. Edit "model.py" and add these lines in the beginning:
```python
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
```

2. Create a table called "Product" with the following variables:
- Name (String)
- Price (Float)
- Picture Link (String)
- Description (String)

## Part 3: Creating Our Database Functions

1. Edit "databases.py" and add these lines in the beginning:
```python
from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
```

2. Write functions to control the database in "databases.py", you have to have at least 5 functions:
- a function that adds a product
- a function that edits a specific product by id
- a function that deletes a specific product by id
- a function that returns all products in the table
- a function that returns a specific product by id


## Part 4: Adding to Cart
1. Open "model.py" and create a new table called "Cart" that has this one variable:
- productID 

** Don't forget the default "id", it's not the same as the variable we created.<br/>
We'll use "productID" later to get it's other values like: name, price, description...etc.

2. Open "databases.py" and create a new function called "Add_To_Cart" that takes one input which is "productID", and adds this "productID" to the new table you just created.
 

## BONUS:
- Show products in store.html and link all the functions so it could work properly.
- Create an extra "admin" page that you can access with a special link that has a dashboard to control the website databse, it could have functions like:
	1. Add Products
	2. Edit Products
	3. Delete Products
	4. Show all products
 
