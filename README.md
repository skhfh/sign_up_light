# Проект простой регистрации пользователей

### Описание
Проект разворачивается в контейнерах:
1. Форма регистрации без верстки.
2. Бэкенд, обрабатывающий POST запрос.
3. БД

---

### Технологии:
- **Backend:**
  - Python 3.9
  - Django 3.2
  - Django REST Framework 3.12
  - PostgreSQL
- **Frontend:**
  - HTML
  - JavaScript
- **Инфраструктура:**
  - Nginx
  - Docker / Docker Compose

---

### Запуск проекта:

1. Клонировать репозиторий и перейти в него:
    ```bash
    git clone git@github.com:skhfh/sign_up_light.git
    ```
    ```bash
    cd sign_up_light
    ```
2. Запустить проект с помощью Docker Compose:
    ```bash
    docker compose up --build -d
    ```
3. Выполнить миграции базы данных:
    ```bash
    docker compose exec backend python manage.py migrate
    ```
4. Перейти на страницу регистрации:
    http://localhost/sign-up/

### Автор 
[skhfh](https://github.com/skhfh) 
