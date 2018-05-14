from flask import Flask, render_template, request
from datetime import datetime
import sqlite3


app = Flask(__name__)

@app.route("/")
def main():
   # Pass the template data into the template main.html and return it to the user
   
   return render_template('temperature.html')

@app.route('/',methods = ['POST'])
def result():
   if request.method == 'POST':
      start_date = request.form['start_date']
      end_date = request.form['end_date']
      
      start_dateObj = datetime.strptime(start_date, '%Y-%m-%d')
      end_dateObj = datetime.strptime(end_date, '%Y-%m-%d')
      
      start_date2 = start_dateObj.strftime('%m/%d/%Y')
      end_date2 = end_dateObj.strftime('%m/%d/%Y')
      
      conn = sqlite3.connect('temperature.db')
      c = conn.cursor()
      c.execute('''SELECT * FROM TempData WHERE date_time BETWEEN ? AND ?''', (start_date2, end_date2,))
      return render_template('temperature.html', data = c.fetchall(), start_date = 'Start date: ' + start_date2, end_date = 'End date: ' + end_date2)
   conn.close()

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8082, debug=True)