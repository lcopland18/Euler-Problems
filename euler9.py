def sqrt(x):
    print (x ** 0.5)
#Test Below
#print sqrt(4)
#Just realized I didn't even need the sqrt D:

#testing pythag_therom

#Range of numbers to test for pythagorean triple
xyz = range(1,1000) #(200, 500)
#triple = [] #this isn't neccessary

def pythag_theorem(a, b, c):
    if a < b < c and a ** 2 + b ** 2 == c ** 2: #Making a pytagorean theorem function
        return True
        #print "True"
    else:
        return False
        #print "False"

def pythag_triple(hello): #Defining what it means to be a pythagorean triple
    for x in hello: #Hello just a placeholder (in this case xyz id put in)
        for y in hello:
            for z in hello:
                if pythag_theorem(x,y,z) == True:
                    if x + y + z == 1000: #Making sure you get the pythagorean triple that adds to 1000
                        print x,y,z #Printing the pythagorean triple
                        print x * y * z #Doing what the problem asked and multiplying the three

pythag_triple(xyz) #Running pythag triple function. Takes xyz from range (at top) to plugs into triple equation
#print triple
