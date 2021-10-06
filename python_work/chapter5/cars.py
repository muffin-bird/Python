# if文
cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
	if car == "bmw":
		print(car.upper())
	else:
		print(car.title())

# True・False
car = "bmw"
print(car == "bmw")

car = "audi"
print(car == "bmw")

# 大文字・小文字
car = "Audi"
print(car == "audi")

car_name = "Audi"
print(car_name.lower() == "audi")
print(car_name)