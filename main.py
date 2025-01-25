import os,sys
import random
from flask import Flask,request
from pymessenger import  Bot#pymessenger is a Python Wrapper for the FB Messenger Bot refer #https://github.com/davidchua/pymessenger
from wit import Wit#wit is a python package for Wit.ai 
from scrapper import test#importing function test from scrapper.py
from data import scrap#importing function scrap from data.py
import os
#page_acess_token is obtained from facebook developer page read the Attatched Report for how to get page_acess_token
page_acess_token=#puttokenhere
#the page_acess_token varies for each page
acess_token="2P5AWUHZ3R55RZOQXB45FHH5OA6BU6VE"#acess token is obtained from Wit refer Report(Wit) for how to get acess_token
client=Wit(access_token=acess_token)
bot=Bot(page_acess_token)#passing page_acess_token to pymessenger
app=Flask(__name__)#creating the flask class object
@app.route('/',methods=['GET'])
def verify():#Facebook Webhook
	# Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "Shiva":#Here "Shiva" can be changed to anything you like refer Attatched Report
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello World",200
@app.route('/',methods=['POST'])
def  webhook():
 data = request.get_json()#to get json from Messenger
 log(data)
 #Facebook JSON Sample#“{'object': 'page', 'entry': [{'id': '113722096692640', 'time': 1571719878674, 'messaging':[{'sender': {'id': '2701441109880031'}, 'recipient': {'id': '113722096692640'}, 'timestamp':1571719878281, 'message': {'mid':'bJ0_BrBAqoD4QISM6MBEGvcZksxQjJPrczPjEPXqTTdz-2Os2oYdTdbgE13cKbLv3PoR3TRZBVJI3w8JHxS-uA', 'text': 'Yes'}}]}]}
 if data['object']=='page':#checking wether the Messenger is linked to a page
    for a in data['entry']:#to scan through messengerJson [as Json can be treated as a Python Dictionary]
       for b in a['messaging']:
          sender_id=b['sender']['id']#togetsenderid
          reciever_id=b['recipient']['id']#togetrecieverid
          if b.get('message'): 
              if 'text' in b['message']:#Checking if the Content Sent by user is a text
                   f=open("{}_post.txt".format(str(sender_id)),"a")#creating a new empty text file to store values provided by user# 'a' represents that file is created in append mode #note open("{}_post.txt".format(str(sender_id)),"a") is used so that each user has their individual text files this allows code to handle multiple users 
                   d=open("{}_place.txt".format(str(sender_id)),"a") 
                   test_text=b['message']['text']#retreive text sent by the user
                   my_text=test_text
                   #The Below code is where the Text is Passed to Wit.AI (refer Report(Wit).pdf for details on Wit and its Operations)
                   resp=client.message(my_text)#storing client message in a varaible
                   entity=None# get entity#in case entity is none
                   value=None
                   intent=None#in case value is none
                   entity1=None
                   try:
                        a=list(resp["entities"])#where resp["entities"] is Json returned by Wit which is a dictionary #we convert to  a list for easier operation
                   except:
                      pass
                   z=len(a)#storing length of list
                   if z==1:#if length of list is 1
                    r=list(resp["entities"])[0]#to get first entity 
                    print(r)
                    if r=="post":#if entity post is detected
                      m=list(resp["entities"])[0]#to get the value of entity
                      entity=resp["entities"]["post"][0]["value"]#to get the value which made Wit classify the Text as a Specefic Entity this is most likley what the user wants
                      print(entity)
                    elif(r=="place"):#if entity place is detected
                       m=list(resp["entities"])[0]#to get the value of entity 
                       entity=resp["entities"]["place"][0]["value"]#to get the value which made Wit classify the Text as a Specefic Entity this is most likley what the user wants
                    elif(r=="intent"):#if the text is a intent in Wit
                       value=list(resp["entities"]["intent"])[0]["value"]#to get the value of entity
                       m=resp["entities"]["intent"][0]["value"]
                       print("value")
                    elif(r=="Yes"):#When the entity Yes is Recognised 
                       entity=resp["entities"]["Yes"][0]["value"]
                       m=0#passing initial value to m
                    elif(r=="no"):#When the entity No is Recognised
                        entity=list(resp["entities"]["no"])[0]["value"]
                        m=0#passing initial value to m
                   if z==3:#when more than 1 entity is detected
                    r1=resp["entities"]["post"][0]["value"]#check wether the entity post is detected if Yes Store it in r1 else r1 is 0
                    r2=resp["entities"]["place"][0]["value"]#check wether the entity place detected if Yes Store it in r2 else r2 is 0
                    r3=resp['entities']["intent"][0]['value']#check wether a intent detected if Yes Store it in r3 else r3 is 0
                    m=0
                    print(r1)
                    print(r2)
                   if z==0:#if the Text Is not Recognised by Wit at all
                       m=None  
                    #this is Where The Wit Code Ends
                   if value=="Job_Search":#if the Value of Intent is Job_Search(Job_Search is defined in our Wit refer Report(Wit)
                       responses=["What post do you want","Specify what post you want","Tell me what post you want","Which Post do you want"]#creating a Python List with all the possible Responses
                       a=random.choice(responses)#select a random value from the list "Responses"
                       bot.send_text_message(sender_id,a)#this command is used to send data back to user here sender_id is sender_id of user and a is the text we want to send back
                   if m=='post':#if the entity is post
                      f.write(test_text)#write the message send by user to  the file {}_post.txt".format(str(sender_id))#we open the file in line 36
                      f.close()                  
                      v1_text=["Which Location do you want","Where do you love to work","Tell me where do you want to work","Location Please"]#creating a Python List with all the possible Responses
                      v_text=random.choice(v1_text)#taking a random value from list v1_text
                      #v_text="What place do you want"
                      bot.send_text_message(sender_id,v_text)#sending message back to user
                   if m=='place':#if the entity is place
                     d.write(test_text)#write the message send by user to  the file {}_place.txt".format(str(sender_id)) #we open the file in line 37
                     d.close()         
                     m_text="Are you Sure you want to proceed"
                     bot.send_text_message(sender_id,m_text)#sending message back to user
                   if  m==None:#if wit dosent identify the Text
                      z_text="Sorry I dont Understand"
                      bot.send_text_message(sender_id,z_text)#sending message back tp user
                   if(z==3):#if place and post are detected in the Same time" eg_text:Get me a Hello World Job in New York 
                     f.write(r1)#writing values to file Refer to line 70,71,72 to find put how we obtained value for r1,r2,r3
                     d.write(r2)
                     f.close()#note to close files after each operation on them
                     d.close()
                     i="Do you want to proceed Answer with Yes or No"
                     bot.send_text_message(sender_id,i)#sending message back 
                   if entity=='Yes':#if Yes is Recognised
                      r1=["We got some jobs for you","Hmm It seems i have got some jobs for you","Hurray i got some jobs for you"]#creating a Python List with all the possible Responses
                      r=random.choice(r1)#select a random value from list r1
                      bot.send_text_message(sender_id,r)#sending back message
                      r1="The Jobs Will be of the form POST,COMPANY,EXPERIENCE,LOCATION,SKILLS/REQUIRMENTS,SALARY,DATE POSTED"
                      bot.send_text_message(sender_id,r1)
                      m=test(sender_id)
                      print(m)#we pass the sender id to the function test inside scrapper.py the dataframe(dataframe contains scrapped data) returned by test is stored inside variable m
                      for i in range(0,5):#we create this loop to obtain first 5 values of dataframe 
                        b=scrap(m,i)#pass values to function scrap inside data.py#every time we loop the value of 'i' in line6 of data.py changes from (1-5) hence allowing us to get first 5 values #also we pass the dataframe stored in the variable m(line 110). the value outputed by scrap is stored in the variable m
                        bot.send_text_message(sender_id,b)#sending back the job list to the user                      
                   if entity=='no':#if entity is no
                      t_text="Good Bye"
                      bot.send_text_message(sender_id,t_text)
              else:#if the user sends anything other than text
                  test_text="no text"
                  response=test_text
                  bot.send_text_message(sender_id,test_text)
 return "ok", 200#returning a ok 200 Message back to Facebook is Crucial as Messenger only sends the next message to the Webhook when it recieves the ok 200 command 
def log(message):
    print(message)
    sys.stdout.flush()#to clear System buffer
 
if __name__ == "__main__":#part of flask
 app.run(debug = True,port=8000)#command to run the code in Port 8000 you can change it as needed
    
