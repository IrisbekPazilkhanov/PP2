def my_function(*, x):
  print(x)

my_function(x = 3)



def my_function1(x):
  print(x)

my_function1(3)



def my_function2(a, b, /, *, c, d):
  print(a + b + c + d)

my_function2(5, 6, c = 7, d = 8)
