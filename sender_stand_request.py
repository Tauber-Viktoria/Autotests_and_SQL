# Виктория Таубер, 10-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import data
import requests

# Создание заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
           json=data.order_body)

# Получение заказа по номеру трека
def get_order_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_PATH,
                        params={"t": track_number})

