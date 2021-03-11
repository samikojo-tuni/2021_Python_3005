from contact import Contact

# Opiskelija laajentaa Contact tyyppiä opiskelijanumerolla
class Student(Contact):
  def __init__(self, first_name, last_name, phone, birth_year, student_number):
    # Suorittaa kantaluokan (Contact) konstructorin
    super().__init__(first_name, last_name, phone, birth_year)
    self.student_number = student_number

  def ToString(self):
    base = super().ToString()
    return f"{base} #{self.student_number}"
