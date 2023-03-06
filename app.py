from flask import Flask, render_template,redirect,request
import requests
import pymongo
from bs4 import BeautifulSoup
client = pymongo.MongoClient("mongodb+srv://DevKarol:gQiTucOEC4Vy9lYe@pp2.axkdroq.mongodb.net/?retryWrites=true&w=majority")
db = client.ceneo["reviews"]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/review', methods=['GET'])
def reviews():
    return render_template('reviews.html')

@app.route('/api/review', methods=['POST'])     
def review():
    product_id = request.form["product_id"]
    error_message = 'Product not found'
    
    return redirect(f'https://www.ceneo.pl/{product_id}#reviews')
        
if __name__ == '__main__':
    app.run(debug=True)
    
