def hello():
    print("Greetings Starfighter!")
hello()

def pack(a,b,c):
    return [a,b,c]

returnValue = pack("alpha","beta","gamma")
print(returnValue)

def eat_lunch(*args):
    if len(args) == 0:
        print("My lunchbox is empty!")
    else:
        firstTimer = True
        for arg in args:
            firstWord = ""
            if firstTimer == True:
                firstWord = "First"
                firstTimer = False          
            else:
                firstWord = "Next"                
            print(f"{firstWord} I eat {arg}")
eat_lunch()
eat_lunch("Apples")
eat_lunch("Ham","Eggs")
eat_lunch("Cookies","Ice Cream","Cake")