class PhoneBook:
  def __init__(self):
    self.contacts = []

  def AddContact(self, contact):
    self.contacts.append(contact)

  def PrintContacts(self):
    for contact in self.contacts:
      print(contact.ToString())
