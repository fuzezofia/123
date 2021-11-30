class cup:
    high = 0.0
    capacity = 0
    color = ""
    material = ""
    water = ""

    def deposit(self):
        print(self.color, "的", self.material, "杯子里放着", self.water)


c = cup()
c.high = 3
c.capacity = 500
c.color = "绿色"
c.material = "玻璃"
c.water = "雪碧"

c.deposit()
