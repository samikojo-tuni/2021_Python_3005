from os import path
from contact import Contact

class PhoneBook:
  def __init__(self, path):
    self.contacts = []
    self.filePath = path

    self.ReadContacts()

  def AddContact(self, contact):
    self.contacts.append(contact)

  def PrintContacts(self):
    for contact in self.contacts:
      print(contact.ToString())

  def ReadContacts(self):
    if path.exists(self.filePath):
      file = open(self.filePath, "r", encoding="utf-8")
      for row in file:
        contact = row.strip().split(",")

        contact_obj = Contact(contact[0], contact[1], contact[2], contact[3])
        self.contacts.append(contact_obj)

      file.close()

  def SaveContacts(self):
    contacts = ""
    for contact in self.contacts:
      contacts += contact.ToCSV() + "\n"

    file = open(self.filePath, "w", encoding="utf-8")
    file.write(contacts)
    file.close()
