import numpy as np
runs = np.array(
    [
        [45, 50, 30, 60, 25],
        [10, 15, 5, 20, 12],
        [80, 60, 75, 100, 90],
        [25, 30, 20, 35, 40],
        [0, 5, 10, 0, 2],
        [50, 55, 60, 65, 70],
        [35, 40, 45, 50, 55],
        [100, 110, 120, 115, 125],
        [10, 12, 15, 10, 8],
        [70, 80, 85, 90, 95],
        [40, 45, 50, 55, 60],
    ]
)
total_sum=np.sum(runs,axis=1)
max_score=np.max(runs,axis=1)
print("total score of each player in all matches :")
print(total_sum)
print("Highest score of each player in all matches :")
print(max_score)
