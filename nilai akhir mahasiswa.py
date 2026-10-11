data_mahasiswa = [
    {"nama": "Hajiasep", "NIM": "2595114017", "tugas": 85, "UTS": 70, "UAS": 75},
    {"nama": "Antoni", "NIM": "2595114015", "tugas": 73, "UTS": 83, "UAS": 76},
    {"nama": "Akrom", "NIM": "2595114001", "tugas": 79, "UTS": 91, "UAS": 90},
    {"nama": "Rizal", "NIM": "2595114020", "tugas": 73, "UTS": 83, "UAS": 95}
]

mahasiswa = [
    {
        **m,
        "nilai_akhir":
        (m["tugas"] * 30/100)
        + (m["UTS"] * 30/100)
        + (m["UAS"] * 40/100)
    }
    for m in data_mahasiswa
]

print("===Nilai Akhir Mahasiswa===")
for m in mahasiswa:
     print(f"{m['nama']}: {m['nilai_akhir']:.1f}")

mahasiswa_berprestasi = list(
     filter(
            lambda m: m["nilai_akhir"] > 80,
            mahasiswa
     )
)
print("\n===Mahasiswa berprestasi===")

for m in mahasiswa_berprestasi:
     print(f"{m['nama']}: {m['nilai_akhir']:.1f}")

rangking_mahasiswa = sorted(
     mahasiswa,
     key=lambda m: m["nilai_akhir"],
     reverse=True
)
print("\n===Rangking mahasiswa===")
for nomor, m in enumerate(rangking_mahasiswa, start=1):
     print(
        f"Rangking {nomor}: {m['nama']} -"
        f"Nilai Akhir: {m['nilai_akhir']:.1f}"
    )

mahasiswa_terbaik = rangking_mahasiswa[0]

print("\n===Mahasiswa terbaik===")
print(f"nama: {mahasiswa_terbaik['nama']}")
print(f"NIM: {mahasiswa_terbaik['NIM']}")
print(f"Nilai tugas: {mahasiswa_terbaik['tugas']}")
print(f"Nilai UTS: {mahasiswa_terbaik['UTS']}")
print(f"Nilai UAS: {mahasiswa_terbaik['UAS']}")
print(f"Nilai Akhir: {mahasiswa_terbaik['nilai_akhir']:.1f}")