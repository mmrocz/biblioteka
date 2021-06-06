import json


class Biblioteka:
    def __init__(self):
        try:
            with open("biblioteka.json", "r") as f:
                sortuj = json.load(f)
                self.biblioteka = sorted(sortuj, key=lambda p: p['year'])
        except FileNotFoundError:
            self.biblioteka = []

    def all(self):
        return self.biblioteka

    def get(self, id):
        book = [book for book in self.all() if book['id'] == id]
        if book:
            return book[0]
        return []

    def create(self, data):
        self.biblioteka.append(data)
        self.save_all()

    def save_all(self):
        with open("biblioteka.json", "w") as f:
            json.dump(self.biblioteka, f)

    def update(self, id, data):
        book = self.get(id)
        if book:
            index = self.biblioteka.index(book)
            self.biblioteka[index] = data
            self.save_all()
            return True
        return False

    def delete(self, id):
        book = self.get(id)
        if book:
            self.biblioteka.remove(book)
            self.save_all()
            return True
        return False


biblioteka = Biblioteka()