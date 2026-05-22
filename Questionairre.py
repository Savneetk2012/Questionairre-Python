# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:59:49 2026

@author: savneet kuar
"""

import random


questions = ["What is AQI?", 
             "What is air pollution?", 
             "Are aliens real?", 
             "Why is the sky blue?",
             "What does the fox say?", 
             "What are integers?", 
             "What is your favourite fruit?"
             ]
num = int(input("How many questions do you want? "))


if num > len(questions):
    print(f'You can not request for more than {len(questions)} questions.')
elif num < 1:
    print("Please enter a number greater than 0")
    
else:
    selected = random.sample(questions, num)
    print(selected)

@app.route('/questions')







