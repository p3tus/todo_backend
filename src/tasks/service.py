from tasks.models import Task


class TaskService:
    """
    Tasks list management service
    """

    def __init__(self):
        self.tasks: list[Task] = []
        self.next_id = 1

    def get_all(self):
        return self.tasks

    def create(self, item: Task):
        item.id = self.next_id
        self.next_id += 1
        self.tasks.append(item)
        return item


def get_one(self, item_id: int) -> Task | None:
    for item in self.tasks:
        if item.id == item_id:
            return item
    return None


def update(self, item_id: int, updated: Task) -> Task | None:
    for i, item in enumerate(self.tasks):
        if item.id == item_id:
            updated.id = item_id
            self.tasks[i] = updated
            return updated
    return None


def delete(self, item_id: int) -> bool:
    for i, item in enumerate(self.tasks):
        if item.id == item_id:
            del self.tasks[i]
            return True
    return False
