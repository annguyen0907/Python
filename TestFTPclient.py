# FTP
#Server thuoc FileZilla
#FTP Client
import ftplib
from ftplib import FTP

def ftp_connect():
    while True:
        try:
                ftp = ftplib.FTP('127.0.0.1')
                ftp.login('An','')
                print(ftp.getwelcome())
                print('Thu much hien hanh la ' +  ftp.pwd())
                #ftp.dir()
                ftp.retrlines('LIST')
                print('Lenh co gia tri:\n\tup de upload file\n\tget de download file\n\tcd de doi dir hien hanh\n\tls de xem danh sach\n\texit de thoat')
                ftp_command(ftp)
                break #Exit program
        except ftplib.all_errors as e:
            print('Failed to connect !', e)
def ftp_command(ftp):
    while True:  
        command = raw_input('Nhap lenh: ')
        if command == 'up': # Upload
            try:
                filename = raw_input('Nhap file ban muon upload: ')
                file = open(filename,'rb')
                ftp.storbinary('STOR '+ filename ,file)
                print('File upload thanh cong.')
                file.close()
            except:
                print('File khong ton tai hoac ban khong du quyen de thuc hien')
        elif command == 'get':  # Download
            try:
                filename = raw_input('Nhap file ban muon download: ')
                #file = open(filename,'wb')
                #data = file.write()
                ftp.retrbinary('RETR ' + filename, open(filename,'wb').write)
                print('File download thanh cong.')
            except:  
                print('File khong ton tai hoac ban khong du quyen de thuc hien')
        elif command == 'cd': #Doi vi tri dir
            try:
                f = raw_input('Nhap thu muc muon den: ')
                ftp.cwd(f)
                print 'Thu muc hien tai ' + ftp.pwd()
                ftp.retrlines('LIST')
            except:
                print 'Thu muc khong ton tai !'
        elif command == 'ls':  # Xuat danh sach
            print('Directory of', ftp.pwd())
            ftp.dir()
        elif command == 'exit':  # Exit 
            ftp.quit()
            print('Goodbye!')
            break
        else:
            print('Cau lenh khong hop le ! (Hay thu lenh: up/get/cd/ls/exit).')

print('Welcome to Python FTP')
ftp_connect()



