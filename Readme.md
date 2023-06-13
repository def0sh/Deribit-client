Асинхронный клиент для криптобиржи Deribit на aiohhtp.
Клиент каждую минуту забирает с биржи текущую цену BTC и ETH, после
чего сохраняет в базу данных тикер валюты, текущую цену и время.

Так же реализовано внешнее API для работы с сохраненными данными.

Стек:
FastApi , Postgres, asyncio, aiohttp

#### Установка:

```
1 Клонировать репозиторий

2 Создать .env файл в корне проекта для конфигурации Postgres

3 Запустить файл schedule.py для получения валюты каждую минуту и записи в БД

4 pip install -r requirements.txt

5 Для запуска FastApi -  uvicorn backend.main:app --reload
```



