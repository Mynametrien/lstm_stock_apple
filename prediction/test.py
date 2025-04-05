import os
import pandas as pd 
# Lấy đường dẫn tuyệt đối của thư mục hiện tại
current_dir = os.path.dirname(os.path.abspath(__file__))

# Xây dựng đường dẫn tệp CSV từ thư mục hiện tại
file_path = os.path.join(current_dir, 'Apple Dataset.csv')

# Đọc tệp CSV
print(file_path)