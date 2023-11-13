import random


class AntColony:
    def __init__(self, tasks):
        self.tasks = tasks
        self.num_ants = 10
        self.pheromone_evaporation = 0.1
        self.alpha = 1.0  # Pheromone influence
        self.beta = 1.0
        self.num_iterations = 50
        self.best_schedule = None
        self.best_makespan = float('inf')
        self.pheromones = {}

    def findSolution(self):
        for task1 in self.tasks:
            for task2 in self.tasks:
                print(task1)
                print(task2)
                if task1 != task2:
                    print("hello")
                    self.pheromones[(task1, task2)] = 1.0
                else:
                    self.pheromones[(task1, task2)] = 10.0
        print("assigned pheromones")
        print(self.pheromones)
        for iteration in range(self.num_iterations):
            for ant in range(self.num_ants):
                schedule = []
                available_tasks = list(self.tasks.keys())
                current_time = 0

                while available_tasks:
                    ant_probabilities = {}
                    for task in available_tasks:
                        valid_dependencies = all(dep in schedule for dep in self.tasks[task]['dependencies'])
                        if valid_dependencies:
                            if self.tasks[task]['dependencies']:
                                last_dependency = self.tasks[task]['dependencies'][-1]
                                pheromone = self.pheromones[(last_dependency, task)]
                            else:
                                pheromone = self.pheromones[(task, task)]
                            duration = self.tasks[task]['duration']
                            completion_time = current_time + duration
                            ant_probabilities[task] = (pheromone ** self.alpha) / (duration ** self.beta)

                    if not ant_probabilities:
                        break

                    total_probability = sum(ant_probabilities.values())
                    ant_probabilities = {task: prob / total_probability for task, prob in ant_probabilities.items()}

                    # Ensure the sum of probabilities is exactly 1.0 due to potential rounding issues
                    if total_probability != 1.0:
                        ant_probabilities = {task: prob / total_probability for task, prob in ant_probabilities.items()}

                    selected_task = \
                    random.choices(list(ant_probabilities.keys()), weights=list(ant_probabilities.values()))[0]
                    schedule.append(selected_task)
                    available_tasks.remove(selected_task)
                    current_time += self.tasks[selected_task]['duration']

                # Calculate makespan (project completion time)
                makespan = current_time

                # Update the best schedule if necessary
                if makespan < self.best_makespan:
                    self.best_schedule = schedule
                    self.best_makespan = makespan

                # Update pheromone levels
                for i in range(len(schedule) - 1):
                    task1, task2 = schedule[i], schedule[i + 1]
                    self.pheromones[(task1, task2)] += 1.0
        # Print the best schedule and its makespan
        print("Best Schedule:", self.best_schedule)
        print("Best Makespan:", self.best_makespan)
