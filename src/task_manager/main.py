# from dataclasses import dataclass


# @dataclass
# class Task:
#     title: str
#     description: str
#     priority: str = "medium"

#     VALID_PRIORITIES = ["low", "medium", "high"]


#     def __post_init__(self):

#         if self.priority not in self.VALID_PRIORITIES:
#             raise ValueError(
#                 f"Invalid priority '{self.priority}'. "
#                 f"Must be one of: {self.VALID_PRIORITIES}"
#             )
        
#     def update_priority(self, new_priority: str) -> None:
        
#         if new_priority not in self.VALID_PRIORITIES:
#             raise ValueError(
#                 f"Invalid priority '{new_priority}'. "
#                 f"Must be one of: {self.VALID_PRIORITIES}. "
#                 )
#         self.priority = new_priority


#         return None
#     def get_title(self) -> str:
#         return f"the task is called  {self.title} is a {self.description} with a priority of {self.priority} "

# task_1 = Task('Bad task', "test", "good" )
# print(task_1.get_title())


# did = "hello world\n"
# print(did * 10)

for i in range (11):
    print("hello world")