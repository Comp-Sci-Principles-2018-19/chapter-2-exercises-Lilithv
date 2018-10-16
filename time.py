time=int(input('what time is it'))
long=int(input('how long do you want your alarm to be for?'))
longmodulo=long%24
alarmt=time+longmodulo
alarmt=alarmt%24 #dont go past 24 k thnks
print('I will set off at',str(alarmt)+', Doctor Luigi')
#x=5100 % 1400
#y=x+1400
#print(y)