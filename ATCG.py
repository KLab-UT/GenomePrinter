from Bio import SeqIO
import time

# Load the sequence from the FASTA file
with open("Example_5.fasta", "r") as fasta_file:
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequence = str(record.seq)

# Timer to stop after 30 minutes (30 minutes * 60 seconds)
end_time = time.time() + 30 * 60

# Loop through the sequence until the timer ends
index = 0
while time.time() < end_time:
    # Print each nucleotide continuously with a delay
    print(sequence[index], end="", flush=True)
    
    # Delay to slow down the printing
    time.sleep(0.3)  # Adjust the delay as needed (0.3 seconds here)
    
    # Move to the next nucleotide
    index += 1
    
    # Restart at the beginning if we reach the end of the sequence
    if index >= len(sequence):
        index = 0


