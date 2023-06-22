# choosing the fastest ending activity gives the biggest amount of possible activities
# array[i] = [start_i, end_i]
# time: O( n*logn )
def asp(activities):
    n = len(activities)

    activities.sort(key=lambda x: x[1])
    result = [activities[0]]

    end = activities[0][1]
    for i in range(1, n):
        if end <= activities[i][0]:
            result.append(activities[i])
            end = activities[i][1]

    return result
