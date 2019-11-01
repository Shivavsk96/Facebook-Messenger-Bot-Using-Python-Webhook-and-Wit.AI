Facebook-Messenger-Bot-Using-Python-Webhook-and-Wit.AI


This Project Allows for Creation of a Facebook Messenger Bot which will take data from the user and use it to find and return jobs to the User based on their needs. The jobs are obtained after Scrapping of popular Job Site(Naukri.com)


This Project was done by me at Curvelogics Advanced Technology Solutions Private Limited,
(http://www.curvelogics.com/ ) as a Intern.Thanks to everyone there for their Continuous
Support and Guidance



INSTRUCTIONS
    1. Run the file main.py (By default main.py is coded to run in port 8000)(you can change it to know how refer the Report)
    2. Download ngrok (https://ngrok.com/download )(ngrok does not need any installation)
    3. run ngrok and type ngrok.exe http 8000 in the terminal which opens up(where 8000 is the port number)
    4. ngrok will generate a link paste it into the Facebook Developer Section Read Report for detailed Instructions
    5. start sending messages to the Messenger

Components
    1. main.py
       The main python Script which is to be run
    2. scrapper.py
       the python script which is linked to main.py it does the scrapping part
    3. data.py
       the python script which will process the data to be submitted back to the user
    4. Report.pdf
       A detailed Report About the project and Instructions on how to use the Facebook Developer page to link the Python Script to the Messenger Platform using Webhook
    5. Report(Wit).pdf
       This Contains details about Wit.Ai how to link it to the program and how to use it
    6. requirments.txt
       contains details of the various different python packages required for this project to work

Packages
In Summary the main packages(Python) required for this project are
    1. Flask(pip install Flask)
    2. pymessenger(pip install pymessenger)
    3. wit(pip install wit)
    4. requests(pip install requests)
    5. pandas(pip install pandas)
    6. beautiful soup4(pip install bs4)
refer requirements.txt for full details on packages

Notes
    • Whenever the Webhook recieves a message it responds with a 200OK Message 
    • in Some lines of Code you may see a “{}” used eg: f=open("{}_post.txt".format(str(sender_id)),"a")
this is done to allow us to give different file name values(eg to give hello.txt in one instance and hello1.txt in other) rather than a fixed value refer(https://www.geeksforgeeks.org/python-format-function/")
A Similar Technique is used in scrapper.py lines(28,30,32)

Issues Faced
    • A Slow Internet Connection on the System Running the Webhook will resultin a delay for the message to reach main.py hence a delay in reply by the bot to reply
    • Facebook has a feature called echoing where the bots reply is treated as the next Message make sure to turn it off to avoid confusion(refer Report)
       
