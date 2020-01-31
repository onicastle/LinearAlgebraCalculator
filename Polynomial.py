from Term import Term
import tokenize
from numba import *
import numpy as np
import time

"""
Polynomial is a List of Terms
"""
class Polynomial():

    def __init__(self):
        self.terms = []

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        result = str()

        if len(self.terms) is 0:
            return "0.00"
        i = 0
        for x in self.terms:
            if i < len(self.terms) - 1:
                result += str(x) + "+"
                i = i + 1
            else:
                result += str(x)
        return result

    def sumDegree(self):
        temporary_term = None
        result = self.terms
        newList = []
        i = 1
        while i < len(result):
            a = result[i - 1]
            b = result[i]

            if(a.exponent is b.exponent):
                newList.append(Term(a.coefficient + b.coefficient, a.exponent))
            else:
                newList.append(b)
            i = i + 1

        self.terms = newList
        return self.terms


    def fix(self):
        self.terms = sorted(self.terms, key=lambda l: l.exponent, reverse=True)

        temporary = self.sumDegree()
        i = 0

        for x in self.terms:
            if x.coefficient is not 0:
                temporary.append(Term(x.coefficient, x.exponent))
        self.terms = temporary
        return self.terms

    def termFromString(self, string):

        string_tokentizer = string.split("+")
        for x in string_tokentizer:
            temp = Term(0,0).fromString(x)
            self.terms.append(temp)

    def add(self, other):
        temp = list()
        result = list()

        for element in other.terms:
            temp.append(element)

        for x,y in zip(temp, self.terms):
            temp1, tempo1 = x.coefficient, y.coefficient
            if temp1 is tempo1:
                newTerm = Term(x.coefficient + y.coefficient, x.exponent)
                temp.append(newTerm)
            elif x.exponent > y.exponent:
                temp.append(x)
            elif x is 'C' or y is 'C':
                pass
            else:
                temp.append(y)

        self.terms = temp
        return self.terms

    def undefined_integral(self):
        temp = list()
        for x in self.terms:
            if np.equal(x.exponent, 0):
                temp.append(Term(x.coefficient, x.exponent+1))
            else:
                a = np.divide(x.coefficient, x.coefficient +1)
                temp.append(Term(a, x.exponent+1))
        temp.append('C')

        return self.terms

    def defined_integral(self, upper, lower):
        integral = self.undefined_integral()

        return self.terms



    def __eq__(self, other):
        if self.terms == other.terms:
            return True
        else:
            return False

t = Polynomial()
t.termFromString("4x^4 + 3x^4 + 5x + 4x^3")
t.sumDegree()
t0 = time.time()
t.undefined_integral()
t1 = time.time()




print(t)
print(np.subtract(t1,  t0))