from abc import ABC, abstractmethod

# Интерфейс устройства (Implementor)
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
    @abstractmethod
    def set_state(self, state):
        pass

# Конкретные устройства
class TV(Device):
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False
        self.channel = None
    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} TV включен")
    def turn_off(self):
        self.is_on = False
        print(f"{self.brand} TV выключен")
    def set_state(self, state):
        self.channel = state
        print(f"{self.brand} TV переключен на канал {state}")

class Light(Device):
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False
        self.brightness = None
    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} Light включен")
    def turn_off(self):
        self.is_on = False
        print(f"{self.brand} Light выключен")
    def set_state(self, state):
        self.brightness = state
        print(f"{self.brand} Light яркость установлена на {state}")

# Конкретные производители
class SonyTV(TV):
    def __init__(self):
        super().__init__("Sony")
class SamsungTV(TV):
    def __init__(self):
        super().__init__("Samsung")
class PhilipsLight(Light):
    def __init__(self):
        super().__init__("Philips")
class IKEALight(Light):
    def __init__(self):
        super().__init__("IKEA")

# Абстракция пульта управления (Abstraction)
class RemoteControl:
    def __init__(self, device: Device):
        self.device = device
    def turn_on(self):
        self.device.turn_on()
    def turn_off(self):
        self.device.turn_off()
    def set_state(self, state):
        self.device.set_state(state)

# Клиентский код
def main():
    sony_tv = SonyTV()
    samsung_tv = SamsungTV()
    philips_light = PhilipsLight()
    ikea_light = IKEALight()

    remote_for_sony = RemoteControl(sony_tv)
    remote_for_samsung = RemoteControl(samsung_tv)
    remote_for_philips = RemoteControl(philips_light)
    remote_for_ikea = RemoteControl(ikea_light)

    remote_for_sony.turn_on()
    remote_for_sony.set_state("HBO")
    remote_for_sony.turn_off()

    remote_for_samsung.turn_on()
    remote_for_samsung.set_state("CNN")
    remote_for_samsung.turn_off()

    remote_for_philips.turn_on()
    remote_for_philips.set_state("75%")
    remote_for_philips.turn_off()

    remote_for_ikea.turn_on()
    remote_for_ikea.set_state("50%")
    remote_for_ikea.turn_off()

if __name__ == "__main__":
    main()
