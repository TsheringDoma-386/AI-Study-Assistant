from ai.recommendation import RecommendationGenerator

coach = RecommendationGenerator()

result = coach.generate_recommendation(
    subject="Software Engineering",
    quizzes_completed=10,
    flashcards_reviewed=40,
    study_hours=8
)

print(result)