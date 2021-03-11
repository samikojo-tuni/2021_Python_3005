from phonebook import PhoneBook
from contact import Contact
from student import Student
from teacher import Teacher

def main():
  phonebook = PhoneBook()

  person1 = Contact("Maija", "Meikäläinen", "123456789", 1990)
  person2 = Contact("Matti", "Meikäläinen", "987654321", 1991)
  person3 = Student("Osku", "Opiskelija", "987656789", 2000, 54321)
  person4 = Teacher("Sami", "Kojo-Fry", "12121212", 1987, "A3-??")

  phonebook.AddContact(person1)
  phonebook.AddContact(person2)
  phonebook.AddContact(person3)
  phonebook.AddContact(person4)

  phonebook.PrintContacts()


if __name__ == "__main__":
  main()
