import random
import json

# Danh sách mô tả bài tập
challenge_descriptions = [
    "Nhập vào một số nguyên N. Nếu N lớn hơn 5 in ra YES, ngược lại in ra NO.",
    "Nhập vào một chuỗi và in ra chiều dài của chuỗi.",
    "Nhập vào hai số nguyên a và b, in ra tổng của chúng.",
    "Nhập vào một số nguyên N và kiểm tra xem N có phải là số nguyên tố không.",
    "Nhập vào một chuỗi, kiểm tra xem chuỗi có phải là Palindrome không.",
    "Nhập vào một số nguyên N và in ra bảng cửu chương của N.",
    "Nhập vào một số nguyên N và tính tổng các số từ 1 đến N.",
    "Nhập vào một danh sách các số và in ra giá trị lớn nhất trong danh sách.",
    "Nhập vào một số nguyên N, nếu N chia hết cho 2 in ra 'Even', ngược lại in ra 'Odd'.",
    "Nhập vào một chuỗi và in ra chuỗi này viết hoa.",
    "Nhập vào một số nguyên N và kiểm tra xem N có phải là số chính phương không.",
    "Nhập vào một chuỗi, đếm số lần xuất hiện của ký tự 'a' trong chuỗi.",
    "Nhập vào một dãy số và in ra số nhỏ nhất trong dãy.",
    "Nhập vào một số nguyên N, in ra tất cả các ước số của N.",
    "Nhập vào một chuỗi, đảo ngược chuỗi và in ra kết quả.",
    "Nhập vào một số nguyên N và in ra số Fibonacci thứ N.",
    "Nhập vào một danh sách các số và in ra số trung bình của danh sách.",
    "Nhập vào một chuỗi và kiểm tra xem chuỗi có chứa ký tự 'b' không.",
    "Nhập vào một số nguyên N, nếu N chia hết cho 3 in ra 'Fizz', chia hết cho 5 in ra 'Buzz', chia hết cả 2 in ra 'FizzBuzz'.",
    "Nhập vào một số nguyên N, in ra N! (Giai thừa của N)."
]

