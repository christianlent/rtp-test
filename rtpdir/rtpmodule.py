def raisetopower(root: int, exponent: int) -> int:
    if exponent == 1:
        return root
    return root * raisetopower(root, exponent - 1)
