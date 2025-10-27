import knowledge_database as kdb
import casestudy_database as cdb
import quiz_database as qdb
def main_menu():
    print('#'*50 )
    print('     Selamat datang di python crash course!!!')
    print('#'*50,'\n')
    print('Pilih menu:')
    print('1. Lihat syllabus atau daftar topik \n' \
    '2. Belajar theory \n' \
    '3. Belajar Case Study \n' \
    '4. Mulai quiz \n' \
    '5. Keluar dari program \n')
    print('#'*50, )

def main():
    while True:
        main_menu()
        choice = input('Pilihan: ')
        try:
            if choice == '1':
                kdb.syllabus()
                input('Tekan enter untuk melanjutkan...')
            elif choice == '2':
                kdb.theory()
                input('Tekan enter untuk melanjutkan...')
            elif choice == '3':
                cdb.case_study()
                input('Tekan enter untuk melanjutkan...')
            elif choice == '4':
                qdb.run_quiz()
                input('Tekan enter untuk melanjutkan...')
            elif choice == '5':
                exit()
        except ValueError:
            print('Pilihan tidak valid')
            break
        except KeyboardInterrupt:
            print('\n\nProgram dihentikan oleh user.')
            break

main()