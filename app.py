from flask import Flask, render_template, request, redirect

app = Flask(__name__)

contacts = []

@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        contacts.append({
            'name': name,
            'phone': phone,
            'email': email
        })

        return redirect('/')
    return render_template('add_contact.html')

@app.route('/delete/<int:index>')
def delete_contact(index):
    if 0 <= index < len(contacts):
        contacts.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)