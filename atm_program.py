import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input("Masukkan pin anda : "))
    trial =0
    while (id != int(atm.CheckPin()) and trial<3):
        id = int(input("Pin anda salah. Silahkan Masukkan lagi: "))
        trial +=1
        if trial==3:
            print("Error. Silahkan ambil kartu dan coba lagi..")
            exit()
    while True:
        print("Selamat datang di Atm..")
        print("\n1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - Keluar")
        selectMenu = int(input("\n Silahkan pilih menu: "))
        if selectMenu ==1:
            print("\n Saldo anda sekarang"+str(atm.CheckBalance())+"\n")
        elif selectMenu == 2:
            nominal = float(input("Masukkan nominal saldo:"))
            verify_withdraw = input("Konfirmasi: Anda akan melakukan debet dengan nominal berikut? y/n"+str(nominal)+" ")
            if verify_withdraw =="y":
                print("Saldo Awal anda adalah: Rp."+str(atm.CheckBalance())+"")
            else:
                break
            if nominal < atm.CheckBalance():
                atm.withdrawBalance(nominal)
                print("Transaksi debet berhasil")
                print("Saldo sisa sekarang: Rp."+str(atm.CheckBalance())+"")
            else:
                print("Maaf. Saldo anda tidak cukup untuk melakukan debet!")
                print("Silahkan lakukan penambahan nominal saldo")
        elif selectMenu == 3:
            nominal = float(input("Masukkan nominal saldo:"))
            verify_deposit = input("Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut? y/n"+str(nominal)+" ")
            if verify_deposit =="y":
                atm.depositBalance(nominal)
                print("Saldo anda sekarang adalah: Rp."+str(atm.CheckBalance())+"\n")
            else:
                break
        elif selectMenu == 4:
            verify_pin = int(input("Masukkan pin anda: "))
            while verify_pin != int(atm.CheckPin()):
                print("pin anda salah, silahkan masukkan pin:")
            updated_pin = int(input("Silahkan masukkan pin baru:"))
            print("pin anda berhasil diganti")
            verify_newpin = int(input("Coba masukkan pin baru: "))
            if verify_newpin == updated_pin:
                print("pin baru anda sukses")
            else:
                print("maaf, pin anda salah")
        elif selectMenu == 5:
            print("Resi tercetak otomatis saat anda keluar.\n Harap simpan tanda terima ini \n sebagai bukti transaksi anda.")
            print("No. Rekord: ",random.randint(100000,1000000))
            print("Tanggal: ", datetime.datetime.now())
            print("Saldo akhir: ",atm.CheckBalance())
            print("Terima kasih telah menggunakan Atm")
            exit()
        else:
            print("Error. Maaf, menu tidak tersedia")



