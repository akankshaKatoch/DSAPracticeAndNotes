The Rabin Karp Algorithm is a string search algorithm that uses hashing to efficienty find patterns in text. 
It's particularly useful for:
1.) Finding multiple patterns in a text.
2.) Plagiarism detection (comparing document fingerprints)
3.) Bioinformatics (DNA sequence matching)

How rabin Karp works:
1st step: Compute the Hash value 
1.) We compute/calculate the hash vaue for the pattern. 
2.) Compute rolling hash for each substring in the text of the same length as the pattern/ 

2nd Step: Compare hashes
1.) if the hash of the substring matches the pattern's hash, perform a ful string comprison( to handle collisions).

3rd step: Rolling hash optimization
1.) Instead of recaculating the hash from the scratch for each substring, update it in constant time using the previous hash. 


Python Implementation:
def rabin_karp(text, pattern):
    d = 256  # Alphabet size (ASCII)
    q = 101  # Prime number
    m = len(pattern)
    n = len(text)
    h = pow(d, m-1, q)  # Precompute d^(m-1) mod q
    p_hash = 0  # Hash for pattern
    t_hash = 0  # Hash for current text window

    # Compute initial hashes
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    # Slide the pattern over the text
    for i in range(n - m + 1):
        if p_hash == t_hash:
            # Verify match (to handle collisions)
            if text[i:i+m] == pattern:
                return i  # Match found at index i

        # Update rolling hash
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            t_hash = (t_hash + q) % q  # Ensure positive

    return -1  # No match found


Wiki link: https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm

