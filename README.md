# SkyPiano 
đây là dự án chuyển từ 1 sheet music bản đầy đủ bằng piano (có thể xài nhạc cụ khác) về format .skysheet trên trang [SkyMusic](https://sky-music.specy.app/) 

### Hướng dẫn sử dụng github hiệu quả
https://codelearn.io/sharing/git-github-tu-co-ban-den-nang-cao-p1




### Công nghệ của SkyPiano
Python: 3.12.4 \
Django: > 4.2 \
React: > 18.3 


### Hướng dẫn khởi động dự án (đừng làm nếu đang làm việc đự án đã tồn tại)
- Đối với django python
```
# tạo & kích hoạt venv (Windows dùng venv\Scripts\activate)
python -m venv .venv
source .venv/bin/activate

pip install "Django==4.2.*" djangorestframework django-cors-headers whitenoise
django-admin startproject backend .
python manage.py startapp app
```

- Đối với React
```
# ở thư mục frontend/
npm create vite@latest . -- --template react-ts
npm i
npm i axios
```

### Hướng dẫn chạy
- Backend
```
# trong /backend
# tạo & kích hoạt venv (Windows dùng venv\Scripts\activate)
python -m venv .venv
source .venv/bin/activate

# đảm bảo đang chạy venv
python manage.py migrate
python manage.py runserver 8000
# API sẽ chạy tại http://localhost:8000/api/...
```
- Frontend
```
# trong /frontend
npm run dev
# FE chạy tại http://localhost:5173 (Vite mặc định)
```

BE (Django): http://localhost:8000 \
FE (React/Vite hoặc CRA/Next): http://localhost:5173 (Vite) hoặc 3000 (CRA/Next)

