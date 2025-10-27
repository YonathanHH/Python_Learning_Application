import time
import random

### Database untuk menambahkan soal quiz
### Struktur dictionary berupa  {"question": "int", "options":[list 4],"answer":"int"}
quiz_database = [{
            "question": "Tipe data apa yang digunakan untuk menyimpan bilangan desimal?",
            "options": ["A. Integer", "B. Float", "C. String", "D. Boolean"],
            "answer": "B"
        },{
            "question": "Variable mana yang menyimpan tipe data String?",
            "options": ["A. angka = 123", "B. nilai = 45.5", "C. nama = 'Budi'", "D. status = True"],
            "answer": "C"
        },{
            "question": "Apa kegunaan dari 'return' dalam fungsi?",
            "options": ["A. Menghentikan program", "B. Mengembalikan nilai", "C. Mencetak output", "D. Memulai fungsi"],
            "answer": "B"
        }, {
            "question": "Method apa yang menambahkan item di akhir list?",
            "options": ["A. add()", "B. append()", "C. insert()", "D. push()"],
            "answer": "B"
        },{
            "question": "Apa output dari: list = [1, 2, 3]; print(list[0])?",
            "options": ["A. 1", "B. 2", "C. 3", "D. Error"],
            "answer": "A"
        },{
            "question": "Apa output dari: for i in range(2, 5): print(i)?",
            "options": ["A. 2 3 4", "B. 2 3 4 5", "C. 1 2 3 4", "D. 3 4 5"],
            "answer": "A"
        },{
            "question": "Keyword apa yang digunakan untuk menghentikan loop sepenuhnya?",
            "options": ["A. continue", "B. break", "C. stop", "D. exit"],
            "answer": "B"
        },{
            "question": "Apa fungsi dari 'continue' dalam loop?",
            "options": ["A. Stop loop", "B. Lompat ke iterasi berikutnya", "C. Reset loop", "D. Pause loop"],
            "answer": "B"
        },{
            "question": "Keyword apa yang digunakan untuk mendefinisikan fungsi di Python?",
            "options": ["A. function", "B. def", "C. func", "D. define"],
            "answer": "B"
        }]


def tampilkan_hasil(skor, total_soal, hasil_jawaban):
    print("\n" + "="*60)
    print("HASIL QUIZ")
    print("="*60)
    
    persentase = (skor / total_soal) * 100
    
    print(f"\nSkor Anda: {skor}/{total_soal}")
    print(f"Persentase: {persentase:.1f}%")
    
    #Menghitung rata2 dan total waktu
    total_waktu = sum(h['waktu'] for h in hasil_jawaban)
    rata_waktu = total_waktu / total_soal
    print(f"Total Waktu: {total_waktu:.1f} detik")
    print(f"Rata-rata Waktu: {rata_waktu:.1f} detik/soal")
    
    # Kategori nilai
    print("\n" + "-"*60)
    if persentase == 100:
        print("Grade: A+ - Perfect! ")
    elif persentase >= 90:
        print("Grade: A - Sangat baik! ")
    elif persentase >= 80:
        print("Grade: B - Baik! ")
    elif persentase >= 70:
        print("Grade: C - Cukup Baik! ")
    elif persentase >= 60:
        print("Grade: D - Cukup! ")
    else:
        print("Grade: E - Masih kurang, Perlu Belajar Lagi")
    print("-"*60)
    print(input("Tekan enter untuk melihat review jawaban..."))
    # Review jawaban
    print("\n" + "="*60)
    print("REVIEW JAWABAN")
    print("="*60)
    
    for hasil in hasil_jawaban:
        status = "✓ BENAR" if hasil['benar'] else "✗ SALAH"
        print(f"\n{hasil['nomor']}. {status}")
        print(f"   Pertanyaan: {hasil['soal'][:60]}...")
        print(f"   Jawaban Anda: {hasil['jawaban_user']}")
        print(f"   Jawaban Benar: {hasil['jawaban_benar']}")
        print(f"   Waktu: {hasil['waktu']:.1f} detik")
    
    print("\n" + "="*60)
    print("Terima kasih telah mengikuti quiz!")
    print("="*60)
    
def run_quiz():
    # Menampilkan instruksi
    print("\n" + "="*60)
    print("QUIZ PYTHON BASICS")
    print("="*60)
    print("\nPetunjuk:")
    print("- Setiap pertanyaan memiliki batas waktu 30 detik")
    print("- Pilih jawaban A, B, C, atau D")
    print("- Jawaban akan otomatis dianggap salah jika waktu habis")
    print("="*60)
    
    # User input untuk menampilkan berapa soal yang dikerjakan
    try:
        jumlah_soal = int(input(f"\nBerapa soal yang ingin dikerjakan? (1-{len(quiz_database)}): "))
        if jumlah_soal < 1 or jumlah_soal > len(quiz_database):
            print(f"Jumlah soal harus antara 1-{len(quiz_database)}")
            return
    except ValueError:
        print("Input harus berupa angka!")
        return
    
    # randomize pertanyaan
    soal_terpilih = random.sample(quiz_database, jumlah_soal)
    
    # Untuk track skor, jawaban, dan store waktu dalam detik
    skor = 0
    hasil_jawaban = []
    waktu_per_soal = 30  # detik
    
    input("\nTekan Enter untuk memulai quiz...")
    
    # Loop untuk setiap soal
    for i, soal in enumerate(soal_terpilih, 1):
        print("\n" + "="*60)
        print(f"SOAL {i} dari {jumlah_soal}")
        print("="*60)
        print(f"\n{soal['question']}\n")
        
        # Tampilkan opsi
        for option in soal['options']:
            print(option)
        
        # Mulai timer
        print(f"\nWaktu: {waktu_per_soal} detik")
        print("-" * 60)
        
        waktu_mulai = time.time()
        jawaban_user = input("Jawaban Anda (A/B/C/D): ").strip().upper()
        waktu_selesai = time.time()
        
        waktu_terpakai = waktu_selesai - waktu_mulai
        
        # Cek apakah waktu habis
        if waktu_terpakai > waktu_per_soal:
            print(f"\n WAKTU HABIS! ({waktu_terpakai:.1f} detik)")
            is_correct = False
            jawaban_user = "TIMEOUT"
        else:
            # Cek jawaban
            is_correct = (jawaban_user == soal['answer'])
            
            if is_correct:
                print(f"\n✓ BENAR! ({waktu_terpakai:.1f} detik)")
                skor += 1
            else:
                print(f"\n✗ SALAH! ({waktu_terpakai:.1f} detik)")
                print(f"Jawaban yang benar: {soal['answer']}")
        
        # Simpan hasil
        hasil_jawaban.append({
            'nomor': i,
            'soal': soal['question'],
            'jawaban_user': jawaban_user,
            'jawaban_benar': soal['answer'],
            'benar': is_correct,
            'waktu': waktu_terpakai
        })
        
        # Jeda sebelum soal berikutnya
        if i < jumlah_soal:
            input("\nTekan Enter untuk soal berikutnya...")
    
    # Tampilkan hasil akhir
    tampilkan_hasil(skor, jumlah_soal, hasil_jawaban)
