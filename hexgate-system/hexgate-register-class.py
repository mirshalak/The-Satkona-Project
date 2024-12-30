# ISC License

# Copyright (c) 2024 James Osborn

# Permission to use, copy, modify, and/or distribute this software for any purpose 
# with or without fee is hereby granted, provided that the above copyright notice 
# and this permission notice appear in all copies.

# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH 
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY 
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, 
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM 
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE 
# OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR 
# PERFORMANCE OF THIS SOFTWARE.

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
