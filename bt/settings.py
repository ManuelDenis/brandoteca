import datetime
import os
from pathlib import Path
from dotenv import load_dotenv
import django_heroku

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = str(os.getenv('SECRET_KEY'))

DEBUG = True

ALLOWED_HOSTS = ['https://brandoteca.herokuapp.com/', 'brandoteca.herokuapp.com', '127.0.0.1:8000/admin', '127.0.0.1',
                 'localhost']
CSRF_TRUSTED_ORIGINS = ['https://brandoteca.herokuapp.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'crispy_forms',
    'crispy_bootstrap5',
    'index.apps.IndexConfig',
    'brand.apps.BrandConfig',
    'contact.apps.ContactConfig',
    'articole.apps.ArticoleConfig',
    'noutati.apps.NoutatiConfig',
    'djrichtextfield',
    'ckeditor',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_http_referrer_policy.middleware.ReferrerPolicyMiddleware',
]
REFERRER_POLICY = 'origin'
ROOT_URLCONF = 'bt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'bt.wsgi.application'
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""
DATABASES = {
    'default': {
        'USER': os.getenv('USER'),
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('NAME'),
        'PASSWORD': os.getenv('PASSWORD'),
        'HOST': os.getenv('HOST'),
        'PORT': '5432',
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'width': '',
        'height': '200',
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
SITE_ID = 1
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
LOGIN_REDIRECT_URL = '/'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'

if not DEBUG:
    django_heroku.settings(locals())

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'brandoteca2023@gmail.com'

DJRICHTEXTFIELD_CONFIG = {
    'js': ['//cdn.tiny.cloud/1/cts1qwx93hp8w7y3049useqxhe835ad1tdyoimeeymx3npee/tinymce/5/tinymce.min.js'],
    'init_template': 'djrichtextfield/init/tinymce.js',
    'settings': {
        'selector': 'textarea',
        'plugins': 'paste searchreplace autolink visualchars link table charmap hr nonbreaking insertdatetime advlist lists wordcount help charmap quickbars emoticons autoresize image code',
        'menubar': 'edit view insert format tools table help',
        'toolbar': 'undo redo | bold italic underline strikethrough | link image | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist | forecolor backcolor removeformat | charmap emoticons',
        'toolbar_sticky': True,
        'quickbars_selection_toolbar': 'bold italic | quicklink h2 h3 blockquote',
        'quickbars_image_toolbar': False,
        'quickbars_insert_toolbar': False,
        'toolbar_mode': 'sliding',
        'contextmenu': 'link',
        'content_style': 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }',
        'max_height': 500,
        'branding': False,
        'image_class_list': [{'title': 'img-fluid', 'value': 'img-fluid'}],
        'smart_paste': False,
        'paste_data_images': False,
        'paste_as_text': True,
        'paste_block_drop': True,
    },
}
BRAND_TYPES = (('Brand comercial', 'Brand comercial'), ('O', 'ONG'))
FOUNDING_YEAR = (
(2023, 2023), (2022, 2022), (2021, 2021), (2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016),
(2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008),
(2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000),
(1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992),
(1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984),
(1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976),
(1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968),
(1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960),
(1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952),
(1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944),
(1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939), (1938, 1938), (1937, 1937), (1936, 1936),
(1935, 1935), (1934, 1934), (1933, 1933), (1932, 1932), (1931, 1931), (1930, 1930), (1929, 1929), (1928, 1928),
(1927, 1927), (1926, 1926), (1925, 1925), (1924, 1924), (1923, 1923), (1922, 1922), (1921, 1921), (1920, 1920),
(1919, 1919), (1918, 1918), (1917, 1917), (1916, 1916), (1915, 1915), (1914, 1914), (1913, 1913), (1912, 1912),
(1911, 1911), (1910, 1910), (1909, 1909), (1908, 1908), (1907, 1907), (1906, 1906), (1905, 1905), (1904, 1904),
(1903, 1903), (1902, 1902), (1901, 1901), (1900, 1900), (1899, 1899), (1898, 1898), (1897, 1897), (1896, 1896),
(1895, 1895), (1894, 1894), (1893, 1893), (1892, 1892), (1891, 1891), (1890, 1890), (1889, 1889), (1888, 1888),
(1887, 1887), (1886, 1886), (1885, 1885), (1884, 1884), (1883, 1883), (1882, 1882), (1881, 1881), (1880, 1880),
(1879, 1879), (1878, 1878), (1877, 1877), (1876, 1876), (1875, 1875), (1874, 1874), (1873, 1873), (1872, 1872),
(1871, 1871), (1870, 1870), (1869, 1869), (1868, 1868), (1867, 1867), (1866, 1866), (1865, 1865), (1864, 1864),
(1863, 1863), (1862, 1862), (1861, 1861), (1860, 1860), (1859, 1859), (1858, 1858), (1857, 1857), (1856, 1856),
(1855, 1855), (1854, 1854), (1853, 1853), (1852, 1852), (1851, 1851), (1850, 1850), (1849, 1849))
