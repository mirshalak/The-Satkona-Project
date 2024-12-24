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

# Generate the 11 random numbers with hyphens
addresses_with_hyphen = [f"{random.randint(100, 999)}-" for _ in range(11)]

# Generate the final number without a hyphen
final_number = f"{random.randint(100, 999)}"

# Concatenate the numbers into the final string
random_hexgate_addresses = ''.join(addresses_with_hyphen) + final_number

print(random_hexgate_addresses)
