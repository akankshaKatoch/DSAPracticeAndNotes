{
  "Set Bit": {
    "prefix": "bit-set",
    "body": ["n |= (1 << ${1:k})"],
    "description": "Set bit at position k"
  },
  "Clear Bit": {
    "prefix": "bit-clear",
    "body": ["n &= ~(1 << ${1:k})"],
    "description": "Clear bit at position k"
  },
  "Toggle Bit": {
    "prefix": "bit-toggle",
    "body": ["n ^= (1 << ${1:k})"],
    "description": "Toggle bit at position k"
  },
  "Check Bit": {
    "prefix": "bit-check",
    "body": ["(n >> ${1:k}) & 1"],
    "description": "Check if bit at position k is 1"
  },
  "Turn Off Rightmost Set Bit": {
    "prefix": "bit-rightoff",
    "body": ["n &= (n - 1)"],
    "description": "Turn off rightmost set bit"
  },
  "Isolate Rightmost Set Bit": {
    "prefix": "bit-rightonly",
    "body": ["n & -n"],
    "description": "Isolate rightmost set bit"
  },
  "Power of Two Check": {
    "prefix": "bit-power2",
    "body": ["n > 0 and (n & (n - 1)) == 0"],
    "description": "Check if n is power of 2"
  },
  "Count Set Bits": {
    "prefix": "bit-count",
    "body": [
      "count = 0",
      "while n:",
      "    n &= (n - 1)",
      "    count += 1"
    ],
    "description": "Count number of set bits in n"
  },
  "XOR All Elements": {
    "prefix": "bit-xor-all",
    "body": [
      "res = 0",
      "for x in arr:",
      "    res ^= x"
    ],
    "description": "Find single number using XOR"
  },
  "Swap Two Numbers": {
    "prefix": "bit-swap",
    "body": [
      "a ^= b",
      "b ^= a",
      "a ^= b"
    ],
    "description": "Swap a and b using XOR"
  },
  "Opposite Signs": {
    "prefix": "bit-opp-sign",
    "body": ["(a ^ b) < 0"],
    "description": "Check if a and b have opposite signs"
  }
}
