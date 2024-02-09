# example:
def increment(nr: float) -> float:
  return nr + 1

def decrement(nr: float) -> float:
  return nr - 1

def add(nr1: float, nr2: float) -> float:
  return nr1 + nr2

def subtract(nr1: float, nr2: float) -> float:
  return nr1 - nr2

def multiply(nr1: float, nr2: float) -> float:
  return nr1 * nr2

def divide(nr1: float, nr2: float) -> float:
  try:
    return nr1 / nr2
  except ZeroDivisionError:
    print("er ging iets fout met het delen")

def Greater(nr1: float, nr2: float) -> float:
  if nr1 > nr2:
    return f"Maximum: {nr1} en minimum: {nr2}"
  elif nr2 > nr1:
    return f"Maximum: {nr2} en minimum: {nr1}"
  else:
    return "Beide getallen zijn even groot"
  

