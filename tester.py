from time import time


class Tester(object):
    def __init__(self, algorithm, hap_training_file, gen_training_file, output_name):
        self.hap_training_data = None
        if hap_training_file != None:
            with open(hap_training_file) as f:
                self.hap_training_data = f.read().split()
        with open(gen_training_file) as f:
            self.gen_training_data = f.read().split()
        self.algorithm = algorithm
        self.output_name = output_name

    def test_valid_solution(self, pairs):
        print 'Testing if the acquired solution is valid...'
        N = 0
        for i,genome in enumerate(self.gen_training_data):
            for j,digit in enumerate(genome):
                if str( int(pairs[i][0][j]) + int(pairs[i][1][j]) ) != digit:
                    print 'Genome/Haplotype mismatch in individual %i' % i
                    print 'Genome:'
                    print genome
                    print 'Haplotype Pair'
                    print pairs[i][0]
                    print pairs[i][1]
                    N += 1
        print 'Total number of Genome/Haplotype mismatches: %i' % N
        print '===================================\n'

    def compare_haps(self, results):
        print 'Comparing analyzed results to training data...'
        print 'Haplotypes in analyzed minimum set: %i' % len(results)
        print 'Haplotypes in training data set: %i' % len(self.hap_training_data)

        print '===================================\n'

        print 'Haplotypes found not in training data:'
        N = 0
        for hap in results:
            if hap not in self.hap_training_data:
                N += 1
                print hap
        print 'Total: %i' % N

        print '===================================\n'

        print 'Haplotypes in training data but not analyzed data:'
        N = 0
        for hap in self.hap_training_data:
            if hap not in results:
                N += 1
                print hap
        print 'Total: %i' % N

    def print_results(self, results):
        print 'Resulting Haplotypes: '
        for result in results:
            print result
        print '===================================\n'

    def output_to_file(self, haps):
        with open(self.output_name, 'w') as f:
            for hap in haps:
                f.write(hap)
                f.write('\n')

    def run_analysis(self):
        t0 = time()
        results, pairs = self.algorithm.run()
        delta_t = time() - t0
        print '==================================='
        print 'Total execution time: %f' % delta_t
        print 'Number of unique haplotypes: %i' % len(results)
        print '===================================\n'
        self.test_valid_solution(pairs)
        if self.hap_training_data != None:
            self.compare_haps(results)
        else:
            self.print_results(results)
        if self.output_name != False:
            self.output_to_file(results)