import tkinter
ekran=tkinter.Tk()
ekran.title("BMI CALCULATOR") ## ekranı oluşturdum ve boyutlarını belirledim.
ekran.minsize(500,500)
label1=tkinter.Label(text="Kilonuzu giriniz(kg)")  ## bu kısımlarda label ve entryleri oluşturdum.
label1.pack()
gırıs1=tkinter.Entry()
gırıs1.pack()
label2=tkinter.Label(text="boyunuzu giriniz(cm)")
label2.pack()
gırıs2=tkinter.Entry()
gırıs2.pack()
def hesaplama():
    try:
     a=float(gırıs1.get()) ## alınan değerler str olduğu için stringe dönüştürdük.
     b=float(gırıs2.get())
     b=b/100 ## boyumuzu 2 basamak kaydırmak için bu yöntemi uyguladım.
     sonuc=a/b**2 ## bmı hesapladım ve bir değişkene atadım.
     if(18.5<sonuc<24.9):
        label3.config(text="BMI değeriniz={}  kilonuz normal".format(round(sonuc,2)),fg="black") ## burada ise sonuçlara göre label3 e değerler yazdırdım.
     elif(sonuc<=18.8):
        label3.config(text="BMI değeriniz={}  kilonuz standartların altında.".format(round(sonuc,2)),fg="black")
        ## round ile virgülden sonraki değeri iki basamağa yuvarladım.
     else:
        label3.config(text="BMI değeriniz={}  kilonuz standartların üstünde.".format(round(sonuc,2)),fg="black")
    except ValueError:
       label3.config(text="lütfen girilen değerlere dikkat ediniz",fg="red") ## eğer string girilirse bu kod bloğu çağrılır ve hata mesajını bize verir.

buton=tkinter.Button(text="hesaplama yap",command=hesaplama) ## button oluşturup içine hesaplama fonksiyonu verdim butona basıldığında o fonksiyonu çalıştıracak.
buton.pack()
label3=tkinter.Label()
label3.pack()
ekran.mainloop()