# Tạo testcases cho từng bài
def generate_testcases_for_challenge(description):
    if description == challenge_descriptions[0]:  # Bài 1: Kiểm tra N > 5
        testcases = [
            {"input": "3", "output": "NO", "source": "manual"},
            {"input": "7", "output": "YES", "source": "manual"},
            {"input": "5", "output": "NO", "source": "manual"},
            {"input": "10", "output": "YES", "source": "manual"}
        ]
    elif description == challenge_descriptions[1]:  # Bài 2: Chiều dài chuỗi
        testcases = [
            {"input": "hello", "output": "5", "source": "manual"},
            {"input": "abc", "output": "3", "source": "manual"},
            {"input": "a", "output": "1", "source": "manual"},
            {"input": "123456", "output": "6", "source": "manual"}
        ]
    elif description == challenge_descriptions[2]:  # Bài 3: Tổng hai số
        testcases = [
            {"input": "4 5", "output": "9", "source": "manual"},
            {"input": "10 20", "output": "30", "source": "manual"},
            {"input": "1 1", "output": "2", "source": "manual"},
            {"input": "100 200", "output": "300", "source": "manual"}
        ]
    elif description == challenge_descriptions[3]:  # Bài 4: Kiểm tra số nguyên tố
        testcases = [
            {"input": "11", "output": "YES", "source": "manual"},
            {"input": "15", "output": "NO", "source": "manual"},
            {"input": "1", "output": "NO", "source": "manual"},
            {"input": "17", "output": "YES", "source": "manual"}
        ]
    elif description == challenge_descriptions[4]:  # Bài 5: Palindrome
        testcases = [
            {"input": "madam", "output": "YES", "source": "manual"},
            {"input": "hello", "output": "NO", "source": "manual"},
            {"input": "racecar", "output": "YES", "source": "manual"},
            {"input": "world", "output": "NO", "source": "manual"}
        ]
    elif description == challenge_descriptions[5]:  # Bài 6: Bảng cửu chương
        testcases = [
            {"input": "2", "output": "2 4 6 8 10 12 14 16 18 20", "source": "manual"},
            {"input": "3", "output": "3 6 9 12 15 18 21 24 27 30", "source": "manual"},
            {"input": "5", "output": "5 10 15 20 25 30 35 40 45 50", "source": "manual"},
            {"input": "10", "output": "10 20 30 40 50 60 70 80 90 100", "source": "manual"}
        ]
    elif description == challenge_descriptions[6]:  # Bài 7: Tổng các số từ 1 đến N
        testcases = [
            {"input": "3", "output": "6", "source": "manual"},
            {"input": "5", "output": "15", "source": "manual"},
            {"input": "10", "output": "55", "source": "manual"},
            {"input": "1", "output": "1", "source": "manual"}
        ]
    elif description == challenge_descriptions[7]:  # Bài 8: Số lớn nhất trong danh sách
        testcases = [
            {"input": "1 2 3 4 5", "output": "5", "source": "manual"},
            {"input": "10 2 30 8", "output": "30", "source": "manual"},
            {"input": "100 200 300 400", "output": "400", "source": "manual"},
            {"input": "5 15 25", "output": "25", "source": "manual"}
        ]
    elif description == challenge_descriptions[8]:  # Bài 9: Kiểm tra số chẵn hoặc lẻ
        testcases = [
            {"input": "4", "output": "Even", "source": "manual"},
            {"input": "7", "output": "Odd", "source": "manual"},
            {"input": "8", "output": "Even", "source": "manual"},
            {"input": "15", "output": "Odd", "source": "manual"}
        ]
    elif description == challenge_descriptions[9]:  # Bài 10: Viết hoa chuỗi
        testcases = [
            {"input": "hello", "output": "HELLO", "source": "manual"},
            {"input": "world", "output": "WORLD", "source": "manual"},
            {"input": "python", "output": "PYTHON", "source": "manual"},
            {"input": "test", "output": "TEST", "source": "manual"}
        ]
    elif description == challenge_descriptions[10]:  # Bài 11: Kiểm tra số chính phương
        testcases = [
            {"input": "16", "output": "YES", "source": "manual"},
            {"input": "20", "output": "NO", "source": "manual"},
            {"input": "25", "output": "YES", "source": "manual"},
            {"input": "10", "output": "NO", "source": "manual"}
        ]
    elif description == challenge_descriptions[11]:  # Bài 12: Đếm ký tự 'a' trong chuỗi
        testcases = [
            {"input": "banana", "output": "3", "source": "manual"},
            {"input": "apple", "output": "1", "source": "manual"},
            {"input": "abcabc", "output": "2", "source": "manual"},
            {"input": "abcdef", "output": "1", "source": "manual"}
        ]
    elif description == challenge_descriptions[12]:  # Bài 13: Số nhỏ nhất trong dãy
        testcases = [
            {"input": "1 2 3 4 5", "output": "1", "source": "manual"},
            {"input": "10 20 5", "output": "5", "source": "manual"},
            {"input": "30 10 50", "output": "10", "source": "manual"},
            {"input": "100 1 0", "output": "0", "source": "manual"}
        ]
    elif description == challenge_descriptions[13]:  # Bài 14: Các ước số của N
        testcases = [
            {"input": "6", "output": "1 2 3 6", "source": "manual"},
            {"input": "12", "output": "1 2 3 4 6 12", "source": "manual"},
            {"input": "15", "output": "1 3 5 15", "source": "manual"},
            {"input": "28", "output": "1 2 4 7 14 28", "source": "manual"}
        ]
    elif description == challenge_descriptions[14]:  # Bài 15: Đảo ngược chuỗi
        testcases = [
            {"input": "hello", "output": "olleh", "source": "manual"},
            {"input": "world", "output": "dlrow", "source": "manual"},
            {"input": "python", "output": "nohtyp", "source": "manual"},
            {"input": "test", "output": "tset", "source": "manual"}
        ]
    elif description == challenge_descriptions[15]:  # Bài 16: Fibonacci
        testcases = [
            {"input": "5", "output": "5", "source": "manual"},
            {"input": "10", "output": "55", "source": "manual"},
            {"input": "0", "output": "0", "source": "manual"},
            {"input": "1", "output": "1", "source": "manual"}
        ]
    elif description == challenge_descriptions[16]:  # Bài 17: Trung bình các số
        testcases = [
            {"input": "1 2 3 4 5", "output": "3", "source": "manual"},
            {"input": "10 20 30", "output": "20", "source": "manual"},
            {"input": "15 25", "output": "20", "source": "manual"},
            {"input": "100 200 300 400 500", "output": "300", "source": "manual"}
        ]
    elif description == challenge_descriptions[17]:  # Bài 18: Kiểm tra chứa ký tự 'b'
        testcases = [
            {"input": "banana", "output": "YES", "source": "manual"},
            {"input": "apple", "output": "NO", "source": "manual"},
            {"input": "boat", "output": "YES", "source": "manual"},
            {"input": "orange", "output": "NO", "source": "manual"}
        ]
    elif description == challenge_descriptions[18]:  # Bài 19: FizzBuzz
        testcases = [
            {"input": "3", "output": "Fizz", "source": "manual"},
            {"input": "5", "output": "Buzz", "source": "manual"},
            {"input": "15", "output": "FizzBuzz", "source": "manual"},
            {"input": "4", "output": "4", "source": "manual"}
        ]
    elif description == challenge_descriptions[19]:  # Bài 20: Giai thừa
        testcases = [
            {"input": "3", "output": "6", "source": "manual"},
            {"input": "5", "output": "120", "source": "manual"},
            {"input": "0", "output": "1", "source": "manual"},
            {"input": "4", "output": "24", "source": "manual"}
        ]
    return json.dumps(testcases)

# Hàm tạo các bài tập ngẫu nhiên
def generate_challenges(num_challenges=20):
    challenges = []
    for i in range(num_challenges):
        description = random.choice(challenge_descriptions)
        testcases = generate_testcases_for_challenge(description)  # Tạo testcases cho từng bài
        challenges.append(f"INSERT INTO challenge (description, testcases) VALUES ('{description}', '{testcases}');\n")
    return challenges

# Ghi các bài tập vào file SQL
def generate_sql_file_for_challenges(filename="challenges.sql"):
    challenges = generate_challenges()
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(challenges)

# Gọi hàm để tạo 20 bài tập và ghi vào challenges.sql
generate_sql_file_for_challenges()
