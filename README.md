# django_api_project

API for mobile app english learning

Инструкция по запуску:

    Из корневой папки с проектом!

        1. docker-compose build

        2. docker-compose up

        3. docker-compose run web python /code/manage.py migrate --noinput

        4. docker-compose run web python /code/manage.py createsuperuser

    Создаем пользователя админ панели

    При запросе страницы без заголовка API-KEY будет выдана 403 ошибка

    Примеры запросов при помощи библиотеки httpie:

        http GET http://localhost:8000/categories/ API-KEY:'secret_value'

        http GET http://localhost:8000/levels/ API-KEY:'secret_value'

        http GET http://localhost:8000/themes/ API-KEY:'secret_value'

        http GET http://localhost:8000/themes/1/ API-KEY:'secret_value'

        http GET http://localhost:8000/words/1/ API-KEY:'secret_value'

Приложение также развернуто на heroku по ссылке: https://shrouded-tor-10313.herokuapp.com/

Создан superuser:

Имя: u15159

Пароль: 1
