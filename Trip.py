import numpy as np
import pandas as pd
import json
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
    
      
      
      return z
      
   if request.method == 'GET':
      res2 = tuple(map(str, z.split(' ', 1)))
      x=res2[0]
      y=res2[1]
      print(z)
      print(res2)
      print(res2[0]) 
      print(res2[1])
      print (x)
      print (y)


      hotels_detail_1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\desktopnew.csv")
      hotels_detail_1.head()
      places_detail_1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\placesnew.csv")
      places_detail_1.head()
      p=pd.merge(places_detail_1, hotels_detail_1, on='item_id')
      #hotels_list = pd.merge(hotels_list,hotels_detail,on='item_id')
      p.head(10)
      l=p[['PLACES','THINGS_TO_DO','LOCATION_y','title','CITY_y']]
      l
      y1=l.loc[l.title==y]
      y1=y1.loc[y1.CITY_y==x]
      y1['PLACES']
      x1=y1['PLACES']

      s1 = str(x1)
      print(type(x1))
      print(type(s1))
      print(s1)

      z=y1['CITY_y']
      print(type(z))
      s2 = str(z)
      print(type(s2))
      print(s2)
      d1=(x1.head(1)).to_json()
      print(d1)
      l1=(z.head(1)).to_json()
      print(l1) 
      jsonObject = json.loads(l1)
      for key in jsonObject:
        value = jsonObject[key]
        print("The key and value are ({}) = ({})".format(key, value))
      print(value)    
      print(key)

      jsonObject = json.loads(d1)    
      for key1 in jsonObject:
         value1 = jsonObject[key1]
         print("The key and value are ({}) = ({})".format(key1, value1))
      print(value1)    
      print(key1)


      if value=="SKARDU":
   
        hotels_detail = pd.read_csv("C:\\Users\\Nova Data\\Desktop\placesnew.csv")
        hotels_detail.head()
        g =hotels_detail.groupby("CITY")
        g
  #  for CITY, data in g:
  #  print("city:",CITY)
  #  print("\n")
  #  print("data:",data)
        g.get_group('HUNZA ')
        g.get_group('GILGIT')
        g.get_group('SKARDU')
        g.get_group('ASTORE')
        g.get_group('GHIZER')
        g.get_group('DIAMER')
        g.get_group('SHIGAR')
       # column_names = ['user_id', 'item_id', 'rating', 'timestamp']
       # df = pd.read_csv('u.data', sep='\t', names=column_names)
       # df1 = pd.read_csv('u.data', sep='\t', names=column_names)
       # df2 = pd.read_csv('u.data', sep='\t', names=column_names)
       # df3 = pd.read_csv('u.data', sep='\t', names=column_names)
       # df4 = pd.read_csv('u.data', sep='\t', names=column_names)
       # df5 = pd.read_csv('u.data', sep='\t', names=column_names)
       # df6 = pd.read_csv('u.data', sep='\t', names=column_names)
        df = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
        df1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
        df2 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
        df3 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
        df4 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
        df5 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
        df6 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
       
       
        df = pd.merge(df,g.get_group('SKARDU'),on='item_id')
        df.head()
        df1 = pd.merge(df1,g.get_group('HUNZA '),on='item_id')
        df1.head()
        df2 = pd.merge(df2,g.get_group('ASTORE'),on='item_id')
        df2.head()
        df3 = pd.merge(df3,g.get_group('GILGIT'),on='item_id')
        df3.head()
        df4 = pd.merge(df4,g.get_group('DIAMER'),on='item_id')
        df4.head()
        df5 = pd.merge(df5,g.get_group('SHIGAR'),on='item_id')
        df5.head()
        df6 = pd.merge(df6,g.get_group('GHIZER'),on='item_id')
        df6.head()
        df.groupby('PLACES')['rating'].mean().sort_values(ascending=False).head()
        df.groupby('PLACES')['rating'].count().sort_values(ascending=False).head()
        ratings = pd.DataFrame(df.groupby('PLACES')['rating'].mean())
        ratings.head()
        ratings['num of ratings'] = pd.DataFrame(df.groupby('PLACES')['rating'].count())
        ratings.head()
        ratings.head()
        placemat = df.pivot_table(index='user_id',columns='PLACES',values='rating')
        placemat.head()
        ratings.sort_values('num of ratings',ascending=False).head(10)
        ratings.head()
        star_place_user_ratings = placemat[value1]
        normal_place_user_ratings = placemat[value1]
        star_place_user_ratings.head()
        similar_to_starplace = placemat.corrwith(star_place_user_ratings)
        similar_to_normalplace = placemat.corrwith(normal_place_user_ratings)
        corr_starplace = pd.DataFrame(similar_to_starplace,columns=['Correlation'])
        corr_starplace.dropna(inplace=True)
        corr_starplace.head()
        corr_starplace.sort_values('Correlation',ascending=False).head(10)
        corr_starplace = corr_starplace.join(ratings['num of ratings'])
        corr_starplace.head()
        corr_starplace[corr_starplace['num of ratings']>100].sort_values('Correlation',ascending=False).head()
        corr_normalplace = pd.DataFrame(similar_to_normalplace,columns=['Correlation'])
        corr_normalplace.dropna(inplace=True)
        corr_normalplace = corr_normalplace.join(ratings['num of ratings'])
        corr_normalplace[corr_normalplace['num of ratings']>100].sort_values('Correlation',ascending=False).head()
        xp=(corr_normalplace[corr_normalplace['num of ratings']>100].sort_values('Correlation',ascending=False).head())
        xp.reset_index(inplace=True)
        z=xp['PLACES']
    
        # print(z)
        d1=(z.head(5)).to_json()
        jsonObject = json.loads(d1)
        C = []
        for key1 in jsonObject:
            value1 = jsonObject[key1]
            C.append(value1)
        #  print(C)
        #  print(C[0])
        #  print(C[1])
        #  print(C[2])
        #  print(C[3])
        #  print(C[4])
        places_detail_1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\Places.csv")
        places_detail_1.head()
        l=places_detail_1[['PLACES','TRIP',]]
        y1=l.loc[l.PLACES==C[0]]
        #  print(y1)
        y2=l.loc[l.PLACES==C[1]]
        #  print(y2)
        y3=l.loc[l.PLACES==C[2]]
        #  print(y3)
        y4=l.loc[l.PLACES==C[3]]
        #  print(y4)
        y5=l.loc[l.PLACES==C[4]]
        #  print(y5)
        X=y1.append(y2)
        Y=X.append(y3)
        Z=Y.append(y4)
        Z1=Z.append(y5)
       #print(Z1)
        z=Z1.to_json()
        print(z)
        return z



      if value=="HUNZA":
 
         hotels_detail = pd.read_csv("C:\\Users\\Nova Data\\Desktop\placesnew.csv")
         hotels_detail.head()
         g =hotels_detail.groupby("CITY")
         g
     #    for CITY, data in g:
     #    print("city:",CITY)
      #   print("\n")
      #   print("data:",data)
         g.get_group('HUNZA ')
         g.get_group('GILGIT')
         g.get_group('SKARDU')
         g.get_group('ASTORE')
         g.get_group('GHIZER')
         g.get_group('DIAMER')
         g.get_group('SHIGAR')
         column_names = ['user_id', 'item_id', 'rating', 'timestamp']
        # df = pd.read_csv('u.data', sep='\t', names=column_names)
        # df1 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df2 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df3 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df4 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df5 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df6 = pd.read_csv('u.data', sep='\t', names=column_names)
         df = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df2 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df3 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df4 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df5 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df6 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         
         
         
         df = pd.merge(df,g.get_group('SKARDU'),on='item_id')
         df.head()
         df1 = pd.merge(df1,g.get_group('HUNZA '),on='item_id')
         df1.head()
         df2 = pd.merge(df2,g.get_group('ASTORE'),on='item_id')
         df2.head()
         df3 = pd.merge(df3,g.get_group('GILGIT'),on='item_id')
         df3.head()
         df4 = pd.merge(df4,g.get_group('DIAMER'),on='item_id')
         df4.head()
         df5 = pd.merge(df5,g.get_group('SHIGAR'),on='item_id')
         df5.head()
         df6 = pd.merge(df6,g.get_group('GHIZER'),on='item_id')
         df6.head()
         df1.groupby('PLACES')['rating'].mean().sort_values(ascending=False).head()
         df1.groupby('PLACES')['rating'].count().sort_values(ascending=False).head()
         ratings = pd.DataFrame(df1.groupby('PLACES')['rating'].mean())
         ratings.head()
         ratings['num of ratings'] = pd.DataFrame(df1.groupby('PLACES')['rating'].count())
         ratings.head()
         ratings.head()
         placemat = df1.pivot_table(index='user_id',columns='PLACES',values='rating')
         placemat.head()
         ratings.sort_values('num of ratings',ascending=False).head(10)
         ratings.head()
         star_place_user_ratings = placemat[value1]
         normal_place_user_ratings = placemat[value1]
         star_place_user_ratings.head()
         similar_to_starplace = placemat.corrwith(star_place_user_ratings)
         similar_to_normalplace = placemat.corrwith(normal_place_user_ratings)
         corr_starplace = pd.DataFrame(similar_to_starplace,columns=['Correlation'])
         corr_starplace.dropna(inplace=True)
         corr_starplace.head()
         corr_starplace.sort_values('Correlation',ascending=False).head(10)
         corr_starplace = corr_starplace.join(ratings['num of ratings'])
         corr_starplace.head()
         corr_starplace[corr_starplace['num of ratings']>100].sort_values('Correlation',ascending=False).head()
         corr_normalplace = pd.DataFrame(similar_to_normalplace,columns=['Correlation'])
         corr_normalplace.dropna(inplace=True)
         corr_normalplace = corr_normalplace.join(ratings['num of ratings'])
         corr_normalplace[corr_normalplace['num of ratings']>100].sort_values('Correlation',ascending=False).head()
         xp=(corr_normalplace[corr_normalplace['num of ratings']>100].sort_values('Correlation',ascending=False).head())
         xp.reset_index(inplace=True)
         z=xp['PLACES']
    
        # print(z)
         d1=(z.head(5)).to_json()
         jsonObject = json.loads(d1)
         C = []
         for key1 in jsonObject:
             value1 = jsonObject[key1]
             C.append(value1)
        #  print(C)
        #  print(C[0])
        #  print(C[1])
        #  print(C[2])
        #  print(C[3])
        #  print(C[4])
         places_detail_1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\Places.csv")
         places_detail_1.head()
         l=places_detail_1[['PLACES','TRIP',]]
         y1=l.loc[l.PLACES==C[0]]
         #  print(y1)
         y2=l.loc[l.PLACES==C[1]]
         #  print(y2)
         y3=l.loc[l.PLACES==C[2]]
         #  print(y3)
         y4=l.loc[l.PLACES==C[3]]
         #  print(y4)
         y5=l.loc[l.PLACES==C[4]]
         #  print(y5)
         X=y1.append(y2)
         Y=X.append(y3)
         Z=Y.append(y4)
         Z1=Z.append(y5)
        #print(Z1)
         z=Z1.to_json()
         print(z)
         return z   
      if value=="ASTORE": 
         hotels_detail = pd.read_csv("C:\\Users\\Nova Data\\Desktop\placesnew.csv")
         hotels_detail.head()
         g =hotels_detail.groupby("CITY")
         g
        # for CITY, data in g:
        # print("city:",CITY)
        # print("\n")
        # print("data:",data)
         g.get_group('HUNZA ')
         g.get_group('GILGIT')
         g.get_group('SKARDU')
         g.get_group('ASTORE')
         g.get_group('GHIZER')
         g.get_group('DIAMER')
         g.get_group('SHIGAR')
        # column_names = ['user_id', 'item_id', 'rating', 'timestamp']
        # df = pd.read_csv('u.data', sep='\t', names=column_names)
        # df1 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df2 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df3 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df4 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df5 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df6 = pd.read_csv('u.data', sep='\t', names=column_names)
         df = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df2 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df3 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df4 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df5 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df6 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         
         
         df = pd.merge(df,g.get_group('SKARDU'),on='item_id')
         df.head()
         df1 = pd.merge(df1,g.get_group('HUNZA '),on='item_id')
         df1.head()
         df2 = pd.merge(df2,g.get_group('ASTORE'),on='item_id')
         df2.head()
         df3 = pd.merge(df3,g.get_group('GILGIT'),on='item_id')
         df3.head()
         df4 = pd.merge(df4,g.get_group('DIAMER'),on='item_id')
         df4.head()
         df5 = pd.merge(df5,g.get_group('SHIGAR'),on='item_id')
         df5.head()
         df6 = pd.merge(df6,g.get_group('GHIZER'),on='item_id')
         df6.head()
         df2.groupby('PLACES')['rating'].mean().sort_values(ascending=False).head()
         df2.groupby('PLACES')['rating'].count().sort_values(ascending=False).head()
         ratings = pd.DataFrame(df2.groupby('PLACES')['rating'].mean())
         ratings.head()
         ratings['num of ratings'] = pd.DataFrame(df2.groupby('PLACES')['rating'].count())
         ratings.head()
         ratings.head()
         placemat = df2.pivot_table(index='user_id',columns='PLACES',values='rating')
         placemat.head()
         ratings.sort_values('num of ratings',ascending=False).head(10)
         ratings.head()
         star_place_user_ratings = placemat[value1]
         normal_place_user_ratings = placemat[value1]
         star_place_user_ratings.head()
         similar_to_starplace = placemat.corrwith(star_place_user_ratings)
         similar_to_normalplace = placemat.corrwith(normal_place_user_ratings)
         corr_starplace = pd.DataFrame(similar_to_starplace,columns=['Correlation'])
         corr_starplace.dropna(inplace=True)
         corr_starplace.head()
         corr_starplace.sort_values('Correlation',ascending=False).head(10)
         corr_starplace = corr_starplace.join(ratings['num of ratings'])
         corr_starplace.head()
         corr_starplace[corr_starplace['num of ratings']>100].sort_values('Correlation',ascending=False).head()
         corr_normalplace = pd.DataFrame(similar_to_normalplace,columns=['Correlation'])
         corr_normalplace.dropna(inplace=True)
         corr_normalplace = corr_normalplace.join(ratings['num of ratings'])
         corr_normalplace[corr_normalplace['num of ratings']>100].sort_values('Correlation',ascending=False).head()
         xp=(corr_normalplace[corr_normalplace['num of ratings']>100].sort_values('Correlation',ascending=False).head())
         xp.reset_index(inplace=True)
         z=xp['PLACES']
    
        # print(z)
         d1=(z.head(5)).to_json()
         jsonObject = json.loads(d1)
         C = []
         for key1 in jsonObject:
             value1 = jsonObject[key1]
             C.append(value1)
        #  print(C)
        #  print(C[0])
        #  print(C[1])
        #  print(C[2])
        #  print(C[3])
        #  print(C[4])
         places_detail_1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\Places.csv")
         places_detail_1.head()
         l=places_detail_1[['PLACES','TRIP',]]
         y1=l.loc[l.PLACES==C[0]]
     #    print(y1)
         y2=l.loc[l.PLACES==C[1]]
      #   print(y2)
         y3=l.loc[l.PLACES==C[2]]
      #   print(y3)
      #   y4=l.loc[l.PLACES==C[3]]
      #   print(y4)
      #   y5=l.loc[l.PLACES==C[4]]
      #   print(y5)
         X=y1.append(y2)
         Y=X.append(y3)
       #  Z=Y.append(y4)
       #  Z1=Z.append(y5)
        #print(Z1)
         z=Y.to_json()
         print(z)
         return z 
         
      if value=="GILGIT": 
         hotels_detail = pd.read_csv("C:\\Users\\Nova Data\\Desktop\placesnew.csv")
         hotels_detail.head()
         g =hotels_detail.groupby("CITY")
         g
        # for CITY, data in g:
        # print("city:",CITY)
        # print("\n")
        # print("data:",data)
         g.get_group('HUNZA ')
         g.get_group('GILGIT')
         g.get_group('SKARDU')
         g.get_group('ASTORE')
         g.get_group('GHIZER')
         g.get_group('DIAMER')
         g.get_group('SHIGAR')
        # column_names = ['user_id', 'item_id', 'rating', 'timestamp']
        # df = pd.read_csv('u.data', sep='\t', names=column_names)
        # df1 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df2 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df3 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df4 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df5 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df6 = pd.read_csv('u.data', sep='\t', names=column_names)
         df = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df2 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df3 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df4 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df5 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df6 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
        
        
        
         df = pd.merge(df,g.get_group('SKARDU'),on='item_id')
         df.head()
         df1 = pd.merge(df1,g.get_group('HUNZA '),on='item_id')
         df1.head()
         df2 = pd.merge(df2,g.get_group('ASTORE'),on='item_id')
         df2.head()
         df3 = pd.merge(df3,g.get_group('GILGIT'),on='item_id')
         df3.head()
         df4 = pd.merge(df4,g.get_group('DIAMER'),on='item_id')
         df4.head()
         df5 = pd.merge(df5,g.get_group('SHIGAR'),on='item_id')
         df5.head()
         df6 = pd.merge(df6,g.get_group('GHIZER'),on='item_id')
         df6.head()
         df3.groupby('PLACES')['rating'].mean().sort_values(ascending=False).head()
         df3.groupby('PLACES')['rating'].count().sort_values(ascending=False).head()
         ratings = pd.DataFrame(df3.groupby('PLACES')['rating'].mean())
         ratings.head()
         ratings['num of ratings'] = pd.DataFrame(df3.groupby('PLACES')['rating'].count())
         ratings.head()
         ratings.head()
         placemat = df3.pivot_table(index='user_id',columns='PLACES',values='rating')
         placemat.head()
         ratings.sort_values('num of ratings',ascending=False).head(10)
         ratings.head()
         star_place_user_ratings = placemat[value1]
         normal_place_user_ratings = placemat[value1]
         star_place_user_ratings.head()
         similar_to_starplace = placemat.corrwith(star_place_user_ratings)
         similar_to_normalplace = placemat.corrwith(normal_place_user_ratings)
         corr_starplace = pd.DataFrame(similar_to_starplace,columns=['Correlation'])
         corr_starplace.dropna(inplace=True)
         corr_starplace.head()
         corr_starplace.sort_values('Correlation',ascending=False).head(10)
         corr_starplace = corr_starplace.join(ratings['num of ratings'])
         corr_starplace.head()
         corr_starplace[corr_starplace['num of ratings']>100].sort_values('Correlation',ascending=False).head()
         corr_normalplace = pd.DataFrame(similar_to_normalplace,columns=['Correlation'])
         corr_normalplace.dropna(inplace=True)
         corr_normalplace = corr_normalplace.join(ratings['num of ratings'])
         corr_normalplace[corr_normalplace['num of ratings']>100].sort_values('Correlation',ascending=False).head()
         xp=(corr_normalplace[corr_normalplace['num of ratings']>100].sort_values('Correlation',ascending=False).head())
         xp.reset_index(inplace=True)
         z=xp['PLACES']
    
        # print(z)
         d1=(z.head(5)).to_json()
         jsonObject = json.loads(d1)
         C = []
         for key1 in jsonObject:
             value1 = jsonObject[key1]
             C.append(value1)
        #  print(C)
        #  print(C[0])
        #  print(C[1])
        #  print(C[2])
        #  print(C[3])
        #  print(C[4])
         places_detail_1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\Places.csv")
         places_detail_1.head()
         l=places_detail_1[['PLACES','TRIP',]]
         y1=l.loc[l.PLACES==C[0]]
         #  print(y1)
         y2=l.loc[l.PLACES==C[1]]
         #  print(y2)
         y3=l.loc[l.PLACES==C[2]]
         #  print(y3)
         y4=l.loc[l.PLACES==C[3]]
         #  print(y4)
         y5=l.loc[l.PLACES==C[4]]
         #  print(y5)
         X=y1.append(y2)
         Y=X.append(y3)
         Z=Y.append(y4)
         Z1=Z.append(y5)
        #print(Z1)
         z=Z1.to_json()
         print(z)
         return z 
      if value=="DIAMER": 
         hotels_detail = pd.read_csv("C:\\Users\\Nova Data\\Desktop\placesnew.csv")
         hotels_detail.head()
         g =hotels_detail.groupby("CITY")
         g
       #  for CITY, data in g:
       #  print("city:",CITY)
       #  print("\n")
       #  print("data:",data)
         g.get_group('HUNZA ')
         g.get_group('GILGIT')
         g.get_group('SKARDU')
         g.get_group('ASTORE')
         g.get_group('GHIZER')
         g.get_group('DIAMER')
         g.get_group('SHIGAR')
        # column_names = ['user_id', 'item_id', 'rating', 'timestamp']
        # df = pd.read_csv('u.data', sep='\t', names=column_names)
        # df1 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df2 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df3 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df4 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df5 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df6 = pd.read_csv('u.data', sep='\t', names=column_names)
         df = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df2 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df3 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df4 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df5 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df6 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         
         
         df = pd.merge(df,g.get_group('SKARDU'),on='item_id')
         df.head()
         df1 = pd.merge(df1,g.get_group('HUNZA '),on='item_id')
         df1.head()
         df2 = pd.merge(df2,g.get_group('ASTORE'),on='item_id')
         df2.head()
         df3 = pd.merge(df3,g.get_group('GILGIT'),on='item_id')
         df3.head()
         df4 = pd.merge(df4,g.get_group('DIAMER'),on='item_id')
         df4.head()
         df5 = pd.merge(df5,g.get_group('SHIGAR'),on='item_id')
         df5.head()
         df6 = pd.merge(df6,g.get_group('GHIZER'),on='item_id')
         df6.head()
         df4.groupby('PLACES')['rating'].mean().sort_values(ascending=False).head()
         df4.groupby('PLACES')['rating'].count().sort_values(ascending=False).head()
         ratings = pd.DataFrame(df4.groupby('PLACES')['rating'].mean())
         ratings.head()
         ratings['num of ratings'] = pd.DataFrame(df4.groupby('PLACES')['rating'].count())
         ratings.head()
         ratings.head()
         placemat = df4.pivot_table(index='user_id',columns='PLACES',values='rating')
         placemat.head()
         ratings.sort_values('num of ratings',ascending=False).head(10)
         ratings.head()
         star_place_user_ratings = placemat[value1]
         normal_place_user_ratings = placemat[value1]
         star_place_user_ratings.head()
         similar_to_starplace = placemat.corrwith(star_place_user_ratings)
         similar_to_normalplace = placemat.corrwith(normal_place_user_ratings)
         corr_starplace = pd.DataFrame(similar_to_starplace,columns=['Correlation'])
         corr_starplace.dropna(inplace=True)
         corr_starplace.head()
         corr_starplace.sort_values('Correlation',ascending=False).head(10)
         corr_starplace = corr_starplace.join(ratings['num of ratings'])
         corr_starplace.head()
         corr_starplace[corr_starplace['num of ratings']>100].sort_values('Correlation',ascending=False).head()
         corr_normalplace = pd.DataFrame(similar_to_normalplace,columns=['Correlation'])
         corr_normalplace.dropna(inplace=True)
         corr_normalplace = corr_normalplace.join(ratings['num of ratings'])
         corr_normalplace[corr_normalplace['num of ratings']>100].sort_values('Correlation',ascending=False).head()
         xp=(corr_normalplace[corr_normalplace['num of ratings']>100].sort_values('Correlation',ascending=False).head())
         xp.reset_index(inplace=True)
         z=xp['PLACES']
    
        # print(z)
         d1=(z.head(5)).to_json()
         jsonObject = json.loads(d1)
         C = []
         for key1 in jsonObject:
             value1 = jsonObject[key1]
             C.append(value1)
        #  print(C)
        #  print(C[0])
        #  print(C[1])
        #  print(C[2])
        #  print(C[3])
        #  print(C[4])
         places_detail_1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\Places.csv")
         places_detail_1.head()
         l=places_detail_1[['PLACES','TRIP',]]
         y1=l.loc[l.PLACES==C[0]]
         #  print(y1)
         y2=l.loc[l.PLACES==C[1]]
         #  print(y2)
         y3=l.loc[l.PLACES==C[2]]
         #  print(y3)
         y4=l.loc[l.PLACES==C[3]]
         #  print(y4)
         y5=l.loc[l.PLACES==C[4]]
         #  print(y5)
         X=y1.append(y2)
         Y=X.append(y3)
         Z=Y.append(y4)
         Z1=Z.append(y5)
        #print(Z1)
         z=Z1.to_json()
         print(z)
         return z 
      if value=="SHIGAR": 
         hotels_detail = pd.read_csv("C:\\Users\\Nova Data\\Desktop\placesnew.csv")
         hotels_detail.head()
         g =hotels_detail.groupby("CITY")
         g
        # for CITY, data in g:
        # print("city:",CITY)
        # print("\n")
        # print("data:",data)
         g.get_group('HUNZA ')
         g.get_group('GILGIT')
         g.get_group('SKARDU')
         g.get_group('ASTORE')
         g.get_group('GHIZER')
         g.get_group('DIAMER')
         g.get_group('SHIGAR')
       #  column_names = ['user_id', 'item_id', 'rating', 'timestamp']
       #  df = pd.read_csv('u.data', sep='\t', names=column_names)
       #  df1 = pd.read_csv('u.data', sep='\t', names=column_names)
       #  df2 = pd.read_csv('u.data', sep='\t', names=column_names)
       #  df3 = pd.read_csv('u.data', sep='\t', names=column_names)
       #  df4 = pd.read_csv('u.data', sep='\t', names=column_names)
       #  df5 = pd.read_csv('u.data', sep='\t', names=column_names)
       #  df6 = pd.read_csv('u.data', sep='\t', names=column_names)
         df = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df2 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df3 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df4 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df5 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df6 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
        
        
        
        
        
        
         df = pd.merge(df,g.get_group('SKARDU'),on='item_id')
         df.head()   
         df1 = pd.merge(df1,g.get_group('HUNZA '),on='item_id')
         df1.head()
         df2 = pd.merge(df2,g.get_group('ASTORE'),on='item_id')
         df2.head()
         df3 = pd.merge(df3,g.get_group('GILGIT'),on='item_id')
         df3.head()
         df4 = pd.merge(df4,g.get_group('DIAMER'),on='item_id')
         df4.head()
         df5 = pd.merge(df5,g.get_group('SHIGAR'),on='item_id')
         df5.head()
         df6 = pd.merge(df6,g.get_group('GHIZER'),on='item_id')
         df6.head()

         df5.groupby('PLACES')['rating'].mean().sort_values(ascending=False).head()
         df5.groupby('PLACES')['rating'].count().sort_values(ascending=False).head()
         ratings = pd.DataFrame(df5.groupby('PLACES')['rating'].mean())
         ratings.head()
         ratings['num of ratings'] = pd.DataFrame(df5.groupby('PLACES')['rating'].count())
         ratings.head()
         ratings.head()
         placemat = df5.pivot_table(index='user_id',columns='PLACES',values='rating')
         placemat.head()
         ratings.sort_values('num of ratings',ascending=False).head(10)
         ratings.head()
         star_place_user_ratings = placemat[value1]
         normal_place_user_ratings = placemat[value1]
         star_place_user_ratings.head()
         similar_to_starplace = placemat.corrwith(star_place_user_ratings)
         similar_to_normalplace = placemat.corrwith(normal_place_user_ratings)
         corr_starplace = pd.DataFrame(similar_to_starplace,columns=['Correlation'])
         corr_starplace.dropna(inplace=True)
         corr_starplace.head()
         corr_starplace.sort_values('Correlation',ascending=False).head(10)
         corr_starplace = corr_starplace.join(ratings['num of ratings'])
         corr_starplace.head()
         corr_starplace[corr_starplace['num of ratings']>100].sort_values('Correlation',ascending=False).head()
         corr_normalplace = pd.DataFrame(similar_to_normalplace,columns=['Correlation'])
         corr_normalplace.dropna(inplace=True)
         corr_normalplace = corr_normalplace.join(ratings['num of ratings'])
         corr_normalplace[corr_normalplace['num of ratings']>100].sort_values('Correlation',ascending=False).head()
         xp=(corr_normalplace[corr_normalplace['num of ratings']>100].sort_values('Correlation',ascending=False).head())
         xp.reset_index(inplace=True)
         z=xp['PLACES']
    
        # print(z)
         d1=(z.head(5)).to_json()
         jsonObject = json.loads(d1)
         C = []
         for key1 in jsonObject:
             value1 = jsonObject[key1]
             C.append(value1)
        #  print(C)
        #  print(C[0])
        #  print(C[1])
        #  print(C[2])
        #  print(C[3])
        #  print(C[4])
         places_detail_1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\Places.csv")
         places_detail_1.head()
         l=places_detail_1[['PLACES','TRIP',]]
         y1=l.loc[l.PLACES==C[0]]
         #  print(y1)
         y2=l.loc[l.PLACES==C[1]]
         #  print(y2)
         y3=l.loc[l.PLACES==C[2]]
         #  print(y3)
         y4=l.loc[l.PLACES==C[3]]
         #  print(y4)
         y5=l.loc[l.PLACES==C[4]]
         #  print(y5)
         X=y1.append(y2)
         Y=X.append(y3)
         Z=Y.append(y4)
         Z1=Z.append(y5)
        #print(Z1)
         z=Z1.to_json()
         print(z)
         return z    
      if value=="GHIZER": 
         hotels_detail = pd.read_csv("C:\\Users\\Nova Data\\Desktop\placesnew.csv")
         hotels_detail.head()
         g =hotels_detail.groupby("CITY")
         g
         #for CITY, data in g:
         #print("city:",CITY)
         #print("\n")
         #print("data:",data)
         g.get_group('HUNZA ')
         g.get_group('GILGIT')
         g.get_group('SKARDU')
         g.get_group('ASTORE')
         g.get_group('GHIZER')
         g.get_group('DIAMER')
         g.get_group('SHIGAR')
        # column_names = ['user_id', 'item_id', 'rating', 'timestamp']
        # df = pd.read_csv('u.data', sep='\t', names=column_names)
        # df1 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df2 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df3 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df4 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df5 = pd.read_csv('u.data', sep='\t', names=column_names)
        # df6 = pd.read_csv('u.data', sep='\t', names=column_names)
         df = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df2 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df3 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df4 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df5 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         df6 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
         
         
         
         df = pd.merge(df,g.get_group('SKARDU'),on='item_id')
         df.head()
         df1 = pd.merge(df1,g.get_group('HUNZA '),on='item_id')
         df1.head()
         df2 = pd.merge(df2,g.get_group('ASTORE'),on='item_id')
         df2.head()
         df3 = pd.merge(df3,g.get_group('GILGIT'),on='item_id')
         df3.head()
         df4 = pd.merge(df4,g.get_group('DIAMER'),on='item_id')
         df4.head()
         df5 = pd.merge(df5,g.get_group('SHIGAR'),on='item_id')
         df5.head()
         df6 = pd.merge(df6,g.get_group('GHIZER'),on='item_id')
         df6.head()

         df6.groupby('PLACES')['rating'].mean().sort_values(ascending=False).head()
         df6.groupby('PLACES')['rating'].count().sort_values(ascending=False).head()
         ratings = pd.DataFrame(df6.groupby('PLACES')['rating'].mean())
         ratings.head()
         ratings['num of ratings'] = pd.DataFrame(df6.groupby('PLACES')['rating'].count())
         ratings.head()
         ratings.head()
         placemat = df6.pivot_table(index='user_id',columns='PLACES',values='rating')
         placemat.head()
         ratings.sort_values('num of ratings',ascending=False).head(10)
         ratings.head()
         star_place_user_ratings = placemat[value1]
         normal_place_user_ratings = placemat[value1]
         star_place_user_ratings.head()
         similar_to_starplace = placemat.corrwith(star_place_user_ratings)
         similar_to_normalplace = placemat.corrwith(normal_place_user_ratings)
         corr_starplace = pd.DataFrame(similar_to_starplace,columns=['Correlation'])
         corr_starplace.dropna(inplace=True)
         corr_starplace.head()
         corr_starplace.sort_values('Correlation',ascending=False).head(10)
         corr_starplace = corr_starplace.join(ratings['num of ratings'])
         corr_starplace.head()
         corr_starplace[corr_starplace['num of ratings']>100].sort_values('Correlation',ascending=False).head()
         corr_normalplace = pd.DataFrame(similar_to_normalplace,columns=['Correlation'])
         corr_normalplace.dropna(inplace=True)
         corr_normalplace = corr_normalplace.join(ratings['num of ratings'])
         corr_normalplace[corr_normalplace['num of ratings']>100].sort_values('Correlation',ascending=False).head()
         xp=(corr_normalplace[corr_normalplace['num of ratings']>100].sort_values('Correlation',ascending=False).head())
         xp.reset_index(inplace=True)
         z=xp['PLACES']
    
        # print(z)
         d1=(z.head(5)).to_json()
         jsonObject = json.loads(d1)
         C = []
         for key1 in jsonObject:
             value1 = jsonObject[key1]
             C.append(value1)
        #  print(C)
        #  print(C[0])
        #  print(C[1])
        #  print(C[2])
        #  print(C[3])
        #  print(C[4])
         places_detail_1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\Places.csv")
         places_detail_1.head()
         l=places_detail_1[['PLACES','TRIP',]]
         y1=l.loc[l.PLACES==C[0]]
         #  print(y1)
         y2=l.loc[l.PLACES==C[1]]
         #  print(y2)
         y3=l.loc[l.PLACES==C[2]]
         #  print(y3)
         y4=l.loc[l.PLACES==C[3]]
         #  print(y4)
         y5=l.loc[l.PLACES==C[4]]
         #  print(y5)
         X=y1.append(y2)
         Y=X.append(y3)
         Z=Y.append(y4)
         Z1=Z.append(y5)
        #print(Z1)
         z=Z1.to_json()
         print(z)
         return z 








       
if __name__ == '__main__':
   app.run( port=7000 )
