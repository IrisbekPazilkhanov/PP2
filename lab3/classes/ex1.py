class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
############################################


class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person1("John", 36)

print(p1)
################################################

class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person2("John", 36)

print(p1)