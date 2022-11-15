import random
import json
import tokenize
from model import NeuralNet
import torch

from torch.utils.data import Dataset, DataLoader

#from nltk_utils import bag_of_words
from nltk_utils import bag_of_words, tokenize, stem
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def check_user_role():
    answer=input("nurse select 1, employer select 2: ")
    
    if answer==1:
        selected_json_file="intents_nurse.json"
        FILE="nurse.pth"
    else:
        answer==2
        selected_json_file="intents_employer.json"
        FILE="employer.pth"
   

    with open(selected_json_file, 'r') as json_data:
        intents = json.load(json_data)

        #FILE = "employer.pth"
        data = torch.load(FILE)

        input_size = data["input_size"]
        hidden_size = data["hidden_size"]
        output_size = data["output_size"]
        all_words = data['all_words']
        tags = data['tags']
        model_state = data["model_state"]

        model = NeuralNet(input_size, hidden_size, output_size).to(device)
        model.load_state_dict(model_state)
        model.eval()

        bot_name = "Sam"
        print("Let's chat! (type 'quit' to exit)")
        
    while True:
        sentence=input("You: ")
        if sentence == "quit":
            break

        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
        else:
            print(f"{bot_name}: I do not understand...")

check_user_role()