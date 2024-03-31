from model import SalaryPredictor
from flask import Flask,request
from flask import Blueprint
import pandas as pd
import csv

from flask_cors import CORS

global salary_predictor 

salary_predictor = SalaryPredictor()    

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["GET"])
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


if __name__ == '__main__':
    app.run(host='0.0.0.0')   