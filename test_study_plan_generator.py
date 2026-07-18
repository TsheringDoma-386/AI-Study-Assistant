from ai.study_plan_generator import StudyPlanGenerator

planner = StudyPlanGenerator()

plan = planner.generate_plan(
    subject="Software Engineering",
    exam_date="30 September 2026",
    hours_per_day=2,
    difficulty="Hard"
)

print(plan)