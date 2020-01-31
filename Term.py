class Term:

    def __init__(self, coefficient = None, exponent = None, string=None):
        if string is not None:
            self = Term(coefficient=0, exponent=0)
            self.fromString(string)
        if coefficient is None:
            self.coefficient = float(0)
        else:
            self.coefficient = coefficient
        if exponent is None:
            self.exponent = 0
        else:
            self.exponent = exponent

    def __repr__(self):
        return [self.coefficient, self.exponent]

    def __str__(self):
        if self.coefficient is not 0 and self.exponent is 0:
            return """{}""".format(float(self.coefficient))
        elif self.coefficient and self.exponent is not 0:
            return """{}x^{}""".format(float(self.coefficient), self.exponent)
        else:
            return """0.00"""

    def get(self):
        return self.coefficient, self.exponent

    def evaluate(self, var=None):

        if var is None:
            return self.coefficient ** self.exponent

        return self.coefficient * (var ** self.exponent)

    def toString(self):
        if self.coefficient or self.exponent is 0:
            return "0.0"
        else:
            return """{)x^{}""".format(self.coefficient, self.exponent)

    def get_exponent(self):
        return self.exponent
    def fromString(self, string):
        temporary = str(string)


        if "x^" in temporary:
            list = temporary.split("x^")

            if len(list) == 0:
                raise NotImplementedError

            elif len(list) == 1:
                exponent = int(list[0])
                result = Term(float(1), exponent)
                self = result
                return result
            else:
                coefficient = float(list[0])
                exponent = int(list[1])
                result = Term(coefficient,exponent)
                self = result
                return result
        elif "x" is temporary:
            result = Term(float(1),1)
            self = result
            return result
        elif "x" in temporary:
            list = temporary.split("x")
            if len(list) is 0:
                result = Term(float(1), 1)
                self = result
                return result
            else:
                coefficient = float(list[0])
                result = Term(coefficient, 1)
                self = result
                return result
        else:
            return Term(float(temporary), 0)