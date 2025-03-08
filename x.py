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







      
      if x=="SKARDU": 
        hotels_detail = pd.read_csv("C:\\Users\\Nova Data\\Desktop\desktopnew.csv")
        hotels_detail.head()
        hotels_detail.shape
        g =hotels_detail.groupby("CITY")
        g
       # for CITY, data in g:
       # print("city:",CITY)
       #print("\n")
       # print("data:",data)
        g.get_group('HUNZA')
        g.get_group('ASTORE')
        g.get_group('GILGIT')
        g.get_group('SKARDU')
        hotels_list = pd.read_csv("C:\\Users\\Nova Data\\Desktop\H_list1new.csv")
        hotels_list.head(15)
       # column_names = ['user_id', 'item_id', 'rating', 'timestamp']
       # df = pd.read_csv('u.data', sep='\t', names=column_names)
       # df1 = pd.read_csv('u.data', sep='\t', names=column_names) 
       # df2 = pd.read_csv('u.data', sep='\t', names=column_names)
       # df3 = pd.read_csv('u.data', sep='\t', names=column_names)
        df = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
        df1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
        df2 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
        df3 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
     
      
      
      
      
      
      
        df.head(5)
        df = pd.merge(df,g.get_group('SKARDU'),on='item_id')
        df.head()
        df1 = pd.merge(df1,g.get_group('HUNZA'),on='item_id')
        df1.head()
        df2 = pd.merge(df2,g.get_group('ASTORE'),on='item_id')
        df2.head()
        df3 = pd.merge(df3,g.get_group('GILGIT'),on='item_id')
        df3.head()
        df.groupby('title')['rating'].mean().sort_values(ascending=False).head()
        import matplotlib.pyplot as plt
        import seaborn as sns
        sns.set_style('white')
        df.groupby('title')['rating'].mean().sort_values(ascending=False).head()
        df.groupby('title')['rating'].count().sort_values(ascending=False).head()
        ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
        ratings.head()
        ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
        ratings.head()
        ratings.head()
        hotelmat = df.pivot_table(index='user_id',columns='title',values='rating')
        hotelmat.head()
        ratings.sort_values('num of ratings',ascending=False).head(10)
        ratings.head()
        star_user_ratings = hotelmat[y]
        standard_user_ratings = hotelmat[y]
        star_user_ratings.head()
        similar_to_star = hotelmat.corrwith(star_user_ratings)
        similar_to_standard = hotelmat.corrwith(standard_user_ratings)
        corr_star = pd.DataFrame(similar_to_star,columns=['Correlation'])
        corr_star.dropna(inplace=True)
        corr_star.head()
        corr_star.sort_values('Correlation',ascending=False).head(10)
        corr_star = corr_star.join(ratings['num of ratings'])
        corr_star.head()
        corr_star[corr_star['num of ratings']>100].sort_values('Correlation',ascending=False).head()
        corr_standard = pd.DataFrame(similar_to_standard,columns=['Correlation'])
        corr_standard.dropna(inplace=True)
        corr_standard = corr_standard.join(ratings['num of ratings'])
        xp=(corr_standard[corr_standard['num of ratings']>100].sort_values('Correlation',ascending=False).head())
        xp.reset_index(inplace=True)
        z=xp.to_json()
      #  print(z)
        return z
      if x=="HUNZA": 
        hotels_detail = pd.read_csv("C:\\Users\\Nova Data\\Desktop\desktopnew.csv")
        hotels_detail.head()
        hotels_detail.shape
        g =hotels_detail.groupby("CITY")
        g
        #for CITY, data in g:
         #print("city:",CITY)
         #print("\n")
         #print("data:",data)
        g.get_group('HUNZA')
        g.get_group('ASTORE')
        g.get_group('GILGIT')
        g.get_group('SKARDU')
        hotels_list = pd.read_csv("C:\\Users\\Nova Data\\Desktop\H_list1new.csv")
        hotels_list.head(15)
      #  column_names = ['user_id', 'item_id', 'rating', 'timestamp']
      #  df = pd.read_csv('u.data', sep='\t', names=column_names)
      #  df1 = pd.read_csv('u.data', sep='\t', names=column_names)
      #  df2 = pd.read_csv('u.data', sep='\t', names=column_names)
      #  df3 = pd.read_csv('u.data', sep='\t', names=column_names)
        df = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
        df1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
        df2 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
        df3 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
      
      
      
        df.head(5)
        df = pd.merge(df,g.get_group('SKARDU'),on='item_id')
        df.head()
        df1 = pd.merge(df1,g.get_group('HUNZA'),on='item_id')
        df1.head()
        df2 = pd.merge(df2,g.get_group('ASTORE'),on='item_id')
        df2.head()
        df3 = pd.merge(df3,g.get_group('GILGIT'),on='item_id')
        df3.head()
        df1.groupby('title')['rating'].mean().sort_values(ascending=False).head()
        import matplotlib.pyplot as plt
        import seaborn as sns
        sns.set_style('white')
        df1.groupby('title')['rating'].mean().sort_values(ascending=False).head()
        df1.groupby('title')['rating'].count().sort_values(ascending=False).head()
        ratings = pd.DataFrame(df1.groupby('title')['rating'].mean())
        ratings.head()
        ratings['num of ratings'] = pd.DataFrame(df1.groupby('title')['rating'].count())
        ratings.head()
        ratings.head()
        hotelmat = df1.pivot_table(index='user_id',columns='title',values='rating')
        hotelmat.head()
        ratings.sort_values('num of ratings',ascending=False).head(10)
        ratings.head()
        star_user_ratings = hotelmat[y]
        standard_user_ratings = hotelmat[y]
        star_user_ratings.head()
        similar_to_star = hotelmat.corrwith(star_user_ratings)
        similar_to_standard = hotelmat.corrwith(standard_user_ratings)
        corr_star = pd.DataFrame(similar_to_star,columns=['Correlation'])
        corr_star.dropna(inplace=True)
        corr_star.head()
        corr_star.sort_values('Correlation',ascending=False).head(10)
        corr_star = corr_star.join(ratings['num of ratings'])
        corr_star.head()
        corr_star[corr_star['num of ratings']>100].sort_values('Correlation',ascending=False).head()
        corr_standard = pd.DataFrame(similar_to_standard,columns=['Correlation'])
        corr_standard.dropna(inplace=True)
        corr_standard = corr_standard.join(ratings['num of ratings'])
        corr_standard[corr_standard['num of ratings']>100].sort_values('Correlation',ascending=False).head()
        xp=(corr_standard[corr_standard['num of ratings']>100].sort_values('Correlation',ascending=False).head())
        xp.reset_index(inplace=True)
        z=xp.to_json()
        return z
      if x=="ASTORE": 
        hotels_detail = pd.read_csv("C:\\Users\\Nova Data\\Desktop\desktopnew.csv")
        hotels_detail.head()
        hotels_detail.shape
        g =hotels_detail.groupby("CITY")
        g
       # for CITY, data in g:
        #   print("city:",CITY)
        #   print("\n")
         #  print("data:",data)
        g.get_group('HUNZA')
        g.get_group('ASTORE')
        g.get_group('GILGIT')
        g.get_group('SKARDU')
        hotels_list = pd.read_csv("C:\\Users\\Nova Data\\Desktop\H_list1new.csv")
        hotels_list.head(15)
       # column_names = ['user_id', 'item_id', 'rating', 'timestamp']
       # df = pd.read_csv('u.data', sep='\t', names=column_names)
       # df1 = pd.read_csv('u.data', sep='\t', names=column_names)
       # df2 = pd.read_csv('u.data', sep='\t', names=column_names)
       # df3 = pd.read_csv('u.data', sep='\t', names=column_names)
        df = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
        df1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
        df2 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
        df3 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
       
        df.head(5)
        df = pd.merge(df,g.get_group('SKARDU'),on='item_id')
        df.head()
        df1 = pd.merge(df1,g.get_group('HUNZA'),on='item_id')
        df1.head()
        df2 = pd.merge(df2,g.get_group('ASTORE'),on='item_id')
        df2.head()
        df3 = pd.merge(df3,g.get_group('GILGIT'),on='item_id')
        df3.head()
        df1.groupby('title')['rating'].mean().sort_values(ascending=False).head()
        import matplotlib.pyplot as plt
        import seaborn as sns
        sns.set_style('white')
        df2.groupby('title')['rating'].mean().sort_values(ascending=False).head()
        df2.groupby('title')['rating'].count().sort_values(ascending=False).head()
        ratings = pd.DataFrame(df2.groupby('title')['rating'].mean())
        ratings.head()
        ratings['num of ratings'] = pd.DataFrame(df2.groupby('title')['rating'].count())
        ratings.head()
        ratings.head()
        hotelmat = df2.pivot_table(index='user_id',columns='title',values='rating')
        hotelmat.head()
        ratings.sort_values('num of ratings',ascending=False).head(10)
        ratings.head()
        star_user_ratings = hotelmat[y]
        standard_user_ratings = hotelmat[y]
        star_user_ratings.head()
        similar_to_star = hotelmat.corrwith(star_user_ratings)
        similar_to_standard = hotelmat.corrwith(standard_user_ratings)
        corr_star = pd.DataFrame(similar_to_star,columns=['Correlation'])
        corr_star.dropna(inplace=True)
        corr_star.head()
        corr_star.sort_values('Correlation',ascending=False).head(10)
        corr_star = corr_star.join(ratings['num of ratings'])
        corr_star.head()
        corr_star[corr_star['num of ratings']>100].sort_values('Correlation',ascending=False).head()
        corr_standard = pd.DataFrame(similar_to_standard,columns=['Correlation'])
        corr_standard.dropna(inplace=True)
        corr_standard = corr_standard.join(ratings['num of ratings'])
        corr_standard[corr_standard['num of ratings']>100].sort_values('Correlation',ascending=False).head()
        xp=(corr_standard[corr_standard['num of ratings']>100].sort_values('Correlation',ascending=False).head())
        xp.reset_index(inplace=True)
        z=xp.to_json()
        return z
      if x=="GILGIT":
        hotels_detail = pd.read_csv("C:\\Users\\Nova Data\\Desktop\desktopnew.csv")
        hotels_detail.head()
        hotels_detail.shape
        g =hotels_detail.groupby("CITY")
        g
        #for CITY, data in g:
         #  print("city:",CITY)
          # print("\n")
          # print("data:",data)
        g.get_group('HUNZA')
        g.get_group('ASTORE')
        g.get_group('GILGIT')
        g.get_group('SKARDU')
        hotels_list = pd.read_csv("C:\\Users\\Nova Data\\Desktop\H_list1new.csv")
        hotels_list.head(15)
       # column_names = ['user_id', 'item_id', 'rating', 'timestamp']
       # df = pd.read_csv('u.data', sep='\t', names=column_names)
       # df1 = pd.read_csv('u.data', sep='\t', names=column_names)
       # df2 = pd.read_csv('u.data', sep='\t', names=column_names)
       # df3 = pd.read_csv('u.data', sep='\t', names=column_names)
        df = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
        df1 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
        df2 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
        df3 = pd.read_csv("C:\\Users\\Nova Data\\Desktop\mylist.csv")
      
        df.head(5)
        df = pd.merge(df,g.get_group('SKARDU'),on='item_id')
        df.head()
        df1 = pd.merge(df1,g.get_group('HUNZA'),on='item_id')
        df1.head()
        df2 = pd.merge(df2,g.get_group('ASTORE'),on='item_id')
        df2.head()
        df3 = pd.merge(df3,g.get_group('GILGIT'),on='item_id')
        df3.head()
        df3.groupby('title')['rating'].mean().sort_values(ascending=False).head()
        import matplotlib.pyplot as plt
        import seaborn as sns
        sns.set_style('white')
        df3.groupby('title')['rating'].mean().sort_values(ascending=False).head()
        df3.groupby('title')['rating'].count().sort_values(ascending=False).head()
        ratings = pd.DataFrame(df3.groupby('title')['rating'].mean())
        ratings.head()
        ratings['num of ratings'] = pd.DataFrame(df3.groupby('title')['rating'].count())
        ratings.head()
        ratings.head()
        hotelmat = df3.pivot_table(index='user_id',columns='title',values='rating')
        hotelmat.head()
        ratings.sort_values('num of ratings',ascending=False).head(10)
        ratings.head()
        star_user_ratings = hotelmat[y]
        standard_user_ratings = hotelmat[y]
        star_user_ratings.head()
        similar_to_star = hotelmat.corrwith(star_user_ratings)
        similar_to_standard = hotelmat.corrwith(standard_user_ratings)
        corr_star = pd.DataFrame(similar_to_star,columns=['Correlation'])
        corr_star.dropna(inplace=True)
        corr_star.head()
        corr_star.sort_values('Correlation',ascending=False).head(10)
        corr_star = corr_star.join(ratings['num of ratings'])
        corr_star.head()
        corr_star[corr_star['num of ratings']>100].sort_values('Correlation',ascending=False).head()
        corr_standard = pd.DataFrame(similar_to_standard,columns=['Correlation'])
        corr_standard.dropna(inplace=True)
        corr_standard = corr_standard.join(ratings['num of ratings'])
        corr_standard[corr_standard['num of ratings']>100].sort_values('Correlation',ascending=False).head()
        xp=(corr_standard[corr_standard['num of ratings']>100].sort_values('Correlation',ascending=False).head())
        xp.reset_index(inplace=True)
        z=xp.to_json()
        return z
      
      
      
      
      
      
      


      


if __name__ == '__main__':
   app.run( port=4000 )
