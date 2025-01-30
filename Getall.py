import Bio as Bio 
from Bio import SeqIO
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import Phylo

def parse_species_names(fan_file):
    return {record.id: record.description.split(":")[-1].strip() for record in SeqIO.parse(fan_file, "fasta")}

fan_file = "Mafft3.1.fasta"
aln_file = "Mafft3.1.fasta"
alignment = AlignIO.read("Mafft3.1.aln", "clustal")

# Open the distance calculator and create a distance matrix

calculator = DistanceCalculator('identity')
distance_matrix = calculator.get_distance(alignment)
# print(distance_matrix)

constructor = DistanceTreeConstructor(calculator, method=("upgma"))
tree = constructor.build_tree(alignment)
tree.rooted = True

tree = constructor.build_tree(alignment)
species_mapping = parse_species_names(fan_file)

for clade in tree.find_clades():
    if clade.name in species_mapping:
        clade.name = species_mapping[clade.name]

Phylo.draw_ascii(tree)

# gen xml file
Phylo.write(tree, "Phylo_tree.xml", "phyloxml")
print("Phylogenetic tree has saved")

with open("phylogenetic_tree.txt", "w") as file:
    Phylo.draw_ascii(tree, file=file)

