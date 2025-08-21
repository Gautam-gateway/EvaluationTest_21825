Task_lists = ['Task1','Task2','Task3']
# "pending_tasks": [
#     {"id": "T1", "name": "Database Optimization", "complexity": 8, "min_skill": 3, "estimated_hours": 4},
#     {"id": "T2", "name": "Bug Fix", "complexity": 3, "min_skill": 1, "estimated_hours": 1},
#   ]
candidates = {
   "John" : { 
    "current_hour": 14,
    "details": [
        {
        "peak_hour": 10,  
        "skill_level": 3,  
        "energy_level": 42, 
        "current_tasks": []
        },
    ],
   },

    "adam" : { 
    "current_hour": 10,
    "details": [
        {
        "peak_hour": 10,  
        "skill_level": 9,  
        "energy_level": 100, 
        "current_tasks": []
        },
    ],
   },


    "michel" : { 
    "current_hour": 14,
    "details": [
        {
        "peak_hour": 9,  
        "skill_level": 7,  
        "energy_level": 88, 
        "current_tasks": []
        },
    ],
   }
}


# Calculate each person's "capacity score" at different hours:
# capacity = base_skill * productivity_modifier * energy_factor
# productivity_modifier = 1 + 0.5 * cos((current_hour - peak_hour) * π/12)
# energy_factor = (100 - current_task_count * 15) / 100


alloocations = []


for i in range(len(Task_lists)):
    if Task_lists[i] not in alloocations:
        

    