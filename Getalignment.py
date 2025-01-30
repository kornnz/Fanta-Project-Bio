from Bio import SeqIO
from Bio.pairwise2 import format_alignment
from Bio.Align.Applications import ClustalwCommandline

fanta_file = "Mafft3.1.fasta" 
clustalw_exe = r"C:\Program Files (x86)\ClustalW2\clustalw2.exe"

species_ids = []

for record in SeqIO.parse(fanta_file, "fasta"):
    if ":" in record.description:
        species_id = record.id
        species_id = record.description.split(":")[-1].strip()
    else:
        species_id = record.description.strip()
    species_ids.append(species_id)

alignment_file = "Mafft3.1.aln"

try:
    clustalw_cline = ClustalwCommandline(clustalw_exe, infile=fanta_file)
    print("ClustalW command:", clustalw_cline)

    # Execute the command
    stdout, stderr = clustalw_cline()

    print("LET GOOOO !!!!  Alignment completed.")

except Exception as e:
    print("Error running ClustalW:", str(e))

