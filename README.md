# AksiWebsite

### Архитектура проекта

1. **Модели (Models):**
   - **Artist**: информация обо мне (имя, биография, фото и т.д.).
   - **Track**: информация о треках (название, дата выпуска, файл, обложка и т.д.).
   - **Beat**: информация о битах (название, дата создания, файл, обложка и т.д.).

2. **Приложения (Apps):**
   - **core**: основное приложение для управления страницами сайта.
   - **music**: приложение для управления треками и битами.
   - **users**: приложение для управления пользователями (если планируется регистрация пользователей).

3. **База данных (PostgreSQL):**
   - Используй PostgreSQL для хранения данных о треках, битах и пользователях.

4. **Шаблоны (Templates):**
   - **base.html**: основной шаблон, который будет использоваться для всех страниц.
   - **index.html**: главная страница с информацией о тебе и последними треками.
   - **track_list.html**: страница со списком всех треков.
   - **beat_list.html**: страница со списком всех битов.

5. **Статические файлы (Static Files):**
   - **CSS**: стили для оформления сайта.
   - **JS**: скрипты для интерактивности.

6. **URL маршрутизация (URLs):**
   - Настрой маршруты для главной страницы, страницы треков и битов.

7. **Админка (Admin):**
   - Настрой админку для удобного управления контентом.

### Пример структуры проекта

```
aksi_website/
│
├── aksi_website/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── base/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── music/
│   ├── migrations/
│   ├── templates/
│   │   ├── beat_list.html
│   │   └── track.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── users/
│   ├── migrations/
│   ├── templates/
│   │   ├── login.html
│   │   ├── profile.html
│   │   └── fign_in.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   └── ...
│
├── README.md
├── .gitignore
├── manage.py
└── requirements.txt
```