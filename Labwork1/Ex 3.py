#Ex 3
n = int(input("Enter the number:"))
if n <= 1:
  print(n, "is a NOT prime number")
else:
  prime = True
  for i in range (2, n):
        if n%i ==0:
          prime = False
          break
  if prime:
      print(n,"is prime")
  else:
      print(n, "is prime")