from flask import Flask, request
from. operations import add, sub, mult, div
 

app = Flask(__name__)

# Put your app in here.

calculations = {
    'add' : add, 
    'sub' : sub, 
    'mult': mult, 
    'div' : div, 
    }


@app.route('/simplemath/<calc>/')
def calculate(calc):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result =  calculations[calc](a,b)

    return str(result)




    




