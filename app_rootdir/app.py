'''This runs in the backend to store values in the database and calls html docs when required'''
import sqlite3 as sql
from flask import Flask, render_template, request
app = Flask(__name__)

#Introduction.html rendered for both the home page and specific URL
@app.route('/')
def home():
    '''This function renders Introduction.html
    Input Type- None
    Return Value- renders the aforementioned html file
    Prints nothing'''
    return render_template('Introduction.html')

@app.route('/Introduction.html/')
def introduction():
    '''This function renders Introduction.html
    Input Type- None
    Return Value- renders the aforementioned html file
    Prints nothing'''

    return render_template('Introduction.html')

#Theory.html rendered at this URL
@app.route('/Theory.html/')
def theory():
    '''This function renders Theory.html
    Input Type- None
    Return Value- renders the aforementioned html file
    Prints nothing'''

    return render_template('Theory.html')

#Objective.html rendered at this URL
@app.route('/Objective.html/')
def objective():
    '''This function renders Objective.html
    Input Type- None
    Return Value- renders the aforementioned html file
    Prints nothing'''

    return render_template('Objective.html')

#Experiment.html rendered at this URL
@app.route('/Experiment.html/')
def experiment():
    '''This function renders Experiment.html
    Input Type- None
    Return Value- renders the aforementioned html file
    Prints nothing'''

    return render_template('Experiment.html')

#Quizzes.html rendered at this URL
@app.route('/Quizzes.html/')
def quizzes():
    '''This function renders Quizzes.html
    Input Type- None
    Return Value- renders the aforementioned html file
    Prints nothing'''

    return render_template('Quizzes.html')

#Procedure.html rendered at this URL
@app.route('/Procedure.html/')
def procedure():
    '''This function renders Procedure.html
    Input Type- None
    Return Value- renders the aforementioned html file
    Prints nothing'''

    return render_template('Procedure.html')

#Further_Readings.html rendered at this URL
@app.route('/Further_Readings.html/')
def further_reading():
    '''This function renders Further_Readings.html
    Input Type- None
    Return Value- renders the aforementioned html file
    Prints nothing'''

    return render_template('Further_Readings.html')

@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    '''This function takes input from the user and fills responses into the database
    INPUT TYPE- None
    RETURN VALUE- renders Result.html
    PRINTS- A message showing if the entry was/wasnt stored in the database successfully'''
    if request.method == 'POST':
        try:
            qu1 = request.form['q1']#Input for question1 of the quiz taken
            qu2 = request.form['q2']#--do--
            qu3 = request.form['q3']#--do--
            qu4 = request.form['q4']#--do--
            with sql.connect("database.db") as con:
                cur = con.cursor()
                if(qu1 is "" or qu2 is "" or qu3 is "" or qu4 is ""):
                    msg = "One or more empty answers. So no submission."
                    #if any of the fields are empty throw this error message
                else:
                    cur.execute("INSERT INTO students (Question_1, Question_2, Question_3, Question_4) VALUES (?, ?, ?, ?)", (qu1, qu2, qu3, qu4))
                    con.commit()
                    #if all fields have been filled then insert the entry into the database
                    msg = "Record successfully added"
        except:
            con.rollback()
            msg = "Error in insert operation"
            #Except block to print this error message incase the insertion wasnt successful
        finally:
            return render_template("Result.html", msg=msg)
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
    rows = cur.fetchall()
    print ("rows=")
    print (len(rows))
    return render_template('Answers.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
