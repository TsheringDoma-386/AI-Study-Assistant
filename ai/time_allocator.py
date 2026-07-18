class TimeAllocator:

    def allocate_time(self, subjects):

        study_plan = []

        for subject in subjects:

            difficulty = subject["difficulty"]

            if difficulty == "Easy":
                hours = 1

            elif difficulty == "Medium":
                hours = 2

            else:
                hours = 3

            study_plan.append({
                "subject": subject["name"],
                "difficulty": difficulty,
                "recommended_hours": hours
            })

        return study_plan