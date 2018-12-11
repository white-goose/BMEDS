from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route('/page1/')
def CHARTS():
    return render_template('BRETT PART.html')

@app.route('/page2/')
def COOL_GRAPH():
    return render_template('MARINA PART.html')

@app.route('/page3/')
def MACHINE_LEARNING():
    return render_template('ENSIE PART.html')

@app.route('/page4/')
def MAPPING():
    return render_template('DENISE PART.html')

if __name__ == "__main__":
    app.run(debug=True)