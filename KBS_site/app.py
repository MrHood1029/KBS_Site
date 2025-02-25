from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/registers')
def registers():
    return render_template('registers.html')

@app.route('/sell_wm')
def sell_wm():
    return render_template('sell_wm.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/zav')
def zav():
    return render_template('zav.html')

if __name__ == '__main__':
    app.run(debug=True)
