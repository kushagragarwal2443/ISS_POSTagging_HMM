from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

#Introduction.html rendered for both the home page and specific URL
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
         Q1 = request.form['q1']#Input for question1 of the quiz taken
         Q2 = request.form['q2']#--do--
         Q3 = request.form['q3']#--do--
         Q4 = request.form['q4']#--do--
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            if(Q1 is "" or Q2 is "" or Q3 is "" or Q4 is ""):
               msg = "One or more empty answers. So no submission.";
               #if any of the fields are empty throw this error message
            else:
               cur.execute("INSERT INTO students (Question_1,Question_2,Question_3,Question_4) VALUES (?,?,?,?)",(Q1,Q2,Q3,Q4))
               con.commit()
               #if all fields have been filled then insert the entry into the database
               msg = "Record successfully added"
      except:
         con.rollback()
         msg = "Error in insert operation"
         #Except block to print this error message incase the insertion wasnt successful
      
      finally:
         return render_template("Result.html",msg = msg)
         con.close()
         #once the entries have been made into the database the result.html is rendered

@app.route('/Answers.html/')
def answers():
    ''' This function prints the contents of the database
    Input parameter- None
    Return value- Renders Answers.html again
    Prints the values of the answers in the database row wise'''
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall();
   print("rows=");print(len(rows));
   return render_template('Answers.html',rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
