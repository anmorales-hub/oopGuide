import math

class SquareRoot:

    # un-abstract square root application
    def squareRoot(base):
        return base ^ (1 / 2)

    #abstract square root app using math module
    def squareRootA(base):
        return math.sqrt(base)