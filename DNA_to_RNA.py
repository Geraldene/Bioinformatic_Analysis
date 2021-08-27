import argparse
import os 
from typing import NamedTuple, List, TextIO

class Args(NamedTuple):
    files: List[TextIO]
    out_dir: str


def get_args():
    
    parser = argparse.ArgumentParser(
    description = 'Transcribe DNA to RNA',
    formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('file',
    help = 'Input DNA file',
    metavar='File',
    type=argparse.FileType('rt'),
    nargs='*')
	
    parser.add_argument('-o',
    '--out_dir',
    help ='Output directory',
    metavar = 'Dir',
    type = str,
    default = 'out')
	
    args = parser.parse_args()

    return Args(args.file, args.out_dir)


def main():
    
    args = get_args()


    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)


    num_files, num_seqs = 0, 0 
    for fh in args.files:
        num_files += 1
        out_file = os.path.join(args.out_dir, os.path.basename(fh.name))
        out_fh = open(out_file, 'wt')
        

        for dna in fh:
            num_seqs += 1
            out_fh.write(dna.replace('T', 'U'))
        out_fh.close()

    print(f'Done, wrote{num_seqs} sequence {"" if num_seqs == 1 else "s"}')


if __name__ == '__main__':
    main()


