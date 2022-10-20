#Import all relevant packages...
import numpy as np
import pandas as pd
import random
import sys
import time

#Variables for our Algorithms...
Moves = ['f','b','q']
Rewards = np.array([10,2])
delay = 2
global i,idx  #Both are the same thing...
i = 0 
global Dungeon, arr
Dungeon = np.array([1,0,0,0,0])
global reward, r
reward = 0
target = 10

#Variables especially for the Gambler....
Actions = ['r','g','q']        #Asked by the user at every iteration.
Learning_Rate = 0.1
Discount = 0.95
global QTable
QTable = np.array([[0,0,0,0,0],[0,0,0,0,0]], dtype=float)

def Q_Table_Score(present_q, next_q, Q):
    print("\nQ_Table Before Update: \n",Q)

    #Creating the update in the table...
    gamma = 0  #Not assumed in the Calculation of scores...
    if (next_q == 4):     
        Q[0][present_q] = Q[0][present_q] + Learning_Rate *( Rewards[0] + Discount * ( max( Q[0][next_q] , Q[0][present_q] ) - gamma))
        print("\n Last State Reached- Value Update: ",Q[0][present_q])
        print("\n\nQ_Table After Update: \n", Q)
        print()
    elif (next_q == 0):
        Q[1][present_q] = float( Q[1][present_q] + Learning_Rate *( Rewards[1] + Discount * ( max( Q[1][next_q] , Q[1][present_q] ) - gamma)) )
        print("\n First State Reached- Value Update: ",Q[1][present_q])
        print("\n\nQ_Table After Update: \n", Q)
        print()
    else:
        print("\nNo Updates...\n\n")
    return Q

def reward_count(i):
    r = 0
    if(i == 0):
        r = Rewards[1]   #2
    elif(i == 4):
        r = Rewards[0]   #10
    return r

def f_movement(idx,arr):
    if (idx == 4):
        arr = [0,0,0,0,0]
        arr[3] = 0
        arr[4] = 1
        print("The Array now is: ",arr)
    elif (idx < 4):
        arr[idx-1] = 0
        arr[idx] = 1
        print("The Array now is: ",arr)
    return arr

def forwards(idx, Dungeon):
    present_q = idx
    print(present_q)
    next_q = present_q + 1 
    if (next_q >= 4):
        next_q = 4
    print(next_q)
    arr = f_movement(next_q,Dungeon)
    return present_q ,next_q ,arr

def backwards(idx,arr):
    present_q = idx
    print(present_q)
    next_q = 0
    print(next_q)
    if (present_q != 0):
        arr[0] = 1
        arr[present_q] = 0
        print("The Array now is: ",arr)
    return present_q, next_q , arr
    
def choices(op,i,Dungeon,reward,QT):

    #Decision-Making Block...
    if (op == Moves[0]):
        print("\nMoving Forward...")
        idx, new_idx, Dungeon = forwards(i,Dungeon)
    elif (op == Moves[1]):
        print("\nMoving backwards...")
        idx, new_idx, Dungeon = backwards(i,Dungeon)
    elif (op == Moves[2]):
        print("\nSkip...")
    else:
        print("\nInvalid Option...")
        
    #Calculating the Rewards...
    reward = reward + reward_count(new_idx)
    print("\nReward Count: ", reward)

    #Updating the Q Table...
    update_QT = Q_Table_Score(idx, new_idx, QT)
    QT = update_QT

    return new_idx,Dungeon,reward,QT
    
def randomize():
    print("\nRandomize...")
    idx = i
    arr = Dungeon
    r = reward
    QT = QTable
    loop = True
    while(loop):
        random_choice = np.random.choice(Moves)
        if (random_choice == Moves[0] or random_choice == Moves[1]):
            idx, arr, r, QT = choices( random_choice, i, Dungeon, reward, QTable)
        elif (random_choice == Moves[2]):
            loop = False
        time.sleep(delay)
    return idx, arr, r, QT

def gamble():
    print("\nGamble...")
    print("\n----------MOVES---------\n")
    print("f - Forward")
    print("b - Backward")
    print("q - None")
    op = input("\n\nPlease select an action: ")
    if (op == Moves[0] or op == Moves[1]):
        idx, arr, r, QT = choices( op, i, Dungeon, reward, QTable)
    elif (op == Moves[2]):
        print("\nSkip...")
    return idx, arr, r, QT


#Main Function....
if __name__ == "__main__":
    
    print("------GAMBLER IN A DUNGEON-------\n\n")
    print(Dungeon)
    print("\n\n")    
    
    loop = True
    while (loop):
        print("\n------------ACTIONS-----------\n")
        print("r - randomize")
        print("g - gamble")
        print("q - quit from program")
        op = input("\n\nPlease select an action: ")
    
        if (op == Actions[0]):
            i, Dungeon, reward, QTable = randomize()
        
        if (op == Actions[1]):
            i, Dungeon, reward, QTable = gamble()

        if (reward >= target):
            loop = False
            print("Target Reached....")
        
        if (op == Actions[2]):
            sys.exit("Exiting the program...")
            
print("Game Over.")
