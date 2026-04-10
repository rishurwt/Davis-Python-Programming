filev = open("First.txt","r")
if(filev):
 data = filev.read()
 print(data) 
 print("No. of characters ",len(data))
 filev.close()
else:
 print("Unable to open file") 