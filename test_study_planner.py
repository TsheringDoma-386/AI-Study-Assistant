print("Hello World")

from ai.study_planner import StudyPlanner

print("Import Successful")

planner = StudyPlanner()

print("Planner Created")

plan = planner.generate_plan(
    subject="Software Engineering",
    hours=2,
    days="Monday, Wednesday, Friday",
    preferred_time="Evening"
)

print("Plan Generated")

print(plan)