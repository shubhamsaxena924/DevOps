import time
from flask import Flask
app = Flask(__name__)
x = 2
y = 1
str = ""


def get_result():
    return x*y


@app.route('/')
def hello():
    global str
    global x
    global y
    if x == 2 and y == 1:
        str = ""
    if y > 10:
        x = x+1
        y = 1
        str += "<br>"
    if x > 5:
        str += "<br>Hope you have enjoyed learning the tables! Refresh to restart."
        x = 2
        y = 1
        return str
    count = get_result()
    str += "<br>{} * {} = {}".format(x, y, count)
    y = y+1
    return str
