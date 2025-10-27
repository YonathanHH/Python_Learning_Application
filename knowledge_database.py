### File ini berisi silabus dan berbagai teori berkaitan dengan python
### Mulai silabus
def syllabus():
    print('''Apa yang akan kita pelajari hari ini?
          1. Printing and comments
          2. Variables and data types
          3. Operators
          4. User input
          5. Conditionals
          6. Loops
          7. Functions
          8. Data Collections
          9. Built-in functions
          10. Error handling
          11. File import
          ''')

### Mulai teori
def printing_comments():
    print("print() digunakan untuk menampilkan output.")
    print("Komentar diawali dengan # untuk satu baris atau '''...''' untuk banyak baris.")

def variables_data_types():
    print("Variable adalah nama untuk menyimpan data.")
    print("Tipe data dasar: int, float, str, bool.")
    print("int = bilangan bulat, float = bilangan pecahan, str = text, bool = True atau False.")
    print('''contoh:
    a = 10 (Int)
    b = 3.14 (Float)
    c = "Hello" (Str)
    d = True (Bool)''')

def operators():
    print("Operator digunakan untuk operasi matematika, logika, perbandingan.\n")
    print('''Contoh: + untuk penjumlahan, - untuk pengurangan, * untuk perkalian,\n
    / untuk pembagian, % untuk modulus, == untuk perbandingan, != untuk perbandingan,\n
    > untuk perbandingan, < untuk perbandingan."''')

def user_input():
    print("input() digunakan untuk menerima input dari user.")
def conditionals():
    print('''if, elif, else digunakan untuk membuat percabangan. \n
    if: jika kondisi benar, maka jalankan kode di dalamnya.\n
    elif: jika kondisi benar, maka jalankan kode di dalamnya.\n
    else: jika kondisi salah, maka jalankan kode di dalamnya.''')

def loops():
    print('''for loop digunakan untuk melakukan perulangan sebanyak n kali.
    while loop digunakan untuk melakukan perulangan selama kondisi benar.
    break digunakan untuk menghentikan perulangan.
    continue digunakan untuk melewati 1 iterasi.''')

def functions():
    print('''Fungsi didefinisikan dengan def. Memungkinkan kode dapat digunakan berulang-ulang (reusable). \n
    Contoh: def nama_fungsi(): \n
                print("Ini adalah fungsi")\n
    nama_fungsi()\n
    global digunakan untuk mengakses variabel di luar fungsi. parameter digunakan untuk memasukkan argumen.''')

def data_collections():
    print('''List, Tuple, Set, Dictionary digunakan untuk menyimpan banyak data. \n
          List adalah daftar yang dapat diubah. \n
          Tuple adalah daftar yang tidak dapat diubah. \n
          Set adalah daftar yang tidak memiliki duplikat. \n
          Dictionary adalah daftar yang memiliki kunci dan nilai. \n
          Contoh: \n
          list = [1, 2, 3] \n
          tuple = (1, 2, 3) \n
          set = {1, 2, 3} \n
          dictionary = {"a": 1, "b": 2, "c": 3}''')
def built_in_functions():
    print('''Fungsi yang sudah tersedia di Python seperti len(), type(), input(), print(), sum(), min(), max(). \n
          len() digunakan untuk menghitung panjang dari suatu objek. \n
          type() digunakan untuk mengetahui tipe data dari suatu objek. \n
          input() digunakan untuk menerima input dari user. \n
          print() digunakan untuk menampilkan output. \n
          sum() digunakan untuk menjumlahkan semua angka dalam suatu daftar. \n
          min() digunakan untuk mencari angka terkecil dalam suatu daftar. \n
          max() digunakan untuk mencari angka terbesar dalam suatu daftar.''')

def error_handling():
    print('''Error handling digunakan untuk menangani error. \n
          try, except digunakan untuk menangani error. \n
          Contoh: \n
          try: \n
              x = int(input("Masukkan angka: ")) \n
          except ValueError: \n
              print("Input harus berupa angka!")''')

def file_import():
    print('''import digunakan untuk mengimpor modul. \n
          Contoh: \n
          import math \n
          print(math.pi)''')
###Print teori
def theory():
    print("\nPilih topik teori yang ingin dipelajari:")
    print("1. Printing and comments")
    print("2. Variables and data types")
    print("3. Operators")
    print("4. User input")
    print("5. Conditionals")
    print("6. Loops")
    print("7. Functions")
    print("8. Data Collections")
    print("9. Built-in functions")
    print("10. Error handling")
    print("11. File import")
    try:
        choice = int(input("Masukkan nomor topik (1-11): "))
        print('\n')
        if choice == 1:
            printing_comments()
        elif choice == 2:
            variables_data_types()
        elif choice == 3:
            operators()
        elif choice == 4:
            user_input()
        elif choice == 5:
            conditionals()
        elif choice == 6:
            loops()
        elif choice == 7:
            functions()
        elif choice == 8:
            data_collections()
        elif choice == 9:
            built_in_functions()
        elif choice == 10:
            error_handling()
        elif choice == 11:
            file_import()
        else:
            print("Pilihan tidak valid. Masukkan angka 1-11.")
    except ValueError:
        print("Input harus berupa angka 1-11.")