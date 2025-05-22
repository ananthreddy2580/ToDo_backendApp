from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = "True"
# ALLOWED_HOSTS = ["*"]

# CORS & CSRF Setup

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# CORS_ALLOW_ALL_ORIGINS = False  # Set False for security

CSRF_COOKIE_NAME = "csrftoken"  # Name of the CSRF cookie
CSRF_COOKIE_DOMAIN = None  # Specify the domain (e.g., "example.com"). Use None for localhost.
CSRF_COOKIE_PATH = "/"  # Path for which the CSRF cookie is valid
CSRF_COOKIE_SECURE = False  # Set to True to only send the cookie over HTTPS
CSRF_COOKIE_HTTPONLY = False  # Allow JavaScript to access the cookie (False is default)
CSRF_COOKIE_SAMESITE = "Lax"  # Helps prevent CSRF attacks during cross-origin navigation (options: Lax, Strict, None)

SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SECURE = True


# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'ToDo <pythonmail17@gmail.com>'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'pythonmail17@gmail.com'  # Your gmail address
EMAIL_HOST_PASSWORD = 'ahwu ukgz dbdo igpk' # Not your

ALLOWED_HOSTS = ["*"]


CORS_ALLOW_ALL_ORIGINS = False  # Set False for security


# Allow frontend origin
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:5173",
#     "https://todo-app-9f6l.vercel.app",  # Your React frontend
# ]

# settings.py


# CSRF_COOKIE_SAMESITE = "Lax"  # or "None" for cross-domain
# CSRF_COOKIE_SECURE = False    # Only True for HTTPS
# CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOWED_ORIGINS = ["http://localhost:5173","https://todo-app-9f6l.vercel.app"]
# CSRF_TRUSTED_ORIGINS = ["http://localhost:5173","https://todo-app-9f6l.vercel.app"]

# ✅ Enable secure cookies for cross-site requests (HTTPS)
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "None"

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = "None"

# ✅ CORS settings to allow React frontend access
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "https://todo-app-9f6l.vercel.app",
    "https://todo-app-six-chi-17.vercel.app"
    "http://localhost:5173"
]

# ✅ Allow cross-origin CSRF protection
CSRF_TRUSTED_ORIGINS = [
    "https://todo-app-9f6l.vercel.app",
    "https://todo-app-six-chi-17.vercel.app"
    "http://localhost:5173"
]



# CSRF_COOKIE_SAMESITE = 'None'  # Allow cookies to be sent with cross-origin requests
# CSRF_COOKIE_SECURE = True    # Use True only with HTTPS

# Applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Todo',  # Your app
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
]

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # must be first
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# DRF & JWT Config
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


# Templates
ROOT_URLCONF = 'TodoBackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'TodoBackend.wsgi.application'

# Database (MySQL)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'todo',
#         'USER': 'root',
#         'PASSWORD': '1234',
#         'HOST': 'localhost',
#         'PORT': '3306',
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         }
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.getenv('DB_NAME', 'todo'),  # Default to 'todo' if not set
#         'USER': os.getenv('DB_USER', 'root'),  # Default to 'root' if not set
#         'PASSWORD': os.getenv('DB_PASSWORD', '1234'),  # Default to '1234' if not set
#         'HOST': os.getenv('DB_HOST', 'localhost'),  # Default to 'localhost' if not set
#         'PORT': os.getenv('DB_PORT', '3306'),  # Default to '3306' if not set
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         },
#     }
# }

from urllib.parse import urlparse

# Parse the MYSQL_URL (if it's set as an environment variable or you want to hardcode it)
mysql_url = os.getenv('MYSQL_URL', 'mysql://root:simpeiLKQRxkGZhbmNIzsZoWQeogyrjN@switchback.proxy.rlwy.net:30612/railway')
url = urlparse(mysql_url)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
    }
}




# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = 'static/'

# Auto primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
