from flask import Flask, render_template, request
import time
import pyautogui

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_clicker():
    number_of_clicks = int(request.form['clicks'])
    interval = float(request.form['interval'])
    for i in range(number_of_clicks):
        pyautogui.click()
        time.sleep(interval)
    return 'Clicking completed!'

if __name__ == '__main__':
    app.run(debug=True)