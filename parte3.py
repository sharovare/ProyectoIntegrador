from readchar import readkey
import os

def delete_terminal():
   os.system('cls' if os.name=='nt' else 'clear')
   
num = 0
while num < 50:
   k = readkey()
   if (k in ["n", "N"]):
     num = num + 1   
     delete_terminal()
     print(num)

    

    


        


