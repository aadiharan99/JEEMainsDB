import pymongo
import pandas as pd
import json
#reading the excel csv file using pandas,one can use any file path here
excel_file=pd.read_csv('/Users/aadiharan99/Downloads/JEE_responses.csv')
print(excel_file.head())
#initializing the mongodb client, running on localhost
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#selecting the database
mydb = myclient["mydb"]
'''selecting the collection,if collection does not exist,
   it will be created with the name as the text in squared brackets.
'''
mycol = mydb["JEE"]
#converting the excel file to json
data_json = json.loads(excel_file.to_json(orient='records'))
#checking conversion once,can comment if not required
print(data_json)
#inserting the json data into the collection we just created.
mycol.insert(data_json)