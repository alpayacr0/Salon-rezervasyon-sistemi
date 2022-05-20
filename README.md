# Salon-rezervasyon-sistemi
Sinema, konser, tiyatro, vb. tarzı etkinliklerin düzenlendiği bir konser salonu için basit bir rezervasyon sistemi geliştirilmiştir. Salondaki koltukların dizilimi aşağıda verilmiştir.

![image](https://user-images.githubusercontent.com/101067222/169596027-3fe8aa0e-e525-4679-bc0b-998f33b395c1.png)

Salondaki koltuklar 4 farklı fiyat kategorisinde değerlendirilmektedir. Sistem, her kategori için o andaki en uygun koltukları rezerve etmek üzerine tasarlanacaktır. Buna göre,
1. kategoriye ilişkin bilet rezervasyon işlemleri, 1. sıra 6 numaralı koltuktan başlayacaktır.Herhangi bir sıranın 15. koltuğunun rezerve edilmesinin ardından bir arkadaki sıranın 6. koltuğundan itibaren rezervasyon işlemleri devam edecektir.

2. kategoriye ilişkin bilet rezervasyon işlemleri, 1. sıra 5 numaralı koltuktan başlayacak ve rezerve sırası sola doğru işleyecektir. Sıra başındaki 1 numaralı koltuğun rezerve edilmesinin ardından, aynı sıradaki 16. koltuktan itibaren sağa doğru işlemlere devam edilecektir. Herhangi bir sıranın 20. koltuğunun rezerve edilmesinin ardından bir arkadaki sıranın 5. koltuğundan itibaren rezervasyon işlemleri devam edecektir.

3. kategoriye ilişkin bilet rezervasyon işlemleri, 11. sıra 6 numaralı koltuktan başlayacaktır. Herhangi bir sıranın 15. koltuğunun rezerve edilmesinin ardından bir arkadaki sıranın 6. koltuğundan itibaren rezervasyon işlemleri devam edecektir.

4. kategoriye ilişkin bilet rezervasyon işlemleri, 11. sıra 5 numaralı koltuktan başlayacak ve rezerve sırası sola doğru işleyecektir. Sıra başındaki 1 numaralı koltuğun rezerve edilmesinin ardından, aynı sıradaki 16. koltuktan itibaren sağa doğru işlemlere devam edilecektir. Herhangi bir sıranın 20. koltuğunun rezerve edilmesinin ardından bir arkadaki sıranın 5. koltuğundan itibaren rezervasyon işlemleri devam edecektir.

Her kategorinin toplam koltuk kapasitesi 100’dür. Herhangi bir anda rezerve edilmek istenen toplam koltuk sayısı, o kategoride kalan boş koltuk sayısını aşıyorsa rezervasyon işlemi red edilmektedir.

Tüm kategoriler için bir kerede en fazla kaç bilet satılacağı bilgisi ile, her kategoride satın alınan bilet adedine göre uygulanacak indirim tutarları, "indirim.txt" isimli bir dosyadan okunmaktadır.

Dosya içerisinde bulunan "indirim.txt" dosyası aşağıda görüntülendiği gibidir:

![image](https://user-images.githubusercontent.com/101067222/169603127-f6ff2014-b7f2-412f-9a98-1f3c0cfb930d.png)

Dosyanın ilk satırı : M-XX şeklinde olup, XX sayısı tüm kategoriler için geçerli olmak üzere, bir seferde satın alınabilecek maksimum bilet sayısını göstermektedir (yukarıdaki örnekte, max. 30 bilet). Rezervasyon işlemlerinde bu sayıdan daha fazla bilet alınmak istendiğinde hata mesajı karşılamaktadır.

Dosyanın 2., 3., 4. ve 5. satırları; her kategori için bir bilet ücretini göstermektedir (yukarıdaki örnekte; 1. kategori 200TL, 2.kategori 150TL, 3.kategori 100TL ve 4.kategori 60TL 'dir).

Dosyanın geri kalan (6. satır ve sonrası) satırları K-MIN-MAX-ORAN formatındadır.

K : kategori

MIN : bilet adedi alt limit

MAX : bilet adedi üst limit

ORAN : uygulanacak indirim oranı

Bir örnek olarak: 1-05-10-10 şeklinde bir satır; 1. kategoride [5-10] aralığında adette bir bilet alımı yapıldığında toplam ücrette %10'luk bir indirim uygulanacağı anlamına gelmektedir.

