class ValueOutOfRangeError(ValueError):
  pass

def main():
  exit = False

  while not exit:
    try:
      user_input = int(input("Syötä luku väliltä [0, 10] > "))

      if user_input < 0 or user_input > 10:
        raise ValueOutOfRangeError()

      exit = True
    except ValueOutOfRangeError:
      print("Arvo ei ole sallitulla välillä")
    except ValueError:
      print("Virheellinen arvo")
    except Exception:
      print("Tuntematon virhe")


if __name__ == "__main__":
  main()
