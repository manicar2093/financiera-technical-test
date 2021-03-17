class InMemoryItem:
    """InMemoryItem representa la información que se solicita guardar en memoria"""

    def __init__(self, value, version, key):
        self.value = value
        self.version = version
        self.key = key

    def __repr__(self):
        return f"InMemoryItem<Key:'{self.key}', Value:'{self.value}', Version:{self.version}>"

    def to_dict(self):
        return {"key":self.key, "value": self.value, "version": self.version}
