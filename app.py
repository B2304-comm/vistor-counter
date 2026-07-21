Ayush Raj Chourasia  to  Everyone 14:25
Has a wa grp been formed for this section?

You  to  Everyone 14:27 (Edited)
No Sir

SAURAV KUMAR  to  Everyone 14:44
Yes 

Rohit Anurag  to  Everyone 14:44
Yes Sir

Anindita Mohanty  to  Everyone 14:44
yes sir

Aditya Biswabandhu  to  Everyone 14:44
yes sir

Pranav Kumar  to  Everyone 14:44
yes sir

Shaswat Subudhi  to  Everyone 14:44
Yes

SAURAV KUMAR  to  Everyone 14:56
Yes

Anindita Mohanty  to  Everyone 14:56
yes sir

SAURAV KUMAR  to  Everyone 14:56
Yes

Shaswat Subudhi  to  Everyone 14:56
Yes

Babul Kumar Sahu  to  Everyone 15:26
devdas stop

You  to  Everyone 15:26
hello sir

Aman Singh  to  Everyone 15:29
@Devdas Das please remove all these asap!

Anindita Mohanty  to  Everyone 15:29
sir screen is not visible
no sir due to those emojis

Omm prakash Sha  to  Everyone 15:30
No sir

Deepti Smita Behera  to  Everyone 15:30
No sir

Srushti swaroop Parida  to  Everyone 15:30
Yes sir

Adarsh Jayaswal  to  Everyone 15:30
no sir

Shanvi Priyadarshini  to  Everyone 15:30
Yes sir

Yashaswee Mishra  to  Everyone 15:30
yes sir

AKSHAT SHUBHAM  to  Everyone 15:30
yes sir

Abhishek Mangaraj  to  Everyone 15:30
yes sir

Rohit Anurag  to  Everyone 15:30
Yes Sir

Babul Kumar Sahu  to  Everyone 15:30
yes

Vaishnobi Mishra  to  Everyone 15:30
yes sir

Anindita Mohanty  to  Everyone 15:30
yes sir

Saswat Mohapatra  to  Everyone 15:30
yes sir

Deepti Smita Behera  to  Everyone 15:30
Yes sir 

You  to  Everyone 15:30
yes sir

Dipankar Panigrahi  to  Everyone 15:30
Yes sir

SAURAV KUMAR  to  Everyone 15:30
Yes

Aryan Nayak  to  Everyone 15:30
yes sir

Pranoy Deb  to  Everyone 15:30
yessirr

Shaswat Subudhi  to  Everyone 15:30
Yes sir 

Aditya Biswabandhu  to  Everyone 15:30
yes sir

Harish Chandra Mohapatra  to  Everyone 15:41
Yes sir

Dipankar Panigrahi  to  Everyone 15:53
Yes sir

Shanvi Priyadarshini  to  Everyone 15:53
Yes sir

Abhishek Mangaraj  to  Everyone 15:53
yes sir

Srushti swaroop Parida  to  Everyone 15:53
Yes sir

Adyasha Mohapatra  to  Everyone 15:53
yes sir

Yashaswee Mishra  to  Everyone 16:08
yes sir

Bishal  to  Everyone 16:08
yes

Anindita Mohanty  to  Everyone 16:08
yes sir

Chetana Jagadev  to  Everyone 16:08
yes

Ayushi Mishra  to  Everyone 16:08
yes sir

You  to  Everyone 16:09
yes sir

Babul Kumar Sahu  to  Everyone 16:09
yes sir

Aman Singh  to  Everyone 16:09
yes sir

sayantan dutta  to  Everyone 16:09
i have sir

Anindita Mohanty  to  Everyone 16:09
yes sir

You  to  Everyone 16:09
yes sir
done sir

Tanvi Tapaswani  to  Everyone 16:11
sir plz again

Shanvi Priyadarshini  to  Everyone 16:11
Done sir

Tanvi Tapaswani  to  Everyone 16:12
yes sir

Aditya Biswabandhu  to  Everyone 16:12
yes sir

Anindita Mohanty  to  Everyone 16:12
yes sir

Abhishek Mangaraj  to  Everyone 16:12
yes sir

Babul Kumar Sahu  to  Everyone 16:12
yes

Tanvi Tapaswani  to  Everyone 16:14
yes sir

Anindita Mohanty  to  Everyone 16:14
yes sir

Abhishek Mangaraj  to  Everyone 16:14
yes sir

KPMG Training  to  Everyone 16:14
flask==2.3.2
gunicorn==21.2.0

Tanvi Tapaswani  to  Everyone 16:14
yes

Akash Sarangi  to  Everyone 16:15
sir can we get this word doc?
yes sir, doing

Aditya Biswabandhu  to  Everyone 16:15
yes sir

Tanvi Tapaswani  to  Everyone 16:15
yes

Anindita Mohanty  to  Everyone 16:15
yes sir

KPMG Training  to  Everyone 16:16
from flask import Flask
import os
 
app = Flask(__name__)
 
# Simple in-memory counter (resets on restart)
visits = 0
 
@app.route('/')
def index():
    global visits
    visits += 1
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Visitor Counter</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }}
            .counter {{ font-size: 48px; color: #2c3e50; }}
        </style>
    </head>
    <body>
        <h1>🚀 Welcome to the Real-World DevOps App!</h1>
        <h2> Hi wellocme to my webpage<h2>
        <p>This page has been visited:</p>
        <div class="counter">{visits} times</div>
        <p><i>Powered by Python, Docker, and GitHub Actions.</i></p>
    </body>
    </html>
    '''
 
if name == '__main__':
    app.run(host='0.0.0.0', port=5000)
