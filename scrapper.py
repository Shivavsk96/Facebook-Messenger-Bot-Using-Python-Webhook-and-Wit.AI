#This is the Code where the data from the user's data is Utilized to Scrap in Naukri.com
import requests
import pandas as pd
import bs4
def test(sender_id):
 agent={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}#agent is specififed to ensure site gives acess for scraping
 file1=open("{}_post.txt".format(str(sender_id)),"r+")#sender_id is obtained from Json provided by Messenger
 file2=open("{}_place.txt".format(str(sender_id)),"r+")
 a=file1.read()#reading contents of file and storing it in a variable# the text file contains value sent by the user It was stored in this text file in line 84 of main.py or line 98 of main.py
 b=file2.read()#reading contents of file and storing it in a variable# the text file contains value sent by the user It was stored in this text file in line 90 of main.pyor line 99 of main.py
 f=open("{}_post.txt".format(str(sender_id)),"w")#this command is used to empty the text files after reading this is done to avoid Accumlation of new user Requirments when the same user "Uses" the System at a future point of time. This can be replaced by deleting the text files using specefic "os" commands
 d=open("{}_place.txt".format(str(sender_id)),"w")
 f.close()#it is important to close the files inorder to complete operations on a file
 d.close()
 c=a.split()#split the string #note: if the user does not leave space eg:machinelearning System will treat it as SingleWord
 d1=0#giving initial values to the variable # this value is just a placeholder and is used only to initiate the variable
 d2=0
 d3=0
 m1=len(c)#storing length of string in a variable
 for i in range (0,m1):#loop to find number of words eg: Hello World has 2 words "Hello" and "World"
  if i==0:#Storing first word in d1 eg:"if the word is Hello World" then Hello is stored in variable. if there is only one word it is stored in d1
    d1=c[i]
  elif(i==1):#Storing Second word in d2 eg:"if the word is Hello World" then World is stored in variable. if there is only one word then d2 is 0
    d2=c[i]
  elif(i==2):#Storing Third word in d3 eg:"if the word is Hello World Jacob" then Jacob is stored in variable. if there is only one or two word then d3 is 0
    d3=c[i]
 if(d2==0) and (d3==0):#if users job requirment is a single word like "Manager" # then this link is used
    res=requests.get("https://www.naukri.com/{}-jobs-in-{}".format(str(d1),str(b)),headers=agent)# "we use {} to pass the Strings as variable" because a variable will be treated as a part of the link "Refer:https://www.geeksforgeeks.org/python-format-function/"
 elif(d3==0):#if users job requirment is a multiple word like "HR Manager"then this link is used
    res=requests.get("https://www.naukri.com/{}-{}-jobs-in-{}".format(str(d1),str(d2),str(b)),headers=agent)
 else:#if users job requirment is a triple word like "Data Science Manager"then this link is used
   res=requests.get("https://www.naukri.com/{}-{}-{}-in-{}".format(str(d1),str(d3),str(d3),str(b)),headers=agent)  
 soup=bs4.BeautifulSoup(res.text,'lxml')#lxml is a parser
 job=[]#empty lists to store data from scrapping
 com=[]
 exp=[]
 loc=[]
 salr=[]
 skill=[]
 date=[]
 for row2 in soup.find_all( {"li":"title"},{"class":"desig"}):#to get job title#refer webscrapping tutorials #this is created after Analysis of naukris HTML
   job.append(row2.text.strip())#to get only text and avoid links and tags
 for row3 in soup.find_all("span", {"class":"org"}):#to get Company
   com.append(row3.text.strip())#to get only text and avoid links and tags 
 for row4 in soup.find_all("span", {"class":"exp"}):#to get Experience
   exp.append(row4.text.strip())#to get only text and avoid links and tags         
 for row5 in soup.find_all("span", {"class":"loc"}):#to get Location
   loc.append(row5.text.strip())#to get only text and avoid links and tags  
 for row6 in soup.find_all("span", {"class":"skill"}):#to get skills
   skill.append(row6.text.strip())#to get only text and avoid links and tags
 for row7 in soup.find_all("span", {"class":"salary"}):#to get Salary
   salr.append(row7.text.strip())#to get only text and avoid links and tags
 for row8 in soup.find_all("span", {"class":"date"}):#to get Posted date 
   date.append(row8.text.strip())#to get only text and avoid links and tags
 l3=list(zip(job,com,exp,loc,skill,salr,date))#zipping all the lists
 df1=pd.DataFrame(l3,columns=['Test',"Comp","exp","loc","skill","salary","date"])#creating a Dataframe using the Zipped List
 return(df1)#returning dataframe
