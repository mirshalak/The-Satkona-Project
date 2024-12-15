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

import hashlib
import json
import random

def generate_hexgate_address():
    """
    Generate a random Hexgate address.
    - First register is the type identifier for hexgates.
    - Remaining 12 registers are random 3-digit numbers.
    """
    type_identifier = "008"  # Hexgate type identifier
    registers = [f"{random.randint(0, 999):03d}" for _ in range(12)]
    address = [type_identifier] + registers
    return "-".join(address)

def hash_hexgate_address(hexgate_address):
    """
    Hash the Hexgate address using SHA-512.
    """
    return hashlib.sha512(hexgate_address.encode()).hexdigest()

def generate_checksum(file_path, hexgate_address=None, output_checksum_file=None):
    """
    Generate a checksum for a given file, incorporating the hashed Hexgate address.
    """
    # Generate a random Hexgate address if not provided
    if not hexgate_address:
        hexgate_address = generate_hexgate_address()
        print(f"Generated Hexgate Address: {hexgate_address}")

    # Hash the Hexgate address
    hashed_hexgate = hash_hexgate_address(hexgate_address)
    
    sha512 = hashlib.sha512()
    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(8192):  # Read file in chunks
                # Combine hashed Hexgate address with file data
                sha512.update(hashed_hexgate.encode() + chunk)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    
    checksum = sha512.hexdigest()

    # Save the checksum and hashed Hexgate address to a JSON file if specified
    if output_checksum_file:
        metadata = {
            "hashed_hexgate": hashed_hexgate,
            "checksum": checksum
        }
        with open(output_checksum_file, "w") as checksum_file:
            json.dump(metadata, checksum_file)
        print(f"Checksum and metadata saved to {output_checksum_file}")
    else:
        print(f"Checksum for {file_path}: {checksum}")
        print(f"Hashed Hexgate Address: {hashed_hexgate}")
    
    return checksum

def verify_checksum(file_path, hexgate_address, checksum_file):
    """
    Verify the checksum of a given file using the hashed Hexgate address from the metadata.
    """
    # Hash the provided Hexgate address
    hashed_hexgate = hash_hexgate_address(hexgate_address)
    
    try:
        # Load metadata from the checksum file
        with open(checksum_file, "r") as f:
            metadata = json.load(f)
        stored_hashed_hexgate = metadata["hashed_hexgate"]
        expected_checksum = metadata["checksum"]
    except FileNotFoundError:
        print(f"Error: Checksum file {checksum_file} not found.")
        return False
    except KeyError:
        print(f"Error: Invalid checksum file format.")
        return False

    # Check if the provided Hexgate address matches the stored hashed Hexgate address
    if hashed_hexgate != stored_hashed_hexgate:
        print("Error: Provided Hexgate address does not match the stored hash.")
        return False

    # Recompute the checksum using the provided Hexgate address
    sha512 = hashlib.sha512()
    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(8192):
                sha512.update(hashed_hexgate.encode() + chunk)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return False

    computed_checksum = sha512.hexdigest()
    if computed_checksum == expected_checksum:
        print(f"Checksum verification passed for {file_path}.")
        return True
    else:
        print(f"Checksum verification failed for {file_path}.")
        print(f"Expected: {expected_checksum}")
        print(f"Computed: {computed_checksum}")
        return False

# Example usage
if __name__ == "__main__":
    import argparse

    # Set up command-line arguments
    parser = argparse.ArgumentParser(description="Hexgate-integrated checksum generator and verifier with SHA-512.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Generate checksum command
    generate_parser = subparsers.add_parser("generate", help="Generate a checksum.")
    generate_parser.add_argument("--file", required=True, help="Path to the file.")
    generate_parser.add_argument("--hexgate", required=False, help="Hexgate address to use as salt.")
    generate_parser.add_argument("--output", required=False, help="Path to save the checksum file.")

    # Verify checksum command
    verify_parser = subparsers.add_parser("verify", help="Verify a checksum.")
    verify_parser.add_argument("--file", required=True, help="Path to the file.")
    verify_parser.add_argument("--hexgate", required=True, help="Hexgate address to verify.")
    verify_parser.add_argument("--checksum", required=True, help="Path to the checksum file.")

    # Parse arguments
    args = parser.parse_args()

    # Execute the appropriate command
    if args.command == "generate":
        generate_checksum(args.file, args.hexgate, args.output)
    elif args.command == "verify":
        verify_checksum(args.file, args.hexgate, args.checksum)
