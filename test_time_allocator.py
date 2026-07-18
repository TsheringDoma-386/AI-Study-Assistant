from ai.time_allocator import TimeAllocator

subjects = [
    {"name": "Software Engineering", "difficulty": "Hard"},
    {"name": "Python", "difficulty": "Medium"},
    {"name": "DBMS", "difficulty": "Easy"}
]

allocator = TimeAllocator()

plan = allocator.allocate_time(subjects)

for item in plan:
    print(item)