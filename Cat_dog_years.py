#I got them at the same time as kitten/puppy. That was humanYears years ago.

#Return their respective ages now as [humanYears,catYears,dogYears]

#humanYears >= 1
#humanYears are whole numbers only
#Cat Years
#15 cat years for first year
#+9 cat years for second year
#+4 cat years for each year after that
#Dog Years
#15 dog years for first year
#+9 dog years for second year
#+5 dog years for each year after that

# Create input to categorise pet (input means people write into terminal)
pet = input("Is your pet a cat or dog?")

if pet == "dog":
    DogAge = input("What is the age of your dog?")
    # Classifies the input text as an integer 
    DogAge = int(DogAge)
    print(f"The age of your dog in human years is {DogAge}")
    if DogAge == 1:
        print (DogAge + 14) # Calculates dog age and presents it
    elif DogAge == 2:
        print (f"The age of your dog in dog years is {DogAge + 22}")
    else:
        print (f"The age of your dog in dog years is {24 + ((DogAge-2)* 5)}")

if pet == "cat":
    CatAge = input("What is the age of your cat?")
    CatAge = int(CatAge)
    print(f"The age of your cat in human years is {CatAge}")
    if CatAge == 1:
       print (f"The age of your cat in cat years is {CatAge + 14}")
    elif CatAge == 2:
        print (f"The age of your cat in cat years is {CatAge + 22}")
    else:
        print (f"The age of your cat in cat years is {24 + ((CatAge-2)* 4)}") 
else:
    print("Sorry, I can't convert the age for that kind of animal!")