import subprocess
import sys

def install_libraries():
    libraries = [
        'flask',
        'sqlalchemy',
        'python-docx',
        'reportlab',
        'apscheduler',
        'flask-cors',
        'groq',
        'flask-mail',
        'flask-sqlalchemy',
        'pytz',
        'pymysql',
    ]
    
    for lib in libraries:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib])
            print(f"Successfully installed {lib}")
        except subprocess.CalledProcessError:
            print(f"Failed to install {lib}")

if __name__ == "__main__":
    install_libraries()
