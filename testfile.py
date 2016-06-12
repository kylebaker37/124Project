from sys import argv
from random import random

if __name__ == '__main__':
	difficulty = argv[1]
	n_snps = int(argv[2])
	n_indv = int(argv[3])
	rate = float(argv[4])

	p_0 = 35
	p_2 = 35
	p_1 = 30

	name = 'data/' + difficulty + '_test_genotypes.txt'

	no_ones = False
	with open(name, 'w') as f:
		for i in range(n_indv):
			r = random() * 100
			if r <= rate:
				no_ones = True
			for j in range(n_snps):
				r2 = random() * 100
				if no_ones:
					if r2 < 50:
						f.write('2')
					else:
						f.write('0')
				else:
					if r2 < p_0:
						f.write('0')
					elif r2 < p_0 + p_2:
						f.write('2')
					else:
						f.write('1')
			no_ones = False
			f.write('\n')

