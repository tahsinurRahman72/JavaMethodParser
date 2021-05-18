import re
read=open("F:\\BRAC Undergraduate Courses\\CSE420\\LAB4\\readFile.txt", "r")
doc = read.readlines()
i=0
methodList =[]

while i < len(doc): 
    doc[i] =  doc[i].replace('\n','')    
    i+=1
docFinal = ''.join(doc)

#regexCategorizing
regex='(?:(?:public)*)+ (((?:(?:int)|(?:static int)|(?:void)|(?:A))+)) +([aA-zZ]+(([(])+))+((((, )*)+((int [aA-zZ])*)+((, )*))*)+((([)])+))' #this regex generalizes the whole method line
regexMethod='([aA-zZ]+(([(])+))+((((, )*)+((int [aA-zZ])*)+((, )*))*)+((([)])+))' #this regex specifies the whole methods only
typeRegex='((?:(?:int)|(?:void))+)' #this regex seperates the types of the methods

#printing
print("Methods:")
for j in range(0,len(doc)):
    final=re.search(regexMethod,doc[j])
    methodCalls=re.search(regex, doc[j])
    if(final!=None and methodCalls!=None):
        types=re.search(typeRegex,final.string)
        print(final[0]+", return type: "+types[0])

#result
# Methods:
# add(int a, int b), return type: int
# subtract(int a, int b), return type: int
# add(), return type: void