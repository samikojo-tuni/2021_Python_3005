def main():
  jatka = True

  while jatka:
    try:
      print("Jakolasku")
      jaettava = int(input("Jaettava > "))
      jakaja = int(input("Jakaja > "))
      tulos = jaettava / jakaja

      print(f"Tulos: {tulos}")
      jatka = False
    except TypeError:
      print("Tekstille ei voida suorittaa laskutoimituksia")
    except ValueError:
      print("Syötä vain numeroita!")
    except ZeroDivisionError:
      print("Nollalla jako ei ole sallittua!")
    except KeyboardInterrupt:
      # Nostaa uudestaan saman virheen. Ctrl+C pitää kaataa sovellus
      raise KeyboardInterrupt()
    except:
      # Käsittelee kaikki muut virheet
      print("Tuntematon virhe!?!")


if __name__ == "__main__":
  main()
