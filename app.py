from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/patient')
def patient():
    return render_template('patient.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/pcos_checker')  # Route for PCOS Checker
def pcos_checker():
    return render_template('pcoschecker.html') 

@app.route('/image_scan')
def image_scan():
    return render_template('imagescan.html')




if __name__ == '__main__':
    app.run(debug=True, port=5001)
