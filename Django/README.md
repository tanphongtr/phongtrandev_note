# Django
## Kiểm tra phiên bản

```bash
python -m django --version
```


# Setup dự án

```bash
django-admin startproject <project-name>
```
Hoặc
```bash
python -m django-admin startproject <project-name>
```

Thêm App vào dự án
```bash
django-admin startapp <project-name>
```


# Run server

```
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'edit---name----project.settings')
os.environ.setdefault('DJANGO_ALLOW_ASYNC_UNSAFE', 'true')

django.setup()

```

# Debug In Container

https://testdriven.io/blog/django-debugging-vs-code/#modify-managepy

