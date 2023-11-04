import pytest
import asyncio
import aiohttp
import sqlite3
import threading


# 1. Тест на успешное разрешение промиса
async def resolve_value():
    await asyncio.sleep(1)
    return "foo"

@pytest.mark.asyncio
async def test_resolve_promise(event_loop):
    result = await resolve_value()
    assert result == "foo"


# 2. Тест на отклонение промиса с ожидаемым исключением
async def reject_value():
    await asyncio.sleep(1)
    raise ValueError("bar")

@pytest.mark.asyncio
async def test_reject_promise(event_loop):
    with pytest.raises(ValueError) as exc_info:
        await reject_value()
    assert str(exc_info.value) == "bar"


# 3. Тест на корректный ответ от HTTP-запроса
async def fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/todos/1') as response:
            return await response.json()

@pytest.mark.asyncio
async def test_http_request(event_loop):
    data = await fetch_data()
    assert data['title'] == "delectus aut autem"


# 4. Тест на корректное добавление новой записи в базу данных SQLite
async def insert_data():
    conn = sqlite3.connect('sevenChekTesting.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS mytable (name TEXT, value INT)")
    cursor.execute("INSERT INTO mytable (name, value) VALUES ('test', 123)")
    conn.commit()
    conn.close()

@pytest.mark.asyncio
async def test_database_insert(event_loop):
    await insert_data()
    conn = sqlite3.connect('sevenChekTesting.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mytable WHERE name='test' AND value=123")
    result = cursor.fetchone()
    conn.close()
    assert result is not None


# 5. Тест на корректный результат выполнения асинхронной функции в отдельном потоке
async def async_function():
    await asyncio.sleep(1)
    return "foobar"

def run_async_function():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(async_function())
    loop.close()
    return result

def test_run_async_function(event_loop):
    result = run_async_function()
    assert result == "foobar"