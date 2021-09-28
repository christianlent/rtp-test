def raisetopower(root: int, exponent: int) -> int:

    if exponent == 0:
        return 1

    return root * raisetopower(root, exponent - 1)
