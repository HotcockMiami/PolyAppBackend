# PolyAppBackend (Under heavy construction)
## Запуск приложения

```pip3 install -r requirements.txt``` 

```python manage.py migrate```

```python manage.py runserver 127.0.0.1:8000```

Опционально:

```python manage.py createsuperuser```
(Для проверки работы токена, api, админ-панель)

## Роутинг приложения
```/api/token-auth``` - получение токена (в дальнейшем его необходимо передавать в HTTP заголовке Authorization: JWT <полученный токен)

```POST /api/commentaries``` - создание категории (в body {"commentary: {"text" : "test"}})

```GET /api/commentaries``` - получение комментариев

```GET /api/commentaries/<int:pk>``` - получение определенного комментария

...

```GET/POST /api/<имя модели в мн.ч>``` - будет расписано позже, но в целом хотя бы GET запрос существуют под каждую модель в проекте

```/admin``` - Админ-панель проекта
