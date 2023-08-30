#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:input_string>')
def print_string(input_string):
    print (f"{input_string}")
    return input_string
    
@app.route('/count/<int:num>')
def count(num):
    numbers = range(0,num)
    return '\n'.join(map(str, numbers)) + '\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1,operation,num2):
    if operation == "+":
        return str(num1+num2)
    if operation == "-":
        return str(num1-num2)
    if operation == "*":
        return str(num1*num2)
    if operation == "div":
        return str(num1/num2)
    if operation == "%":
        return str(num1%num2)
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
