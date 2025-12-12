from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    status: str = "todo"
    deadline: str = None
