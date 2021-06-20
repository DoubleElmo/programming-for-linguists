"""
Programming for linguists

Implementation of the Reverse Polish Notation Converter
"""
from algorithms.calculator.reverse_polish_notation import ReversePolishNotation, Digit, Op
from data_structures.stack.stack import Stack


class ReversePolishNotationCalculator:
    """
    Calculator of expression in Reverse Polish Notation
    """
    def __init__(self):
        self.stack = Stack()

    def calculate(self, rpn_expression: ReversePolishNotation) -> float:
        """
        Main method of the ReversePolishNotationCalculator class.
        Calculating result of expression in Reverse Polish Notation.

        :param rpn_expression: expression in Reverse Polish Notation Format
        :return: result of the expression
        """
        for el in rpn_expression:
            if isinstance(el, Digit):
                self.stack.push(el)
            if isinstance(el, Op):
                hitotsu = self.stack.top()
                self.stack.pop()
                futatsu = self.stack.top()
                self.stack.pop()
                self.stack.push(el(hitotsu, futatsu))
            res = self.stack.top()
            return res