from Bio import SeqIO
import sys
import time

infile = sys.argv[1]

with open(infile, "r") as infile:
    chunk_size = 100
    delay = 0.5
    for record in SeqIO.parse(infile, "fasta"):
        sequence = record.seq
        print(f"Sequence ID: {record.id}")
        for i in range(0, len(sequence), chunk_size):
            print(sequence[i:i+chunk_size])
            time.sleep(delay)
