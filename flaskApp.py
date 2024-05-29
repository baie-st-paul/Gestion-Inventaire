from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home/index.html')

@app.route('/inventoryout')
def inventory_out_page():
    return render_template('inventoryout/index.html')