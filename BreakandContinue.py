#Break and Continue Statement 
#When we want to end the loop so we used break statement and sometimes we need to skip one 
#condition then we have to use the continue statement.
for i in range(12):
     if(i==10):
         print("Skip the iteration")
         continue
print("5 X", i, "=",5*i)