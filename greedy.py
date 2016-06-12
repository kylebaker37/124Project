import operator

FILENAME = 'data/hard_training_genotypes.txt'


class Greedy(object):
    def __init__(self, fname):
        with open(fname) as f:
            self.data = f.read().split()
        self.n_indv = len(self.data)
        self.n_snp = len(self.data[0])
        self.initialize_hap_pairs()
        self.chosen_haps = []
        self.potential_haps = []
        self.n_haps = 0

    def initialize_hap_pairs(self):
        self.hap_pairs = [[None, None] for genotype in self.data]


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

    def required_haps(self):
        for i,genotype in enumerate(self.data):
            if '1' not in genotype:
                to_enter = genotype.replace('2', '1')
                self.hap_pairs[i][0] = to_enter
                self.hap_pairs[i][1] = to_enter
                if to_enter not in self.chosen_haps:
                    self.chosen_haps.append(to_enter)
                    self.n_haps += 2

    def can_chosen_haps_explain(self):
        new_haps = []
        N = self.n_haps
        for i,genotype in enumerate(self.data):
            for hap in self.chosen_haps:
                if self.explains(hap, genotype, self.hap_pairs[i]):
                    pair = self.get_hap_pair(hap, genotype)
                    if pair in self.chosen_haps:
                        self.hap_pairs[i][0] = hap
                        self.hap_pairs[i][1] = pair
                        self.n_haps += 2
        if self.n_haps > N:
            return True
        return False

    def can_cross_choose(self):
        new_haps = []
        for i,genotype in enumerate(self.data):
            for hap in self.chosen_haps:
                if self.explains(hap, genotype, self.hap_pairs[i]):
                    pair = self.get_hap_pair(hap, genotype)
                    self.hap_pairs[i][0] = hap
                    self.hap_pairs[i][1] = pair
                    if pair not in new_haps:
                        new_haps.append(pair)
        for hap in new_haps:
            if hap not in self.chosen_haps:
                self.chosen_haps.append(hap)
                self.n_haps += 2
        if new_haps:
            return True
        return False

    def prepend(self, lst, element):
        for i in range(len(lst)):
            lst[i] = element + lst[i]
        return lst

    def pick_haplotype_pair(self, genotype):
        hap = ''
        pair = ''
        for digit in genotype:
            if digit == '0':
                pair += '0'
                hap += '0'
            elif digit == '2':
                pair += '1'
                hap += '1'
            else:
                pair += '0'
                hap += '1'
        return (hap, pair)

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

    def get_max_key(self, d):
        m = max(d.iteritems(), key=operator.itemgetter(1))[0]
        if d[m] > 0:
            return m
        else:
            return -1

    def generate_candidate_haplotypes(self, pairs):
        candidate_haps = {}
        for i,genotype in enumerate(self.data):
            if pairs[i][0] != None:
                continue
            else:
                potential_hap_list = self.genotype_to_haplotypes(genotype)
                for hap in potential_hap_list:
                    if hap not in candidate_haps:
                        candidate_haps[hap] = 1
                    else:
                        candidate_haps[hap] += 1
        m = self.get_max_key(candidate_haps)
        return m

    def choose_new_pairing(self):
        hap = self.generate_candidate_haplotypes(self.hap_pairs)
        for i,genotype in enumerate(self.data):
            # print genotype
            # print self.hap_pairs[i]
            if self.explains(hap, genotype, self.hap_pairs[i]):
                p = self.get_hap_pair(hap, genotype)
                self.hap_pairs[i][0] = hap
                self.hap_pairs[i][1] = p
                self.chosen_haps.append(hap)
                self.chosen_haps.append(p)
                break

    def is_pairs_full(self):
        for i in range(len(self.hap_pairs)):
            if self.hap_pairs[i][0] == None or self.hap_pairs[i][1] == None:
                return False
        return True

    def run(self):
        self.required_haps()
        while not self.is_pairs_full():
            if self.can_chosen_haps_explain():
                continue
            elif self.can_cross_choose():
                continue
            else:
                self.choose_new_pairing()
                continue
        return self.chosen_haps, self.hap_pairs





if __name__ == '__main__':
    hapP = Greedy(FILENAME)
    print hapP.run()
