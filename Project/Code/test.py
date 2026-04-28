# Simple Task class definition
class Task:
	def __init__(self, name, trigger, members):
		self.name = name
		self.trigger = trigger
		self.members = members

	def __repr__(self):
		return f"Task(name={self.name!r}, trigger={self.trigger!r}, members={self.members!r})"
