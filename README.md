# UTS-python_V3922042

==penjelasan program==
1. IMPORT
import mysql lalu mengkoneksikan Python dan MySQL. berikut sintaksnya
>> import mysql.connector
>> conn = mysql.connector.connect(
    host = 'localhost', ---> nama server tempat mysql dijalankan
    user = "root",      ---> nama user untukakses mysql
    password = "")      ---> password kosong/tidak menggunakan password

  print(conn)
  print("database telah terhubung") ----> apabila mysql sudah terkoneksi maka ouypuut berupa "database telah terhubung" 
 
 2. CREATE DATABASE
 >> cursor = db.cursor() --->objek cursor mengirimkan query ke method execute
    #create database
    cursor.execute("CREATE DATABASE db_sales_V3922042")
    
3. CREATE TABLE
>> cursor = db.cursor()
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
    
=> untuk penjelasan CRUD sudah ada pada komentar di source code
