# This is the example of print simple pyramid pattern  
n = int(input("Enter the number of rows"))  

for i in range(0, n+1):  
    
        for j in range(0, i + 1):  
            
            print("* ", end="")       

    
        print()  

 
for i in range(n + 1, 0, -1):    
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")  