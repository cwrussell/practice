from collections import defaultdict

from frequent_words import retrieve_sequence, frequent_words


def get_kmers_with_frequent_words(path, k):
    """ Using the FrequentWords approach """
    seq = retrieve_sequence(path)
    max_kmers = frequent_words(seq, k)
    return max_kmers


def get_kmers_with_dict(path, k):
    """ My approach: iterate once, tally counts for each kmer """
    seq = retrieve_sequence(path)

    # count the kmers
    kmer_ct = defaultdict(int)
    for i in range(len(seq) - k):
        kmer = seq[i:i+k]
        kmer_ct[kmer] += 1

    # find the kmers with the max count
    max_ct = max(kmer_ct.values())
    max_kmers = set()
    for kmer, ct in kmer_ct.items():
        if ct == max_ct:
            max_kmers.add(kmer)

    return max_kmers