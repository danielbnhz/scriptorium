from dataclasses import dataclass

@dataclass
class GutenbergText:
    gutenberg_id: int
    title: str
    author: str
    language: str
    content: str
    fetched_at: str