import random, math
from PIL import Image

random.seed()

class X:
  def eval(self, x, y):
    return x
  
  def __str__(self):
    return "x"

class Y:
  def eval(self, x, y):
    return y
  
  def __str__(self):
    return "y"

class SinPi:
  def __init__(self, prob):
    self.arg = buildExpr(prob * prob)

  def __str__(self):
    return "sin(pi*" + str(self.arg) + ")"

  def eval(self, x, y):
    return math.sin(math.pi * self.arg.eval(x, y))

class CosPi:
  def __init__(self, prob):
    self.arg = buildExpr(prob * prob)
  
  def __str__(self):
    return "cos(pi*" + str(self.arg) + ")"

  def eval(self, x, y):
    return math.cos(math.pi * self.arg.eval(x, y))

class TanPi:
  def __init__(self, prob):
    self.arg = buildExpr(prob * prob)

  def __str__(self):
    return "tan(pi/4*" + str(self.arg) + ")"

  def eval(self, x, y):
    return math.tan((math.pi / 4) * self.arg.eval(x, y))

class ArcsinPi:
  def __init__(self, prob):
    self.arg = buildExpr(prob * prob)

  def __str__(self):
    return "arcsin(pi/4*" + str(self.arg) + ")"

  def eval(self, x, y):
    return math.asin((math.pi / 4) * self.arg.eval(x, y))

class ArccosPi:
  def __init__(self, prob):
    self.arg = buildExpr(prob * prob)

  def __str__(self):
    return "arccos(pi/4*" + str(self.arg) + ")-pi/2"

  def eval(self, x, y):
    return math.acos((math.pi / 4) * self.arg.eval(x, y)) - (math.pi / 2)

class ArctanPi:
  def __init__(self, prob):
    self.arg = buildExpr(prob * prob)

  def __str__(self):
    return "(2/3)*arctan(pi*" + str(self.arg) + ")"

  def eval(self, x, y):
    return (2/3) * math.atan(math.pi * self.arg.eval(x, y))

class Multiplication:
  def __init__(self, prob):
    self.lhs = buildExpr(prob * prob)
    self.rhs = buildExpr(prob * prob)

  def __str__(self):
    return str(self.lhs) + "*" + str(self.rhs)

  def eval(self, x, y):
    return self.lhs.eval(x, y) * self.rhs.eval(x, y)

class Division:
  def __init__(self, prob):
    self.lhs = buildExpr(prob * prob)
    self.rhs = buildExpr(prob * prob)

  def __str__(self):
    return str(self.lhs) + "/" + str(self.rhs)

  def eval(self, x, y):
    try:
      return self.lhs.eval(x,y) / self.rhs.eval(x, y)
    except: # usually ValueError or ZeroDivisionError
      return random.uniform(-1.0, 1.0)

def buildExpr(prob = 0.99):
  if random.random() < prob:
    return random.choice([SinPi, CosPi, TanPi, ArcsinPi, ArccosPi, ArctanPi, Multiplication, Division])(prob)
  else:
    return random.choice([X, Y])()

# print(str(buildExpr()))

def plotIntensity(exp, pixelsPerUnit = 500):
  canvasWidth = 2 * pixelsPerUnit + 1
  canvas = Image.new("L", (canvasWidth, canvasWidth))

  for py in range(canvasWidth):
    for px in range(canvasWidth):
      # Convert pixel location to [-1,1] coordinates
      x = float(px - pixelsPerUnit) / pixelsPerUnit 
      y = -float(py - pixelsPerUnit) / pixelsPerUnit
      # z = exp.eval(x, y)
      z = calculateZ(exp, x, y)
      # z = zCalculate['result']
      # exp = zCalculate['exp']

      # Scale [-1,1] result to [0,255].
      intensity = int(z * 127.5 + 127.5)
      canvas.putpixel((px, py), intensity)

  return canvas

def calculateZ(exp, x, y):
  try:
    return exp.eval(x, y)
  except:
    return random.uniform(-1.0, 1.0)

def plotColor(redExp, greenExp, blueExp, pixelsPerUnit = 500):
    redPlane = plotIntensity(redExp, pixelsPerUnit)
    greenPlane = plotIntensity(greenExp, pixelsPerUnit)
    bluePlane = plotIntensity(blueExp, pixelsPerUnit)

    return Image.merge("RGB", (redPlane, greenPlane, bluePlane))

def makeImage(numPics = 5):
  with open("eqns.txt", 'w') as eqnsFile:
    for i in range(numPics):
      redExp = buildExpr()
      greenExp = buildExpr()
      blueExp = buildExpr()

      eqnsFile.write("img" + str(i) + ":\n")
      eqnsFile.write("red = " + str(redExp) + "\n")
      eqnsFile.write("green = " + str(greenExp) + "\n")
      eqnsFile.write("blue = " + str(blueExp) + "\n\n")

      image = plotColor(redExp, greenExp, blueExp)
      image.save("./output/img" + str(i) + ".png", "PNG")

makeImage()

# expTest = buildExpr()
# print(str(expTest))
# print(str(expTest.eval(0, 1)))
# plotIntensity(expTest)

# exp = math.cos(math.pi*math.asin((math.pi/4)*math.cos(math.pi*math.tan((math.pi/3)*(2/3)*math.atan(math.pi*math.tan((math.pi/3)*500))))))
# print(exp)