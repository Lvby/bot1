# My hybrid bot

Enlighted by [this project](https://github.com/python-engineer/pytorch-chatbot/blob/master/chat.py), added check user roles method to make those answers more relevant, increased also a couple of layers in neuron networks.This is a test for my another application. You can make answers more accurate by asking user to give answers to more choices. A better orginized intents.json file could also improve user experiences. 

Background: The bot Sam works for a nursing job agency. He tries to answer questions raised by poential employers and nurses (both are not current users). The intents json files are seperated for each user group. After user answered if he/she is nurse or employer, the question will be answered based on corresponding pth files.

# How to use it:

Django index page and view not ready yet.  So your interaction with bot will be implemented through terminal.

go to path >core
# run python train.py to train (option if you want to train the model)
run python chat.py 

#this is the result

[nltk_data]   Package punkt is already up-to-date!
nurse select 1, employer select 2: 2
Let's chat! (type 'quit' to exit)
You: hello
Sam: Hey :-)
You: i am a nursing manager, we need some nurses
Sam: Great! Please visit potential employer page https://www.google.com and our staff will contact you within one hour in business days.
You: thanks 
Sam: Happy to help!
You: are you a bot
Sam: Yes, I am an AI bot using maching learning and natural language processing technique to answer your questions. When needed, I can forward your question to my human colleagues and they will reach you within two working days.
You: nice, you are smart
Sam: Glad to hear that :D
You: BTW, what are your office hours
Sam: We are open 7am-4pm Monday-Friday!
You: Great. Do you have any emails that I can write to your customer service
Sam: Happy to help!
You: do you have any emails
Sam: Happy to help!
You: you are dummy now
Sam: Thank you, do you need any other help?
