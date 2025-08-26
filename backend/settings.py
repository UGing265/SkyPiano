INSTALLED_APPS = [
    # ...
    "rest_framework",
    "corsheaders",
    # app của bạn, ví dụ: "scores",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    # ...
]

# Cho phép web app gọi API (chỉnh domain/port thực tế của bạn)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",   # Vite
    "http://localhost:3000",   # Next.js
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}
