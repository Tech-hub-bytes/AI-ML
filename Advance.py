import numpy as np
import pandas as pd
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
      user3 = request.form['key3']

      print(user1)
      print(user2)
      print(user3)
      x=user1
      y=user2
      w=user3
      z='{} {} {}'.format(x, y, w)
    
      
      
      return z
       
      
         
   if request.method == 'GET':
       hotels_detail = pd.read_csv("C:\\Users\\Nova Data\\Desktop\desktopnew.csv")
       hotels_detail.head()
       g =hotels_detail.groupby("CITY")
       g
       g.get_group('SKARDU')

       hotels_list = pd.read_csv("C:\\Users\\Nova Data\\Desktop\H_list1new.csv")
       hotels_list.head(5)
       df = pd.merge(hotels_list,g.get_group('SKARDU'),on='item_id')
       df1 = pd.merge(hotels_list,g.get_group('HUNZA'),on='item_id')
       df2 = pd.merge(hotels_list,g.get_group('ASTORE'),on='item_id')
       df3 = pd.merge(hotels_list,g.get_group('GILGIT'),on='item_id')
       df3.head()
       df2.head()
       df1.head()
       df.head()
       l=df[['title','BUDGET','STANDRED','CITY','DAYS']]
       l1=df1[['title','BUDGET','STANDRED','CITY','DAYS']]
       l2=df2[['title','BUDGET','STANDRED','CITY','DAYS']]
       l3=df3[['title','BUDGET','STANDRED','CITY','DAYS']]
       def get_demo_data(day,buget,city):
           
        if city=="Skardu" or city=="skardu" or city=="SKARDU" :   
         if day==1 and buget==40000:
            x1=l.loc[l.DAYS==1]
            x1=x1.loc[x1.BUDGET=='40,000']
            return x1
         elif day==2 and buget==40000:
            x2=l.loc[l.DAYS==2]
            x2=x2.loc[x2.BUDGET=='40,000']
            return x2
         elif day==3 and buget==40000:
            x3=l.loc[l.DAYS==3]
            x3=x3.loc[x3.BUDGET=='40,000']
            return x3
        
         elif day==4 and buget==40000:
            x4=l.loc[l.DAYS==4]
            x4=x4.loc[x4.BUDGET=='40,000']
            return x4
    
         elif day==5 and buget==40000:
            x5=l.loc[l.DAYS==5]
            x5=x5.loc[x5.BUDGET=='40,000']
            return x5
        
         elif day==6 and buget==40000:
            x6=l.loc[l.DAYS==6]
            x6=x6.loc[x6.BUDGET=='40,000']
            return x6
    
         elif day==7 and buget==40000:
            x7=l.loc[l.DAYS==7]
            x7=x7.loc[x7.BUDGET=='40,000']
            return x7
         elif day==1 and buget==35000:
            y1=l.loc[l.DAYS==1]
            y1=y1.loc[y1.BUDGET=='35,000']
            return y1
         elif day==2 and buget==35000: 
            y2=l.loc[l.DAYS==2]
            y2=y2.loc[y2.BUDGET=='35,000']
            return y2
         elif day==3 and buget==35000:
            y3=l.loc[l.DAYS==3]
            y3=y3.loc[y3.BUDGET=='35,000']
            return y3
         elif day==4 and buget==35000:
            y4=l.loc[l.DAYS==4]
            y4=y4.loc[y4.BUDGET=='35,000']
            return y4
         elif day==5 and buget==35000:
            y5=l.loc[l.DAYS==5]
            y5=y5.loc[y5.BUDGET=='35,000']
            return y5
         elif day==6 and buget==35000:
            y6=l.loc[l.DAYS==6]
            y6=y6.loc[y6.BUDGET=='35,000']
            return y6
         elif day==7 and buget==35000:
            y7=l.loc[l.DAYS==7]
            y7=y7.loc[y7.BUDGET=='35,000']
            return y7
         elif day==1 and buget==30000:
            z1=l.loc[l.DAYS==1]
            z1=z1.loc[z1.BUDGET=='30,000']
            return z1
         elif day==2 and buget==30000:   
            z2=l.loc[l.DAYS==2]
            z2=z2.loc[z2.BUDGET=='30,000']
            return z2
         elif day==3 and buget==30000:
            z3=l.loc[l.DAYS==3]
            z3=z3.loc[z3.BUDGET=='30,000']
            return z3
         elif day==4 and buget==30000:
            z4=l.loc[l.DAYS==4]
            z4=z4.loc[z4.BUDGET=='30,000']
            return z4
         elif day==5 and buget==30000:
            z5=l.loc[l.DAYS==5]
            z5=z5.loc[z5.BUDGET=='30,000']
            return z5
         elif day==6 and buget==30000:
            z6=l.loc[l.DAYS==6]
            z6=z6.loc[z6.BUDGET=='30,000']
            return z6
         elif day==7 and buget==30000:
            z7=l.loc[l.DAYS==7]
            z7=z7.loc[z7.BUDGET=='30,000']
            return z7
         elif day==1 and buget==25000:   
            y_1=l.loc[l.DAYS==1]
            y_1=y_1.loc[y_1.BUDGET=='25,000']
            return y_1
         elif day==2 and buget==25000:
            y_2=l.loc[l.DAYS==2]
            y_2=y_2.loc[y_2.BUDGET=='25,000']
            return y_2
         elif day==3 and buget==25000:
            y_3=l.loc[l.DAYS==3]
            y_3=y_3.loc[y_3.BUDGET=='25,000']
            return y_3
         elif day==4 and buget==25000:
            y_4=l.loc[l.DAYS==4]
            y_4=y_4.loc[y_4.BUDGET=='25,000']
            return y_4
         elif day==5 and buget==25000:
            y_5=l.loc[l.DAYS==5]
            y_5=y_5.loc[y_5.BUDGET=='25,000']
            return y_5
         elif day==6 and buget==25000:
            y_6=l.loc[l.DAYS==6]
            y_6=y_6.loc[y_6.BUDGET=='25,000']
            return y_6
         elif day==7 and buget==25000:
            y_7=l.loc[l.DAYS==7]
            y_7=y_7.loc[y_7.BUDGET=='25,000']
            return y_7
         elif day==1 and buget==20000:
            x_1=l.loc[l.DAYS==1]
            x_1=x_1.loc[x_1.BUDGET=='20,000']
            return x_1
         elif day==2 and buget==20000:
            x_2=l.loc[l.DAYS==2]
            x_2=x_2.loc[x_2.BUDGET=='20,000']
            return x_2
         elif day==3 and buget==20000:
            x_3=l.loc[l.DAYS==3]
            x_3=x_3.loc[x_3.BUDGET=='20,000']
            return x_3
         elif day==4 and buget==20000:
            x_4=l.loc[l.DAYS==4]
            x_4=x_4.loc[x_4.BUDGET=='20,000']
            return x_4
         elif day==5 and buget==20000:
            x_5=l.loc[l.DAYS==5]
            x_5=x_5.loc[x_5.BUDGET=='20,000']
            return x_5
         elif day==6 and buget==20000:
            x_6=l.loc[l.DAYS==6]
            x_6=x_6.loc[x_6.BUDGET=='20,000']
            return x_6
         elif day==7 and buget==20000:
            x_7=l.loc[l.DAYS==7]
            x_7=x_7.loc[x_7.BUDGET=='20,000']
            return x_7
         elif day==1 and buget==15000:
            z_1=l.loc[l.DAYS==1]
            z_1=z_1.loc[z_1.BUDGET=='15,000']
            return z_1
         elif day==2 and buget==15000:
            z_2=l.loc[l.DAYS==2]
            z_2=z_2.loc[z_2.BUDGET=='15,000']
            return z_2
         elif day==3 and buget==15000:
            z_3=l.loc[l.DAYS==3]
            z_3=z_3.loc[z_3.BUDGET=='15,000']
            return z_3
         elif day==4 and buget==15000:
            z_4=l.loc[l.DAYS==4]
            z_4=z_4.loc[z_4.BUDGET=='15,000']
            return z_4
         elif day==5 and buget==15000:
            z_5=l.loc[l.DAYS==5]
            z_5=z_5.loc[z_5.BUDGET=='15,000']
            return z_5
         elif day==6 and buget==15000:
            z_6=l.loc[l.DAYS==6]
            z_6=z_6.loc[z_6.BUDGET=='15,000']
            return z_6
         elif day==7 and buget==15000:
            z_7=l.loc[l.DAYS==7]
            z_7=z_7.loc[z_7.BUDGET=='15,000']
            return z_7
         if day==1 and buget==50000:
            x1=l.loc[l.DAYS==1]
            x1=x1.loc[x1.BUDGET=='50,000']
            return x1
    
         elif day==2 and buget==50000:
            x2=l.loc[l.DAYS==2]
            x2=x2.loc[x2.BUDGET=='50,000']
            return x2
         elif day==3 and buget==50000:
            x3=l.loc[l.DAYS==3]
            x3=x3.loc[x3.BUDGET=='50,000']
            return x3
        
         elif day==4 and buget==50000:
            x4=l.loc[l.DAYS==4]
            x4=x4.loc[x4.BUDGET=='50,000']
            return x4
    
         elif day==5 and buget==50000:
            x5=l.loc[l.DAYS==5]
            x5=x5.loc[x5.BUDGET=='50,000']
            return x5
        
         elif day==6 and buget==50000:
            x6=l.loc[l.DAYS==6]
            x6=x6.loc[x6.BUDGET=='50,000']
            return x6
    
         elif day==7 and buget==50000:
            x7=l.loc[l.DAYS==7]
            x7=x7.loc[x7.BUDGET=='50,000']
            return x7
        if city=="Hunza" or city=="hunza" or city=="HUNZA":
         if day==1 and buget==40000:
            x1=l1.loc[l1.DAYS==1]
            x1=x1.loc[x1.BUDGET=='40,000']
            return x1
         elif day==2 and buget==40000:
            x2=l1.loc[l1.DAYS==2]
            x2=x2.loc[x2.BUDGET=='40,000']
            return x2
         elif day==3 and buget==40000:
            x3=l1.loc[l1.DAYS==3]
            x3=x3.loc[x3.BUDGET=='40,000']
            return x3
        
         elif day==4 and buget==40000:
            x4=l1.loc[l1.DAYS==4]
            x4=x4.loc[x4.BUDGET=='40,000']
            return x4
    
         elif day==5 and buget==40000:
            x5=l1.loc[l1.DAYS==5]
            x5=x5.loc[x5.BUDGET=='40,000']
            return x5
        
         elif day==6 and buget==40000:
            x6=l1.loc[l1.DAYS==6]
            x6=x6.loc[x6.BUDGET=='40,000']
            return x6
    
         elif day==7 and buget==40000:
            x7=l1.loc[l1.DAYS==7]
            x7=x7.loc[x7.BUDGET=='40,000']
            return x7
         elif day==1 and buget==35000:
            y1=l1.loc[l1.DAYS==1]
            y1=y1.loc[y1.BUDGET=='35,000']
            return y1
         elif day==2 and buget==35000: 
            y2=l1.loc[l1.DAYS==2]
            y2=y2.loc[y2.BUDGET=='35,000']
            return y2
         elif day==3 and buget==35000:
            y3=l1.loc[l1.DAYS==3]
            y3=y3.loc[y3.BUDGET=='35,000']
            return y3
         elif day==4 and buget==35000:
            y4=l1.loc[l1.DAYS==4]
            y4=y4.loc[y4.BUDGET=='35,000']
            return y4
         elif day==5 and buget==35000:
            y5=l1.loc[l1.DAYS==5]
            y5=y5.loc[y5.BUDGET=='35,000']
            return y5
         elif day==6 and buget==35000:
            y6=l1.loc[l1.DAYS==6]
            y6=y6.loc[y6.BUDGET=='35,000']
            return y6
         elif day==7 and buget==35000:
            y7=l1.loc[l1.DAYS==7]
            y7=y7.loc[y7.BUDGET=='35,000']
            return y7
         elif day==1 and buget==30000:
            z1=l1.loc[l1.DAYS==1]
            z1=z1.loc[z1.BUDGET=='30,000']
            return z1
         elif day==2 and buget==30000:   
            z2=l1.loc[l1.DAYS==2]
            z2=z2.loc[z2.BUDGET=='30,000']
            return z2
         elif day==3 and buget==30000:
            z3=l1.loc[l1.DAYS==3]
            z3=z3.loc[z3.BUDGET=='30,000']
            return z3
         elif day==4 and buget==30000:
            z4=l1.loc[l1.DAYS==4]
            z4=z4.loc[z4.BUDGET=='30,000']
            return z4
         elif day==5 and buget==30000:
            z5=l1.loc[l1.DAYS==5]
            z5=z5.loc[z5.BUDGET=='30,000']
            return z5
         elif day==6 and buget==30000:
            z6=l1.loc[l1.DAYS==6]
            z6=z6.loc[z6.BUDGET=='30,000']
            return z6
         elif day==7 and buget==30000:
            z7=l1.loc[l1.DAYS==7]
            z7=z7.loc[z7.BUDGET=='30,000']
            return z7
         elif day==1 and buget==25000:   
            y_1=l1.loc[l1.DAYS==1]
            y_1=y_1.loc[y_1.BUDGET=='25,000']
            return y_1
         elif day==2 and buget==25000:
            y_2=l1.loc[l1.DAYS==2]
            y_2=y_2.loc[y_2.BUDGET=='25,000']
            return y_2
         elif day==3 and buget==25000:
            y_3=l1.loc[l1.DAYS==3]
            y_3=y_3.loc[y_3.BUDGET=='25,000']
            return y_3
         elif day==4 and buget==25000:
            y_4=l1.loc[l1.DAYS==4]
            y_4=y_4.loc[y_4.BUDGET=='25,000']
            return y_4
         elif day==5 and buget==25000:
            y_5=l1.loc[l1.DAYS==5]
            y_5=y_5.loc[y_5.BUDGET=='25,000']
            return y_5
         elif day==6 and buget==25000:
            y_6=l1.loc[l1.DAYS==6]
            y_6=y_6.loc[y_6.BUDGET=='25,000']
            return y_6
         elif day==7 and buget==25000:
            y_7=l1.loc[l1.DAYS==7]
            y_7=y_7.loc[y_7.BUDGET=='25,000']
            return y_7
         elif day==1 and buget==20000:
            x_1=l1.loc[l1.DAYS==1]
            x_1=x_1.loc[x_1.BUDGET=='20,000']
            return x_1
         elif day==2 and buget==20000:
            x_2=l1.loc[l1.DAYS==2]
            x_2=x_2.loc[x_2.BUDGET=='20,000']
            return x_2
         elif day==3 and buget==20000:
            x_3=l1.loc[l1.DAYS==3]
            x_3=x_3.loc[x_3.BUDGET=='20,000']
            return x_3
         elif day==4 and buget==20000:
            x_4=l1.loc[l1.DAYS==4]
            x_4=x_4.loc[x_4.BUDGET=='20,000']
            return x_4
         elif day==5 and buget==20000:
            x_5=l1.loc[l1.DAYS==5]
            x_5=x_5.loc[x_5.BUDGET=='20,000']
            return x_5
         elif day==6 and buget==20000:
            x_6=l1.loc[l1.DAYS==6]
            x_6=x_6.loc[x_6.BUDGET=='20,000']
            return x_6
         elif day==7 and buget==20000:
            x_7=l1.loc[l1.DAYS==7]
            x_7=x_7.loc[x_7.BUDGET=='20,000']
            return x_7
         elif day==1 and buget==15000:
            z_1=l1.loc[l1.DAYS==1]
            z_1=z_1.loc[z_1.BUDGET=='15,000']
            return z_1
         elif day==2 and buget==15000:
            z_2=l1.loc[l1.DAYS==2]
            z_2=z_2.loc[z_2.BUDGET=='15,000']
            return z_2
         elif day==3 and buget==15000:
            z_3=l1.loc[l1.DAYS==3]
            z_3=z_3.loc[z_3.BUDGET=='15,000']
            return z_3
         elif day==4 and buget==15000:
            z_4=l1.loc[l1.DAYS==4]
            z_4=z_4.loc[z_4.BUDGET=='15,000']
            return z_4
         elif day==5 and buget==15000:
            z_5=l1.loc[l1.DAYS==5]
            z_5=z_5.loc[z_5.BUDGET=='15,000']
            return z_5
         elif day==6 and buget==15000:
            z_6=l1.loc[l1.DAYS==6]
            z_6=z_6.loc[z_6.BUDGET=='15,000']
            return z_6
         elif day==7 and buget==15000:
            z_7=l1.loc[l1.DAYS==7]
            z_7=z_7.loc[z_7.BUDGET=='15,000']
            return z_7
         if day==1 and buget==50000:
            x1=l1.loc[l1.DAYS==1]
            x1=x1.loc[x1.BUDGET=='50,000']
            return x1
    
         elif day==2 and buget==50000:
            x2=l1.loc[l1.DAYS==2]
            x2=x2.loc[x2.BUDGET=='50,000']
            return x2
         elif day==3 and buget==50000:
            x3=l1.loc[l1.DAYS==3]
            x3=x3.loc[x3.BUDGET=='50,000']
            return x3
        
         elif day==4 and buget==50000:
            x4=l1.loc[l1.DAYS==4]
            x4=x4.loc[x4.BUDGET=='50,000']
            return x4
    
         elif day==5 and buget==50000:
            x5=l1.loc[l1.DAYS==5]
            x5=x5.loc[x5.BUDGET=='50,000']
            return x5
        
         elif day==6 and buget==50000:
            x6=l1.loc[l1.DAYS==6]
            x6=x6.loc[x6.BUDGET=='50,000']
            return x6
    
         elif day==7 and buget==50000:
            x7=l1.loc[l1.DAYS==7]
            x7=x7.loc[x7.BUDGET=='50,000']
            return x7
        if city=="Astore" or city == "astore" or city == "ASTORE": 
         
         if day==1 and buget==40000:
            x1=l2.loc[l2.DAYS==1]
            x1=x1.loc[x1.BUDGET=='40,000']
            return x1
         elif day==2 and buget==40000:
            x2=l2.loc[l2.DAYS==2]
            x2=x2.loc[x2.BUDGET=='40,000']
            return x2
         elif day==3 and buget==40000:
            x3=l2.loc[l2.DAYS==3]
            x3=x3.loc[x3.BUDGET=='40,000']
            return x3
        
         elif day==4 and buget==40000:
            x4=l2.loc[l2.DAYS==4]
            x4=x4.loc[x4.BUDGET=='40,000']
            return x4
    
         elif day==5 and buget==40000:
            x5=l2.loc[l2.DAYS==5]
            x5=x5.loc[x5.BUDGET=='40,000']
            return x5
        
         elif day==6 and buget==40000:
            x6=l2.loc[l2.DAYS==6]
            x6=x6.loc[x6.BUDGET=='40,000']
            return x6
    
         elif day==7 and buget==40000:
            x7=l2.loc[l2.DAYS==7]
            x7=x7.loc[x7.BUDGET=='40,000']
            return x7
         elif day==1 and buget==35000:
            y1=l2.loc[l2.DAYS==1]
            y1=y1.loc[y1.BUDGET=='35,000']
            return y1
         elif day==2 and buget==35000: 
            y2=l2.loc[l2.DAYS==2]
            y2=y2.loc[y2.BUDGET=='35,000']
            return y2
         elif day==3 and buget==35000:
            y3=l2.loc[l2.DAYS==3]
            y3=y3.loc[y3.BUDGET=='35,000']
            return y3
         elif day==4 and buget==35000:
            y4=l2.loc[l2.DAYS==4]
            y4=y4.loc[y4.BUDGET=='35,000']
            return y4
         elif day==5 and buget==35000:
            y5=l2.loc[l2.DAYS==5]
            y5=y5.loc[y5.BUDGET=='35,000']
            return y5
         elif day==6 and buget==35000:
            y6=l2.loc[l2.DAYS==6]
            y6=y6.loc[y6.BUDGET=='35,000']
            return y6
         elif day==7 and buget==35000:
            y7=l2.loc[l2.DAYS==7]
            y7=y7.loc[y7.BUDGET=='35,000']
            return y7
         elif day==1 and buget==30000:
            z1=l2.loc[l2.DAYS==1]
            z1=z1.loc[z1.BUDGET=='30,000']
            return z1
         elif day==2 and buget==30000:   
            z2=l2.loc[l2.DAYS==2]
            z2=z2.loc[z2.BUDGET=='30,000']
            return z2
         elif day==3 and buget==30000:
            z3=l2.loc[l2.DAYS==3]
            z3=z3.loc[z3.BUDGET=='30,000']
            return z3
         elif day==4 and buget==30000:
            z4=l2.loc[l2.DAYS==4]
            z4=z4.loc[z4.BUDGET=='30,000']
            return z4
         elif day==5 and buget==30000:
            z5=l2.loc[l2.DAYS==5]
            z5=z5.loc[z5.BUDGET=='30,000']
            return z5
         elif day==6 and buget==30000:
            z6=l2.loc[l2.DAYS==6]
            z6=z6.loc[z6.BUDGET=='30,000']
            return z6
         elif day==7 and buget==30000:
            z7=l2.loc[l2.DAYS==7]
            z7=z7.loc[z7.BUDGET=='30,000']
            return z7
         elif day==1 and buget==25000:   
            y_1=l2.loc[l2.DAYS==1]
            y_1=y_1.loc[y_1.BUDGET=='25,000']
            return y_1
         elif day==2 and buget==25000:
            y_2=l2.loc[l2.DAYS==2]
            y_2=y_2.loc[y_2.BUDGET=='25,000']
            return y_2
         elif day==3 and buget==25000:
            y_3=l2.loc[l2.DAYS==3]
            y_3=y_3.loc[y_3.BUDGET=='25,000']
            return y_3
         elif day==4 and buget==25000:
            y_4=l2.loc[l2.DAYS==4]
            y_4=y_4.loc[y_4.BUDGET=='25,000']
            return y_4
         elif day==5 and buget==25000:
            y_5=l2.loc[l2.DAYS==5]
            y_5=y_5.loc[y_5.BUDGET=='25,000']
            return y_5
         elif day==6 and buget==25000:
            y_6=l2.loc[l2.DAYS==6]
            y_6=y_6.loc[y_6.BUDGET=='25,000']
            return y_6
         elif day==7 and buget==25000:
            y_7=l2.loc[l2.DAYS==7]
            y_7=y_7.loc[y_7.BUDGET=='25,000']
            return y_7
         elif day==1 and buget==20000:
            x_1=l2.loc[l2.DAYS==1]
            x_1=x_1.loc[x_1.BUDGET=='20,000']
            return x_1
         elif day==2 and buget==20000:
            x_2=l2.loc[l2.DAYS==2]
            x_2=x_2.loc[x_2.BUDGET=='20,000']
            return x_2
         elif day==3 and buget==20000:
            x_3=l2.loc[l2.DAYS==3]
            x_3=x_3.loc[x_3.BUDGET=='20,000']
            return x_3
         elif day==4 and buget==20000:
            x_4=l2.loc[l2.DAYS==4]
            x_4=x_4.loc[x_4.BUDGET=='20,000']
            return x_4
         elif day==5 and buget==20000:
            x_5=l2.loc[l2.DAYS==5]
            x_5=x_5.loc[x_5.BUDGET=='20,000']
            return x_5
         elif day==6 and buget==20000:
            x_6=l2.loc[l2.DAYS==6]
            x_6=x_6.loc[x_6.BUDGET=='20,000']
            return x_6
         elif day==7 and buget==20000:
            x_7=l2.loc[l2.DAYS==7]
            x_7=x_7.loc[x_7.BUDGET=='20,000']
            return x_7
         elif day==1 and buget==15000:
            z_1=l2.loc[l2.DAYS==1]
            z_1=z_1.loc[z_1.BUDGET=='15,000']
            return z_1
         elif day==2 and buget==15000:
            z_2=l2.loc[l2.DAYS==2]
            z_2=z_2.loc[z_2.BUDGET=='15,000']
            return z_2
         elif day==3 and buget==15000:
            z_3=l2.loc[l2.DAYS==3]
            z_3=z_3.loc[z_3.BUDGET=='15,000']
            return z_3
         elif day==4 and buget==15000:
            z_4=l2.loc[l2.DAYS==4]
            z_4=z_4.loc[z_4.BUDGET=='15,000']
            return z_4
         elif day==5 and buget==15000:
            z_5=l2.loc[l2.DAYS==5]
            z_5=z_5.loc[z_5.BUDGET=='15,000']
            return z_5
         elif day==6 and buget==15000:
            z_6=l2.loc[l2.DAYS==6]
            z_6=z_6.loc[z_6.BUDGET=='15,000']
            return z_6
         elif day==7 and buget==15000:
            z_7=l2.loc[l2.DAYS==7]
            z_7=z_7.loc[z_7.BUDGET=='15,000']
            return z_7
         if day==1 and buget==50000:
            x1=l2.loc[l2.DAYS==1]
            x1=x1.loc[x1.BUDGET=='50,000']
            return x1
    
         elif day==2 and buget==50000:
            x2=l2.loc[l2.DAYS==2]
            x2=x2.loc[x2.BUDGET=='50,000']
            return x2
         elif day==3 and buget==50000:
            x3=l2.loc[l2.DAYS==3]
            x3=x3.loc[x3.BUDGET=='50,000']
            return x3
        
         elif day==4 and buget==50000:
            x4=l2.loc[l2.DAYS==4]
            x4=x4.loc[x4.BUDGET=='50,000']
            return x4
    
         elif day==5 and buget==50000:
            x5=l2.loc[l2.DAYS==5]
            x5=x5.loc[x5.BUDGET=='50,000']
            return x5
        
         elif day==6 and buget==50000:
            x6=l2.loc[l2.DAYS==6]
            x6=x6.loc[x6.BUDGET=='50,000']
            return x6
    
         elif day==7 and buget==50000:
            x7=l2.loc[l2.DAYS==7]
            x7=x7.loc[x7.BUDGET=='50,000']
            return x7
        if city=="Gilgit" or city=="gilgit" or city=="GILGIT": 
         
         if day==1 and buget==40000:
            x1=l3.loc[l3.DAYS==1]
            x1=x1.loc[x1.BUDGET=='40,000']
            return x1
         elif day==2 and buget==40000:
            x2=l3.loc[l3.DAYS==2]
            x2=x2.loc[x2.BUDGET=='40,000']
            return x2
         elif day==3 and buget==40000:
            x3=l3.loc[l3.DAYS==3]
            x3=x3.loc[x3.BUDGET=='40,000']
            return x3
        
         elif day==4 and buget==40000:
            x4=l3.loc[l3.DAYS==4]
            x4=x4.loc[x4.BUDGET=='40,000']
            return x4
    
         elif day==5 and buget==40000:
            x5=l3.loc[l3.DAYS==5]
            x5=x5.loc[x5.BUDGET=='40,000']
            return x5
        
         elif day==6 and buget==40000:
            x6=l3.loc[l3.DAYS==6]
            x6=x6.loc[x6.BUDGET=='40,000']
            return x6
    
         elif day==7 and buget==40000:
            x7=l3.loc[l3.DAYS==7]
            x7=x7.loc[x7.BUDGET=='40,000']
            return x7
         elif day==1 and buget==35000:
            y1=l3.loc[l3.DAYS==1]
            y1=y1.loc[y1.BUDGET=='35,000']
            return y1
         elif day==2 and buget==35000: 
            y2=l3.loc[l3.DAYS==2]
            y2=y2.loc[y2.BUDGET=='35,000']
            return y2
         elif day==3 and buget==35000:
            y3=l3.loc[l3.DAYS==3]
            y3=y3.loc[y3.BUDGET=='35,000']
            return y3
         elif day==4 and buget==35000:
            y4=l3.loc[l3.DAYS==4]
            y4=y4.loc[y4.BUDGET=='35,000']
            return y4
         elif day==5 and buget==35000:
            y5=l3.loc[l3.DAYS==5]
            y5=y5.loc[y5.BUDGET=='35,000']
            return y5
         elif day==6 and buget==35000:
            y6=l3.loc[l3.DAYS==6]
            y6=y6.loc[y6.BUDGET=='35,000']
            return y6
         elif day==7 and buget==35000:
            y7=l3.loc[l3.DAYS==7]
            y7=y7.loc[y7.BUDGET=='35,000']
            return y7
         elif day==1 and buget==30000:
            z1=l3.loc[l3.DAYS==1]
            z1=z1.loc[z1.BUDGET=='30,000']
            return z1
         elif day==2 and buget==30000:   
            z2=l3.loc[l3.DAYS==2]
            z2=z2.loc[z2.BUDGET=='30,000']
            return z2
         elif day==3 and buget==30000:
            z3=l3.loc[l3.DAYS==3]
            z3=z3.loc[z3.BUDGET=='30,000']
            return z3
         elif day==4 and buget==30000:
            z4=l3.loc[l3.DAYS==4]
            z4=z4.loc[z4.BUDGET=='30,000']
            return z4
         elif day==5 and buget==30000:
            z5=l3.loc[l3.DAYS==5]
            z5=z5.loc[z5.BUDGET=='30,000']
            return z5
         elif day==6 and buget==30000:
            z6=l3.loc[l3.DAYS==6]
            z6=z6.loc[z6.BUDGET=='30,000']
            return z6
         elif day==7 and buget==30000:
            z7=l3.loc[l3.DAYS==7]
            z7=z7.loc[z7.BUDGET=='30,000']
            return z7
         elif day==1 and buget==25000:   
            y_1=l3.loc[l3.DAYS==1]
            y_1=y_1.loc[y_1.BUDGET=='25,000']
            return y_1
         elif day==2 and buget==25000:
            y_2=l3.loc[l3.DAYS==2]
            y_2=y_2.loc[y_2.BUDGET=='25,000']
            return y_2
         elif day==3 and buget==25000:
            y_3=l3.loc[l3.DAYS==3]
            y_3=y_3.loc[y_3.BUDGET=='25,000']
            return y_3
         elif day==4 and buget==25000:
            y_4=l3.loc[l3.DAYS==4]
            y_4=y_4.loc[y_4.BUDGET=='25,000']
            return y_4
         elif day==5 and buget==25000:
            y_5=l3.loc[l3.DAYS==5]
            y_5=y_5.loc[y_5.BUDGET=='25,000']
            return y_5
         elif day==6 and buget==25000:
            y_6=l3.loc[l3.DAYS==6]
            y_6=y_6.loc[y_6.BUDGET=='25,000']
            return y_6
         elif day==7 and buget==25000:
            y_7=l3.loc[l3.DAYS==7]
            y_7=y_7.loc[y_7.BUDGET=='25,000']
            return y_7
         elif day==1 and buget==20000:
            x_1=l3.loc[l3.DAYS==1]
            x_1=x_1.loc[x_1.BUDGET=='20,000']
            return x_1
         elif day==2 and buget==20000:
            x_2=l3.loc[l3.DAYS==2]
            x_2=x_2.loc[x_2.BUDGET=='20,000']
            return x_2
         elif day==3 and buget==20000:
            x_3=l3.loc[l3.DAYS==3]
            x_3=x_3.loc[x_3.BUDGET=='20,000']
            return x_3
         elif day==4 and buget==20000:
            x_4=l3.loc[l3.DAYS==4]
            x_4=x_4.loc[x_4.BUDGET=='20,000']
            return x_4
         elif day==5 and buget==20000:
            x_5=l3.loc[l3.DAYS==5]
            x_5=x_5.loc[x_5.BUDGET=='20,000']
            return x_5
         elif day==6 and buget==20000:
            x_6=l3.loc[l3.DAYS==6]
            x_6=x_6.loc[x_6.BUDGET=='20,000']
            return x_6
         elif day==7 and buget==20000:
            x_7=l3.loc[l3.DAYS==7]
            x_7=x_7.loc[x_7.BUDGET=='20,000']
            return x_7
         elif day==1 and buget==15000:
            z_1=l3.loc[l3.DAYS==1]
            z_1=z_1.loc[z_1.BUDGET=='15,000']
            return z_1
         elif day==2 and buget==15000:
            z_2=l3.loc[l3.DAYS==2]
            z_2=z_2.loc[z_2.BUDGET=='15,000']
            return z_2
         elif day==3 and buget==15000:
            z_3=l3.loc[l3.DAYS==3]
            z_3=z_3.loc[z_3.BUDGET=='15,000']
            return z_3
         elif day==4 and buget==15000:
            z_4=l3.loc[l3.DAYS==4]
            z_4=z_4.loc[z_4.BUDGET=='15,000']
            return z_4
         elif day==5 and buget==15000:
            z_5=l3.loc[l3.DAYS==5]
            z_5=z_5.loc[z_5.BUDGET=='15,000']
            return z_5
         elif day==6 and buget==15000:
            z_6=l3.loc[l3.DAYS==6]
            z_6=z_6.loc[z_6.BUDGET=='15,000']
            return z_6
         elif day==7 and buget==15000:
            z_7=l3.loc[l3.DAYS==7]
            z_7=z_7.loc[z_7.BUDGET=='15,000']
            return z_7
         if day==1 and buget==50000:
            x1=l3.loc[l3.DAYS==1]
            x1=x1.loc[x1.BUDGET=='50,000']
            return x1
    
         elif day==2 and buget==50000:
            x2=l3.loc[l3.DAYS==2]
            x2=x2.loc[x2.BUDGET=='50,000']
            return x2
         elif day==3 and buget==50000:
            x3=l3.loc[l3.DAYS==3]
            x3=x3.loc[x3.BUDGET=='50,000']
            return x3
        
         elif day==4 and buget==50000:
            x4=l3.loc[l3.DAYS==4]
            x4=x4.loc[x4.BUDGET=='50,000']
            return x4
    
         elif day==5 and buget==50000:
            x5=l3.loc[l3.DAYS==5]
            x5=x5.loc[x5.BUDGET=='50,000']
            return x5
        
         elif day==6 and buget==50000:
            x6=l3.loc[l3.DAYS==6]
            x6=x6.loc[x6.BUDGET=='50,000']
            return x6
    
         elif day==7 and buget==50000:
            x7=l3.loc[l3.DAYS==7]
            x7=x7.loc[x7.BUDGET=='50,000']
            return x7 
        else:
            return "ERROR"  

      # re = z.split(' ')
      # r=list[re]
      # print(r)
      # print(re)
      # print(r[0])
      # print(r[1])
      # print(r[2])                      
      # res = tuple(map(int, z.split(' ')))
       res = tuple(map(int, z[:7].split(' ')))
       print(res)
       print(res[0])
       print(res[1])
    #   print(res[2])
       res2 = tuple(map(str, z[8:].split(' ')))
       print(res2)

       print(res2[0])


     #  words = z.split()
     #  f=tuple(map(int,words))
     #  print(f[0])
     #  print(f[1])
     #  print(f[2])
     #  print(words)
     #  print(f)


       final=get_demo_data(res[0],res[1],res2[0])
       t=final.to_json()
       print(t)
       
       print(z)
      # res = tuple(map(int, z.split(' ')))
     #  print(res[0])
      # print(res[1])
       
      

       print("Get it") 
       return t
       


      


if __name__ == '__main__':
   app.run()










       
      


      

