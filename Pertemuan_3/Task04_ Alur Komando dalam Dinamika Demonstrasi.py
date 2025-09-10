import networkx as nx
import matplotlib.pyplot as plt

# 1. Definisikan Aktor (Simpul) dan Alur Komunikasi (Sisi)
nodes = [
    # Pemerintah
    "Mendagri", "Jubir Pemerintah",
    # Aparat Keamanan
    "Panglima TNI", "Dandim", "Kapolda", "Kapolres", "Pasukan PHH",
    # Mahasiswa
    "Korlap", "Jubir Mahasiswa", "Massa Mahasiswa",
    # Pihak Eksternal
    "Penyusup"
]

edges = [
    # Rantai komando Pemerintah ke Polisi
    ("Mendagri", "Kapolda"),
    ("Kapolda", "Kapolres"),
    ("Kapolres", "Pasukan PHH"),

    # Rantai komando TNI
    ("Panglima TNI", "Dandim"),

    # Koordinasi Aparat
    ("Kapolda", "Dandim"),

    # Alur Aksi Mahasiswa
    ("Korlap", "Massa Mahasiswa"),
    ("Jubir Mahasiswa", "Massa Mahasiswa"),

    # Interaksi dua arah (SCC)
    ("Kapolres", "Korlap"),
    ("Korlap", "Kapolres"),
    ("Jubir Mahasiswa", "Jubir Pemerintah"),
    ("Jubir Pemerintah", "Jubir Mahasiswa"),

    # Pengaruh Penyusup/Provokator
    ("Penyusup", "Massa Mahasiswa"),
]

# 2. Pastikan menggunakan DiGraph (Directed Graph)
G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

is_connected = nx.is_strongly_connected(G)
print("1. Analisis Keterhubungan Graf (Strongly Connected)")
if not is_connected:
    print("   -> Hasil: Graf ini TIDAK terhubung kuat (Not Strongly Connected).\n")
    print("   -> Bukti Jalur Terputus:")
    path_forward_exists = nx.has_path(G, "Mendagri", "Pasukan PHH")
    path_backward_exists = nx.has_path(G, "Pasukan PHH", "Mendagri")
    print(f"      - Apakah ada alur komando dari 'Mendagri' ke 'Pasukan PHH'? {path_forward_exists}")
    print(f"      - Apakah ada alur komando dari 'Pasukan PHH' kembali ke 'Mendagri'? {path_backward_exists}")
    print("   -> Ini membuktikan bahwa komunikasi tidak dapat mengalir kembali ke atas melalui seluruh rantai komando, sehingga graf tidak terhubung kuat.\n")
else:
    print("   Graf ini terhubung kuat.\n")

print("2. Komponen yang Terhubung Kuat (Strongly Connected Components - SCC)")
scc_groups = [scc for scc in nx.strongly_connected_components(G) if len(scc) > 1]
if scc_groups:
    print("   -> Ditemukan grup aktor dengan komunikasi dua arah (timbal balik):\n")
    for i, scc in enumerate(scc_groups):
        print(f"      - Grup {i+1}: {scc}")
    print("") 
else:
    print("   Tidak ditemukan grup dengan komunikasi dua arah.\n")

print("3. Makna Strongly Connected Components (SCC) dalam Skenario Ini")
print("   -> Sebuah SCC adalah sekelompok aktor di mana setiap aktor dapat berkomunikasi\n      dengan setiap aktor lain di dalam kelompok yang sama secara timbal balik.")
print("\n   -> Dalam konteks unjuk rasa ini, SCC merepresentasikan 'lingkaran komunikasi tertutup'\n      atau 'saluran negosiasi' di mana terjadi dialog dua arah:\n")
for scc in scc_groups:
    if "Korlap" in scc:
        print("      - Grup {'Korlap', 'Kapolres'}: Menandakan adanya jalur NEGOSIASI LANGSUNG\n        di lapangan antara perwakilan mahasiswa dan pimpinan aparat keamanan setempat.")
    if "Jubir Pemerintah" in scc:
        print("      - Grup {'Jubir Mahasiswa', 'Jubir Pemerintah'}: Menandakan adanya PERANG\n        PERNYATAAN atau DIALOG MEDIA antara juru bicara dari kedua belah pihak.")
print("\n   -> Aktor lain yang tidak masuk dalam SCC ini cenderung berada dalam alur\n      komunikasi satu arah (memberi atau menerima perintah/informasi).")

# --- Visualisasi Graf dengan Panah yang Jelas ---
fig, ax = plt.subplots(figsize=(20, 15))

# Menggunakan posisi manual 
pos = {
    "Mendagri": (0.9, 0.95), "Jubir Pemerintah": (0.9, 0.75),
    "Panglima TNI": (0.28, 1.01), "Dandim": (0.3, 0.82),
    "Kapolda": (0.7, 0.85), "Kapolres": (0.5, 0.65), "Pasukan PHH": (0.5, 0.35),
    "Jubir Mahasiswa": (0.1, 0.65), "Korlap": (0.3, 0.55),
    "Massa Mahasiswa": (0.1, 0.35), "Penyusup": (0.3, 0.20)
}

# Memberikan warna berbeda untuk setiap grup aktor
node_colors = []
for node in G.nodes():
    if node in ["Mendagri", "Jubir Pemerintah"]: node_colors.append("lightsalmon")
    elif node in ["Panglima TNI", "Dandim", "Kapolda", "Kapolres", "Pasukan PHH"]: node_colors.append("skyblue")
    elif node in ["Korlap", "Jubir Mahasiswa", "Massa Mahasiswa"]: node_colors.append("lightgreen")
    else: node_colors.append("gold")

# Opsi untuk node dan label
node_options = {"node_size": 1500, "node_color": node_colors}
label_options = {"font_size": 13, "font_weight": "bold"}

# Opsi untuk sisi (edge) dengan panah
edge_options = {
    "width": 2.5,
    "alpha": 0.8,
    "edge_color": "black",
    "arrowstyle": "-|>",
    "arrowsize": 30,
    "connectionstyle": 'arc3,rad=0.15'
}

# Gambar semua komponen graf
nx.draw_networkx_nodes(G, pos, ax=ax, **node_options)
nx.draw_networkx_labels(G, pos, ax=ax, **label_options)
nx.draw_networkx_edges(G, pos, ax=ax, **edge_options)

# Atur judul dan tampilkan
ax.set_title("Model Alur Komando dengan Arah Panah Jelas", size=16, weight='bold')
plt.axis('off')
plt.tight_layout()
plt.show()