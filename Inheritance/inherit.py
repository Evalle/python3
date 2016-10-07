#!/usr/bin/env python3


class LogicGate(object):

    def __init__(self, n):
        self.label = n
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None

    def get_pinA(self):
        return int(input("Enter Pin A input for gate " + self.get_label() + "-->"))

    def get_pinB(self):
        return int(input("Enter Pin B input for gate " + self.get_label() + "-->"))
