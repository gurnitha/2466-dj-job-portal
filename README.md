# 2466-dj-job-portal
Membuat aplikasi JOB PORTAL


## 1. SETUP


#### 1. Membuat remote repositori dan meng-clone-nya


#### 2. Membuat virtual environment dengan nama venv312503

        modified:   .gitignore
        modified:   README.md


#### 3. Menginstal Django versi 5.0.3

        modified:   README.md


## 2. PROYEK DAN APPS DJANGO 


#### 1. Membuat proyek django dengan nama 'config'

        (jobportal) λ REM: Membuat proyek django dengan nama 'config'

        (jobportal) λ django-admin

        ...
            dbshell
            makemigrations
            migrate
            shell
            sqlmigrate
            startapp
            startproject
        ...

        (jobportal) λ django-admin startproject config .

        (jobportal) λ tree config /f
        Folder PATH listing for volume Local Disk
        Volume serial number is 000000C3 42EB:BBDC
        E:\_WORKSPACE\2024\DJANGO\2466\2466-DJ-JOB-PORTAL\CONFIG
            asgi.py
            settings.py
            urls.py
            wsgi.py
            __init__.py

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py