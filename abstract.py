class form:

  def __init__(self, name, height, width):
    self.name = name
    self.height = height
    self.width  = width

  def calcFace(self):
    print("Formel is missing")

  def __repr__(self) -> str:
    return self.name


class square(form):

  def __init__(self, name, height, width):
    super().__init__(name, height, width)

  def calcFace(self):
    face = self.height *self.width
    print(face)


mySquare = square("peter", 4, 3)

mySquare.calcFace()
