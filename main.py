import os
import time
os.system("pip install PyQt5 PyQtWebEngine")
print("""
Naber bu bilalOS
""")

print("""
[1] sistemle devam et.
[2] kurdum zaten(hawli).
""")
setup = input("[?]: ")

if setup == '1':
    name = input("adını git: ")
    pas = input("şifreni gir: ")

    with open('user/username.txt', "w") as f:
        f.writelines(name)

    with open('user/password.txt', "w") as f:
        f.writelines(pas)
    print("kurdum yay!")
    time.sleep(3)
    quit()

elif setup == '2':
    try:
        with open('user/password.txt', 'r') as login_pass, open('user/username.txt', 'r') as login_name:
            l_p = login_pass.read().strip()
            l_n = login_name.read().strip()
    except FileNotFoundError:
        print("hatta: kurulum dosyalarını bulamadım. lütfen önce kurulumu yap.")
        quit()
else:
    print("yanlış cevap seçildi. bye.")
    quit()

while True:
    login = input("şifre girermisin uwu " + l_n + " kullanıcı adı: ")
    if login == l_p:
        os.startfile('second.py')
        quit()
    else:
        print("yanlış şifre AGAGĞAGĞAĞGGĞĞGAĞGĞ!")
