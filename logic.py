def decimal_to_binary(num, num_bits):
    return format(int(num), f'0{num_bits}b')

def group_minterms(minterms, num_bits):
    groups = {}
    for minterm in minterms:
        num_ones = bin(minterm).count('1')
        if num_ones not in groups:
            groups[num_ones] = []
        groups[num_ones].append(minterm)
    return groups

def combine_terms(term1, term2, num_bits):
    if isinstance(term1, int):
        term1_bin = decimal_to_binary(term1, num_bits)
    else:
        term1_bin = term1

    if isinstance(term2, int):
        term2_bin = decimal_to_binary(term2, num_bits)
    else:
        term2_bin = term2

    combined = ""
    difference_count = 0

    for bit1, bit2 in zip(term1_bin, term2_bin):
        if bit1 == bit2:
            combined += bit1
        else:
            combined += "-"
            difference_count += 1

    if difference_count == 1:
        return combined
    return None

def find_prime_implicants(minterms, dont_care, num_bits):
    all_terms = minterms + dont_care
    groups = group_minterms(all_terms, num_bits)
    used = set()
    prime_implicants = set()

    while groups:
        next_groups = {}
        combined_terms = set()

        for i in sorted(groups.keys()):
            if i + 1 not in groups:
                continue
            for term1 in groups[i]:
                for term2 in groups[i + 1]:
                    combined = combine_terms(term1, term2, num_bits)
                    if combined:
                        used.add(term1)
                        used.add(term2)
                        if combined not in combined_terms:
                            combined_terms.add(combined)
                            count = combined.count('1')  # Count '1's for proper grouping
                            next_groups.setdefault(count, []).append(combined)

        prime_implicants.update(set(groups.get(i, [])) - used)
        groups = next_groups

    return list(prime_implicants)

def main():
    minterms = [0, 1, 2,5,6, 7,8,9,10,14]
    dont_care = [4, 15]
    num_bits = 4

    print("Minterms:", minterms)
    print("Don't Care Terms:", dont_care)

    prime_implicants = find_prime_implicants(minterms, dont_care, num_bits)
    print("Prime Implicants:", prime_implicants)

if __name__ == "__main__":
    main()
