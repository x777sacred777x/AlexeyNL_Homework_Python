from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 16", "+79123336050"),
    Smartphone("Samsung", "Galaxy S24", "+79231234567"),
    Smartphone("Tecno", "CAMON 40", "+79601234567"),
    Smartphone("Xiaomi", "Redmi Note 14", "+79371234567"),
    Smartphone("HONOR", "Magic7", "+79131234567")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
