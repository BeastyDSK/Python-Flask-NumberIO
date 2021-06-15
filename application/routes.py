from application import app
from flask import render_template
from math import sqrt


result = [
    {"res":"True"},
    {"res":"False"}
    ]

#Router for Home page
@app.route("/")
def home():
    return render_template("home.html", title="Home")

#Router for Prime Number
@app.route("/check/0/<int:value>")
def primeChecker(value):
    if value in [0,1]:    return result[1]
    elif value == 2:   return result[0]
    
    for div in range(2,int(sqrt(value))+1):
        if value%div==0:    return result[1]
    return result[0]

#Router for Palidrome Number
@app.route("/check/1/<int:value>")
def palindromeChecker(value):
    if value == int(str(value)[-1::-1]):    return result[0]
    return result[1]

#Router for Fibonacci Series
@app.route("/check/2/<int:value>")
def fibChecker(value):
    first,second = 0,1
    if value==0:    return result[0]

    for i in range(0,10000000000000000000000000):
        temp = first
        first = second
        second = temp + second
        if second == value:    return result[0]
        elif second > value:    return result[1]

#Router for Perfect Number
@app.route("/check/3/<int:value>")
def perfectChecker(value):
    if value==0 or value==1:    return result[1]
    
    perfect_sum = 0
    for i in range(1,value):
        if value%i==0:
            perfect_sum += i
    
    if perfect_sum == value:    return result[0]
    return result[1]


#Router for Happy Number
@app.route("/check/4/<int:value>")
def happyChecker(value):
    
    if value==0:    return result[1]

    temp = value
    while True:
        sum = 0
        while temp:
            sum += (temp%10)**2
            temp //= 10

        if value == sum or sum in [1,7,10]:    return result[0]
        elif sum<=9:    return result[1]
        temp = sum

# Router for Armstrong Number
@app.route("/check/5/<int:value>")
def armstrongChecker(value):
    digits = len(str(value))
    temp = value
    sum = 0
    
    while temp:
        sum += ( ( temp % 10 )**digits)
        temp //= 10

    if sum == value:    return result[0]
    return result[1]
