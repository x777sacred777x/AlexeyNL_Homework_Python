from address import Address
from mailing import Mailing

to_address = Address("654000", "Новокузнецк", "Кирова", "20", "10")
from_address = Address("650000", "Кемерово", "Ленина", "12", "5")

mail = Mailing(
    to_address = to_address,
    from_address = from_address,
    cost = 700,
    track = "45005145009749"
)

print(
    f"Отправление {mail.track} из "
    f"{mail.from_address.index}, {mail.from_address.city}, "
    f"{mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} в "
    f"{mail.to_address.index}, {mail.to_address.city}, "
    f"{mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. "
    f"Стоимость {mail.cost} рублей."
)
