import random


#DICHOTOMIC SEARCH
def search():
    turn = 0 
    high = 100
    low = 1 
    n = random.randrange(1 , 100)

    while ( high - low >=2 ):
        
        turn = turn + 1
        med = (low + high)/2
        if med == n :
            print("Right answer")
        elif med < n :
            print("too low")
            low = med + 1
        elif med > n : 
            print("too high")
            high = med - 1


search()