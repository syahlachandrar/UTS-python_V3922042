#!/usr/bin/env python
# coding: utf-8

# In[1]:


#koneksi database
import mysql.connector

#conec dari server
conn = mysql.connector.connect(
    host = 'localhost', 
    user = "root", 
    password = "")

print(conn)
print("database telah terhubung")

#disconec dr server
conn.close()


# In[3]:


#membuat database
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="")

cursor = db.cursor()
#create database
cursor.execute("CREATE DATABASE db_sales_V3922042")

print("Database berhasil dibuat!")

#disconec
db.close()


# In[5]:


#membuat table data stok di database
import mysql.connector


db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
    database="db_sales_V3922042")

cursor = db.cursor()
sql = """CREATE TABLE stok_barang (id_barang VARCHAR(10) PRIMARY KEY,
  nama_barang VARCHAR(255),
  harga_barang INT,
  stok_awal INT,
  barang_in INT,
  barang_out INT,
  stok_akhir INT
)
"""
cursor.execute(sql)

print("Tabel stok_barang berhasil dibuat!")


# In[1]:


#membuat menu crud
import mysql.connector

#Koneksi database
dataBase = mysql.connector.connect(
    user = 'root',
    host = 'localhost',
    database = 'db_sales_V3922042'
)

cursorObject = dataBase.cursor()

#tambah data
def insert_data( id_barang, nama_barang, harga_barang, stok_awal, barang_in, barang_out, stok_akhir ):
    sql = "INSERT INTO stok_barang (id_barang, nama_barang, harga_barang, stok_awal, barang_in, barang_out, stok_akhir)    VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (id_barang, nama_barang, harga_barang, stok_awal, barang_in, barang_out, stok_akhir)
    
    cursorObject.execute(sql, val)
    dataBase.commit()

    print(" ")
    print("Data berhasil ditambahkan")

#menampilkan data
def show_data():
    query = "SELECT * FROM stok_barang"
    
    cursorObject.execute(query)

    myresult = cursorObject.fetchall()

    for x in myresult:
        print(x)
        
    print(" ")
    print("Data berhasil ditampilkan")

#update data
def update_data(id_barang, nama_barang, harga_barang, stok_awal, barang_in, barang_out, stok_akhir):
    #mengedit data
    sql = "UPDATE stok_barang SET nama_barang = %s, harga_barang = %s, stok_awal = %s, barang_in = %s, barang_out = %s, stok_akhir = %s WHERE id_barang = %s"
    val = (nama_barang, harga_barang, stok_awal, barang_in, barang_out, stok_akhir, id_barang)
    
    cursorObject.execute(sql, val)
    dataBase.commit()
    
    print(" ")
    print("Data berhasil diupdate")

#hapus data
def delete_data(Id_Barang):
    sql = "DELETE FROM stok_barang WHERE id_barang = %s" #menghapus data dari table
    val = (id_barang,)
    
    cursorObject.execute(sql, val)
    dataBase.commit()
    
    print(" ")
    print("Data berhasil dihapus")

#mencari data 
def search_data(id_barang):
    sql = "SELECT * FROM stok_barang WHERE id_barang = %s" #menampilkan data dengan id barang sebagai keyword
    val = (id_barang,)
    
    cursorObject.execute(sql, val)
    
    myresult = cursorObject.fetchall()
    
    for x in myresult:
        print(x)
        
    print(" ")
    print("Data berhasil dicari")

#opssi menu crud
while True:
    print(" ")
    print("=== APLIKASI DATABASE PYTHON ===")
    print("1. Insert data")
    print("2. Show data")
    print("3. Update data")
    print("4. Hapus data")
    print("5. Cari data")
    print("6. Keluar")
    print("-------------------")
    menu = input("Pilih menu> ") #input untuk pilihan menu yang akan dicari
    print(" ")

    #pilihan 1 "insert data"
    if menu == "1":
        id_barang = input("Masukkan id barang : ")
        nama_barang = input("Masukkan nama barang : ")
        harga_barang = int(input("Masukkan harga barang : "))
        stok_awal = int(input("Masukkan stok awal : "))
        barang_in = int(input("Masukkan barang masuk : "))
        barang_out = int(input("Masukkan barang keluar : "))
        
        #Rumus untuk mencari stok_akhir
        stok_akhir = stok_awal + barang_in - barang_out
        
        #mencetak Stok_Akhir dari rumus sebelumnya
        print("stok akhir : ", stok_akhir)
        
        insert_data(id_barang, nama_barang, harga_barang, stok_awal, barang_in, barang_out, stok_akhir)
    
    #pilihan 2 "show data"
    elif menu == "2":
        show_data()

    #pilihan 3 "update data"
    elif menu == "3":
        id_barang = input("Masukkan id barang yang akan diupdate : ")
        nama_barang = input("Masukkan nama barang baru : ")
        harga_barang = int(input("Masukkan harga barang baru : "))
        stok_awal = int(input("Masukkan stok awal baru : "))
        barang_in = int(input("Masukkan barang masuk baru : "))
        barang_out = int(input("Masukkan barang keluar baru : "))
        
        stok_akhir = stok_awal + barang_in - barang_out
        print("stok akhir setelah diupdate : ", stok_akhir)
        
        update_data(id_barang, nama_barang, harga_barang, stok_awal, barang_in, barang_out, stok_akhir)

    #pilihan 4 "hapus data"
    elif menu == "4":
        id_barang = input("Masukkan id barang yang ingin dihapus : ")
        
        delete_data(id_barang)

    #pilihan 5 "cari data"
    elif menu == "5":
        id_barang = input("Masukkan id barang yang ingin dicari : ")
        
        search_data(id_barang)

    #pilihan 6 "keluar dari program"
    elif menu == "6":
        print("Terima kasih sudah menggunakan Aplikasi ini, HAVE A NICE DAYY ;)")
        break

    #ketika menginputkan tidak sesuai dengan pilihan yang tertera
    else:
        print("Pilihan anda tidak valid, Mohon coba lagi dan pilihlah dengan benar")


# In[ ]:





# In[ ]:




