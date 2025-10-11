from datetime import datetime
import random

# Hàm tạo thời gian hiện tại
def generate_date():
    return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

# Tạo file SQL
with open("user_organization.sql", "w") as file:
    file.write("INSERT INTO user_organization (user_id, organization_id, role, joined_at) VALUES\n")
    
    user_count = 20  # Số lượng user
    organization_id = 3  # Giả sử tất cả user thuộc tổ chức ID 1
    roles = ["member"]  # Vai trò có thể là 'admin' hoặc 'member'

    for i in range(3, user_count + 1):
        user_id = i  # Lấy user ID từ 1 đến 200
        role = random.choice(roles)  # Chọn ngẫu nhiên 'admin' hoặc 'member'
        joined_at = generate_date()  # Thời gian tham gia

        # Ghi dòng SQL
        file.write(f"({user_id}, {organization_id}, '{role}', '{joined_at}')")
        file.write(",\n" if i < user_count else ";\n")
