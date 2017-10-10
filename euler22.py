#Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this caule by its alphabetical position in the list to obtain a name sore. For example, when the list is sorted into alphabetical order, COLIN, which is worth 3+15+12+9+14=53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714. What is the total of all the name scores in the file?

names = open("p022_names.txt").read().replace(',',' ').replace('"','').split()
alpha = []
lower_names = []
#Assigning every letter a number
alphabet = {"a": 1, "b": 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8, "i" : 9, "j" : 10,
"k" : 11, "l" : 12, "m" : 13, "n" : 14, "o" : 15, "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20,
"u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25, "z" : 26}
#print alphabet["a"]
total = 0

#making everything lowercase
for x in names:
    lower_names.append (x.lower())
#print lower_names

# To make the name list alphabetical (from the newly made lower case names)
beta = sorted(lower_names)
for x in beta:
    alpha.append(x)
#print alpha

#Making the name score for individual name
for x in alpha:
    letters = []
    temp = 0 #Making temporary list so each name can be appended individually
    letter_value = 0 #Letters added up for each name
    while temp <= len(x)-1:
        letters.append(x[temp])
        temp += 1
    for y in letters:
        letter_value += alphabet[y] #Calling on alphabet dictionay to add letters together
    #print letter_value
    word_value = letter_value * (alpha.index(x) + 1) #Multiplying namescore by position
    total += word_value #Adding all word values together
print total
