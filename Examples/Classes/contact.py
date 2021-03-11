# Haetaan moduulista datetime luokka datetime ja otetaan se käyttöön tässä skriptissä
from datetime import datetime

class Contact:
  def __init__(self, first_name, last_name, phone, birth_year):
    self.first_name = first_name
    self.last_name = last_name
    self.phone = phone
    self.birth_year = birth_year

  def ToString(self):
    # f-string formatoi stringin siten, että {} sisällä oleva muuttuja korvataan muuttujan arvolla
    return f"{self.first_name} {self.last_name}, p. {self.phone}"

  def Age(self):
    current_year = datetime.now().year
    age = current_year - self.birth_year
    return age


def main():
  # Testataan Contact-luokan toimintaa main-funktiossa
  person1 = Contact("Maija", "Meikäläinen", "123456789", 1990)
  person2 = Contact("Matti", "Meikäläinen", "987654321", 1991)

  print(person1.first_name)
  print(person1.Age())
  print(person2.first_name)
  print(person2.Age())


if __name__ == "__main__":
  main()
