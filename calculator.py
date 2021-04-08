"""
Calculator module
Provides a single class with one public method calculate
Pass in a text string with an algorithmic expression to determine the result
"""
import re

class Calculator:
    # valid_expression is a class variable because this is the same for all instances
    # This regex pattern determines if the expression represents a valid sum
    # It assumes no spaces or variables are used
    valid_expression = re.compile(
        "\(?(\d{1,})((\+|\-|\*|\/)(\d{1,}))?\)?(\+|\-|\*|\/)?"
    )

    def calculate(self, expression):
        """
        Given a valid algorithmitc expression, return result.
        Return None if expression is not valid.
        """
        # Guard clause - protect against being passed nothing
        if expression is None:
            return None

        processed_expression = self.__remove_whitespace(expression)

        if self.__is_valid_expression(processed_expression) is None:
            return None

        try:
            result = eval(processed_expression)
        except Exception:
            # Handles case where expression is not correctly formed
            result = None

        return result

    def __remove_whitespace(self, expression):
        # This removes trailing new line as well (if expression has come from a file)
        return expression.rstrip().replace(" ", "")

    def __is_valid_expression(self, expression):
        # regex match method returns an object or none if the pattern does not match
        match = self.valid_expression.match(expression)
        if match:
            return True
        else:
            return False


if __name__ == "__main__":
    # Simple test code
    c = Calculator()

    assert c.calculate("1+1") == 2
    assert c.calculate("(3+4)*6") == 42
    assert c.calculate("(1*4)+(5*2)") == 14
    assert c.calculate("(1*4)+(5*2") == None
    assert c.calculate("a+b") == None
    assert c.calculate("") == None

    print("Tests passed OK")
