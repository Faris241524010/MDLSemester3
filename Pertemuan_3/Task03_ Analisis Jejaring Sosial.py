import networkx as nx
import matplotlib.pyplot as plt

# Fungsi analisis komponen
def analyze_components(G, stage):
    print(f"\n--- {stage} ---")
    n_comp = nx.number_connected_components(G)
    print(f"Jumlah connected components: {n_comp}")
    for i, comp in enumerate(nx.connected_components(G)):
        sorted_comp = sorted(comp)
        print(f"  Komponen {i+1}: {sorted_comp}")
    return n_comp

# MEMBUAT GRAF: 5 KELOMPOK TERPISAH
G = nx.Graph()

# Warna per kampus
color_map = {
    "UGM": "skyblue",
    "ITB": "lightcoral",
    "UI": "gold",
    "Unpad": "lightgreen",
    "IPB": "violet",
    "Jembatan": "orange"
}

# Daftar tokoh
ugm = ["Anies", "Mahfud", "Najwa"]
itb = ["Ridwan", "Bambang", "Emil_S"]
ui = ["Sandiaga", "Wishnutama", "Rizal"]
unpad = ["Luhut", "Basuki", "Emil_D"]
ipb = ["Syahrul", "Andi", "Dedi"]

# menambahkan node + atribut kampus
for node in ugm:
    G.add_node(node, univ="UGM")
for node in itb:
    G.add_node(node, univ="ITB")
for node in ui:
    G.add_node(node, univ="UI")
for node in unpad:
    G.add_node(node, univ="Unpad")
for node in ipb:
    G.add_node(node, univ="IPB")

# menambhakan sisi internal
G.add_edges_from([
    ("Anies", "Mahfud"), ("Mahfud", "Najwa"), ("Anies", "Najwa"),
    ("Ridwan", "Bambang"), ("Bambang", "Emil_S"), ("Ridwan", "Emil_S"),
    ("Sandiaga", "Wishnutama"), ("Wishnutama", "Rizal"), ("Sandiaga", "Rizal"),
    ("Luhut", "Basuki"), ("Basuki", "Emil_D"), ("Luhut", "Emil_D"),
    ("Syahrul", "Andi"), ("Andi", "Dedi"), ("Syahrul", "Dedi")
])

# menganalisis sebelum jembatan
analyze_components(G, "SEBELUM: 5 CONNECTED COMPONENTS")


# MENAMBAHKAN TOKOH JEMBATAN: DIDIK (S1 IPB, S2 UGM)
G.add_node("Didik", univ="Jembatan")
G.add_edges_from([
    ("Didik", "Syahrul"), 
    ("Didik", "Mahfud")   
])

# menganalisis setelah jembatan
analyze_components(G, "SESUDAH: DIDIK (S1 IPB, S2 UGM) MENGHUBUNGKAN IPB & UGM")


#POSISI DAN WARNA
pos = {
    "Anies": (-3, 3), "Mahfud": (-2.5, 3.5), "Najwa": (-2, 3),
    "Syahrul": (-3, 0), "Andi": (-2.5, 0.5), "Dedi": (-2, 0),
    "Ridwan": (3, 3), "Bambang": (2.5, 3.5), "Emil_S": (2, 3),
    "Sandiaga": (-3, -3), "Wishnutama": (-2.5, -3.5), "Rizal": (-2, -3),
    "Luhut": (3, -3), "Basuki": (2.5, -3.5), "Emil_D": (2, -3),
    "Didik": (-2.5, 1.5)
}

# Warna berdasarkan atribut univ
colors = [color_map[G.nodes[node].get("univ", "Jembatan")] for node in G.nodes()]

#VISUALISASI 
plt.figure(figsize=(18, 10))

nx.draw(G, pos, with_labels=True,
        node_color=colors, node_size=800,
        font_size=10, font_weight='bold',
        edge_color='gray', width=1.5, alpha=0.9)

# Legenda di luar graf (sebelah kanan)
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='skyblue', label='UGM'),
    Patch(facecolor='lightcoral', label='ITB'),
    Patch(facecolor='gold', label='UI'),
    Patch(facecolor='lightgreen', label='Unpad'),
    Patch(facecolor='violet', label='IPB'),
    Patch(facecolor='orange', label='Jembatan (Didik)')
]
plt.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, 0.5),
           fontsize=12, title="Kampus", title_fontsize=14, frameon=True, edgecolor='black')

plt.title("Simulasi Jejaring Sosial: Alumni Ganda (S1 IPB, S2 UGM) sebagai Jembatan\n"
          "Total Connected Components: 4 (dengan 3 tetap terpisah)", fontsize=14, pad=20)

plt.axis('off')
plt.tight_layout()  
plt.subplots_adjust(right=0.75)  
plt.show()
print(f"""
{'='*60}
ANALISIS & INTERPRETASI GRAF
{'='*60}

1. Struktur Awal (Sebelum adanya hubungan):
   Graf terdiri dari 5 kelompok terpisah, masing-masing mewakili komunitas alumni:
     • UGM: Anies, Mahfud, Najwa
     • ITB: Ridwan, Bambang, Emil_S
     • UI: Sandiaga, Wishnutama, Rizal
     • Unpad: Luhut, Basuki, Emil_D
     • IPB: Syahrul, Andi, Dedi
   Tidak ada hubungan antar kampus, yang menunjukan jejaring sosial sangat terfragmentasi.

2. Peran Tokoh Jembatan (Didik):
   Didik adalah alumni S1 IPB dan S2 UGM, beliau memiliki afiliasi ganda.
   Beliau merupakan Rektor IPB (2020–2024) terhubung dengan Syahrul (IPB) dan Mahfud (UGM).
   Karena itu, komponen IPB dan UGM menyatu menjadi satu jejaring besar.

3. Perubahan Struktur (setelah ada hubungan) :
   Jumlah connected components berkurang dari 5 menjadi 4.
   Komponen baru: UGM + IPB (melalui Didik)
   ITB, UI, dan Unpad tetap terisolasi, jadi masih 3 connected components terpisah.

4. Makna keterhubungan dunia nyata:
   Afiliasi universitas memang membentuk 'lingkaran sosial' eksklusif.
   Namun, individu dengan latar belakang pendidikan lintas kampus (alumni ganda)
   bisa menjadi 'broker' atau 'penghubung' yang menyatukan jejaring terpisah.
   Ini menunjukkan pentingnya keragaman latar belakang dalam membangun kolaborasi satu sama lain.

""")


