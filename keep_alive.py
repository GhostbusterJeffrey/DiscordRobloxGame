from os import environ
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello, I am alive!"

@app.route('/send/<username>/<data>/<key>')
def send(username=None,data=None,key=None):
  if(key == environ("API Key")):
    print("Valid Key")
  else:
    return 'Invalid API Key'
  pass

def run ():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()