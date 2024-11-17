from abc import ABC, abstractmethod

class Transformer(ABC):
    @abstractmethod
    def serialize(self, obj):
        """"Abstract method to serialize an object"""
        pass