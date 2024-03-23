from model import SalaryPredictor
from flask import Flask,request
from flask import Blueprint
import pandas as pd
main = Blueprint('main', __name__)
import csv

from flask_cors import CORS

@main.route("/predict", methods=["GET"])
def movie_ratings():
    age=request.args.get('age')
    gender=request.args.get('gender')
    educationLevel=request.args.get('educationLevel')
    yearsExperience=request.args.get('yearsExperience')
    fields = ['Age','Gender','EducationLevel','YearsExperience','Salary']
    rows = [[age,gender,educationLevel,yearsExperience,'0']]
    filename = "testing.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
    ratings = salary_predictor._predict('testing.csv')
    ratings=ratings.to_json(orient="records")
    return ratings

def create_app():
    global salary_predictor 
 
    salary_predictor = SalaryPredictor()    
    
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(main)
    return app

app = create_app()
app.run()