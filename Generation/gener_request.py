import random

# Hàm tạo các join request ngẫu nhiên
def generate_join_requests(num_requests=10, organization_id=3):
    requests = []
    for _ in range(num_requests):
        user_id = random.randint(30, 100)  # Chọn user_id ngẫu nhiên từ 600 đến 800
        status = random.choice(['pending'])  # Trạng thái ngẫu nhiên
        requests.append(f"INSERT INTO join_request (user_id, organization_id, status) VALUES ({user_id}, {organization_id}, '{status}');\n")
    return requests

# Ghi các câu lệnh SQL vào file
def generate_sql_file_for_join_requests(filename="join_requests.sql"):
    join_requests = generate_join_requests()
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(join_requests)

# Gọi hàm để tạo 100 join requests và ghi vào join_requests.sql
generate_sql_file_for_join_requests()
