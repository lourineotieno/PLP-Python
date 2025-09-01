
# Base Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

# Child Class (Inheritance from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Call parent constructor
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        return f"Calling {number} from {self.device_info()} 📞"

    def charge(self):
        return f"{self.device_info()} is charging 🔋"

# Create Objects
phone1 = Smartphone("Samsung", "Galaxy S24", "256GB", "5000mAh")
phone2 = Smartphone("Apple", "iPhone 15", "128GB", "4500mAh")

# Use Methods
print(phone1.make_call("+254700123456"))
print(phone2.charge())
