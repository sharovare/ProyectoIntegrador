from readchar import readkey, key


while True:
   k = readkey()
   print(k)
   if (k == key.UP):   
     break
   
print("Fuera del bucle")