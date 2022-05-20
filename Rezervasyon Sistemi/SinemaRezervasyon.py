import time
matr = []
for i in range(20):
    satir = []
    for j in range(20):
        x = "-"
        satir.append(x)
    matr.append(satir)
KategoriKolSayısı=[100,100,100,100]
KategoriCiro = [0,0,0,0]
def SalonRezerve_TipBir(Kategori):
    if Kategori==1:
        SatirBas=0
        SatirSon=10
    elif Kategori==3:
        SatirBas=10
        SatirSon=20
    RezerveKoltuklar = ""
    sayac=0
    for i in range(SatirBas,SatirSon):
        for j in range(5,15):
            while matr[i][j] !="X" and sayac!=BilAd:
                matr[i][j]="X"
                sayac = sayac + 1
                KategoriKolSayısı[Kategori-1]= KategoriKolSayısı[Kategori-1]-1
                RezerveKoltuklar = RezerveKoltuklar +str(i+1)+"-"+str(j+1)+","
    print("Rezerve edilen koltuklar (Sira-Koltuk):"+RezerveKoltuklar)
    if KategoriKolSayısı[Kategori-1]-(BilAd-sayac)<0:
        print(Kategori,". Kategori için uygun bilet kalmamıştır kalan",BilAd-sayac,"bileti tekrardan rezerve edebilirsiniz.")
    elif KategoriKolSayısı[Kategori-1] == 0:
        print(Kategori,". Kategori icin biletler tükenmiştir")
    else:
        print(Kategori,". Kategori için kalan bilet sayısı:",KategoriKolSayısı[Kategori-1])
    
def SalonRezerve_TipIki(Kategori):
    if Kategori == 2:
        SatirBas=0
        SatirSon=10
        SonKolSat =9
        SonKolStu =19
    elif Kategori == 4:
        SatirBas=10
        SatirSon=20
        SonKolSat =19
        SonKolStu =19
    RezerveKoltuklar = ""
    sayac = 0
    while sayac != BilAd and matr[SonKolSat][SonKolStu]=="-":
        for i in range(SatirBas, SatirSon):
            for j in range(4,-1,-1):
                if matr[i][j] !="X" and sayac!=BilAd:
                    matr[i][j] = "X"
                    sayac = sayac + 1
                    KategoriKolSayısı[Kategori-1]= KategoriKolSayısı[Kategori-1]-1
                    RezerveKoltuklar = RezerveKoltuklar +str(i+1)+"-"+str(j+1)+","
            for k in range(15,20):
                if matr[i][k] != "X" and sayac != BilAd:
                    matr[i][k] ="X"
                    sayac += 1
                    KategoriKolSayısı[Kategori-1]= KategoriKolSayısı[Kategori-1]-1
                    RezerveKoltuklar = RezerveKoltuklar +str(i+1)+"-"+str(k+1)+","
    print("Rezerve edilen koltuklar (Sira-Koltuk):"+RezerveKoltuklar)
    if KategoriKolSayısı[Kategori-1]-(BilAd-sayac)<0:
        print(Kategori,". Kategori için uygun bilet kalmamıştır kalan",BilAd-sayac,"bileti tekrardan rezerve edebilirsiniz.")
    elif KategoriKolSayısı[Kategori-1] == 0:
        print(Kategori,". Kategori icin biletler tükenmiştir")
    else:
        print(Kategori,". Kategori için kalan bilet sayısı:",KategoriKolSayısı[Kategori-1])
        
def SalonDüzenleme():
    print("Salon temizleniyor...")
    time.sleep(0.5)
    for i in range(20):
        for j in range(20):
            matr[i][j]="-"
    
def SalonCikti():
    print("Salon Planı Goruntuleniyor...")
    time.sleep(1)
    print("""
          *******************
              Salon Planı
          *******************
    """)
    for i in range(20):
        for j in range(20):
            print(matr[i][j], end=" ")
        print()
def KalanBiletler():
    print(Kategori,""". Kategori için uygun bilet sayısı bulunmamaktadır.
Dilerseniz diğer kategorilerimizden rezervasyonunuzu gerçekleştirebilirsiniz.""")
    for i in range(len(KategoriKolSayısı)):
        print(i+1 ,".Kategori için kalan koltuk sayısı -> [",KategoriKolSayısı[i],"]") 
    input("Ana Menüye dönmek için 'Enter' tuşuna basınız")

