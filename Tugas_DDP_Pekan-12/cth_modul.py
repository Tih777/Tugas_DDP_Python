class Bank:
    # Member 1 variabel
    norek = ''
    nama = ''
    saldo = 0
    jmlhNasabah = 0 # Variabel static 
    BANK = 'Bank syariah Nurul Fikri' # Variabel konstanta

    # Member 2 kosntruktor
    def __init__(self, no, nasabah, saldo):
        self.norek = no
        self.nama = nasabah
        self.saldo = saldo
        Bank.jmlhNasabah += 1

    # Member 3 method
    def nabung(self, uang):
        # self.saldo = self.saldo + uang
        self.saldo += uang

    def tarik(self,uang):
        # self.saldo = self.saldo - uang
        self.saldo -= uang

    def cetak(self):
        print(Bank.BANK,
        '\n ==================== '
        '\n No. Rekening\t: ',self.norek,
        '\n Nama Nasabah\t: ',self.nama,
        '\n Saldo\t\t: Rp. ',format(self.saldo, ','),
        '\n -------------------- '
        )