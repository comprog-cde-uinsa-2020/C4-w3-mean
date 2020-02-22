array = []
total = 0

print ('MENGHITUNG NILAI RATA-RATA')
n = int(input("Masukkan banyaknya siswa: "))

for x in range(n):
    nilai = float(input("Masukkan nilai siswa ke-{} : ".format(x+1)))
    array.append(nilai)
rata = (sum(array)/n )   
kamu = int(input("Masukkan nilai kamu: "))
print("Hasil rata-rata adalah : ",rata)

if kamu < rata:
    print ('nilaimu dibawah rata-rata')
elif kamu == rata :
    print ('nilaimu sama dengan rata-rata',x)
else:
    print ('nilaimu diatas rata-rata')
