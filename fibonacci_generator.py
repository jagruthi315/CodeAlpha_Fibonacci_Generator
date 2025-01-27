def fibonacci_gen():
     a,b=0,1
     while True:
        yield a
        a,b=b,a+b

try:
    n= int(input("please enter the number of times you want the fibonacci number to be printed:"))
    if n<=0:
        print("please enter a positive integer")
    else:
      fib_gen = fibonacci_gen()
      for _ in range(n):

        print(next(fib_gen))

except ValueError :
        print( " invalid input please enter an integer value")

# here why is there a need to first store the function into a variable we could have just printed the function ryt  won't that be the same, well actually NO if we don't store the function in the variable before the print statement what will happen is in the for loop everytime function will be called from the start and not from the previous iteration why you ask because in that case we would be printing a function basically calling a function again and again in loop ..and the output will come 0 as many times you have given the range but now whats happening is we are calling a variable again and again which has stored the function of ours and if our function has values it also stores that so everytime we call it, it gives the stored value and the new value  also the variable should be created before the for loop starts..
