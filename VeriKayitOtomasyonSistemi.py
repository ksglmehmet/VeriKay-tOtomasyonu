# Kullanıcı Kayıt Otomasyon Sistemi #

# Kişiye bir menü sunacağız. Kayıt girebilecek, kayıtları okuyabileceği, gerektiğinde kayıtları sileceği bir tür olacak.
# Desktopda "Bilgiler.txt" olsun.

import re # kontrol mekanizması için. Kişinin girdiği bilgileri kontrol edicek.
import time # bekleme süresi için kullanacağız.

class Kayit:
    def __init__(self, programad):
        self.programad = programad
        self.dongu = True # Program sürekli çalışsın diye, aksini söylemediğimiz müddetçe çalışacak. ATM yapısındaki mantık ile aynı.
    
    def program(self):
        
        secim = self.menu()
        
        if secim == "1":
            print("Kayıt Ekleme Menüsüne Yönlendiriliyorsunuz...")
            time.sleep(1)
            self.kayitekle()
            
        if secim == "2":
            print("Kayıt Silme Menüsüne Yönlendiriliyorsunuz...")
            time.sleep(1)
            self.kayitcikar()
            
        if secim == "3":
            print("Verilere Erişiliyor...")
            time.sleep(1)
            self.kayitoku()
        
        if secim == "4":
            self.cikis()
        
    
    def menu(self):
        
        def kontrol(secim):
            
            if re.search("[^1-4]", secim): # 1 ve 4 değerleri (dahil) arasındaki sayırlar dışında bir secim yaparsa hata döndüreceğiz.
                raise Exception("Lütfen 1 ve 4 arasında geçerli bir seçim yapınız.")
            elif len(secim) != 1:
                raise Exception("Lütfen 1 ve 4 arasında geçerli bir seçim yapınız.")
            
        while True:
            try:
                secim = input(f"Merhaba, {self.programad}'na hoşgeldiniz. \n\nLütfen Yapmak İstediğiniz İşlemi Seçiniz...\n\n[1]-Kayıt Ekle\n[2]-Kayıt Sil\n[3]-Kayıt Oku\n[4]-Çıkış\n\n")
                kontrol(secim)
            except Exception as Hata:
                print(Hata)
                time.sleep(1)
            else:
                break
        return secim
    
    def kayitekle(self): # Bilgiler alacağız, masaüstünde oluşturduğumuz .txt'ye kayıt edeceğiz. # Ad-Soyad-Yaş-Tc-Mail bilgilerini isteyelim(varsayım) Bunlarda kendi içinde denetlenmeli. İsim Soyisimde Sayı olmamalı gibi.
        
        def kontrolad(Ad):
            
            if not all(char.isalpha() or char.isspace() for char in Ad): # Tamamen karakterden oluşuyorsa True döndürür. Yoksa False, Eski Halinde iki isimlide hata vardı düzelttim. Mehmet Akif gibi.
                raise Exception("Adınız Sadece Alfabetik Karakterlerden Oluşmalıdır.")
        while True:
            try:
                Ad = input("Lütfen Adınızı Giriniz: ")
                kontrolad(Ad)
            except Exception as HataAd:
                print(HataAd)
                time.sleep(1)
            else:
                break
                
        def kontrolSoyad(Soyad):
            
            if not all(char.isalpha() or char.isspace() for char in Soyad): # Tamamen karakterden oluşuyorsa True döndürür. Yoksa False, iki soyadda olabilir. Kızlık soyadı vs.
                raise Exception("Soyadınız Sadece Alfabetik Karakterlerden Oluşmalıdır.")
            
        while True:
            try:
                Soyad = input("Lütfen Soyadınızı Giriniz: ")
                kontrolSoyad(Soyad)
            except Exception as HataSoyad:
                print(HataSoyad)
                time.sleep(1)
            else:
                break
        
        def kontrolYas(Yas):
            
            if Yas.isdigit() == False: # Girilenler tamamen sayısal değerse True, Yoksa False
                raise Exception("Yaşınız Sadece Rakamlardan Oluşmalıdır.")
            
        while True:
            try:
                Yas = input("Lütfen Yaşınızı Giriniz: ")
                kontrolYas(Yas)
            except Exception as HataYas:
                print(HataYas)
                time.sleep(1)
            else:
                break
        
        def kontrolTc(Tc):
            
            if Tc.isdigit() == False: 
                raise Exception("Kimlik Numaranız Sadece Rakamlardan Oluşmalıdır.")
            elif len(Tc) != 11: 
                raise Exception("Kimlik Numaranız 11 Karakterden Oluşmalıdır.")
            
        while True:
            try:
                Tc = input("Lütfen Kimlik Numaranızı Giriniz: ")
                kontrolTc(Tc)
            except Exception as HataTc:
                print(HataTc)
                time.sleep(1)
            else:
                break
                
        def kontrolMail(Mail):
            
            if not re.search("@", Mail): # Eğer Bulundurmuyorsa. if not.
                raise Exception("Geçerli bir mail adresi giriniz.")
            if not re.search(".com", Mail): # Eğer Bulundurmuyorsa. if not.
                raise Exception("Geçerli bir mail adresi giriniz.")
            
        while True:
            try:
                Mail = input("Lütfen Mail Adresinizi Giriniz: ")
                kontrolMail(Mail)
            except Exception as HataMail:
                print(HataMail)
                time.sleep(1)
            else:
                break
        with open("C:/Users/Mehmet Akif/Desktop/Bilgiler.txt", "r") as Dosya:
            satirsayisi = Dosya.readlines() # Belge boş ise 0-boş liste olarak dönecek, böylelikle txt belgemin boş olup olmadığını tespit ediyorum.
        
        if len(satirsayisi) == 0: #Yani dosya boş ise
            Id = 1 # Dosya içerisinde herhangi bir bilgi yoksa Id = 1 olacak.
        else:
            with open("C:/Users/Mehmet Akif/Desktop/Bilgiler.txt", "r") as Dosya:
                Id = int(Dosya.readlines()[-1].split("-")[0]) + 1
        
        with open("C:/Users/Mehmet Akif/Desktop/Bilgiler.txt", "a+") as Dosya:
            Dosya.write("{}-{} {} {} {} {}\n".format(Id, Ad, Soyad, Yas, Tc, Mail))
            print("Veriler İşlenmiştir.")
        self.menudon()
            
    def kayitcikar(self):
        
        y = input("Lütfen silmek istediğiniz kişinin Id numarasını giriniz: ")
        with open("C:/Users/Mehmet Akif/Desktop/Bilgiler.txt", "r") as Dosya:
            liste = []
            liste2 = Dosya.readlines()
            for i in range(0, len(liste2)):
                liste.append(liste2[i].split("-")[0])
                
        del liste2[liste.index(y)]
        
        with open("C:/Users/Mehmet Akif/Desktop/Bilgiler.txt", "w+") as YeniDosya:
            for i in liste2:
                YeniDosya.write(i)
        print("İlgili Id'ye ait kayıt siliniyor...")
        time.sleep(1)
        print("Kayıt başarıyla silinmiştir.")
        self.menudon()
    
    def kayitoku(self):
        
        with open("C:/Users/Mehmet Akif/Desktop/Bilgiler.txt", "r") as Dosya:
            for i in Dosya:
                print(i)
        self.menudon()
    
    def cikis(self):
        
        print("Veri Kayıt Otomasyonundan çıkışınız yapılmaktadır.")
        time.sleep(1)
        self.dongu = False
        exit()
    
    def menudon(self):
        
        while True:
            x = input("Ana müneye dönmek için 6'ya, uygulamadan çıkmak için lütfen 5'e basınız.")
            if x == "6":
                print("Ana müneye dönülüyor.")
                time.sleep(1)
                self.program()
                break
            if x == "5":
                self.cikis()
                break
            else:
                print("Lütfen geçerli bir seçim yapınız.")
    
    
Sistem = Kayit("Veri Kayıt Otomasyonu")
while Sistem.dongu:
    Sistem.program()
    
    