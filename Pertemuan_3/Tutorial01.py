import networkx as nx
import matplotlib.pyplot as plt

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

if __name__ == "__main__":
    # --- Materi: Path dan Circuit ---
    print("--- Materi: Path dan Circuit ---")
    # Contoh graf sederhana
    G_path = nx.Graph()
    G_path.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'a'), ('b', 'd')])
    visualize_graph(G_path, "Contoh Graf dengan Path dan Circuit")

    # Path dari a ke e: a-b-c-d-e
    path_nodes = ['a', 'b', 'c', 'd', 'e']
    path_edges = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')]
    print("Path dari a ke e: a -> b -> c -> d -> e")
    visualize_graph(G_path, "Visualisasi Path", highlight_edges=path_edges)

    # Circuit: a-b-d-c-a
    circuit_nodes = ['a', 'b', 'd', 'c', 'a']
    circuit_edges = [('a', 'b'), ('b', 'd'), ('d', 'c'), ('c', 'a')]
    print("\nCircuit: a -> b -> d -> c -> a")
    visualize_graph(G_path, "Visualisasi Circuit", highlight_edges=circuit_edges)


    print("\n--- Materi: Keterhubungan Graf Tak Berarah ---")
    # Contoh graf terhubung dan tidak terhubung
    G_connected = nx.Graph()
    G_connected.add_edges_from([('1', '2'), ('2', '3'), ('3', '4'), ('4', '1'), ('1', '3')])
    visualize_graph(G_connected, "Graf Terhubung")
    print(f"Apakah graf terhubung? {nx.is_connected(G_connected)}")

    G_disconnected = nx.Graph()
    G_disconnected.add_edges_from([('1', '2'), ('3', '4'), ('5', '6')])
    visualize_graph(G_disconnected, "Graf Tidak Terhubung")
    print(f"Apakah graf terhubung? {nx.is_connected(G_disconnected)}")
    print(f"Jumlah komponen terhubung: {nx.number_connected_components(G_disconnected)}")

    # Contoh Cut Vertex dan Cut Edge
    G_cut = nx.Graph()
    G_cut.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'g'), ('g', 'd')])
    visualize_graph(G_cut, "Contoh Cut Vertex dan Cut Edge")

    # Menemukan cut vertices
    cut_vertices = list(nx.articulation_points(G_cut))
    print(f"Cut Vertices (Titik Potong): {cut_vertices}")
    # Visualisasi dengan menghapus cut vertex 'd'
    G_cut_d = G_cut.copy()
    G_cut_d.remove_node('d')
    visualize_graph(G_cut_d, "Graf setelah menghapus Cut Vertex 'd'")

    # Menemukan cut edges
    cut_edges = list(nx.bridges(G_cut))
    print(f"Cut Edges (Sisi Potong): {cut_edges}")
    # Visualisasi dengan menghapus cut edge ('a', 'b')
    G_cut_ab = G_cut.copy()
    G_cut_ab.remove_edge('a', 'b')
    visualize_graph(G_cut_ab, "Graf setelah menghapus Cut Edge ('a', 'b')")

    print("\n--- Latihan Praktikum Minggu 3 ---")

    # Latihan 1: Analisis Keterhubungan Graf Tak Berarah
    G_latihan_1 = nx.Graph()
    G_latihan_1.add_edges_from([('1', '2'), ('1', '3'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('4', '6')])
    visualize_graph(G_latihan_1, "Latihan 1: Analisis Keterhubungan")
    print("\nLatihan 1:")
    print(f"Apakah graf terhubung? {nx.is_connected(G_latihan_1)}")
    print(f"Cut Vertices (Titik Potong): {list(nx.articulation_points(G_latihan_1))}")
    print(f"Cut Edges (Sisi Potong): {list(nx.bridges(G_latihan_1))}")

    # Latihan 2: Keterhubungan Graf Berarah
    G_latihan_2 = nx.DiGraph()
    G_latihan_2.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'a'), ('a', 'd')])
    visualize_graph(G_latihan_2, "Latihan 2: Keterhubungan Graf Berarah")
    print("\nLatihan 2:")
    print(f"Apakah graf terhubung kuat? {nx.is_strongly_connected(G_latihan_2)}")
    print(f"Apakah graf terhubung lemah? {nx.is_weakly_connected(G_latihan_2)}")
    # Menemukan komponen yang terhubung kuat
    strong_components = list(nx.strongly_connected_components(G_latihan_2))
    print(f"Strongly Connected Components: {strong_components}")
