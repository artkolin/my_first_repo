def hamming_metric(father, child):
    distance = 0
    for c in zip(child, father):
        cn, fn = c
        if cn != fn:
            distance += 1

    return distance

FIRST_MSG = 'First candidate is a father'
SEC_MSG = 'Second candidate is a father'
ERROR_MSG = 'Error - someone is cheating'

def dna_check_results(first, second, child):
    first_distance = hamming_metric(first, child)
    second_distance = hamming_metric(second, child)
    if first_distance < second_distance:
        return FIRST_MSG
    elif first_distance == second_distance:
        return SEC_MSG
    else:
        return ERROR_MSG

if __name__ == "__main__":
    first_dna = input("1st candidate DNA: ")
    second_dna = input("2nd candidate DNA: ")
    child_dna = input('child\'s  DNA: ')
    print(dna_check_results(first_dna, second_dna, child_dna))