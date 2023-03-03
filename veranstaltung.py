class Sitzplatz:


  def __init__(self, r, s):
    self.reihe = r
    self.sitznummer = s

  # def __del__(self):
  #   print("Buchung gelöscht")

  def __repr__(self):
    return(f"Reihe: {self.reihe} Nummer: {self.sitznummer}")



class Veranstaltung:


  def __init__(self, n):
    self.name = n
    self.sitzplatzliste = []

  # def __del__(self):
  #   print("Veranstaltung gelöscht")

  def buche(self, r, s):
    self.sitzplatzliste.append(Sitzplatz(r, s))
    print("*** Sitzplatz gebucht ***")

  def __repr__(self):   # Representations Methode
    return self.name

  def show(self):
    print("Veranstaltung:", self.name)
    for b in self.sitzplatzliste:
      print(b)



v = Veranstaltung("Vorstellung Python 4.0")
v.buche(3,2)
v.buche(7,4)
v.buche(2,2)
v.buche(8,3)

v.show()