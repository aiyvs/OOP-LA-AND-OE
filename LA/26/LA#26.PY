# MODULE
# FILE NAME - turtle.py
from abc import ABC, abstractmethod

class NinjaTurtle(ABC):
    @property
    @abstractmethod
    def alias(self):
        pass

class Leonardo(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias

    @property
    def alias(self):
        return self.__alias

class Michelangelo(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias

    @property
    def alias(self):
        return self.__alias

class Donatello(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias

    @property
    def alias(self):
        return self.__alias

class Raphael(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias

    @property
    def alias(self):
        return self.__alias

# MAIN
# FILE NAME - main.py
import turtle

leo = turtle.Leonardo("Leonardo", "Katana")
gelo = turtle.Michelangelo("Michelangelo", "Nunchaku")
tel = turtle.Donatello("Donatello", "Bo staff")
rap = turtle.Raphael("Raphael", "Sai")

print(leo.alias)
print(gelo.alias)
print(tel.alias)
print(rap.alias)
