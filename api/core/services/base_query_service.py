from abc import ABC, abstractmethod
from typing import Sequence, TypeVar, Generic, Optional


_T = TypeVar('_T')


class QueryService(ABC, Generic[_T]):

    @abstractmethod
    def find_by_id(self, id_: int) -> Optional[_T]:
        raise NotImplementedError()

    @abstractmethod
    def findall(self) -> Sequence[_T]:
        raise NotImplementedError()
