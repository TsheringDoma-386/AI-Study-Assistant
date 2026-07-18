class BreakOptimizer:

    def generate_schedule(self, total_hours):

        schedule = []

        total_minutes = total_hours * 60
        studied = 0

        while studied < total_minutes:

            study_time = min(50, total_minutes - studied)

            schedule.append({
                "activity": "Study",
                "minutes": study_time
            })

            studied += study_time

            if studied < total_minutes:

                break_time = 10

                if studied % 120 == 0:
                    break_time = 30

                schedule.append({
                    "activity": "Break",
                    "minutes": break_time
                })

        return schedule