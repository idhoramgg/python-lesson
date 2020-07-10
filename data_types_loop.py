# string #skalar #sederhana
firstName = 'Ridho'
lastName = "Abdul Majid"
job = "Software Engineer"

# tipe data list/daftar atau array pada js
# TIPE DATA LIST/DAFTAR ATAU ARRAY PADA JAVASCRIPT

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

# ----------------------------------#
for a in range(0, len(siswa)):
    print(f'{a + 1} Halo lagi {siswa[a]}')

print('------------------------------------------------------------------')

# TIPE DATA DICTIONARY
# KVP -> OBJECT DI JAVASCRIPT

obj = {
    'nama': 'ridho',
    'usia': 26,
    'hobby': {
        'olahraga': 'renang',
        'makanan': 'nasi padang'
    },
    'panggilan': ['ido', 'ridho', 'majid']
}
# akses nama objek['key']['another key']
print(obj['hobby']['olahraga'])
print(obj['panggilan'][1])
