from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 13", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79987654321"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 10", "+79111111111"))
catalog.append(Smartphone("Huawei", "P40 Pro", "+79222222222"))
catalog.append(Smartphone("Google", "Pixel 5", "+79333333333"))

for phone in catalog:
    print(phone)
