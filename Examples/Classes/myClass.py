# Yksinkertainen esimerkki luokan määrittämisestä Pythonissa.
class MyClass:
  name = "My Object"  # Luokan jäsenmuuttuja. Jäsenmuuttujat määrittävät luokan datan

  # Luokassa määritettyä funktiota kutsutaan jäsenfunktioksi tai metodiksi
  def printName(self):  # parametri self viittaa olioon itseensä
    print(self.name)


object1 = MyClass()  # Luo olion luokasta MyClass ja tallentaa sen muuttujaan object1
object2 = MyClass()

object1.name = "The best object there is"

object1.printName()
object2.printName()
