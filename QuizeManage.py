import json

import numpy as numpy

class QuizM:
    def creat_quiz(self):
        new_quize = {'2': 'whats is python  ',
                     'repense': ["language strcutur ", "language de bas nieau", "accepte oop "]}
        with open('Qeasy.json', 'r') as file:
            data = json.load(file)
            data.append(new_quize)
        with open('Qeasy.json', 'w') as file2:
            json.dump(data, file2, indent=4)

    def view_data(self):
        with open('Qeasy.json', 'r') as f1:
             data1=json.load(f1)
        with open('Qinter.json', 'r') as f2:
            data2 = json.load(f2)
        with open('Qdif.json', 'r') as f3:
            data3 = json.load(f3)
            data=data1+data2+data3

        return data




