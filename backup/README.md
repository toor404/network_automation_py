# Backup Config #
aplikasi untuk otomasi backup configuration dan kirim statusnya di telegram

aplikasi ini terdiri dari 2 file utama
1. backup_config.py ==> aplikasi pythonnya
2. listdevice.csv ==> tempat menyimpan list data device yang akan di backup config nya

# Cara Penggunaan #

# Langkah Awal Siapin Virtual Environment

python3 -m venv namaenvnya

# Cara mengaksesnya

1. Macbook / Linux

source env/bin/activate

2. Windows

venv\scrpits\activate.bat

# install requirement nya

pip install requirements.txt

# Masukan list device yang akan di backup di file listdevice.csv
formatnya
ip address,hostname,user,password,secondpassword

contoh
127.0.0.1,localhost,admin,admin123,admin321


# jalankan aplikasinya

python backup_config.py




