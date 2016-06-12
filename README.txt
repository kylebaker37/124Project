This is all the code I created for my Haplotype Phasing: Minimum Parsimony Formulation project. The code in main.py parses command-line input and runs the code. tester.py contains a tester class that runs tests on the results and analyzes them to make sure they're correct. optimal.py, exhaustive.py, and greedy.py contain the optimal, exhaustive, and greedy algorithms. testfile.py was a script I used to create random haplotype data with a given amount of SNPs and individuals.

To run the code, type python main.py <options>

The options are as follows:
-t signifies you want to run a _test_genotypes.txt test file
	the absence of this flag means you want to run a _training_haplotypes.txt file with the code

-o <filename> means you want to output the unique haplotypes to a file designated as <filename>. It is required you include a filename

-a <algorithm> signifies the algorithm you want to run. By default, it'll run greedy. If you include the -a flag, you must include an algoritm name too valid algorithm names are as follows:
	greedy
	exhaustive
	optimal

-d <difficulty> signifies the difficulty you want to run. By default, it'll run with very_easy. If you include the -d flag, you must also include a difficulty.

Whatever difficulty you signify, the data file it will look for will be <difficulty>_test_genotypes.txt or <difficulty>_training_haplotypes.txt, depending on if you used the -t flag or not. As of now, the valid difficulties are as follows:
very_easy
easy
medium
hard

You can add more difficulties, you just have to include <difficulty>_test_genotypes.txt or <difficulty>_training_haplotypes.txt under the data directory.

Example of running the code:
python main.py -a greedy -d medium -o mexium_results.txt
	This will run the greedy algorithm with the data medium_training_haplotypes.txt and output the haplotypes to medium_results.txt
python main.py -a optimal -d very_easy -t
	This will run the optimal algorithm with the very_easy_test_genotypes.txt data. It will not output the haplotype data to a file, just to the console
