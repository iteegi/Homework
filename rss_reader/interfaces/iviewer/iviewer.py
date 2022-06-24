from __future__ import annotations
from abc import ABC, abstractmethod


class IViewHandler(ABC):
    def set_next(self, handler: IViewHandler) -> IViewHandler:
        pass
