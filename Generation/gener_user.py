import random
from datetime import datetime

# Danh sách họ và tên phổ biến
first_names = ["John", "Jane", "Michael", "Emily", "Chris", "Sarah", "David", "Laura", "James", "Anna", "Robert", "Sophia", "William", "Olivia", "Daniel", "Isabella", "Matthew", "Mia", "Joseph", "Charlotte"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee"]

# Hàm tạo tên người dùng chân thật hơn
def generate_username(existing_usernames):
    while True:
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        number = random.randint(1, 99)  # Thêm số ngẫu nhiên để tránh trùng
        username = f"{first_name}.{last_name}{number}"
        if username not in existing_usernames:  # Kiểm tra trùng lặp
            existing_usernames.add(username)
            return username

# Hàm tạo email ngẫu nhiên
def generate_email(username):
    domains = ["example.com", "mail.com", "test.com", "gmail.com", "yahoo.com", "hotmail.com"]
    return username.replace('.', '').lower() + "@" + random.choice(domains)

# Hàm tạo mật khẩu ngẫu nhiên
def generate_password(length=10):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@"
    return ''.join(random.choices(chars, k=length))

# Hàm tạo JSON rỗng
def generate_empty_json():
    return "[]"

# Hàm tạo thời gian hiện tại
def generate_date():
    return datetime.utcnow().strftime('%Y-%m-%d')

# Tạo file SQL
with open("users.sql", "w") as file:
    file.write("INSERT INTO user (username, email, password, admin, avatar, slogan, points, purchase_points, "
               "problems_solved, problems_solved_today, points_earned_today, last_point_update, tasks_completed, "
               "completed_tasks, achievements, selected_frame_id) VALUES\n")
    
    existing_usernames = set()  # Tập hợp để lưu các username đã tạo
    for i in range(400):
        username = generate_username(existing_usernames)
        email = generate_email(username)
        password = generate_password()
        admin = "false"
        avatar = "/static/images/anonymous.svg"
        slogan = "NULL"
        points = random.randint(0, 700)
        purchase_points = random.randint(0, 700)
        problems_solved = random.randint(0, 1)
        problems_solved_today = random.randint(0, 1)
        points_earned_today = 0
        last_point_update = generate_date()
        tasks_completed = random.randint(0, 50)
        completed_tasks = generate_empty_json()
        achievements = generate_empty_json()
        selected_frame_id = "NULL"
        
        # Ghi dòng SQL
        file.write(
            f"('{username}', '{email}', '{password}', {admin}, '{avatar}', {slogan}, "
            f"{points}, {purchase_points}, {problems_solved}, {problems_solved_today}, {points_earned_today}, "
            f"'{last_point_update}', {tasks_completed}, '{completed_tasks}', '{achievements}', {selected_frame_id})"
        )
        file.write(",\n" if i < 399 else ";\n")
