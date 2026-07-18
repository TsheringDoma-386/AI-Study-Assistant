from ai.break_optimizer import BreakOptimizer

optimizer = BreakOptimizer()

schedule = optimizer.generate_schedule(3)

for item in schedule:
    print(item)