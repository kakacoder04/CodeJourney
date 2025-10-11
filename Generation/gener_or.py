import random
from datetime import datetime

# Danh sách tên tổ chức liên quan đến lập trình (hoàn toàn mới)
organization_names = [
    "Cộng đồng Lập Trình Việt Nam", "Cộng đồng Phát Triển Phần Mềm", "Hội Lập Trình Viên", "Lập Trình Sáng Tạo", 
    "Nhóm Lập Trình Cộng Đồng", "Coder's Paradise", "Lập Trình Viên Tương Lai", "Sáng Tạo Lập Trình", "Lập Trình Tiên Tiến", 
    "Cộng Đồng Coder Việt", "Tương Lai Công Nghệ", "Lập Trình Mọi Lúc Mọi Nơi", "Lập Trình Ứng Dụng", 
    "Hội Coder Việt Nam", "Cộng Đồng Lập Trình Việt", "Giải Pháp Lập Trình", "Đội Ngũ Lập Trình Viên", 
    "Lập Trình Viên Học Viện", "Cộng Đồng Lập Trình Sáng Tạo", "Cộng Đồng TechCoders", "Lập Trình Viên Cung Cấp Giải Pháp", 
    "Lập Trình Viên Toàn Cầu", "Phát Triển Phần Mềm Mới", "Tạo Ra Lập Trình Đột Phá", "Lập Trình Viên Học Hỏi", 
    "Lập Trình Công Nghệ Mới", "Cộng Đồng Phát Triển Phần Mềm", "Nhóm Lập Trình Dành Cho Người Mới", 
    "Lập Trình Viên Cải Tiến", "Cộng Đồng Phát Triển Web", "Coder Academy", "Lập Trình Viên Cộng Đồng Sáng Tạo", 
    "Cộng Đồng Lập Trình Mới", "Học Viện Lập Trình Việt", "Nhóm Coder Toàn Cầu", "Cộng Đồng Lập Trình Mobile", 
    "Coder Lab", "Lập Trình Mới Mỗi Ngày", "Đội Ngũ Lập Trình Viên Mới", "Phát Triển Công Nghệ Mới", 
    "Cộng Đồng Coder Học Viện", "Nhóm Lập Trình Viên Thực Hành", "Cộng Đồng Phát Triển Công Nghệ", 
    "Nhóm Lập Trình Viên Tương Lai", "Phát Triển Phần Mềm Thông Minh", "Lập Trình Viên Đột Phá", 
    "Cộng Đồng Phát Triển Lập Trình", "Nhóm Lập Trình Viên Chuyên Nghiệp", "Phát Triển Lập Trình Di Động", 
    "Coder X", "Nhóm Lập Trình Viên Xu Hướng", "Cộng Đồng Lập Trình Viên", "Lập Trình Viên 4.0", 
    "Cộng Đồng AI Lập Trình", "Blockchain Coder", "Lập Trình Viên Sáng Tạo", "Nhóm Coder Toàn Cầu", 
    "Lập Trình Web Mới", "Cộng Đồng Coder Quốc Tế", "Coder Network", "Lập Trình Viên Mới", "Đội Ngũ Phát Triển Phần Mềm"
]

# Mẫu mô tả tổ chức liên quan đến lập trình
organization_descriptions = [
    "Cộng đồng lập trình dành cho những người đam mê công nghệ và muốn học hỏi, chia sẻ kinh nghiệm lập trình.",
    "Nhóm lập trình viên sáng tạo, chuyên phát triển các phần mềm và ứng dụng hiện đại.",
    "Cung cấp các giải pháp lập trình tiên tiến giúp doanh nghiệp tối ưu hóa quy trình làm việc và công nghệ.",
    "Cộng đồng lập trình viên đam mê sáng tạo và đổi mới trong lĩnh vực công nghệ phần mềm.",
    "Học viện lập trình chuyên đào tạo các kỹ năng lập trình từ cơ bản đến nâng cao, đặc biệt là lập trình web và mobile.",
    "Cộng đồng lập trình viên chuyên nghiệp, luôn sáng tạo và phát triển những sản phẩm phần mềm đột phá.",
    "Đưa ra các giải pháp lập trình cho các dự án công nghệ với đội ngũ lập trình viên tài năng và sáng tạo.",
    "Chuyên cung cấp các giải pháp lập trình phần mềm dựa trên công nghệ mới nhất như trí tuệ nhân tạo, blockchain.",
    "Chúng tôi là nhóm lập trình viên đầy nhiệt huyết, chuyên nghiên cứu và phát triển các sản phẩm công nghệ tiên tiến.",
    "Cộng đồng lập trình viên đang xây dựng các phần mềm phục vụ cho việc phát triển các công ty khởi nghiệp công nghệ.",
    "Lập trình viên sáng tạo, luôn khám phá và ứng dụng công nghệ mới vào trong các dự án phần mềm hiện đại.",
    "Chúng tôi là đội ngũ lập trình viên chuyên nghiệp, cung cấp các giải pháp lập trình tối ưu cho doanh nghiệp.",
    "Nhóm lập trình viên đam mê học hỏi và phát triển công nghệ thông qua các dự án thực tế.",
    "Cung cấp các dịch vụ lập trình phần mềm chất lượng cao cho các công ty và tổ chức toàn cầu.",
    "Chuyên đào tạo và phát triển lập trình viên trong các lĩnh vực như phát triển web, ứng dụng di động và AI."
]

# Hàm tạo tổ chức ngẫu nhiên
def generate_random_organization(used_names):
    name = random.choice(organization_names)
    # Kiểm tra trùng lặp
    while name in used_names:
        name = random.choice(organization_names)
    
    used_names.add(name)  # Thêm tên vào danh sách đã sử dụng
    description = random.choice(organization_descriptions)
    org_type = 'private'  # Tất cả tổ chức là công khai (public)
    created_by = random.randint(30, 100)  # Chọn user ID ngẫu nhiên từ 600 đến 800
    return name, description, org_type, created_by

# Tạo các tổ chức ngẫu nhiên và ghi vào file SQL
def generate_sql_file(num_organizations=78, filename="lesson.sql"):
    used_names = set()  # Bộ chứa tên tổ chức đã sử dụng
    with open(filename, "w", encoding="utf-8") as f:
        for _ in range(num_organizations):
            name, description, org_type, created_by = generate_random_organization(used_names)
            # Tạo câu lệnh SQL
            sql = f"INSERT INTO organization (name, description, org_type, created_by, created_at) " \
                  f"VALUES ('{name}', '{description}', '{org_type}', {created_by}, '{datetime.utcnow()}');\n"
            f.write(sql)

# Gọi hàm để tạo 78 tổ chức và ghi vào lesson.sql
generate_sql_file(5)
