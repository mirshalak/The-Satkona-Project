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

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <fcntl.h>
#include <unistd.h>

#define REGISTER_COUNT 12
#define REGISTER_MAX 999

void generate_random_address(char *output) {
    // Define the size of the seed to cover the 10^36 space
    uint64_t seed_high, seed_low;

    // Open /dev/urandom for cryptographically secure randomness
    int fd = open("/dev/urandom", O_RDONLY);
    if (fd < 0) {
        perror("Failed to open /dev/urandom");
        exit(EXIT_FAILURE);
    }

    // Read two 64-bit random values (for a 128-bit seed)
    if (read(fd, &seed_high, sizeof(seed_high)) < 0 ||
        read(fd, &seed_low, sizeof(seed_low)) < 0) {
        perror("Failed to read from /dev/urandom");
        close(fd);
        exit(EXIT_FAILURE);
    }
    close(fd);

    // Combine seed_high and seed_low into a single large number
    __uint128_t seed = ((__uint128_t)seed_high << 64) | seed_low;

    // Divide the large seed into 12 registers
    for (int i = 0; i < REGISTER_COUNT; i++) {
        // Extract a 3-digit number from the seed
        uint32_t value = (uint32_t)(seed % (REGISTER_MAX + 1));
        seed /= (REGISTER_MAX + 1); // Reduce seed for next register

        // Append to the output string
        if (i < REGISTER_COUNT - 1) {
            sprintf(output + i * 4, "%03d-", value); // Add a hyphen
        } else {
            sprintf(output + i * 4, "%03d", value);  // No hyphen for last
        }
    }
}

int main() {
    char address[50]; // Enough space for 12 registers (11 hyphens + null terminator)
    generate_random_address(address);
    printf("Random Hexgate Address: %s\n", address);
    return 0;
}
