from Bio import Phylo

tree = "Phylo_tree.xml"

phylo_tree = Phylo.read(tree, "phyloxml")

# แสดงชื่อเฉพาะโหนดปลาย (leaf nodes)
Phylo.draw(phylo_tree, label_func=lambda x: x.name if x.is_terminal() else None)