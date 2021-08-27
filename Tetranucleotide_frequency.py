import argparse
from typing import NamedTuple
import os 

class Args(NamedTuple):
	dna: str 

def get_args():
	parser = argparse.ArgumentParser(
	description='Tetranucleotide frequency', 
	formatter_class = argparse.ArgumentDefaultsHelpFormatter)

	parser.add_argument('dna', metavar='DNA', help='Input DNA sequence')


	args = parser.parse_args()


	if os.path.isfile(args.dna):
		args.dna = open(args.dna).read().rstrip().upper()

	return Args(args.dna.upper())


def main():
	args = get_args()
	count_a, count_t, count_c, count_g = 0, 0, 0, 0 

	for base in args.dna:
		if base == 'A':
			count_a += 1
		elif base == 'C':
			count_c += 1
		elif base == 'G':
			count_g += 1
		elif base == 'T':
			count_t += 1
	print(count_a, count_c, count_g, count_t)


if __name__ == '__main__':
	main()
