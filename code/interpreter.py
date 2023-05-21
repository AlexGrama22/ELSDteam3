from geometrydslParser import geometrydslParser
import math


class GInter:
    def __init__(self, tree):
        self.tree = tree
        self.vars = {}

    def getVars(self):
        print(self.vars)
        i = 0
        start = self.tree.getChild(0)
        while start is not None:
            if isinstance(start, geometrydslParser.VariableDeclarationsContext):
                self.vcontext(start)
            i += 1
            start = self.tree.getChild(i)
        print(self.vars)

    def getMeth(self):
        i = 0
        start = self.tree.getChild(0)
        while start is not None:
            if isinstance(start, geometrydslParser.MethodInvocationsContext):
                self.mcontext(start)
            i += 1
            start = self.tree.getChild(i)

    def vcontext(self, var):
        if isinstance(var, geometrydslParser.VariableDeclarationContext):
            self.vars[var.getChild(1).getText()] = {"type": var.getChild(0).getText()}
        if isinstance(var, geometrydslParser.VariableDeclarationsContext):
            self.vcontext(var.getChild(0))
            self.vcontext(var.getChild(1))

    def mcontext(self, var):
        if isinstance(var, geometrydslParser.MethodInvocationContext):
            if var.getChild(2).getText() == "setParameters":
                var_name = var.getChild(0).getText()
                if self.vars[var_name]['type'] == "Square" or self.vars[var_name]['type'] == "Cube":
                    print(var_name)
                    self.vars[var_name]['side'] = var.getChild(4).getText()
                if self.vars[var_name]['type'] == "Triangle":
                    print(var_name)
                    a = float(var.getChild(4).getChild(0).getChild(0).getText())
                    b = float(var.getChild(4).getChild(0).getChild(2).getText())
                    c = float(var.getChild(4).getChild(2).getText())
                    if (a + b) > c and (a + c) > b and (b + c) > a:
                        self.vars[var_name]['side1'] = var.getChild(4).getChild(0).getChild(0).getText()
                        self.vars[var_name]['side2'] = var.getChild(4).getChild(0).getChild(2).getText()
                        self.vars[var_name]['side3'] = var.getChild(4).getChild(2).getText()
                    else:
                        raise Exception("Impossible Triangle")
                if self.vars[var_name]['type'] == "Circle" or self.vars[var_name]['type'] == "Sphere":
                    print(var_name)
                    self.vars[var_name]['diameter'] = var.getChild(4).getText()
                if self.vars[var_name]['type'] == "Rectangle":
                    print(var_name)
                    self.vars[var_name]['length'] = var.getChild(4).getChild(0).getText()
                    self.vars[var_name]['width'] = var.getChild(4).getChild(2).getText()
                if self.vars[var_name]['type'] == "Cylinder" or self.vars[var_name]['type'] == "Cone":
                    print(var_name)
                    self.vars[var_name]['diameter'] = var.getChild(4).getChild(0).getText()
                    self.vars[var_name]['height'] = var.getChild(4).getChild(2).getText()
                if self.vars[var_name]['type'] == "Parallelogram":
                    print(var_name)
                    if var.getChild(4).getChild(0).getChild(2) is not None:
                        self.vars[var_name]['length'] = var.getChild(4).getChild(0).getChild(0).getText()
                        self.vars[var_name]['width'] = var.getChild(4).getChild(0).getChild(2).getText()
                        self.vars[var_name]['angle'] = var.getChild(4).getChild(2).getText()
                    else:
                        self.vars[var_name]['length'] = var.getChild(4).getChild(0).getText()
                        self.vars[var_name]['width'] = var.getChild(4).getChild(2).getText()
                        self.vars[var_name]['angle'] = "60"
                if self.vars[var_name]['type'] == "Ellipse":
                    print(var_name)
                    self.vars[var_name]['major'] = var.getChild(4).getChild(0).getText()
                    self.vars[var_name]['minor'] = var.getChild(4).getChild(2).getText()
            if var.getChild(2).getText() == "perimeter":
                var_name = var.getChild(0).getText()
                if self.vars[var_name]['type'] == "Square":
                    a = float(self.vars[var_name]['side'])
                    p = a * 4
                    print("Perimeter of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        p) + " units")
                if self.vars[var_name]['type'] == "Cube":
                    a = float(self.vars[var_name]['side'])
                    p = a * 12
                    print("Perimeter of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        p) + " units")
                if self.vars[var_name]['type'] == "Triangle":
                    a = float(self.vars[var_name]['side1'])
                    b = float(self.vars[var_name]['side2'])
                    c = float(self.vars[var_name]['side3'])
                    p = a + b + c
                    print("Perimeter of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        p) + " units")
                if self.vars[var_name]['type'] == "Circle":
                    a = float(self.vars[var_name]["diameter"])
                    r = a / 2
                    p = 2 * math.pi * r
                    print("Perimeter of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        p) + " units")
                if self.vars[var_name]['type'] == "Rectangle":
                    l = float(self.vars[var_name]['length'])
                    w = float(self.vars[var_name]['width'])
                    p = 2 * l + 2 * w
                    print("Perimeter of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        p) + " units")
                if self.vars[var_name]['type'] == "Cylinder":
                    d = float(self.vars[var_name]['diameter'])
                    h = float(self.vars[var_name]['height'])
                    r = d / 2
                    p = 4 * r + 2 * h
                    print("Perimeter of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        p) + " units")
                if self.vars[var_name]['type'] == "Parallelogram":
                    l = float(self.vars[var_name]['length'])
                    w = float(self.vars[var_name]['width'])
                    p = 2 * l + 2 * w
                    print("Perimeter of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        p) + " units")
                if self.vars[var_name]['type'] == "Ellipse":
                    # using Ramanujan formula
                    a = float(self.vars[var_name]['major']) / 2
                    b = float(self.vars[var_name]['minor']) / 2
                    h = pow((a - b), 2) / pow((a + b), 2)
                    p = math.pi * (a + b) * (1 + ((3 * h) / (10 + math.sqrt(4 - 3 * h))))
                    print("Perimeter of a " + self.vars[var_name][
                        'type'] + " " + var_name + " is approximately equal to " + str(p) + " units")
            if var.getChild(2).getText() == "area":
                var_name = var.getChild(0).getText()
                if self.vars[var_name]['type'] == "Square":
                    a = float(self.vars[var_name]['side'])
                    area = pow(a, 2)
                    print("Area of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        area) + " square units")
                if self.vars[var_name]['type'] == "Cube":
                    a = float(self.vars[var_name]['side'])
                    area1 = 4 * pow(a, 2)
                    area2 = 6 * pow(a, 2)
                    print("Lateral area of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        area1) + " square units")
                    print("Total area of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        area2) + " square units")
                if self.vars[var_name]['type'] == "Triangle":
                    a = float(self.vars[var_name]['side1'])
                    b = float(self.vars[var_name]['side2'])
                    c = float(self.vars[var_name]['side3'])
                    s = (a + b + c) / 2
                    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                    print("Area of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        area) + " square units")
                if self.vars[var_name]['type'] == "Circle":
                    a = float(self.vars[var_name]['diameter'])
                    r = a / 2
                    area = math.pi * pow(r, 2)
                    print("Area of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        area) + " square units")
                if self.vars[var_name]['type'] == "Sphere":
                    a = float(self.vars[var_name]['diameter'])
                    r = a / 2
                    area = 4 * math.pi * pow(r, 2)
                    print("Area of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        area) + " square units")
                if self.vars[var_name]['type'] == "Rectangle":
                    l = float(self.vars[var_name]['length'])
                    w = float(self.vars[var_name]['width'])
                    area = l * w
                    print("Area of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        area) + " square units")
                if self.vars[var_name]['type'] == "Cylinder":
                    d = float(self.vars[var_name]['diameter'])
                    h = float(self.vars[var_name]['height'])
                    r = d / 2
                    area1 = 2 * math.pi * r * h
                    area2 = 2 * math.pi * r * (r + h)
                    print("Lateral area of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        area1) + " square units")
                    print("Total area of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        area2) + " square units")
                if self.vars[var_name]['type'] == "Cone":
                    d = float(self.vars[var_name]['diameter'])
                    h = float(self.vars[var_name]['height'])
                    r = d / 2
                    l = math.sqrt(pow(r, 2) + pow(h, 2))
                    area1 = math.pi * r * l
                    area2 = math.pi * r * (r + l)
                    print("Lateral area of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        area1) + " square units")
                    print("Total area of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        area2) + " square units")
                if self.vars[var_name]['type'] == "Parallelogram":
                    l = float(self.vars[var_name]['length'])
                    w = float(self.vars[var_name]['width'])
                    a = float(self.vars[var_name]['angle'])
                    h = math.sin(math.radians(a)) * w
                    area = l * h
                    print("Area of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        area) + " square units")
                if self.vars[var_name]['type'] == "Ellipse":
                    a = float(self.vars[var_name]['major']) / 2
                    b = float(self.vars[var_name]['minor']) / 2
                    area = math.pi * a * b
                    print("Area of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        area) + " square units")
            if var.getChild(2).getText() == "radius":
                var_name = var.getChild(0).getText()
                if self.vars[var_name]['type'] == "Circle" or self.vars[var_name]['type'] == "Sphere" or self.vars[var_name]['type'] == "Cylinder" or self.vars[var_name]['type'] == "Cone":
                    a = float(self.vars[var_name]["diameter"])
                    r = a / 2
                    print("Radius of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        r) + " units")
            if var.getChild(2).getText() == "diagonal":
                var_name = var.getChild(0).getText()
                if self.vars[var_name]['type'] == "Square":
                    a = float(self.vars[var_name]['side'])
                    diagonal = a * math.sqrt(2)
                    print("Diagonal of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        diagonal) + " units")
                if self.vars[var_name]['type'] == "Rectangle":
                    l = float(self.vars[var_name]['length'])
                    w = float(self.vars[var_name]['width'])
                    diagonal = math.sqrt(pow(l, 2) + pow(w, 2))
                    print("Diagonal of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        diagonal) + " units")
                if self.vars[var_name]['type'] == "Parallelogram":
                    l = float(self.vars[var_name]['length'])
                    w = float(self.vars[var_name]['width'])
                    a = float(self.vars[var_name]['angle'])
                    diagonal1 = math.sqrt((pow(l, 2) + pow(w, 2) + 2 * l * w * math.cos(math.radians(a))))
                    diagonal2 = math.sqrt((pow(l, 2) + pow(w, 2) - 2 * l * w * math.cos(math.radians(a))))
                    print("First diagonal of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        diagonal1) + " and second diagonal is equal to " + str(diagonal2) + " units")
            if var.getChild(2).getText() == "volume":
                var_name = var.getChild(0).getText()
                if self.vars[var_name]['type'] == "Cube":
                    a = float(self.vars[var_name]['side'])
                    v = pow(a, 3)
                    print("Volume of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        v) + " cube units")
                if self.vars[var_name]['type'] == "Circle":
                    a = float(self.vars[var_name]['diameter'])
                    r = a / 2
                    v = (4 / 3) * math.pi * pow(r, 3)
                    print("Volume of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        v) + " cube units")
                if self.vars[var_name]['type'] == "Cylinder":
                    d = float(self.vars[var_name]['diameter'])
                    h = float(self.vars[var_name]['height'])
                    r = d / 2
                    v = math.pi * pow(r, 2) * h
                    print("Volume of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        v) + " cube units")
                if self.vars[var_name]['type'] == "Cone":
                    d = float(self.vars[var_name]['diameter'])
                    h = float(self.vars[var_name]['height'])
                    r = d / 2
                    v = math.pi * pow(r, 2) * (h / 3)
                    print("Volume of a " + self.vars[var_name]['type'] + " " + var_name + " is equal to " + str(
                        v) + " cube units")
            if var.getChild(2).getText() == "median":
                var_name = var.getChild(0).getText()
                if self.vars[var_name]['type'] == "Triangle":
                    a = float(self.vars[var_name]['side1'])
                    b = float(self.vars[var_name]['side2'])
                    c = float(self.vars[var_name]['side3'])
                    m1 = math.sqrt((2 * pow(b, 2) + 2 * pow(c, 2) - pow(a, 2)) / 4)
                    m2 = math.sqrt((2 * pow(a, 2) + 2 * pow(c, 2) - pow(b, 2)) / 4)
                    m3 = math.sqrt((2 * pow(b, 2) + 2 * pow(a, 2) - pow(c, 2)) / 4)
                    print("Median of a first side of a " + self.vars[var_name][
                        'type'] + " " + var_name + " is equal to " + str(m1) + " units")
                    print("Median of a second side of a " + self.vars[var_name][
                        'type'] + " " + var_name + " is equal to " + str(m2) + " units")
                    print("Median of a third side of a " + self.vars[var_name][
                        'type'] + " " + var_name + " is equal to " + str(m3) + " units")
        if isinstance(var, geometrydslParser.MethodInvocationsContext):
            self.mcontext(var.getChild(0))
            self.mcontext(var.getChild(1))
