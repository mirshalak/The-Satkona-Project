# Hexgate SHA-256 Input generation script.
#
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

import random
import os
import hashlib

def generate_hexgate_address():

# First register is always the type identifier for hexgates
    type_identifier = "008"

    # Generates a random Hexgate address.
    
    # Generate random values for all 12 registers
    registers = [f"{random.randint(0, 999):03d}" for _ in range(12)]
    
    # Combine into the final address
    address = [type_identifier] + registers
    return "-".join(address)

def generate_salt():
    # Generates a random 47 byte cryptographic salt.  This length is used because
    # 47 bytes is the complete length of a hexgate address, with hyphens. 
    
    return os.urandom(47)

def hash_with_salt(hexgate_address, salt):
    """
    Hashes a Hexgate address with a given salt using SHA-256.
    """
    # Combine the salt and Hexgate address into a single input
    hash_input = salt + hexgate_address.encode()
    # Generate the SHA-256 hash
    hashed_output = hashlib.sha256(hash_input).hexdigest()
    return hashed_output

def main():
    """
    Main function to generate a Hexgate address, salt it, and hash it.
    """
    # Generate a random Hexgate address
    hexgate_address = generate_hexgate_address()
    print(f"Generated Hexgate Address: {hexgate_address}")
    
    # Generate a random salt
    salt = generate_salt()
    print(f"Generated Salt (hex): {salt.hex()}")
    
    # Hash the address with the salt
    hashed_address = hash_with_salt(hexgate_address, salt)
    print(f"Hashed Address (SHA-256): {hashed_address}")

if __name__ == "__main__":
    main()
