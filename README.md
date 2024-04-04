# Тестовое задание UpTrader

Задание на позицию Junior Python Backend Developer.

## Запуск

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```sh
$ pip install -r requirements.txt
```

Базу данных SQLite оставлена специально


Запустите разработческий сервер

```sh
$ python3 manage.py runserver
```

На сайте имеются 3 страницы(`/products`, `/faq`, `/about`). Для каждой страницы можно сделать `свое меню в админ-панели`, и указать название меню в `html` файле. При клике на ссылку, интерфейс изменяется в зависимости от страницы

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные(не обязательные):
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)


## Цели проекта

Код написан для трудоустройства на вакасию указанную выше.
