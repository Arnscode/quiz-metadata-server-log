# SOAL 1: Inisialisasi Metadata Server Log

# Nama server production database
server_name: str = "prod-db-01"

# Nomor port yang digunakan oleh server database
port_number: int = 5432

# Persentase beban CPU server
cpu_load: float = 78.45

# Menunjukkan apakah server dalam kondisi sehat
is_healthy: bool = True

# Pesan error terakhir, None berarti belum ada error
last_error: str | None = None

print(server_name)
print(port_number)
print(cpu_load)
print(is_healthy)
print(last_error)