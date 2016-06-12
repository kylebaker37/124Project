from sys import argv

from greedy import Greedy
from optimal import Optimal
from exhaustive import Exhaustive

from tester import Tester

def get_training_file_paths(difficulty):
	genotype = 'data/' + difficulty + '_training_genotypes.txt'
	haplotype = 'data/' + difficulty + '_training_haplotypes.txt'
	return genotype, haplotype

def run_training(difficulty, algorithm, output_name):
	genotype, haplotype = get_training_file_paths(difficulty)
	if algorithm == 'greedy':
		g = Greedy(genotype)
		t = Tester(g, haplotype, genotype, output_name)
		t.run_analysis()
	elif algorithm == 'optimal':
		o = Optimal(genotype)
		t = Tester(o, haplotype, genotype, output_name)
		t.run_analysis()
	elif algorithm == 'exhaustive':
		e = Exhaustive(genotype)
		t = Tester(e, haplotype, genotype, output_name)
		t.run_analysis()

def get_test_data_path(difficulty):
	genotype = 'data/' + difficulty + '_test_genotypes.txt'
	return genotype

def run_test(difficulty, algorithm, output_name):
	genotype = get_test_data_path(difficulty)
	if algorithm == 'greedy':
		g = Greedy(genotype)
		t = Tester(g, None, genotype, output_name)
		t.run_analysis()
	elif algorithm == 'optimal':
		o = Optimal(genotype)
		t = Tester(o, None, genotype, output_name)
		t.run_analysis()
	elif algorithm == 'exhaustive':
		e = Exhaustive(genotype)
		t = Tester(e, None, genotype, output_name)
		t.run_analysis()


def main():
	n = len(argv)
	i = 1
	difficulty = 'very_easy'
	test_data = False
	algorithm = 'greedy'
	output_name = False
	while i < n:
		if argv[i] == '-d':
			difficulty = argv[i+1]
		elif argv[i] == '-t':
			test_data = True
		elif argv[i] == '-a':
			algorithm = argv[i+1]
		elif argv[i] == '-o':
			output_name = argv[i+1]
		i += 1
	if not test_data:
		run_training(difficulty, algorithm, output_name)
	else:
		run_test(difficulty, algorithm, output_name)


if __name__ == '__main__':
	main()