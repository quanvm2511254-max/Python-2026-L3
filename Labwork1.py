#Ex1
radius  = float(input("Enter the radius:"))
area = 3.14 * radius**2
print(area)

#Ex 2
Celsius = int(input("Enter the Celsius:"))
Fahrenheit = Celsius*1.8 + 32
print(Fahrenheit)

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

#Ex 4
n = int(input("Enter number:"))
s = 0 # sum all divisors
for i in range(1, n):
  if n % i ==0:
    s +=i

if s ==n:
  print("YES perfect")

#Ex 5
a = input(str("Enter strings"))
if ("the color is my favorite"):
  print("Your colod is at index 3 in my list.")
else ("the color is not my favorite"):
  print("Sorry, I could not find your color")
print("What is your favorite color?")

#Ex 6
range1 = list(range(0, 7))
range2 = list(range(1, 11, 3))
range3 = list(range(5, 0, -1))
range4 = list(range(6, -4, -2))
print(range1, range2, range3, range4)

#Ex 7
s="hell$$$no$$$"
s1 = s.replace("$", "")
print(s1)
s2 = "".join([ c for c in s if c != "$"])
print(s2)

#Ex 8
col = int(input("cols? "))
row = int(input("rows? "))
for i in range(row):
    for j in range(col):
        if i == 0 or i == row - 1 or j == 0 or j == col - 1:
            s+="* "
        else:
            s+=" "
    print(s)

#Ex 9
col = int(input("cols? "))
row = int(input("rows? "))
print("* " * col)
for i in range(row-2):
    print("* " + " " * (col-2)+ "* ")
    print("* " * col)

#Ex 10
col = int(input("cols? "))
row = int(input("rows? "))
for i in range(row):
    for j in range(col):
        if i == 0 or i == row - 1 or j == 0 or j == col - 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()