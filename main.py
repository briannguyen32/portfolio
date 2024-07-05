"""Server"""
import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def my_home():
    """homepage"""
    return render_template('index.html')


@app.route("/<string:page_name>")
def my_home2(page_name):
    """homepage"""
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    """login"""
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')


def write_to_csv(data):
    """fgb"""
    with open('database.csv', newline='', mode='a', encoding='utf-8') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
