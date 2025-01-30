from Bio import SeqIO
import Bio as Bio 
from Bio import AlignIO
from Bio import Phylo
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
import numpy as np
from Bio.Align.Applications import ClustalwCommandline
from Bio.Phylo.TreeConstruction import _DistanceMatrix

fanta = "Mafft3.1.fasta"
sequences = list(SeqIO.parse(fanta, "fasta"))

for i in range(len(sequences)):
    for j in range(i + 1, len(sequences)):
        score = pairwise2.align.globalxx(sequences[i].seq, sequences[j].seq, score_only=True)
        print(f"Alignment between {sequences[i].id} and {sequences[j].id}:")

        max_length = max(len(sequences[i].seq), len(sequences[j].seq))
        print(f"Score : {score} / {max_length}")

