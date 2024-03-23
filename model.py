from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression 

class SalaryPredictor:

    def __init__(self):
        spark = SparkSession.builder.master('local').appName('Test_Spark').getOrCreate()
        df_pyspark = spark.read.csv('SalaryData.csv', header=True, inferSchema=True)
        featureAssembler = VectorAssembler(inputCols=['Age','Gender','EducationLevel','YearsExperience'], outputCol='Independent_Features')
        output = featureAssembler.transform(df_pyspark)
        finalData = output.select('Independent_Features', 'Salary')
        regressor = LinearRegression(featuresCol='Independent_Features', labelCol='Salary')
        regressor = regressor.fit(finalData)
        self.regressor=regressor
            
    def _predict(self,path):
        self.regressor.coefficients
        self.regressor.intercept
        spark = SparkSession.builder.master('local').appName('Test_Spark').getOrCreate()
        df_pyspark2 = spark.read.csv(path, header=True, inferSchema=True)
        featureAssembler = VectorAssembler(inputCols=['Age','Gender','EducationLevel','YearsExperience'], outputCol='Independent_Features')
        output = featureAssembler.transform(df_pyspark2)
        finalData = output.select('Independent_Features', 'Salary')
        testingData=finalData
        linearRegressionPrediction = self.regressor.transform(testingData).select('prediction')
        lrPredictionDF = linearRegressionPrediction.toPandas()
        return lrPredictionDF
