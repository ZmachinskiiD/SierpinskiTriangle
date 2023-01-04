
Length=int(input("Please specify the size of pattern, more than 3: "))
F=open("Output.txt","w",encoding="utf-16")
F.write(chr(11035))
F.write('\n')
F.write(chr(11035)+chr(11035))
F.write('\n')
F.write(chr(11035)+chr(11036)+chr(11035))
F.write('\n')
prevArray=[1,2,1]
for i in range(3,Length):
    newArray=[]
    
    for j in range(len(prevArray)):
        if j!=0:
            temp=prevArray[j]+prevArray[j-1]
            newArray.append(temp)
        if j==0 or j==(len(prevArray)-1):
            newArray.append(1) 
    prevArray=newArray
    for number in newArray:
        if number%2==1:
            F.write(chr(11035))
        else:
            F.write(chr(11036))
    F.write('\n')   
F.close()
print("DONE!")            
        
    