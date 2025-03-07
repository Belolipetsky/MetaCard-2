# Пока интеграция с Google Sheets не требуется для MVP,
# здесь реализованы заглушки для функций логирования.

def save_user(user_id, username, name, phone):
    # Здесь должен быть код для сохранения пользователя в Google Sheets.
    # Пока логгирование отключено для MVP.
    print(f"[DB] User saved: {user_id}, {username}, {name}, {phone}")

def update_user_attempts(user_id, attempts):
    # Здесь должен быть код для обновления баланса попыток пользователя.
    print(f"[DB] Updated attempts for user {user_id}: {attempts}")
