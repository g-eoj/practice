def numbers(n, ia):
  i = 0
  numbers = []
  for i in range(0, n, ia):
    print "At the top i is %d" % i
    numbers.append(i)
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
  return numbers

numbers = numbers(5, 2)

print "The numbers: "

for num in numbers:
  print num
