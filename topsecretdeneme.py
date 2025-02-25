import tkinter
from tkinter import messagebox
import base64
ekran=tkinter.Tk()
ekran.minsize(800,800)
ekran.title("Top Secret Project")  ## burada tkinter ekranını oluşturduk ve ardından padx ve pady ile altında bir miktar boşluk bıraktık.
ekran.config(padx=20,pady=20)
FONT="Arial",20,"normal"
resım=tkinter.PhotoImage(file="topsecret.png")  ## resmimizi png formatında bir değişkene atadık ve ardından ise bir label içine yerleştirdik.
fotolabel=tkinter.Label(image=resım)
fotolabel.pack()

def encode(key, clear):   ## girilen içeriği şifrelemek için bir encode fonksiyonu yazdım. içine şifre ve ıçeriğimizi alıyor.
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):  ## burada ise textimizden şifrelenmiş içeriği alıp anahtar yardımıyla şifresini çözmek adına decode fonksiyonu yazdım.
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def sıfrele():
    adı=adgırıs.get()
    ıcerık=gızlııcerık.get("1.0",tkinter.END)  ## girilen tüm değerleri bir değişkene atadım.
    sıfre=sıfregırıs.get()
    if len(adı)==0 or len(ıcerık)==0 or len(sıfre)==0:  ## eğer boş bırakılan alan varsa uyarı vermesi için messagebox kullandım.
        messagebox.showinfo(title="!! UYARI !!",message="boş alan bırakmayınız..")
    else:
        sıfrelııcerık=encode(sıfre,ıcerık) ## içeriğimizi şifreli bir şekilde bir değişkene atadım.
        try:
            with open("TopSecret.txt","a") as file:  ## ardından ise bir metin belgesi oluşturup içine dosya adını ve şifreli içeriği yazdırdım.
                file.write(f"\n{adı} \n {sıfrelııcerık}")
        finally:
            adgırıs.delete(0,tkinter.END)
            gızlııcerık.delete("1.0",tkinter.END)  ## her şeyi temizledim.
            sıfregırıs.delete(0,tkinter.END)

def sıfrecoz():
    ıcerık=gızlııcerık.get("1.0",tkinter.END)  ## şifreli içerik ve yeni girilen şifreyi değişkenlere atadım.
    sıfrenız=sıfregırıs.get() ## buradaki içerik şifrelenmiş olarak dosyada verilen hard dizinidir. oradan kopyalayıp text kısmın yapıştırmalıyız.
    if len(ıcerık)==0 or len(sıfrenız)==0:  ## boş kısım olursa hata mesajı verecek bir satır ekledim.
        messagebox.showinfo(title="!! UYARI !!",message="boş alan bırakmayınız")
    else:
        cozulenıcerık=decode(sıfrenız,ıcerık)  ## eğer girilen şifre bir önceki ile uyuyorsa text kısmı temizlenip şifresi çözülmüş içeriğimiz yazıcak.
        gızlııcerık.delete("1.0",tkinter.END)
        gızlııcerık.insert("1.0",cozulenıcerık)

labelad=tkinter.Label(text="dosya adını giriniz",font=FONT)
labelad.pack()
adgırıs=tkinter.Entry()
adgırıs.pack()
labelıcerık=tkinter.Label(text="gizlenecek içeriği giriniz",font=FONT)  ## buralarda ise labellar,buttonlar,entry ve text kısımlarını oluşturdum.
labelıcerık.pack()
gızlııcerık=tkinter.Text(width=50,height=30)
gızlııcerık.pack()
labelsıfre=tkinter.Label(text="şifre girişi",font=FONT)
labelsıfre.pack()
sıfregırıs=tkinter.Entry()
sıfregırıs.pack()
buton1=tkinter.Button(text="kaydet ve şifrele",command=sıfrele)
buton1.pack()
buton2=tkinter.Button(text="şifre çöz ve göster",command=sıfrecoz)
buton2.pack()
adgırıs.focus() ## imleci buradan başlatmak adına focusladım.


ekran.mainloop()
