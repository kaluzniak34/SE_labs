import pickle
import unittest
from datetime import datetime, timedelta

from tasks import Task, TaskManager, validate_time, User


class TestTask(unittest.TestCase):
    def test_task_initialization(self):
        name = "Sample Task"
        time = "2024-06-01 10:00:00"
        executable = "calc"
        task = Task(name, time, executable)
        self.assertEqual(task.name, name)
        self.assertEqual(task.time, time)
        self.assertEqual(task.executable, executable)
        self.assertFalse(task.completed)

    def test_is_due(self):
        past = datetime.now() - timedelta(seconds = 5)
        task = Task("name", past, "notepad")
        self.assertTrue(task.is_due())
        self.assertFalse(task.completed)

    def test_is_completed(self):
        task = Task("sample name", "2024-06-01 10:00:00", "calc")
        task.complete()
        self.assertTrue(task.completed)


class TestTaskManager(unittest.TestCase):

    def test_init_manager(self):

        task_list = [Task("sample name 2", "2024-06-01 10:00:00", "notepad")]
        manager = TaskManager(task_list)
        self.assertEqual(task_list, manager.tasks)

    def test_add_task(self):
        manager = TaskManager(tasks=[])
        manager.add_task(Task("sample name", "2024-06-01 10:00:00", "calc"))
        self.assertEqual(len(manager.tasks), 1)

    def test_task_execution(self):
        past = datetime.now() - timedelta(seconds=5)
        manager = TaskManager([Task("name", past, "")])
        manager.execute_pending_tasks()
        self.assertTrue(manager.tasks[0].completed)

    def test_future_task_is_not_executed(self):
        past = datetime.now() + timedelta(seconds=5)
        manager = TaskManager([Task("name", past, "notepad")])
        manager.execute_pending_tasks()
        self.assertFalse(manager.tasks[0].completed)

    def test_remove_task(self):
        task_list = [Task("sample name 2", "2024-06-01 10:00:00", "notepad")]
        manager = TaskManager(task_list)
        manager.remove_task(manager.tasks[0])
        self.assertEqual(task_list, manager.tasks)

    def test_save_load_empty_list(self):
        manager = TaskManager()
        file = "tasks.pkl"
        manager.save_to_file(file)
        manager2 = TaskManager()
        manager2.load_from_file(file)
        self.assertEqual(manager.tasks, manager2.tasks)

    def test_save_load_task_list(self):
        manager = TaskManager([Task("name", "2024-06-01 10:00:00", "notepad")])
        file = "tasks2.pkl"
        manager.save_to_file(file)
        manager2 = TaskManager()
        manager2.load_from_file(file)
        self.assertEqual(manager.tasks, manager2.tasks)

    def test_wrong_filename(self):
        manager = TaskManager([Task("name", "2024-06-01 10:00:00", "notepad")])
        file = "\\"
        self.assertRaises(OSError, manager.save_to_file, file)

    def test_load_from_wrong_file(self):
        manager = TaskManager()
        file = "test_task.py"
        self.assertRaises(pickle.UnpicklingError, manager.load_from_file, file)

    def test_load_from_nonexistent_file(self):
        manager = TaskManager()
        file = "thisfiledoesnotexist.pkl"
        self.assertRaises(FileNotFoundError, manager.load_from_file, file)

    def test_load_from_directory(self):
        manager = TaskManager()
        file = "."
        self.assertRaises(PermissionError, manager.load_from_file, file)



class TestTime(unittest.TestCase):
    def test_invalid_format(self):
        time = "10:00.00 01/06/24"
        self.assertRaises(ValueError, validate_time, time)

    def test_invalid_date(self):
        time = "2024-13-58 10:00:00"
        self.assertRaises(ValueError, validate_time, time)

    def test_invalid_hour(self):
        time = "2024-10-10 40:00:00"
        self.assertRaises(ValueError, validate_time, time)

    def test_non_date_string(self):
        time = "agodfsdgfkhj9"
        self.assertRaises(ValueError, validate_time, time)

    def test_correct_date(self):
        time = "2024-06-01 10:00:00"
        self.assertEqual(validate_time(time), datetime(2024, 6, 1, 10, 0, 0))

class TestUser(unittest.TestCase):
    def test_correct_password(self):
        user = User("passwd123")
        self.assertTrue(user.check_password("passwd123"))

    def test_incorrect_password(self):
        user = User("passwd123")
        self.assertFalse(user.check_password("nope"))


if __name__ == "__main__":
    unittest.main()
