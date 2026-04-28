import unittest
from test import Task

class TestTask(unittest.TestCase):
    def test_task_initialization(self):
        name = "Sample Task"
        trigger = "on_event"
        members = ["Alice", "Bob"]
        task = Task(name, trigger, members)
        self.assertEqual(task.name, name)
        self.assertEqual(task.trigger, trigger)
        self.assertEqual(task.members, members)

if __name__ == "__main__":
    unittest.main()
