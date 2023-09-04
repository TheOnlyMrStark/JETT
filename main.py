#---------------Modules---------------#
import random
import json
import torch
from core import NeuralNet
from neuralnet import bag_of_words, tokenize
from tasks import nonInputExecution
from tasks import inputExecution
from listen import Listen
from speak import Say

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json", "r") as json_data:
    intents = json.load(json_data)
    
FILE = "trainedData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#---------------------main--------------------#
name = "Jett"



def Main():
    
    #Tester() #Removed as creating issues
    #sentence = Listen()
    sentence = input("You : ")
    result = str(sentence)
    
    if sentence == "bye":
        exit()
        
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)
    
    output = model(X)
    
    _ , predicted = torch.max(output, dim=1)
    
    tag = tags[predicted.item()]
    
    prob = torch.softmax(output, dim=1)
    prob = prob[0][predicted.item()]
    
    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                response = random.choice(intent["responses"])
                
                if "time" in response:
                    nonInputExecution(response)
                
                elif "date" in response:
                    nonInputExecution(response)
                     
                elif "wikipedia" in response:
                    inputExecution(response, result)
                    
                elif "google" in response:
                    inputExecution(response, result) 
                
                elif "switch" in response:
                    inputExecution(response, result)
                    
                elif "download" in response:
                    inputExecution(response, result)  
                    
                elif "music" in response:
                    nonInputExecution(response)
                    
                else:               
                    Say(response)
while True:
    Main()