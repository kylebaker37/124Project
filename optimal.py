class Optimal(object):
    def __init__(self, fname):
        with open(fname) as f:
            self.data = f.read().split()
        self.n_indv = len(self.data)
        self.n_snp = len(self.data[0])

    def get_required_pairs(self):
        pairs = [[None, None] for i in range(self.n_indv)]
        for i,genotype in enumerate(self.data):
            if '1' not in genotype:
                hap = genotype.replace('2', '1')
                pairs[i][0] = hap
                pairs[i][1] = hap
        return pairs

    def prepend(self, lst, element):
        for i in range(len(lst)):
            lst[i] = element + lst[i]
        return lst

    def genotype_to_haplotypes(self, genotype):
        if len(genotype) == 0:
            return ['']

        lst = self.genotype_to_haplotypes(genotype[1:])
        if genotype[0] == '1':
            one = self.prepend(lst[:], '1')
            zero = self.prepend(lst[:], '0')
            return one + list(set(zero) - set(one))
        elif genotype[0] == '0':
            return self.prepend(lst, '0')
        else:
            return self.prepend(lst, '1')

    def generate_candidate_haplotypes(self, pairs):
        candidate_haps = []
        for i,genotype in enumerate(self.data):
            if pairs[i][0] != None:
                continue
            else:
                potential_hap_list = self.genotype_to_haplotypes(genotype)
                for hap in potential_hap_list:
                    if hap not in candidate_haps:
                        candidate_haps.append(hap)
        return candidate_haps

    def get_unique_haplotype_count(self, pairs, return_list=False):
        unique_haps = []
        for i in range(len(pairs)):
            if pairs[i][0] not in unique_haps:
                unique_haps.append(pairs[i][0])
            if pairs[i][1] not in unique_haps:
                unique_haps.append(pairs[i][1])
        if return_list:
            return unique_haps
        return len(unique_haps)

    def is_pairs_full(self, pairs):
        for i in range(len(pairs)):
            if pairs[i][0] == None or pairs[i][1] == None:
                return False
        return True

    def explains(self, hap, genotype, hap_pair):
        # If we already have a pairing, return false
        if hap_pair[0] != None:
            return False
        for i in range(len(genotype)):
            if genotype[i] == '0' and hap[i] == '1':
                return False
            elif genotype[i] == '2' and hap[i] == '0':
                return False
            elif genotype[i] == '1' and hap_pair[0] != None and hap_pair[0][i] == hap[i]:
                return False
        return True

    # Assuming hap explains genotype
    def get_hap_pair(self, hap, genotype):
        pair = ''
        for i in range(len(hap)):
            if genotype[i] == '0':
                pair += '0'
            elif genotype[i] == '2':
                pair += '1'
            elif genotype[i] == '1' and hap[i] == '1':
                pair += '0'
            else:
                pair += '1'
        return pair

    def choose_hap(self, hap, pairs):
        for i,genotype in enumerate(self.data):
            if self.explains(hap, genotype, pairs[i]):
                pair = self.get_hap_pair(hap, genotype)
                pairs[i][0] = hap
                pairs[i][1] = pair
        return pairs

    def calc_optimal(self, pairs):
        if self.is_pairs_full(pairs):
            n = self.get_unique_haplotype_count(pairs)
            return (pairs, n)

        best_pairing = (None, None)
        candidate_haps = self.generate_candidate_haplotypes(pairs)
        for hap in candidate_haps:
            candidate_pairs = self.choose_hap(hap, pairs[:])
            potential_pairing = self.calc_optimal(candidate_pairs)
            if best_pairing[1] == None or potential_pairing[1] < best_pairing[1]:
                best_pairing = potential_pairing
        return best_pairing

    def run(self):
        pairs = self.get_required_pairs()
        optimal = self.calc_optimal(pairs)
        chosen_haps = self.get_unique_haplotype_count(pairs, return_list=True)
        return chosen_haps, optimal[0]



if __name__ == '__main__':
    o = Optimal('data/mid_easy_genotypes.txt')
    o.run()