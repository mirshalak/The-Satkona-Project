# Hexgate SHA-256 Input generation script.
#
# Copyright 2024 James Osborn.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
