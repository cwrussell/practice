import argparse
import sys


def retrieve_sequence(fasta):
    seq_ct = 0
    seq = ""
    for line in open(fasta):
        ls = line.strip()
        if ls.startswith(">"):
            seq_ct += 1
            if seq_ct > 1: break
        else:
            seq += ls
    return seq.upper()


def pattern_count(seq, pattern):
    ct = 0
    k = len(pattern)
    for i in range(len(seq) - k):
        kmer = seq[i:i+k]
        if kmer == pattern:
            ct += 1
    return ct


def frequent_words(seq, k):

    # for each kmer in the sequence, count the number of times it is found in the sequence
    positional_count = []
    for i in range(len(seq) - k):
        kmer = seq[i:i+k]
        count = pattern_count(seq, kmer)
        positional_count.append(count)

    # find the kmer(s) with the highest number of counts
    max_kmers = set()
    max_count = max(positional_count)
    for i, ct in enumerate(positional_count):
        if ct == max_count:
            kmer = seq[i:i+k]
            max_kmers.add(kmer)

    return max_kmers


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the kmer(s) with the highest count in a sequence")
    parser.add_argument("-f", "--fasta", required=True, metavar="<path>", help="Path to fasta file containing sequence of interest")
    parser.add_argument("-k", "--kmer_size", required=True, type=int, metavar="<int>", help="kmer size")
    args = parser.parse_args()

    seq = retrieve_sequence(args.fasta)
    max_kmers = frequent_words(seq, args.kmer_size)
    for mk in max_kmers:
        sys.stdout.write("{}\n".format(mk))
    sys.stdout.flush()