def isPrime(n): 
    # Corner case 
    if (n <= 1): 
        return False
  
    # Check from 2 to n-1 
    for i in range(2, n): 
        if (n % i == 0): 
            return False
  
    return True 
  

# Driver Program  
mas = input("number please:")
count = 0

for i in range(0,int(mas)+2):
    if isPrime(i):
        count = count + 1
        print(str(i) + " is the " + str(count) + " Prime number")
