from abc import ABC, abstractclassmethod
from typing import Dict
from src.domain.models import Users


class RegisterUser(ABC):
    """Interface to Register use case"""

    @abstractclassmethod
    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """Case"""

        raise Exception("Should implement method: register")
