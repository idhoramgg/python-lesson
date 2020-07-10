# string #skalar #sederhana
firstName = 'Ridho'
lastName = "Abdul Majid"
job = "Software Engineer"

# tipe data list/daftar atau array pada js
siswa = []
siswa.append('Agung')
siswa.append('Budhi')
siswa.append('Chris')

# ------------------- #
pelajar = ['Agung', 'Angga', 'Budhi']
print(siswa)
print(f'Haloo {siswa[0]}')

print('Sapa semua pelajar :')
for a in siswa:
    print(f'{a}')

#----------------------------------#
for a in range(0, len(siswa)):
    print(f'{a+1} Halo lagi {siswa[a]}')
