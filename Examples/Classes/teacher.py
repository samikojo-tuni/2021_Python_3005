from contact import Contact

class Teacher(Contact):
  def __init__(self, first_name, last_name, phone, birth_year, office):
    super().__init__(first_name, last_name, phone, birth_year)
    self.office = office

  def ToString(self):
    return f"{super().ToString()}, office: {self.office}"
