import re
from datetime import datetime
from functools import wraps

class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, nilai):
        self._username = nilai

    @property
    def password(self,):
        return self._password

    @password.setter
    def password(self, nilai):
        self._password = nilai

    @staticmethod
    def validasi_username(username):
         return re.fullmatch(r'[a-zA-Z0-9]{5,}', username) is not None
    @staticmethod
    def validasi_password(password):
        return re.fullmatch(r'(?=.*\d).{8,}', password) is not None

def audit_log(fungsi):
    @wraps(fungsi)
    def wrapper(username, password, akun):
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        berhasil, alasan = fungsi(username, password, akun)

        status = "BERHASIL" if berhasil else "DITOLAK"

        catatan = (
            f"[{waktu}] - Username: {username} | "
            f"Status: {status} | keteerangan: {alasan}"
        )

        print(catatan)

        with open("audit.log", "a", encoding="utf-8") as file:
            file.write(catatan + "\n")

        return berhasil
    
    return wrapper

@audit_log
def login(username, password, akun):
    if not user.validasi_username(username):
        return False, "Username tidak valid"

    if not user.validasi_password(password):
        if len(password) < 8:
            return False, "Password harus memiliki minimal 8 karakter"
        return False, "Password harus mengandung angka"

    if username != akun.username:
        return False, "Username tidak terdaftar"
    
    if password != akun.password:
        return False, "Password salah"

    return True, "Login berhasil"

if __name__=="__main__":
    akun = user("Mork1212", "PERIA_WR_100%")

    print("===Sistem keamanan login===")

    print("\n1. Username tidak valid")
    login("Mork@1212", "PERIA_WR_100%", akun)

    print("\n2. Password terlalu pendek")
    login("Mork1212", "abc12", akun)

    print("\n3. Password tidak mengandung angka")
    login("Mork1212", "PERIASOLO", akun)

    print("\n4. Login berhasil")
    login("Mork1212", "PERIA_WR_100%", akun)