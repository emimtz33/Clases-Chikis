def countdown(n):
    if n <= 0:
        print("Done")
    else:
        print(n)
        countdown(n-1)

countdown(5)

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print("Factorial" ,factorial(5))

def fibonachi(n):
   if n <= 1:
      return n
   else:
      return fibonachi(n-1) + fibonachi(n-2)

print("Func: ", fibonachi(7))
