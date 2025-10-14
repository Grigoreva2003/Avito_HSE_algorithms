class HashTable:
    """Простая реализация хеш-таблицы с разрешением коллизий методом цепочек (separate chaining)."""

    def __init__(self, capacity=8, load_factor=0.75):
        self.capacity = capacity          # текущая вместимость
        self.size = 0                     # количество элементов
        self.load_factor = load_factor    # степень заполненности
        self.buckets = [[] for _ in range(self.capacity)]  # список списков (цепочек)

    def _hash(self, key):
        """Простая хеш-функция."""
        return hash(key) % self.capacity

    def _resize(self):
        """Увеличивает размер таблицы, если нагрузка превышает load_factor."""
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self.insert(key, value)

    def insert(self, key, value):
        """Добавляет или обновляет элемент по ключу."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1

        # Проверяем, не нужно ли расширить таблицу
        if self.size / self.capacity > self.load_factor:
            self._resize()

    def get(self, key):
        """Возвращает значение по ключу, или None, если ключ не найден."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        """Удаляет элемент по ключу, если он существует."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def __len__(self):
        return self.size

    def __contains__(self, key):
        return self.get(key) is not None

    def __repr__(self):
        items = [f"{k}: {v}" for bucket in self.buckets for k, v in bucket]
        return "{" + ", ".join(items) + "}"
