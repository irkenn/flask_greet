from flask import Flask, request

@app.route('/welcome')
def welcome():
    return "Welcome"

@app.route('/welcome/<variable>')
def welcome_home(variable):
    if variable == "home"
        return "welcome home"
    elif variable == "back"
        return "welcome back"
