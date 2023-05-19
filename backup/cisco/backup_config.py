import getpass
import sys
import os
import csv
import subprocess
import paramiko
import time
import datetime


f = open('listdevice.csv', 'r')
reader = csv.reader(f)
berhasil = []
gagal = []
for row in reader:
    try:
        ip=row[0]
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn = ssh.connect(ip,username=row[2],password=row[3], timeout=10)
        print("Success login to {}".format(row[1]))
        conn = ssh.invoke_shell()
        time.sleep(1)
        conn.send("enable\n")
        conn.send(row[4])
        conn.send("\n")
        time.sleep(1)		
        conn.send("show run\n")
        #conn.send(100*spasi)
        time.sleep(2)
        output = conn.recv(65535)
        output_decode = output.decode()
        #print(output_decode)
        ssh.close()
        print("Berhasil Ambil Konfigurasi : ",ip)
        berhasil.append(ip)
        saveoutput = open("backup-" + row[1] + "_" + ip, "w")
        saveoutput.write(output_decode)
        saveoutput.close
    except Exception as e:
        print("Gagal Ambil Konfigurasi : ",ip," Dengan Error : ",e)
        gagal.append(ip)
        pass
    

x = datetime.datetime.now()
bulan = (x.strftime("%B"))
pesan_berhasil = "Device yang berhasil di Konfigurasi di bulan "+bulan+" Sebanyak "+str(len(berhasil))+" Device Berikut listnya -->" + str(berhasil)
pesan_gagal = "Device yang gagal di Konfigurasi di bulan "+bulan+" Sebanyak "+str(len(gagal))+" Device Berikut listnya -->" + str(gagal)


print(pesan_berhasil)
print(pesan_gagal)

