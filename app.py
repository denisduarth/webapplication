# Ao abrir o gitpod, execute:
# pip install -r requirements.txt

from flask import Flask

app = Flask(__name__)

@app.route('/')
def daniel():
    return 'Daniel Calvo'

app.run()

print('Daniel Calvo')