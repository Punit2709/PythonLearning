x = 5

def function():
    global x
    y = x
    y = 15
    
    # magical line below
    x = y
    
    print("Y:", y)
    print("X:", x)
    print("ID of Y: ", id(y))
    print("ID of X: ", id(x))
    
    y = 20
    print("ID of Y: ", id(y))
    print("ID of X: ", id(x))
    print("Y:", y)
    print("X:", x)
    
function()
print("X:",x)