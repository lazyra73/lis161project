from flask import Flask, render_template
from menu import menu

app = Flask(__name__) #instantiate an object is same as assigning a variable


@app.route('/') 
def index():
    return render_template('index.html')


@app.route('/about') 
def about():
    return render_template('aboutus.html')

@app.route('/menu') 
def menupage():
    return render_template('menu.html')

@app.route('/contact') 
def contactus():
    return render_template('contact.html')

#html page for each animal type
@app.route("/menu/<food_type>")
def animals(food_type):  
    food_list = menu[food_type] #communicating with data model aka calling the menu dict with food_type key  
    return render_template('foodtype.html', food_type = food_type, food_list =food_list) 


@app.route("/menu/<food_type>/<int:food_index>")
def pet(food_type, food_index):
    food_profile = menu[food_type][food_index] #menu[food type so appetizer etc][index in food type]
    return render_template('food.html', food_profile = food_profile)

















#pinakalast ito
if __name__ == '__main__': #nilalagay ito sa bottom ; kapag nirun yung file + app yung name edi marurun yung code
    app.run(debug=True) #doing this kasi we're still in development code, pagtapos na gagawin nang False

