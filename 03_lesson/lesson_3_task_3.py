
from address import Address
from mailing import Mailing


address_from = Address("123456", "Москва", "Ленинградская улица", "10", "1")
address_to = Address("654321", "Санкт-Петербург", "Невская улица", "20", "2")


mailing = Mailing(address_to, address_from, 500, "TRACK-123456")


print(
    f"Отправление {mailing.track} из\n"
    f"{mailing.from_address.index}, {mailing.from_address.city},\n"
    f"{mailing.from_address.street}, {mailing.from_address.house}-\n"
    f"{mailing.from_address.apartment}\n"
    f"В {mailing.to_address.index}, {mailing.to_address.city},\n"
    f"{mailing.to_address.street}, {mailing.to_address.house}-\n"
    f"{mailing.to_address.apartment}.\n"
    f"Стоимость {mailing.cost} рублей."
)
