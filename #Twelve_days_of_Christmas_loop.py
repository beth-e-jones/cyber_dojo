#Twelve days of Christmas

#Creating dictionary of values for each gift
christmas_gifts = {"1st": "a partridge in a pear tree",
                   "2nd": "two turtle doves, and",
                   "3rd": "three french hens",
                   "4th": "four calling birds",
                   "5th": "FIVE GOLDEN RINGS",
                   "6th": "six geese a-laying", 
                   "7th": "seven swans a-swimming",
                   "8th": "eight maids a-milking",
                   "9th": "nine ladies dancing",
                   "10th": "ten lords a-leaping",
                   "11th": "eleven pipers piping",
                   "12th": "twelve drummers drumming"}


previous_gifts = []

#this is an f string where you can add the key value pairs for dictionary inro a string
for day, gift in christmas_gifts.items(): #if you were just doing the keys or values you'd do .keys or .values 
       #but because it's both you do .items
       print(f"on the {day} of Christmas my true love gave to me, {gift + ', ' + ', '.join(reversed(previous_gifts))}")
       previous_gifts.append(gift) #adds the extra stuff every time