def İndirim(Kategori):
    İndirimDosyası = open("indirim.txt","r")
    İndirimListesi = İndirimDosyası.readlines()
    İndirimDosyası.close()
    BilFiyatı = int(İndirimListesi[Kategori][2:5])
    Oran = 0
    if Kategori == 1:
        if BilAd > 4 and BilAd < 11:
            Oran = int(İndirimListesi[5][8:10])
        elif BilAd > 10 and BilAd < 21:
            Oran = int(İndirimListesi[6][8:10])
        elif BilAd >20:
            Oran = int(İndirimListesi[7][7:9])
    elif Kategori == 2:
        if BilAd > 4 and BilAd < 11:
            Oran = int(İndirimListesi[8][8:10])
        elif BilAd > 10 and BilAd < 21:
            Oran = int(İndirimListesi[9][8:10])
        elif BilAd > 20:
            Oran = int(İndirimListesi[10][7:9])
    elif Kategori == 3:
        if BilAd > 4 and BilAd < 16:
            Oran = int(İndirimListesi[11][8:10])
        elif BilAd > 15 and BilAd < 26:
            Oran = int(İndirimListesi[12][8:10])
        elif BilAd > 25:
            Oran = int(İndirimListesi[13][7:9])
    elif Kategori == 4:
        if BilAd > 4 and BilAd < 11:
            Oran = int(İndirimListesi[14][8:10])
        elif BilAd > 10 and BilAd < 21:
            Oran = int(İndirimListesi[15][8:10])
        elif BilAd > 20:
            Oran = int(İndirimListesi[16][7:9])
    ToplamTutar = BilAd*BilFiyatı
    print("Rezervasyon edilen bilet adedi:",BilAd)
    print("Rezerve edilen biletlerin toplam tutarı:",ToplamTutar,"TL'dir.")
    if BilAd > 4:
        Hesaplama = (ToplamTutar *(100-Oran))/100
        KategoriCiro[Kategori-1]= KategoriCiro[Kategori-1] + Hesaplama
        print("Rezervasyona uygulanan indirim","%",Oran,"'dır.")
        print("Ödenecek tutar:",Hesaplama,"TL'dir.")
    elif BilAd < 5 and BilAd > 0:
        KategoriCiro[Kategori-1]= KategoriCiro[Kategori-1] + ToplamTutar
def CiroYazdır():
    for i in range(len(KategoriCiro)):
        print(i+1 ,".Kategori için yapılan ciro -> [",KategoriCiro[i],"]")
    TopCiro = 0
    for i in KategoriCiro:
        TopCiro = TopCiro + i
    print("Toplam ciro =", TopCiro)
    input("Ana Menüye dönmek için 'Enter' tuşuna basınız")        
#ANA PROGRAM
Secim=-1
while Secim!=0:
    print("""
**********************
* [1] Rezervasyon    *
* [2] Salonu Yazdır  *
* [3] Yeni Etkinlik  *
* [4] Toplam Ciro    *
* [0] Çıkış          * 
**********************
    """)
    Secim = input("Seciminiz ?")
    if Secim =="1":
        Kategori = int(input("Kategori (1-4) ? "))
        if Kategori ==1 or Kategori==2 or Kategori==3 or Kategori==4:
            BilAd = int(input("Bilet Adeti (1-30) ? "))
            if BilAd > 30 or BilAd < 1:
                input("Lütfen Geçerli sayıda bilet adeti seçiniz(Ana menüye dönmek için enter tuşuna basınız.)")
            else:
                if Kategori==1 or Kategori==3:
                    if BilAd>KategoriKolSayısı[Kategori-1]:
                        KalanBiletler()
                    elif BilAd<=KategoriKolSayısı[Kategori-1]:
                        SalonRezerve_TipBir(Kategori)
                        İndirim(Kategori)
                elif Kategori==2 or Kategori==4:
                    if BilAd>KategoriKolSayısı[Kategori-1]:
                        KalanBiletler()
                    elif BilAd<=KategoriKolSayısı[Kategori-1]:
                        SalonRezerve_TipIki(Kategori)
                        İndirim(Kategori)
        elif Kategori>4 or Kategori<=0:
            input("Lütfen doğru bir kategori seçiniz.(Ana Menüye dönmek için 'Enter' tuşuna basınız)")
    elif Secim == "2":
        SalonCikti()
    elif Secim == "3":
        SalonDüzenleme()
        KategoriKolSayısı=[100,100,100,100]
        KategoriCiro = [0,0,0,0]
        TopCiro = 0
    elif Secim == "4":
        CiroYazdır()
    elif Secim =="0":
        Secim = 0
    else:
        print("Lütfen geçerli bir seçim yapınız.(Ana Menüye dönmek için 'Enter' tuşuna basınız)")
        input()
