import math


def main():

  while True:
    num = int(input("Enter a positive number: "))
    
    if num > 0:
      ans = math.factorial(num)
      print(f"Factorial of {num} is equal to {ans}")
      break
    else:
      print("Invalid input! Enter a positive number!")
    

main()