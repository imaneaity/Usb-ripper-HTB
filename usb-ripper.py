import json

#extract the manufacturers from the log file 

f = open("syslog", "r")
li=[]
x=0
users=[] #will contain the manufacturors that are peresent in the log file
for line in f:
  
  li=line.split()
  if li[-2] == "SerialNumber:":
   x+=1 
   users.append(li[-1])

f.close()


#extract the trusted manufacturers
f = open('auth.json',)

trusted=[]

data = json.load(f) # returns JSON object as a dictionary
trusted=data['serial']


f.close()


#compare trusted and users to get the intruder

intruder=list(set(users) - set(trusted))
print(intruder)

#now to find the flag you just need to decode the hached serial number



