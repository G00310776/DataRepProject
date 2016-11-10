from flask import Flask, render_template, request
app = Flask(__name__)  

@app.route('/')
def index():
	return render_template("index.html",)

@app.route('/shopping')
def shopping():
	food = ["Chesse", "Tuna", "Beef"]
	return render_template("shopping.html", food=food)


if __name__ == "__main__":
	app.run (debug=True)