from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/contacts')
def contacts():
    developer_name = "Bybyby Bebebe"
    developer_adres = "Bebebe Bybyby"
    return render_template('contacts.html', name = developer_name, adres = developer_adres)

@app.route("/ctranuca")
def ctranuca():
    dict_info = {'Разработчик': 'Bebebebe', 'Адрес': 'kfkkkaka'}
    return render_template('ctranuca.html', info = dict_info)


if __name__ == "__main__":
    app.run(debug = True)