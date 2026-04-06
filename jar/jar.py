class Jar:
    def __init__(self, capacity=12):
        self.size = 0
        try:
            if capacity >= 0:
                self.capacity = capacity
            else:
                raise ValueError
        except:
            raise ValueError

    def __str__(self):
        return "🍪" * int(self.size)

    def deposit(self, n):
        if int(self.size) + int(n) > self.capacity:
            raise ValueError
        else:
            self.size = int(self.size) + int(n)

    def withdraw(self, n):
        if int(self.size) - int(n) < 0:
            raise ValueError
        else:
            self.size = int(self.size) - int(n)

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value


def main():
    jars = Jar()
    jars.deposit()
    print(jars)


if __name__ == "__main__":
    main()