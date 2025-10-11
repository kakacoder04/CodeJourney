import random
import string

# Danh sách các ngôn ngữ lập trình
languages = ['C++', 'Python', 'JavaScript', 'Java', 'Ruby', 'Swift', 'Go', 'PHP', 'SQL']

# Các chủ đề chung cho bài học
topics = ['Giới thiệu về', 'Biến và kiểu dữ liệu trong', 'Câu lệnh điều kiện trong', 'Vòng lặp trong', 'Hàm trong', 'Xử lý chuỗi trong', 'Xử lý mảng trong']

# Mẫu nội dung ngẫu nhiên
content_templates = [
    'Ngôn ngữ {lang} được sử dụng rộng rãi trong phát triển phần mềm và ứng dụng hệ thống. Nó có thể thực hiện nhiều chức năng khác nhau từ phát triển ứng dụng đến xử lý dữ liệu.',
    'Trong {lang}, bạn có thể sử dụng các kiểu dữ liệu như int, float, string và các kiểu dữ liệu phức tạp khác như mảng và đối tượng.',
    'Câu lệnh điều kiện trong {lang} cho phép bạn kiểm tra các điều kiện và thực hiện các hành động khác nhau tùy thuộc vào kết quả.',
    'Vòng lặp trong {lang} cho phép bạn thực hiện các hành động nhiều lần, rất hữu ích khi bạn cần lặp qua dãy dữ liệu hoặc thực hiện các phép toán lặp đi lặp lại.',
    'Hàm trong {lang} cho phép bạn tái sử dụng mã nguồn, giúp chương trình trở nên gọn gàng và dễ bảo trì.',
    'Xử lý chuỗi trong {lang} giúp bạn thao tác với các chuỗi văn bản, ví dụ như nối chuỗi, cắt chuỗi và tìm kiếm trong chuỗi.',
    'Xử lý mảng trong {lang} cho phép bạn làm việc với các dãy giá trị, giúp đơn giản hóa việc lưu trữ và xử lý dữ liệu.'
]

# Hàm tạo tên bài học ngẫu nhiên
def generate_random_title(language):
    topic = random.choice(topics)
    return f"{topic} {language}"

# Hàm tạo nội dung ngẫu nhiên cho bài học
def generate_random_content(language):
    template = random.choice(content_templates)
    return template.format(lang=language)

# Hàm tạo file path ngẫu nhiên (không cần sử dụng)
def generate_random_file_paths():
    return '[]'  # Không cần file, trả về mảng trống

# Tạo các bài học ngẫu nhiên và ghi vào file SQL
def generate_sql_file(num_lessons, filename="lesson.sql"):
    with open(filename, "w", encoding="utf-8") as f:
        for _ in range(num_lessons):
            language = random.choice(languages)
            title = generate_random_title(language)
            content = generate_random_content(language)
            file_paths = '[]'  # Đảm bảo là chuỗi JSON hợp lệ

            sql = f"INSERT INTO lesson (title, content, file_paths) VALUES ('{title}', '{content}', '{file_paths}');\n"
            f.write(sql)


# Tạo 300 bài học ngẫu nhiên và ghi vào lesson.sql
generate_sql_file(300)
