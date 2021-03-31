
from flask import Flask, render_template, request, json, redirect
import requests
import json
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/expenses')
def expenses():
    return render_template("expenses.html")

@app.route('/getexpenses',methods=['POST'])
def getexpenses(): 
    month=request.form['month']
    year=request.form['year']
    query = {'month': str(month), 'year': str(year)}
    response = requests.get("http://localhost:9090/server/flaskapplication/dv_food_expenses/views/dv_food_expenses?$format=json", params=query)
    s=response.json()['elements']
    res={"data":s}
    return res


@app.route('/savedquery',methods=['POST'])
def savedquery(): 
    month=request.form['month']
    year=request.form['year']
    queryname ="Employees_food_expenses_"+year
    querydetails = str({"month":month,"year":year})
    conn = mysql.connector.connect(user='root', password='Jwala@123', host='localhost', database='mydb')
    cursor = conn.cursor()
    insert_stmt = ("INSERT INTO savedquery(queryname,querydetails) VALUES (%s, %s)")
    data = (queryname,querydetails)
    cursor.execute(insert_stmt, data)
    conn.commit()
    conn.close()
    return "Success"

   
@app.route('/sports_salary')
def sports():
    return render_template("sports.html")


@app.route('/getsports',methods=['POST'])
def getsports():
    sport_choice=request.form['sport']
    year=request.form['year']
    query = {"sport_choice": str(sport_choice), "year": year}
    response1 = requests.get("http://localhost:9090/server/flaskapplication/dv_employee_sports_data/views/dv_employee_sports_data?$format=json", params=query)
    s=response1.json()['elements']
    res={"data":s}
    return res


@app.route('/getsalary',methods=['POST'])
def getsalary():
    response2 = requests.get("http://localhost:9090/server/flaskapplication/dv_employee_details_salary/views/dv_employee_details_salary?$format=json")
    ss=response2.json()['elements']
    result={"data":ss}
    return result

@app.route('/savedquerysports',methods=['POST'])
def savedquerysports(): 
    sport_choice=request.form['sport']
    year=request.form['year']
    querydetails = str({"sport_choice": sport_choice, "year": year})
    queryname ="Employees_played_sports_"+year
    conn = mysql.connector.connect(user='root', password='Jwala@123', host='localhost', database='mydb')
    cursor = conn.cursor()
    insert_stmt = ("INSERT INTO savedquery(queryname,querydetails) VALUES (%s, %s)")
    data = (queryname,querydetails)
    cursor.execute(insert_stmt, data)
    conn.commit()
    conn.close()
    return "Successfully inserted"

@app.route('/savedquerysalary',methods=['POST'])
def savedquerysalary(): 
    salary_low=request.form['salary_low']
    salary_high=request.form['salary_high']
    if salary_high!='' and salary_low!='':
        querydetails = str({"salary_low_range": salary_low, "salary_high_range": salary_high})
        queryname ="Employees_salary_"+salary_low+" to "+salary_high
        conn = mysql.connector.connect(user='root', password='Jwala@123', host='localhost', database='mydb')
        cursor = conn.cursor()
        insert_stmt = ("INSERT INTO savedquery(queryname,querydetails) VALUES (%s, %s)")
        data = (queryname,querydetails)
        cursor.execute(insert_stmt, data)
        conn.commit()
        conn.close()
        return "Success"

@app.route('/saved_query1')
def saved_query1():
    return render_template("squery.html")

@app.route('/saved_query',methods=['POST'])
def saved_query():
    conn = mysql.connector.connect(user='root', password='Jwala@123', host='localhost', database='mydb')
    cursor = conn.cursor()
    sql = '''SELECT * from savedquery'''
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    result1={"data":result}
    return result1



if __name__=="__main__":
    app.run()
