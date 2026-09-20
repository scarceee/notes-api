# Notes API

Учебный REST API для управления заметками.

## Используемые технологии

- Python 3.13
- Flask
- SQLAlchemy
- SQLite
- Pytest
- Docker

## Возможности

- Создание заметок
- Получение списка заметок
- Изменение заметок
- Удаление заметок
- Фильтрация
- Пагинация
- Работа со связанными таблицами

## Структура базы данных

### User

| Поле | Тип |
|--------|--------|
| id | Integer |
| name | String |

### Category

| Поле | Тип |
|--------|--------|
| id | Integer |
| name | String |

### Note

| Поле | Тип |
|--------|--------|
| id | Integer |
| title | String |
| content | Text |
| created_at | DateTime |
| user_id | Integer |
| category_id | Integer |

## Установка

```bash
git clone <repository>
cd notes-api

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

## Запуск

```bash
python app.py
```

Сервис будет доступен по адресу:

```text
http://127.0.0.1:5000
```

## API

### Создать тестовые данные

```http
POST /seed
```

### Получить список заметок

```http
GET /notes
```

### Получить список заметок с пагинацией

```http
GET /notes?page=1&per_page=5
```

### Фильтрация по заголовку

```http
GET /notes?title=Practice
```

### Получить заметки с информацией о пользователе и категории

```http
GET /notes/details
```

### Создать заметку

```http
POST /notes
```

Пример JSON:

```json
{
    "title": "Practice",
    "content": "Finish Flask project",
    "user_id": 1,
    "category_id": 1
}
```

### Изменить заметку

```http
PUT /notes/1
```

### Удалить заметку

```http
DELETE /notes/1
```

## Тестирование

```bash
pytest
```

Пример результата:

```text
1 passed
```

## Docker

Сборка образа:

```bash
docker build -t notes-api .
```

Запуск контейнера:

```bash
docker run -p 5000:5000 notes-api
```

## Repository

https://github.com/scarceee/notes-api

## Live Demo

https://notes-api-uz9n.onrender.com