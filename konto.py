class Konto:

  def __init__(self, besitzer:str, kontostand:float=0.0):

    self.besitzer = besitzer
    self.__kontostand = kontostand

  def buchung(self, betrag:float):
    pass

  def getKontostand(self):
    return self.__kontostand

  def __repr__(self) -> str:
    return self.besitzer


class Girokonto(Konto):

  def __init__(self, besitzer:str, kontostand:float=0.0):
    super().__init__(besitzer, kontostand)


meinGiro = Girokonto("Alexander Schumacher", 3652.23)

print(meinGiro.getKontostand())

