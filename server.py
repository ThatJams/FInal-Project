from flask import Flask, render_template, request, redirect, url_for

import csv

app = Flask(__name__)
print('Kanjo')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
        
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return 'You have successfully submitted a form. Thank you for your cooperation. Click backspace to go back to page!'

def write_to_csv(data):
    with open('database.csv', mode='a') as database:
        subject = data["subject"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"',quoting= csv.QUOTE_MINIMAL)
        csv_writer.writerow([subject,email,message])