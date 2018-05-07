
from os import environ
from flask import Flask

app = Flask(__name__)
app.run(environ.get('PORT'))

print('helllooooo world')
print("hii gm")
