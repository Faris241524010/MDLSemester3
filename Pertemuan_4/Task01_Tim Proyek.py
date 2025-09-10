import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk memvisualisasikan graf
def visualize_graph(G, title, pos=None, highlight_edges=None, highlight_nodes=None):
    plt.figure(figsize=(8, 6))
    if pos is None:
        if isinstance(G, nx.DiGraph):
            pos = nx.spring_layout(G, seed=42)
        else:
            pos = nx.spring_layout(G, seed=42)
            
    # Menggambar semua simpul
    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=700)
    
    # Menggambar semua sisi
    nx.draw_networkx_edges(G, pos, edge_color='gray')

    # Menggambar simpul yang di-highlight
    if highlight_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=highlight_nodes, node_color='red', node_size=700)

    # Menggambar sisi yang di-highlight
    if highlight_edges:
        nx.draw_networkx_edges(G, pos, edgelist=highlight_edges, edge_color='red', width=2)
        
    # Menggambar label
    nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")
    
    plt.title(title)
    plt.axis('off')
    plt.show()

def display_representations(graph, title):
    print(f"\n--- Representasi untuk {title} ---")
    
    # 1. Adjacency List
    adj_list = nx.to_dict_of_lists(graph)
    print("\nAdjacency List:")
    print(adj_list)
    
    # 2. Adjacency Matrix
    # Pastikan nodelist terurut untuk representasi matriks yang konsisten
    nodelist = sorted(list(graph.nodes()))
    adj_matrix = nx.to_numpy_array(graph, nodelist=nodelist)
    print("\nAdjacency Matrix:")
    print(adj_matrix)

if __name__ == "__main__":
    v1 = ["A","B", "C",  "D", "E"] #Developer
    v2 = ["T1", "T2", "T3", "T4", "T5"] #Tugas
    skill = [
        (v1[0], v2[0]), (v1[0], v2[1]), # A bisa mengerjakan T1 dan T2
        (v1[1], v2[1]), (v1[1], v2[2]), # B bisa mengerjakan T2 dan T3
        (v1[2], v2[2]), (v1[2], v2[3]), # C bisa mengerjakan T3 dan T4
        (v1[3], v2[3]), (v1[3], v2[4]), # D bisa mengerjakan T4 dan T5
        (v1[4], v2[4]), (v1[4], v2[0])  # E bisa mengerjakan T5 dan T1
    ]
    G1 = nx.Graph()
    G1.add_edges_from(skill)
    #G.add_nodes_from(v1)
    #G.add_nodes_from(v2)
    
    display_representations(G1, "Model tim proyek 5 developer")
    pos1 = nx.spring_layout(G1, seed=42)
    visualize_graph(G1, "Model tim proyek 5 developer", pos1)

    G_cut_E = G1.copy()
    G_cut_E.remove_node('E')
    
    print("\nSoal 1:")

    print(f"Apakah graf terhubung? {nx.is_connected(G1)}")
    print(f"Cut Vertices (Titik Potong): {list(nx.articulation_points(G1))}")
    print(f"Cut Edges (Sisi Potong): {list(nx.bridges(G1))}")
    
    visualize_graph(G_cut_E, "Graf setelah memecat salah satu (developer 'E')")
