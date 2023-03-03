class SquareFunc:

  def parable(x, scale, r=2, reverse = False):

    x = x / scale
    x -= 0.5

    rev = -1

    if reverse:
      rev = 1

    f = rev*(4*scale) *((x) *(x)) + scale

    return round(f,r)

value = 500

def test():

  for i in range(value):
    
    print(SquareFunc.parable(i, value))

if __name__ == "__main__":
  test()
