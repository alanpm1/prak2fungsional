expenses = [
    {'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
    {'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
    {'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},
]

# TODO 1: Fungsi untuk menambahkan pengeluaran baru
add_expense = lambda expenses, date, description, amount: expenses + [{'tanggal': date, 'deskripsi': description, 'jumlah': amount}]

# TODO 2: Fungsi untuk menghitung total pengeluaran harian
calculate_total_expenses = lambda expenses, date: sum(expense['jumlah'] for expense in expenses if expense['tanggal'] == date)

# TODO 3: Fungsi untuk menyaring pengeluaran berdasarkan tanggal tertentu
get_expenses_by_date = lambda expenses, date: [expense for expense in expenses if expense['tanggal'] == date]

# TODO 4: Fungsi untuk menghasilkan laporan pengeluaran harian sebagai generator
generate_expenses_report = lambda expenses: (f"{expense['tanggal']}: {expense['deskripsi']} - Rp {expense['jumlah']}" for expense in expenses)

# TODO 6: Fungsi lambda untuk mendapatkan input pengguna
get_user_input = lambda command: int(input(command))

# TODO 5: Definisi display_menu
display_menu = lambda: print("\n===== Aplikasi Pencatat Pengeluaran Harian =====\n1. Tambah Pengeluaran\n2. Total Pengeluaran Harian\n3. Lihat Pengeluaran berdasarkan Tanggal\n4. Lihat Laporan Pengeluaran Harian\n5. Keluar")

def main():
    global expenses
    while True:
        display_menu()
        choice = get_user_input("Pilih menu (1/2/3/4/5): ")
        if choice == 1:
            date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
            description = input("Masukkan deskripsi pengeluaran: ")
            amount = int(input("Masukkan jumlah pengeluaran: "))
            expenses = add_expense(expenses, date, description, amount)
            print("Pengeluaran berhasil ditambahkan.")
        elif choice == 2:
            date = input("Masukkan tanggal (YYYY-MM-DD): ")
            total_expenses = calculate_total_expenses(expenses, date)
            print(f"\nTotal Pengeluaran Harian: Rp {total_expenses}")
        elif choice == 3:
            date = input("Masukkan tanggal (YYYY-MM-DD): ")
            expenses_on_date = get_expenses_by_date(expenses, date)
            print(f"\nPengeluaran pada tanggal {date}:")
            for expense in expenses_on_date:
                print(f"{expense['deskripsi']} - Rp {expense['jumlah']}")
        elif choice == 4:
            print("\nLaporan Pengeluaran Harian:")
            expenses_report = generate_expenses_report(expenses)
            for entry in expenses_report:
                print(entry)
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih menu yang benar.")

if __name__ == "__main__":
    main()