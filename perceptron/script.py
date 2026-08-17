from random import random

randomize_amount = 100
neurons = []

while randomize_amount != 0:
    cur_neuron = random()
    neurons.append(cur_neuron)
    randomize_amount -= 1

inputs = [1,2]

for neuron in neurons:
    
    
