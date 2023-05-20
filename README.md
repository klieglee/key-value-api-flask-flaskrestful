# Прототип API хранилища ключ-значение
Prototype of API storage key-value

Команда для сборки контейнера: docker build -t имя_образа .

Запуск контейнера: docker run -p 5000:5000 имя_образа

Главная страница: http://127.0.0.1:5000/

Все данные: http://127.0.0.1:5000/api/v1/storage/json/all

Поиск по ключу: http://127.0.0.1:5000/api/v1/storage/json/read/key1
