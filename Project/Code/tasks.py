from datetime import datetime
import os
import time

def validate_time(time):
	return datetime.strptime(time, "%Y-%m-%d %H:%M:%S")

class Task:
	def __init__(self, name, time, executable):
		self.name = name
		self.time = time
		self.executable = executable
		self.completed = False

	def __repr__(self):
		return f"Task(name={self.name!r}, time={self.time!r}, executable={self.executable!r}, completed={self.completed!r})"

	def is_due(self):
		now = datetime.now()
		return now >= self.time

	def complete(self):
		os.system(self.executable)
		self.completed = True

class TaskManager:
	def __init__(self, tasks=None):
		self.tasks = tasks

	def add_task(self, task):
		self.tasks.append(task)

	def execute_pending_tasks(self):
		any_completed = False
		for task in self.tasks:
			if task.is_due() and not task.completed:
				task.complete()
				any_completed = True
		
		return any_completed

	def remove_task(self, task):
		self.tasks.remove(task)

	def save_to_file(self, path):
		raise NameError

	def load_from_file(self, path):
		raise NameError

class User:
	def __init__(self, password):
		self.password = password

	def check_password(self, password):
		return self.password == password
