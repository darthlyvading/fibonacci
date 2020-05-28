terms = int(input("enter the number of terms "))
n1 = 0
n2 = 1
count = 0
if terms <= 0:
   print("terms should be > 0")
elif terms == 1:
   print("Fibonacci series of ",terms," is :")
   print(n1)
else:
   print("Fibonacci series is :")
   while count < terms:
       print(n1)
       total = n1 + n2
       n1 = n2
       n2 = total
       count += 1
