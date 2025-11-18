from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save(self, filename: str, data: bytes):
        pass

class LocalStorage(Storage):
    def save(self, filename, data):
        print(f"Saving {filename} locally.")

class CloudStorage(Storage):
    def save(self, filename, data):
        print(f"Uploading {filename} to the cloud.")

class ReadOnlyStorage(Storage):
    def save(self, filename, data):
        raise PermissionError("Cannot save in read-only mode!")  # Violates the contract

# Client
def backup(storage: Storage):
    storage.save("report.txt", b"Hello world")

# Substitution works
backup(LocalStorage())  # Works
backup(CloudStorage())  # Works
