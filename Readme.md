Тестовое задание наставник Python Skypro
============
Текст задания:


>Шаг 1
>
>Создайте API эндпоинты
>
>GET /resume
>
>Схема данных
>
>status: ...
>grade:  ...
>specialty: ...
>salary: ...
>education: ...
>experience: ...
>portfolio: ...
>title: ...
>phone: ...
>email: ….
>
>
>PATCH /resume 
>
>Права только у пользователя-владельца
>
>status: ...
>grade:  ...
>specialty: ...
>salary: ...
>education: ...
>experience: ...
>portfolio: ...
>title: ...
>phone: ...
>email: ….
>
>
>Шаг 2
>Напишите тесты на эти два эндпоинта с помощью APIClient

Запуск проекта
------------

```
python -m venv env
pip install -r requiremets.txt
python manage.py migrate
python manage.py loaddata fixtures.json (добавил 1 user и 1 resume)
python mange.py runserver
```

пользователь: john

пароль : johnpassword

Тесты
------------

```
pytest
```