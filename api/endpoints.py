class Endpoints:
    create_courier = "/api/v1/courier"  # Эндпоинт для регистрации курьера
    login_courier = "/api/v1/courier/login"  # Эндпоинт для авторизации курьера
    create_order = "/api/v1/orders"  # Эндпоинт для создания заказа
    delete_courier = "/api/v1/courier/"  # Эндпоинт для удаления курьера
    get__number_courier_orders = "/api/v1/courier/:id/ordersCount"  # Получение количества заказов курьера
    finish_order = "/api/v1/orders/finish/"  # Завершение выполнения заказа
    cancel_order = "/api/v1/orders/cancel"  # Отмена существующего заказа
    get_orders_list = "/api/v1/orders"  # Получение перечня всех заказов
    accept_order_by_number = "/api/v1/orders/track"  # Получение информации о заказе по его номеру
    accept_order = "/api/v1/orders/accept/:id"  # Принятие заказа курьером
