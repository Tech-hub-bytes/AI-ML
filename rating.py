import numpy as np
import pandas as pd
import numpy as np
import csv
import json
import random
from flask import Flask, redirect, url_for, request
app = Flask(__name__)



@app.route('/login',methods = ['POST','GET'])
   
def login():
   global x
   global y
   global z

   if request.method == 'POST':
      user1 = request.form['key1']
      user2 = request.form['key2']
   

      print(user1)
      print(user2)
    
      x=user1
      y=user2
   
      z='{} {}'.format(x, y)
      hotels_detail_1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\desktopnew.csv")

      l=hotels_detail_1[['item_id','title']]
      l
      y1=l.loc[l.title==y]
      y1['item_id']
      x1=y1['item_id']
      print(x1)
      print(type(x1))
      s1 = str(x1)
      print(s1)
      d1=(x1.head(1)).to_json()
      print(d1)
      jsonObject = json.loads(d1)
      for key in jsonObject:
        value = jsonObject[key]
        print("The key and value are ({}) = ({})".format(key, value))
      print(value)    
      print(key)
      n = random.randint(0,700)
      n1 = random.randint(0,7000000)
      with open("C:\\Users\\Nova Data\\Desktop\mylist.csv",'a+', newline='') as cs:
            csv_writer=csv.writer(cs)
            csv_writer.writerow([n,value,x,n1])
#     cs.seek(0)
#     csv_reader=csv.reader(cs)
#     for line in csv_reader:
#        print(line)
      print(x)
      print(value)
      cs.close() 
      
      return z
















   
if __name__ == '__main__':
   app.run( port=6000)

   