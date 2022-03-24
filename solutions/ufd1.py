'''WAS to enter 5 string in a list and check and print
string whose length has even number of character'''
count=0
l=[]
def createlist():
    for i in range(1,6):
        s=input("enter any string:")
        l.append(s)

def even(l):
    count=0
    for i in l:
            count+=1
    if len(l)%2==0:
        print(l)
    return(count)
createlist()
ans=count(even(l))
print(ans)















        

    
        

    
    

    
