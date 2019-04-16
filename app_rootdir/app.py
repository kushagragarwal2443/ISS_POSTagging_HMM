from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

# conn = sql.connect('database.db')
# conn.execute('CREATE TABLE students (Question_1 TEXT,Question_2 TEXT,Question_3 TEXT,Question_4 TEXT)')
# print ("Table created successfully");
# conn.close()

@app.route('/')
def home():
   return render_template('Introduction.html')

@app.route('/Introduction.html/')
def introduction():
   return render_template('Introduction.html')

@app.route('/Theory.html/')
def theory():
   return render_template('Theory.html')

@app.route('/Objective.html/')
def objective():
   return render_template('Objective.html')

@app.route('/Experiment.html/')
def experiment():
   return render_template('Experiment.html')

@app.route('/Quizzes.html/')
def quizzes():
   return render_template('Quizzes.html')

@app.route('/Procedure.html/')
def procedure():
   return render_template('Procedure.html')

@app.route('/Further_Readings.html/')
def further_reading():
   return render_template('Further_Readings.html')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['q1']
         addr = request.form['q2']
         city = request.form['q3']
         pin = request.form['q4']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            if(nm is "" or addr is "" or city is "" or pin is ""):
               msg = "One or more empty answers. So no submission.";
            else:
               cur.execute("INSERT INTO students (Question_1,Question_2,Question_3,Question_4) VALUES (?,?,?,?)",(nm,addr,city,pin))
               con.commit()
               msg = "Record successfully added"
      except:
         con.rollback()
         msg = "Error in insert operation"
      
      finally:
         return render_template("Result.html",msg = msg)
         con.close()

@app.route('/Answers.html/')
def answers():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall();
   print("rows=");print(len(rows));
   return render_template('Answers.html',rows = rows)


# @app.route('/list')
# def list():
#    con = sql.connect("database.db")
#    con.row_factory = sql.Row
   
#    cur = con.cursor()
#    cur.execute("select * from students")
   
#    rows = cur.fetchall();
#    return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)