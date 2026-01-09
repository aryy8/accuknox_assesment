# for this problem I am using requests to fetch data and visualise it.

import requests
import matplotlib.pyplot as plt

def solve_problem_2():
    # Fetching mock data
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    students = response.json()

    # Assuming 'id' * 10 is their score for this simulation
    names = [s['name'] for s in students]
    scores = [s['id'] * 9 for s in students] 

    avg_score = sum(scores) / len(scores)
    
    # Visualization
    plt.figure(figsize=(10, 5))
    plt.bar(names, scores, color='teal')
    plt.axhline(y=avg_score, color='r', linestyle='--', label=f'Avg: {avg_score}')
    plt.xticks(rotation=45, ha='right')
    plt.title('Student Test Scores Visualization')
    plt.ylabel('Score')
    plt.legend()
    plt.tight_layout()
    plt.savefig('question2_plot.png')
    plt.show()

solve_problem_2()