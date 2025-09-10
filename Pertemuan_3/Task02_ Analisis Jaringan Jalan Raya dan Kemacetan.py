import networkx as nx
import matplotlib.pyplot as plt
from Tutorial01 import visualize_graph

jalan = ["Jl. Sunda","Jl. Gatot Subroto", "Jl. Sunda–Karapitan",  "Jl. Asia Afrika", "Jl. Ahmad Yani."]
G_SimpangLima = nx.complete_graph(jalan)
pos = nx.spring_layout(G_SimpangLima, seed=42)

visualize_graph(G_SimpangLima, "Model persimpangan jalan Soekarno-Hatta (Simpang Lima).", pos)

H = G_SimpangLima.copy()
H.remove_edge(jalan[0], jalan[1])		#cut edges
H.remove_edge(jalan[2], jalan[1])		#cut edges
H.remove_edge(jalan[3], jalan[1])		#cut edges
path_edges = [(jalan[4], jalan[1]), (jalan[0], jalan[4]), (jalan[2], jalan[4]), (jalan[3], jalan[4])]
visualize_graph(H, "Model jalan Soekarno-Hatta dengan cut edges (3).", pos, highlight_edges=path_edges )


H = G_SimpangLima.copy()
H.remove_edges_from(list(H.edges(jalan[0])))		#cut vertex
visualize_graph(H, "Model jalan Soekarno-Hatta salah satu Cut Vertex dihapus.", pos)