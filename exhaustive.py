import operator

FILENAME = 'data/mid_easy_test_genotypes.txt'


class Exhaustive(object):
    def __init__(self, fname):
        with open(fname) as f:
            self.data = f.read().split()
        self.n_indv = len(self.data)
        self.n_snp = len(self.data[0])

    def generate_haplotypes(self):
        lim = 2**self.n_snp
        N_str = '0' + str(self.n_snp) + 'b'
        hap_lst = {}
        for i in range(0,lim):
            hap_lst[format(i, N_str)] = 0
        return hap_lst

    def generate_empty_hap_pairing(self):
        return [['-1', '-1'] for i in range(self.n_indv)]

    def is_possible_match(self, hap, genotype, confirmed_hap_pair):
        # If we already have a pairing, return false
        if confirmed_hap_pair[0] != '-1' and confirmed_hap_pair[1] != '-1':
            return False

        for i in range(len(genotype)):
            if genotype[i] == '0' and hap[i] == '1':
                return False
            elif genotype[i] == '2' and hap[i] == '0':
                return False
            elif genotype[i] == '1' and confirmed_hap_pair[0] != '-1' and confirmed_hap_pair[0][i] == hap[i]:
                return False
        return True

    def getHapCount(self, hap_lst, confirmed_hap_pairs):
        for hap in hap_lst:
            for i,genotype in enumerate(self.data):
                if (self.is_possible_match(hap, genotype, confirmed_hap_pairs[i])):
                    hap_lst[hap] += 1

    def get_max_key(self, d):
        m = max(d.iteritems(), key=operator.itemgetter(1))[0]
        if d[m] > 0:
            return m
        else:
            return -1

    def update_confirmed_haps(self, confirmed_hap_pairs, hap):
        for i,genotype in enumerate(self.data):
            if (self.is_possible_match(hap, genotype, confirmed_hap_pairs[i])):
                if confirmed_hap_pairs[i][0] == '-1':
                    confirmed_hap_pairs[i][0] = hap
                else:
                    confirmed_hap_pairs[i][1] = hap

    def purge_hap_list(self, haps):
        to_remove = []
        for hap in haps:
            if haps[hap] == 0:
                to_remove.append(hap)
            else:
                haps[hap] = 0
        for hap in to_remove:
            haps.pop(hap, None)

    def required_hap(self, confirmed_haps):
        for genotype in self.data:
            if '1' not in genotype:
                hap = genotype.replace('2', '1')
                if hap not in confirmed_haps:
                    return hap
        return None

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

    def run(self):
        haps = self.generate_haplotypes()
        confirmed_hap_pairs = self.generate_empty_hap_pairing()
        confirmed_haps = []
        while(True):
            # req = self.required_hap(confirmed_haps)
            req = None
            self.getHapCount(haps, confirmed_hap_pairs)
            if req != None:
                best_hap = req
            else:
                best_hap = self.get_max_key(haps)
            if best_hap == -1:
                break
            self.update_confirmed_haps(confirmed_hap_pairs, best_hap)
            confirmed_haps.append(best_hap)
            haps.pop(best_hap, None)
            self.purge_hap_list(haps)
            if len(haps) == 0:
                break
        for i in range(len(confirmed_hap_pairs)):
            if confirmed_hap_pairs[i][1] == '-1':
                confirmed_hap_pairs[i][1] = confirmed_hap_pairs[i][0]
        return self.get_unique_haplotype_count(confirmed_hap_pairs, return_list=True), confirmed_hap_pairs



if __name__ == '__main__':
    hapP = Exhaustive(FILENAME)
    print hapP.run()
