# 베이스 이미지로 Python 3.9를 사용합니다.
FROM python:3.9

# 작업 디렉토리를 설정합니다.
WORKDIR /app

# 호스트의 requirements.txt를 컨테이너 내의 /app/requirements.txt로 복사합니다.
COPY requirements.txt .

# 필요한 패키지를 설치합니다.
RUN pip install -r requirements.txt

# 나머지 소스 코드를 컨테이너 내의 /app 디렉토리로 복사합니다.
COPY . .

# 컨테이너 내에서 장고 애플리케이션을 실행합니다.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
