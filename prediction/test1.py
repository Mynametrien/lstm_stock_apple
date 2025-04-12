import sqlite3

# Kết nối tới cơ sở dữ liệu SQLite (nếu cơ sở dữ liệu không tồn tại, nó sẽ được tạo tự động)
connection = sqlite3.connect('example.db')  # Đường dẫn đến file cơ sở dữ liệu SQLite

# Tạo một đối tượng cursor để thực thi các lệnh SQL
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL
)
""")

connection.commit()


# Đóng kết nối
cursor.close()
connection.close()
