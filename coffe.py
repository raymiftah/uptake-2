product = {
"caffe americano": 37000,
"caramel macchiato": 59000,
"asian dolce latte": 55000,
"caramel latte": 52000,
"cappuccino": 48000,
"caffe mocha": 55000,
}

def coffe():
    print("Selamat datang,selamat ngopi bosku")
    print("Berikut adalah daftar menu coffe tersedia:")
    for coffe, harga in product.items():
        print(f"{coffe}: Rp{harga} per rasa")
        total_belanja = 0
        while True :
            kopi_dipilih = input("Masukan nama kopi yang ingin anda beli (atau 'selesai' untuk selesai)")
            if kopi_dipilih.lower() == 'selesai':
                break
            if kopi_dipilih not in product:
                print("Maaf, kopi tersebut sudah habis")
                continue
            jumlah = float(input(f"kopi rasa {barang_dipilih} apa yang anda inginkan"))
            total_belanja += product[barang_dipilih] * jumlah
            print(f"total belanja anda adalah: Rp {total_belanja}")

        ppn = total_belanja * 0.1
        print (f"PPN 10%: Rp {ppn: .2f}")

        if total_belanja > 350000:
            diskon = total_belanja * 0.15
            print(f"Diskon 15%: Rp{diskon:.2f}")
            total_belanja -= diskon

        print(f"Total belanja anda setelah pajak dan diskon: Rp {total_belanja:.2f}")    

coffe()