PI = 3.14159265359

def sum(*numbers):
  result = 0
  for number in numbers:
    result += number
  return result

def factorial(n):
  if n < 0:
    return None
  elif n == 0 or n == 1:
    return 1

  result = 1
  while n > 1:
    result *= n
    n -= 1

  return result

def max(*numbers):
  maxValue = None
  for number in numbers:
    if maxValue == None or number > maxValue:
      maxValue = number
  return maxValue


def min(*numbers):
  minValue = None
  for number in numbers:
    if minValue == None or number < minValue:
      minValue = number
  return minValue


def main():
  print("matikkakirjasto")


if __name__ == "__main__":
  main()
