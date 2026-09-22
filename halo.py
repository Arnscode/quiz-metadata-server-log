# SOAL 1: Inisialisasi Metadata Server Log

# Membuat metadata untuk server database produksi
prod_db_01 = {
    "server_name": "prod_db_01",
    "environment": "production",
    "server_type": "database",
    "status": "active"
}

# Membuat metadata untuk server aplikasi produksi
prod_app_01 = {
    "server_name": "prod_app_01",
    "environment": "production",
    "server_type": "application",
    "status": "active"
}

# Menampilkan metadata server
print("Metadata Server:")
print(prod_db_01)
print(prod_app_01)