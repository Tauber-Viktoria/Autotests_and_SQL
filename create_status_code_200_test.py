# Виктория Таубер, 10-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request

def test_create_and_get_order():
    # Создание заказа
    create_order_response = sender_stand_request.post_new_order()
    track_number = create_order_response.json()["track"]

    # Получение заказа по номеру трека
    get_order_response = sender_stand_request.get_order_track(track_number)
    assert get_order_response.status_code == 200  # Проверяем код состояния 200






