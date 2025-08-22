# settings.py

from pathlib import Path
from decouple import config, Csv
import dj_database_url

# Caminho base
BASE_DIR = Path(__file__).resolve().parent.parent

# ========================
# Segurança / Debug
# ========================
SECRET_KEY = config('SECRET_KEY') 
DEBUG = config('DEBUG', default=False, cast=bool)

# <-- MUDANÇA: Forma correta e limpa de ler os hosts a partir das variáveis de ambiente
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# ========================
# Apps instalados
# ========================
INSTALLED_APPS = [
    'tessera.apps.TesseraConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# ========================
# Middleware
# ========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

# ========================
# Templates
# ========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# ========================
# Banco de Dados
# ========================
# <-- MELHORIA: Usa a variável DATABASE_URL fornecida pelo Railway. É muito mais simples!
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

# ========================
# Validação de senha
# ========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ========================
# Internacionalização
# ========================
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# ========================
# Arquivos estáticos / mídia
# ========================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
# <-- MELHORIA: Otimiza o WhiteNoise para servir arquivos comprimidos, melhorando a performance
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
