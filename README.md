# 🛍️ Django Store Backend

Pet-проект по созданию полнофункционального Backend'а интернет-магазина одежды с использованием современного стека технологий.

## 🚀 Особенности проекта

- ✅ Полноценный REST API для интернет-магазина
- ✅ Система управления товарами и категориями
- ✅ Управление заказами и корзиной
- ✅ Аутентификация и авторизация пользователей
- ✅ Redis кэширование для повышения производительности
- ✅ Контейнеризация с Docker
- ✅ Готов к production развертыванию

## 🛠 Технологический стек

- **Backend**: Django + Django REST Framework
- **База данных**: PostgreSQL
- **Кэширование**: Redis
- **Контейнеризация**: Docker & Docker Compose
- **Code Quality**: Flake8
- **Production**: VDS Selectel + .ru домен

## 📁 Структура проекта
```
Django-Store-Backend/
├── common/              # Общие компоненты и утилиты
├── products/            # Управление товарами и категориями
├── orders/              # Система заказов и корзины
├── users/               # Пользователи и аутентификация
├── store/               # Основные настройки Django
├── media/               # Загружаемые файлы (изображения товаров)
├── static/              # Статические файлы
├── redisdata/           # Данные Redis
├── docker-compose.yaml  # Конфигурация Docker
├── requirements.txt     # Python зависимости
└── .flake8             # Настройки линтера
```

## 🚀 Быстрый старт

### Предварительные требования

- Docker и Docker Compose
- Python 3.8+
- Git

### Установка и запуск

1. **Клонируйте репозиторий:**
```bash
git clone https://github.com/ChayannFamali/Django-Store-Backend.git
cd Django-Store-Backend
docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --noinput
```
## 🐳 Docker конфигурация

Проект использует Docker Compose со следующими сервисами:

- **web** - Django приложение
- **db** - PostgreSQL база данных
- **redis** - Redis для кэширования

## 📊 API Endpoints

### Товары (Products)
- `GET /api/products/` - Список всех товаров
- `GET /api/products/{id}/` - Детали товара
- `POST /api/products/` - Создание товара (admin)
- `PUT /api/products/{id}/` - Обновление товара (admin)
- `DELETE /api/products/{id}/` - Удаление товара (admin)

### Заказы (Orders)
- `GET /api/orders/` - Список заказов пользователя
- `POST /api/orders/` - Создание заказа
- `GET /api/orders/{id}/` - Детали заказа

### Пользователи (Users)
- `POST /api/users/register/` - Регистрация
- `POST /api/users/login/` - Авторизация
- `GET /api/users/profile/` - Профиль пользователя
- `PUT /api/users/profile/` - Обновление профиля

## 🚀 Production развертывание

Проект был успешно развернут в production с использованием:

- **VDS**: Selectel
- **Домен**: .ru домен
- **Веб-сервер**: Nginx
- **WSGI**: Gunicorn
- **SSL**: Let's Encrypt

### Основные шаги развертывания:

1. Настройка VDS сервера
2. Установка Docker и Docker Compose
3. Конфигурация Nginx как reverse proxy
4. Настройка SSL сертификатов
5. Настройка автоматических бэкапов БД

