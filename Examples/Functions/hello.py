# None on Python-kielen null eli tyhjä arvo. None ei viittaa mihinkään.
# Huom! eri asia kuin esim. 0, False tai ""
def hello(name=None):
  if name is None:
    print("Hello")
  else:
    print("Hello", name)


hello()
hello("Saara")
