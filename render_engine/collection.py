import logging
import urllib.parse
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Sequence, Type

from .helpers import PathString
from render_engine.page import Page


class Collection:
    def __init__(
        self,
        content_path: Optional[PathString] = "content",
        content_type: Type[Page] = Page,
    ):
        """initialize a collection object"""
        self.content_type = content_type
        self.content_path = Path(content_path)
        self.pages = {}
        self.includes = ["*.md", "*.html"]

    @property
    def pages(self):
        return (
                self.content_type(content_path=p)
                for i in self.includes
                for p in self.content_path.glob(i)
            )
