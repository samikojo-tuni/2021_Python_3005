#!/usr/bin/python3

import cgi
import cgitb
import os

cgitb.enable()  # Virheenkäsittelijä, joka osaa tulostaa lisätietoa virheestä nettisivulla.

def get_page_content(page_number):
  if page_number == 1:
    return "<p>Sivu 1</p>"
  elif page_number == 2:
    return "<p>Sivu 2</p>"
  else:
    return "<p>Tuntematon sivu</p>"

def print_page():
  print("Content-type: text/html")

  # GET tai POST, GET noutaa dataa serveriltä, POST lähettää dataa serverille
  cgi_method = os.environ["REQUEST_METHOD"]

  data = cgi.FieldStorage()
  page = int(data.getvalue("page", 1))

  page_content = get_page_content(page)

  page = f'''
  <html>
  <head><title>Testisivu</title></head>
  <body>
  Kutsu tehty seuraavalla metodilla: {cgi_method}
  {page_content}
  </body>
  </html>
  '''

  print(page)


print_page()
