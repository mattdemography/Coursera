#Starting
print "hello world"

zot='abc'
print zot[2] #Print

x=len(zot)  #Length Function - Counts how long object is
x #Print to Display

#Loop Though Index
f='banana'
index=0
while index < len(f): #While less than length of f
    letter=f[index]
    print(index, letter)
    index= index + 1 #Keeps loop moving
     
#Does same as above except just prints each letter one by one
for l in f:
    print(l)

#Slicing Strings
s='Monty Python'
print(s[0:4])
print(s[6:20]) #There are not 20 characters so it gives everything after 6->
print(s[:2]) #Everything Up to 2

#Is 'n' in 'banana'?
'n' in f
'm' in f

if 'a' in f:
    print 'Found It'

if f == 'banana':
    print 'All right, bananas'
    
#This code allows us to find where the order of a word is.
f='ban'
if f < 'banana':
    print 'Your word,' + f + ', comes before banana.'
elif f > 'banana':
    print 'Your word,' + f + ', comes after banana.'
else:
    print 'All right, bananas.'
    
greet='   HELLO World!   '
zap=greet.lower()
print(zap)
type(zap)   #Tells you the type of object 
dir(zap)    #Tells us what functions are in 'str'

pos=greet.find('or')
print(pos)  #Tells us what position string is

nstr=greet.replace('World', 'Earth')
print(nstr) #Replace string in another

nstr=nstr.strip() #Removes white space from both ends
print(nstr)

#The following is used to keep everything after first space. Can be done
#to find address in twitter
bpos=nstr.find(' ')
print(bpos)

