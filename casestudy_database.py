### File Case Study untuk menstore berbagai case study di python ###
def case_study():
    print("\nPilih topik teori yang ingin dipelajari:")
    print("1. Case Study 1: Kalkulator konversi suhu")
    print('2. Case Study 2: Program penjualan buah')
    print('3. Case Study 3: Program penilaian siswa')
 
    try:
        choice = int(input(f"Masukkan nomor topik (1-3): "))
        print('\n')
        if choice == 1:
            print('''Membuat program untuk mengkonversi suhu Celsius ke Fahrenheit dan Kelvin:
            # Contoh implementasi:
            # Data suhu dalam Celsius
            celsius = 25
            # Konversi ke Fahrenheit
            fahrenheit = (celsius * 9/5) + 32
            # Konversi ke Kelvin
            # kelvin = celsius + 273.15
            
            # Tampilkan hasil
            print(f"Suhu: {celsius}°C")
            print(f"Fahrenheit: {fahrenheit}°F")
            print(f"Kelvin: {kelvin}K")

            # Cek tipe data
            print(f"Tipe data celsius: {type(celsius)}")
            print(f"Tipe data fahrenheit: {type(fahrenheit)}")''')
        elif choice == 2:
            print('''Membuat program penjualan buah:
            # Contoh implementasi:
            # Data buah
            buah = {
                "apel": 5,
                "jeruk": 10,
                "mangga": 8,
                "pisang": 15
            }

            # Tampilkan daftar buah
            print("Daftar buah:")
            for buah, stok in buah.items():
                print(f"- {buah}: {stok} buah")

            # Tampilkan total stok buah
            total_stok = sum(buah.values())
            print(f"Total stok buah: {total_stok} buah")''')

        elif choice == 3:
            print('''Membuat program penilaian siswa:
            # Contoh implementasi:
            # Data siswa
            siswa = {
                "Alice": 85,
                "Bob": 92,
                "Charlie": 78,
                "David": 95
            }

            # Tampilkan daftar siswa dan nilai
            print("Daftar siswa dan nilai:")
            for nama, nilai in siswa.items():
                print(f"- {nama}: {nilai}")

            # Tampilkan rata-rata nilai
            total_nilai = sum(siswa.values())
            jumlah_siswa = len(siswa)
            rata_rata = total_nilai / jumlah_siswa
            print(f"Rata-rata nilai: {rata_rata}")''')

    except ValueError:
        print("Input harus berupa angka.")
