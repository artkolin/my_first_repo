"""

"""

def hamming_metric(father, child):
    distance = 0
    for c in zip(child, father):
        if c[0] == c[1]:
            distance += 1

    return distance


if __name__ == '__main__':
    object_1 = input('1st candidate DNA: ')
    object_2 = input('2nd candidate DNA: ')
    child = input('Child\'s DNA: ')

    first_distance = hamming_metric(object_1, child)
    second_distance = hamming_metric(object_2, child)

    if first_distance > second_distance:
        print('Candidate 2 is a father')
    else:
        print('Candidate 1 is a father')

        """git test comment"""