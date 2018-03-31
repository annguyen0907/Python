# FTP
#Server thuoc FileZilla
#FTP Client
import sys
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
                print('Lenh co gia tri:\n\tup de upload file\n\tget de download file\n\tls de xem danh sach\n\texit de thoat')
                ftp_command(ftp)
                break #Exit program
        except ftplib.all_errors as e:
            print('Failed to connect !', e)


def ftp_command(ftp):
    while True:  
        command = raw_input('Nhap lenh: ')
        if command == 'up': # Upload
            try:
                filename = 'text.txt'
                file = open(filename,'r')
                ftp.storbinary('STOR'+ filename ,file)
                print('File upload thanh cong.')
                file.close()
            except ftplib.error_perm as e:
                print('Fail!!!.')
        elif command == 'get':  # Download
            try:
                filename = 'text.txt'
                file = open(filename,'wb')
                #data = file.write()
                ftp.retrbinary('RETR' + filename, file.write)
                print('File download thanh cong.')
            except ftplib.error_perm as e:  
                print('Fail!!!.')
        elif command == 'ls':  # Print directory list
            print('Directory of', ftp.pwd())
            ftp.dir()
        elif command == 'exit':  # Exit 
            ftp.quit()
            print('Goodbye!')
            break
        else:
            print('Cau lenh khong hop le ! (Hay thu lenh: up/get/ls/exit).')

print('Welcome to Python FTP')
ftp_connect()



