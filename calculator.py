#defining a function to add numbers
def add(a,b):
        return int(a)+int(b)

#defining a function to subtract numbers    
def subtract(a,b):
        return int(a)-int(b)
    
#defining a function to multiply numbers   
def multiply(a,b):
        return int(a)*int(b)

if __name__ == '__main__':
    input1 = input('Enter first number: ')
    input2 = input('Enter second number: ')
    operation = input(str("Enter the operation : "))
    
    if operation == "+":
        print(add(input1,input2))
            
    elif operation == "-":
        print(subtract(input1,input2))
        
    elif operation == "*":
        print(multiply(input1,input2))
        
    else:
        print("Invalid Operation")
