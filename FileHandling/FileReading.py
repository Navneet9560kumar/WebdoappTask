



# file = open("Report.txt","r")
# #  jo bhi kare yaha per ham bas itana karna hai ke jab bhi jo bhi kaam karn ahai karo bas last mai file close karna important hai 😎 or ek acch baat jase he ham with ka use karnge to file close nahi kar skate hai ok 
# file.close()

# with open("Report.txt", "r")as f:
#     data= f.read()
#     print("File data", data)



    # agrline byy line read karna ho to ye aase hoga likw 


with open("newTextFile.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    line4 = f.readline()
    line5 = f.readline()
    print("Line 1", line1)
    print("Line 2", line2)
    print("Line 3", line3)
    print("Line 4", line4)
    print("Line 5", line5)
   
    
    