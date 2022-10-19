#Write your code below this row 👇

#How I solved it!
range1=range(1,101)

for fizzy in range1:
  if fizzy % 3 == 0 and fizzy % 5 == 0:
    fizzy = "FizzBuzz"
  elif fizzy % 3 == 0:
    fizzy = "Fizz"
  elif fizzy % 5 == 0:
    fizzy = "Buzz"
  print(fizzy)
  
  #How my professor solved it!
for fizzy in range1:
  if fizzy % 3 == 0 and fizzy % 5 == 0:
    print("FizzBuzz")
  elif fizzy % 3 == 0:
    print("Fizz")
  elif fizzy % 5 == 0:
    print("Buzz")
  else:
      print(fizzy)
