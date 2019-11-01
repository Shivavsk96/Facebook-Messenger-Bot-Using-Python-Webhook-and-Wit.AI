import requests
import pandas as pd
import bs4
import json
def scrap(df1,i):
 df=df1.loc[[i]]#to iterate through each rows #here the value of i  and df1 are obtained from main.py
 Row_list =[] #empty list
 for rows in df.itertuples():#to iterate over DataFrame rows as namedtuples.  
   my_list =[rows.Test, rows.Comp, rows.exp,rows.loc,rows.skill,rows.salary,rows.date]#where (Test,Comp,exp,etc....) are names of Columns of the Dataframe 
   Row_list.append(my_list) #appending my list to Row_list
 a= " ".join(str(x) for x in Row_list )#converting the list Row_list to a String so that it can be passed to Messenger
 a=a.strip("]")#the string will be of the form "[foo_bar,foo_bar1]" we use a=a.strip("]") to remove [ to make it more presentable 
 a=a.strip("[")
 return(a)#returning the String




