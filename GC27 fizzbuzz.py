import random
FizzBuzz=1
for x in range(0,20):
  if FizzBuzz%3==0:
    number=print("Fizz")
  elif FizzBuzz%5==0:
    number=print("Buzz")
  elif FizzBuzz%3==0 and FizzBuzz%5==0:
    number=print("FizzBuzz")
  else:
    print(random.sample(range(21),1))
  FizzBuzz=FizzBuzz+1
