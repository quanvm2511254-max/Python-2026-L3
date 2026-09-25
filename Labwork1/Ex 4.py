#Ex 4
n = int(input("Enter number:"))
s = 0 # sum all divisors
for i in range(1, n):
  if n % i ==0:
    s +=i

if s ==n:
  print("YES perfect")