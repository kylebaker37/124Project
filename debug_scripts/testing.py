import time


def prepend(lst, element):
    for i in range(len(lst)):
        lst[i] = element + lst[i]
    return lst

def genotype_to_haplotypes(genotype):
    if len(genotype) == 0:
        return ['']

    lst = genotype_to_haplotypes(genotype[1:])
    if genotype[0] == '1':
        one = prepend(lst[:], '1')
        zero = prepend(lst[:], '0')
        return one + list(set(zero) - set(one))
    elif genotype[0] == '0':
        return prepend(lst, '0')
    else:
        return prepend(lst, '1')

# O(2^M * N)
def get_bin(genotype):
    lst = []
    i = 0
    n_ones = genotype.count('1') # O(N)
    format_str = '0' + str(n_ones) + 'b'    # O(N)
    while True:                             # O(2^M * N)
        s = format(i, format_str)
        if (len(s) != n_ones):
            break
        lst.append(s)
        i += 1
    return lst

# O(N^2)
def get_parsers(genotype):
    string = ''
    parse_lst = []
    for c in genotype:
        if c == '1':
            parse_lst.append(string)
            string = ''
        elif c == '0':
            string += '0'
        else:
            string += '1'
    parse_lst.append(string)
    return parse_lst


def generate_potential_haps(genotype):
    bin_lst = get_bin(genotype)
    parser_lst = get_parsers(genotype)
    N1 = len(bin_lst)
    N2 = len(parser_lst) - 1
    for i in range(N1):
        string = ''
        for j in range(N2):
            string += parser_lst[j] + bin_lst[i][j]
        string += parser_lst[j+1]
        bin_lst[i] = string
    return bin_lst


# def generate_haplotypes():
#     n_snp = 3
#     lim = 2**n_snp
#     N_str = '0' + str(n_snp) + 'b'
#     hap_lst = []
#     for i in range(0,lim):
#         hap_lst.append(format(i, N_str))
#     return hap_lst

SSS = '2010120101201012010120101201012010120101'
t0 = time.time()
generate_potential_haps(SSS)
t1 = time.time()
genotype_to_haplotypes(SSS)
t2 = time.time()

print t1-t0
print t2-t1