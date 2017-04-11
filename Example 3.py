a =eval(input("A's Guess: "))
b =eval(input("B's Guess: "))
actual=eval(input("Actual Price: "))

if a< actual and b> actual:
    print("The Winner is: Player A")
    
if a> actual and b< actual:
    print("The Winner is: Player B")
    
if a> actual and b> actual:
    print("No Winner")

if (a/actual)> (b/actual) and a< actual and b < actual:
    print("The Winner is: Player A")
    
if (a/actual)< (b/actual) and a< actual and b < actual:
    print("The Winner is: Player B")
