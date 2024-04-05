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


#### 2. Membuat app django dengan nama 'main'

        (jobportal) λ REM: Membuat app django dengan nama 'main'
        (jobportal) λ mkdir app\main
        (jobportal) λ django-admin startapp main app\main
        (jobportal) λ ls
        app/  config/  manage.py*  README.md  venv312503/

        E:\_WORKSPACE\2024\django\2466\2466-dj-job-portal(main -> origin)
        (jobportal) λ tree app/main /f
        Folder PATH listing for volume Local Disk
        Volume serial number is 0000006B 42EB:BBDC
        E:\_WORKSPACE\2024\DJANGO\2466\2466-DJ-JOB-PORTAL\APP\MAIN
        │   admin.py
        │   apps.py
        │   models.py
        │   tests.py
        │   views.py
        │   __init__.py
        │
        └───migrations
                __init__.py

        modified:   README.md
        new file:   app/main/__init__.py
        new file:   app/main/admin.py
        new file:   app/main/apps.py
        new file:   app/main/migrations/__init__.py
        new file:   app/main/models.py
        new file:   app/main/tests.py
        new file:   app/main/views.py
