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
    komando = ["D","M", "Ta", "Tb"] #Developer
    alur = [
        (komando[0], komando[1]), # Direktur (D) dapat memberi perintah ke Manajer (M).
        (komando[1], komando[2]), (komando[1], komando[3]), # Manajer ke tim A (TA) dan tim B (TB).
        (komando[2], komando[3]), (komando[3], komando[2]), # Tim A dapat berkoordinasi dengan tim B (Kedua tim dapat saling bertukar informasi).
        (komando[3], komando[1]) #Laporan dari tim B kembali ke Manajer.
    ]
    G1 = nx.DiGraph()
    G1.add_edges_from(alur)
    
    display_representations(G1, "Model alur komando organisasi.")
    pos1 = nx.spring_layout(G1, seed=42)

    #Keterhubungan Graf Berarah
    print("\nSoal 2:")
    print(f"Apakah graf terhubung kuat? {nx.is_strongly_connected(G1)}")
    print(f"Apakah graf terhubung lemah? {nx.is_weakly_connected(G1)}")
    # Menemukan komponen yang terhubung kuat dan terhubung lemah
    strong_components = list(nx.strongly_connected_components(G1))
    print(f"Komponen yang terhubung kuat: {strong_components}")
    
    visualize_graph(G1, "Model alur komando organisasi.", pos1)
    
    
    


