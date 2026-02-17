class Array:
    def __init__(self, size):
        self.size = size
        self.data = [0] * size  # inisialisasi array dengan 0

    def get(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError("Index di luar batas")

    def set(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Index di luar batas")

    def get_size(self):
        return self.size

    def display(self):
        return self.data
