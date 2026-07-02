import os

# Получаем переменную окружения. 
# Если она не задана, будет использовано значение по умолчанию ('development').
app_env = os.getenv('APP_ENV', 'development')

# Получаем обязательную переменную. 
# Если она не задана, функция вернет None.
database_url = os.getenv('DATABASE_URL')  # should be SECRET_ENVIRONMENT_VARIABLE

def main():
    print(f"Запуск приложения в режиме: {app_env}")
    
    # Проверяем, задана ли обязательная переменная
    if not database_url:
        print("Ошибка: переменная окружения DATABASE_URL не установлена.")
        return
        
    # Используем переменную в коде (имитация подключения)
    print(f"Подключение к базе данных по адресу: {database_url}")

if __name__ == '__main__':
    main()
