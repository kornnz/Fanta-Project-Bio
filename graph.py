from Bio import Phylo

tree = "Phylo_tree.xml"

phylo_tree = Phylo.read(tree, "phyloxml")

Phylo.draw(phylo_tree)