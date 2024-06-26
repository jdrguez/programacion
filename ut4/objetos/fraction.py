from __future__ import annotations


class Fraction:
    def __init__(self, num: int, den: int):
        self.max_cmon_div = self.gcd(num, den)
        self.num = num // self.max_cmon_div
        self.den = den // self.max_cmon_div
        

    def __add__(self, other: Fraction):
        if isinstance(other, Fraction):
            new_num = self.num * other.den + self.den * other.num 
            new_den = self.den * other.den 
            return Fraction(new_num, new_den)

    def __sub__(self, other: Fraction):
        if isinstance(other, Fraction):
            new_num = self.num * other.den - self.den * other.num
            new_den = self.den * other.den 
            return Fraction(new_num, new_den)

    def __mul__(self, other: Fraction):
        if isinstance(other, Fraction):
            new_num = self.num * other.num
            new_den = self.den * other.den
            return Fraction(new_num, new_den)

    def __truediv__(self, other: Fraction):
        if isinstance(other, Fraction):
            new_num = self.num * other.den 
            new_den = self.den * other.num 
            return Fraction(new_num, new_den)

    def __str__(self):
        return f'Your Fraction is {self.num}/{self.den}' 

    @staticmethod
    def gcd(a: int, b: int) -> int:
        '''Euclid's Algorithm'''
        while b > 0:
            a, b = b, a % b
        return a
