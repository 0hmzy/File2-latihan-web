nilai = [['001', 50, 64, 40], #nilai 0
         ['002', 80, 65, 78], #nilai 1
         ['003', 79, 53, 30]] #nilai 2
#semua anggota nilai(0,1,2) termasuk ketipe list sehingga  pernyataan diatas akan
#mengembalikan list

mhs1_id = nilai[1][0]   
mhs1_nilai1 = nilai[1][1] 
mhs1_nilai2 = nilai[1][2] #untuk merubah akses nilai mahasiswanya tinggal rubah elemen pertamanya
mhs1_nilai3 = nilai[1][3]
print(mhs1_id, mhs1_nilai1, mhs1_nilai2, mhs1_nilai3)
