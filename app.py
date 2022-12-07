from flask import Flask, request, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = '123'

@app.route('/')
def hello_world():  # put application's code here
    return render_template('register.html')

@app.route('/date')
def date():  # put application's code here
    return render_template('date.html')


@app.route('/available', methods= ["GET", "POST"])
def available():  # put application's code here
    if request.method == "POST":
        selected_room = request.form.get("ROOM_TYPE")
    return render_template('available.html',rooms="12")

@app.route('/customer')
def customer():  # put application's code here
    if request.method == "POST":
        fname = request.form.get("customer_name")
        email = request.form.get("Email")

    return render_template('customer.html')


if __name__ == '__main__':
    app.static_folder = 'static'
    app.run(debug=True)
