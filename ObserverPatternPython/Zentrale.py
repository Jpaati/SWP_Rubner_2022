class Zentrale():
    def __init__(self) -> None:
        self.observer = []
        self.temp = 0
        self.humidity = 0

    def addObserver(self, *args):
        for ob in args:
            self.observer.append(ob)
        print("Observer added")
    
    def updateObserversPush(self, temp, humidity):
        for obs in self.observer:
            obs.notify(temp, humidity)
        print("All observers notified")
    
    def updatePull(self, temp, humidity):
        self.temp = temp
        self.humidity = humidity
        for obs in self.observer:
            obs.getInfo(self)
        print("All observers are ready for pull")

    def getTemp(self):
        return self.temp
    
    def getHum(self):
        return self.humidity

class Display1():
    def __init__(self, name) -> None:
        self.name = name

    def notify(self, temp, humidity):
        print(self.name, "got" , temp, humidity)
    
    def getInfo(self, z):
        print(self.name, "got", z.getHum(), "humidity")

class Display2():
    def __init__(self, name) -> None:
        self.name = name

    def notify(self, temp, humidity):
        print(self.name, "got" , temp, humidity)
    
    def getInfo(self, z):
        print(self.name, "got", z.getTemp() , "temperature")

def main():
    z = Zentrale()
    d1 = Display1("Observer1")
    d2 = Display2("Observer2")
    z.addObserver(d1,d2)
    z.updateObserversPush(18,20)

    print("---------------------------")

    z.updatePull(24,40)

if __name__ == '__main__':
    main()