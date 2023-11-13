from Metaheuristic.AntColony import AntColony

if __name__ == '__main__':
    tasks = {
        'Task1': {'duration': 3, 'dependencies': ['Task5']},
        'Task2': {'duration': 5, 'dependencies': ['Task1']},
        'Task3': {'duration': 4, 'dependencies': []},
        'Task4': {'duration': 2, 'dependencies': ['Task2', 'Task3']},
        'Task5': {'duration': 6, 'dependencies': []},
    }
    antColony = AntColony(tasks)
    antColony.findSolution()
