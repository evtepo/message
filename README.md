# О сервисе
Данный сервис предназначен для создания и чтения сообщений(с учетом пагинации).

## Message API
### Документация к API:
``````
http://localhost:80/docs
``````
### Ендпоинты:
```GET http://.../api/v1/messages/``` - для получения списка сообщений;  
```POST http://.../api/v1/messages/ body = {"author": "", "text": ""}``` - для создания сообщения.

## Telegram Bot
``````
https://t.me/msgCusBot
``````
### Команды:
```/start``` - для начала работы;  
```/write``` - для создания сообщения(Ожидает от юзера текст сообщения, автор создается автоматически по имени юзера);
```/messages``` - для получения списка сообщений(Ожидает от юзера номер страницы и размер - Пример: 1 20);  
```/menu``` - для отображения списка команд.

# Запуск:
## .env файлы:  
Bot - ```./bot/config/.env.example```(Присутствует токен для тестирования);  
API - ```./message_service/config/.env.example```.  
## Поднятие контейнеров:
``````
docker compose up --build
``````
# Стек технологий

| Компонент                       | Технология                               |
|---------------------------------|------------------------------------------|
| **Фреймворк для создания API**  | [FastAPI](https://fastapi.tiangolo.com/) |
| **Веб-сервер**                  | [Nginx](https://www.nginx.com/)          |
| **База данных**                 | [MongoDB](https://www.mongodb.com/)      |
| **Фреймворк для создания бота** | [aiogram](https://docs.aiogram.dev/)     |
| **Контейнеризация**             | [Docker](https://www.docker.com/)        |


