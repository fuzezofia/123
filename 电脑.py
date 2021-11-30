class Computer :
    screen = 0
    Price = 0
    cpu = ''
    memory = ''
    time = 0

    def typing(self):
        print("使用电脑打字中......")
    def game(self,gamename):
        print("使用电脑玩",gamename,"")
    def Video(self,video):
        print("使用电脑观看",video)

c = Computer()
c.screen = 32
c.price = 8888
c.cpu = 'i7 7700'
c.memory = '8G'
c.time = 24

c.typing()
c.game("战地5")
c.Video("黑客帝国")