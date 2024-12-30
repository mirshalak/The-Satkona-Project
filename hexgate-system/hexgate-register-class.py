class HexgateRegister:
    def __init__(self, value=0):
        if value < 0:
            raise ValueError("HexgateRegister cannot have negative values")
        self.value = value

    def __repr__(self):
        return f"{self.value:03d}"  # Ensures at least 3 digits

    def __add__(self, other):
        if isinstance(other, HexgateRegister):
            return HexgateRegister(self.value + other.value)
        elif isinstance(other, int):
            return HexgateRegister(self.value + other)
        else:
            raise TypeError("Unsupported type for addition")

    def __sub__(self, other):
        if isinstance(other, HexgateRegister):
            result = self.value - other.value
        elif isinstance(other, int):
            result = self.value - other
        else:
            raise TypeError("Unsupported type for subtraction")

        if result < 0:
            raise ValueError("HexgateRegister cannot have negative values")
        return HexgateRegister(result)

    def __mul__(self, other):
        if isinstance(other, HexgateRegister):
            return HexgateRegister(self.value * other.value)
        elif isinstance(other, int):
            return HexgateRegister(self.value * other)
        else:
            raise TypeError("Unsupported type for multiplication")

    def __floordiv__(self, other):
        if isinstance(other, HexgateRegister):
            return HexgateRegister(self.value // other.value)
        elif isinstance(other, int):
            return HexgateRegister(self.value // other)
        else:
            raise TypeError("Unsupported type for division")

    def __eq__(self, other):
        if isinstance(other, HexgateRegister):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return False
