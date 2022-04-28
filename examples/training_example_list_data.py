from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


'''
This is an example showing how to train a chat bot using the
ChatterBot ListTrainer.
'''
text_file= open("DPCA_short.txt", errors="ignore")
data=text_file.read()
listOfSentences = data.split("\n")

chatbot = ChatBot('DanBot')

# Start by training our bot with the ChatterBot corpus data
trainer = ListTrainer(chatbot)

#trainer.train(listOfSentences)

# You can train with a second list of data to add response variations

trainer.train([
    'Hello, how are you?',
    'I am great.',
    'That is awesome.',
    'Thanks'
])

# Now let's get a response to a greeting
response = chatbot.get_response('Scrub')
print(response)
