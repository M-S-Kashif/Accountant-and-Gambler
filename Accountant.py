#Import all relevant packages...
import numpy as np
import pandas as pd
import random
import sys
import time

def f_movement(idx,arr):
    if (idx == 4):
        arr = [0,0,0,0,0]
        arr[3] = 0
        arr[4] = 1
        print("The Array now is: ",arr)
    elif (idx < 4):
        #temp = arr[idx-1]
        arr[idx-1] = 0
        arr[idx] = 1
        print("The Array now is: ",arr)
    return arr

def forwards(i,Dungeon):
    print(i)
    i = i + 1 
    if (i >= 4):
        i = 4
    print(i)
    arr = f_movement(i,Dungeon)
    return i, arr

def b_movement(idx,arr):
    temp = arr[idx]
    arr[idx] = arr[0]
    arr[0] = temp
    print("The Array now is: ",arr)
    return arr

def backwards(i,Dungeon):
    print(i)
    print(0)
    arr = b_movement(i,Dungeon)
    i = 0
    return i , arr
    
def choices(op,idx,Dungeon,reward):
    if (op == Moves[0]):
        print("\nMoving Forward...")
        idx, Dungeon = forwards(i,Dungeon)
    elif (op == Moves[1]):
        print("\nMoving backwards...")
        idx, Dungeon = backwards(i,Dungeon)
    elif (op == Moves[2]):
        print("\nSkip...")
    else:
        print("\nInvalid Option...")
        
    reward = reward + reward_count(idx)
    print("\nReward Count: ", reward)
    
    return idx,Dungeon,reward
    
def randomize():
    print("\nRandomize...")
    loop = True
    while(loop):
        random_choice = np.random.choice(Moves)
        idx, arr, r = choices(random_choice,i, Dungeon,reward)
        time.sleep(delay)
    
        if (random_choice == Moves[2]):
            loop = False
            print("\nOut of the Loop...")
    return idx, arr, r

def reward_count(i):
    r = 0
    if(i == 0):
        r = Rewards[1]
    elif(i == 4):
        r = Rewards[0]
    return r

if __name__ == "__main__":
    
    #Variables for our Algorithms...
    Moves = ['f','b','q']
    Rewards = np.array([10,2])
    delay = 2
    global i,idx  #Both are the same thing...
    i = 0 
    global Dungeon
    Dungeon = np.array([1,0,0,0,0])
    global reward
    reward = 0
    target = 10
    
    print("------ACCOUNTANT IN A DUNGEON-------\n\n")
    print(Dungeon)
    print("\n\n")    
    
    loop = True
    while (loop):
        print("f - forward")
        print("b - backward")
        print("q - quit from program")
        op = input("\n\nPlease enter a move to get started:")
        i, Dungeon, reward = choices(op,i,Dungeon,reward)
    
        if (op == Moves[0] or op == Moves[1]):
            i, Dungeon, reward = randomize()
        
        if (reward >= target):
            loop = False
            print("Target Reached....")
        
        if (op == Moves[2]):
            sys.exit("Exiting the program...")
            
print("Game Over.")
