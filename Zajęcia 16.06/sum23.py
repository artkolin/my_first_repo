"""
Sum numbers, ignore 2 and 3 sequence
"""

def sum(numbers):
    num_seq = numbers
    sum_all = 0
    seq_flag = False
    for i in num_seq:
        num = int(i)
        if num == 2:
            seq_flag = True
        if not seq_flag:
            sum_all += num
        elif num == 3:
            seq_flag = False
    return sum_all


if __name__ == '__main__':
    input_seq = input('Provide numbers: ').strip().split(' ')
    print(input_seq)
    print(sum(input_seq))
