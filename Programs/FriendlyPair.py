def printDivisors(n, factors) :
     
    # Note that this loop runs till square root
    i = 1
    while i <= pow(n,0.5):
         
        if (n % i == 0) :
             
            # If divisors are equal, print only one
            if (n / i == i) :
                factors.append(i)
            else :
                # Otherwise print both
                factors.append(i)
                factors.append(int(n/i))
        i = i + 1
    return sum(factors) - n

if __name__ == "__main__": 
  number1, number2 = 6, 28
  if int(printDivisors(number1, [])/number1) == int(printDivisors(number2, [])/number2):
    print("Friendly pair")
  else:
    print("Not a Friendly Pair")
