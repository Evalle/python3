#!/usr/bin/env python3


class LogicGate(object):

    def __init__(self, n):
        self.label = n
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
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


class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def get_pin(self):
        return int(input("Enter Pin input for gate " + self.get_label() + "-->"))


class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):

        a = self.get_pinA()
        b = self.get_pinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):

        a = self.get_pinA()
        b = self.get_pinB()
        if a == 0 and b == 0:
            return 0
        else:
            return 1


class NotGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def perform_gate_logic(self):

        a = self.get_pin()
        if a == 0:
            return 1
        else:
            return 0
