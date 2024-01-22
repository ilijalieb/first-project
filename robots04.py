# ID 105059321

def count_platforms(robots_input: str, max_weight: int) -> int:
    robots_unsorted = [int(x) for x in robots_input.split()]
    count: int = 0
    end_window: int = -1
    robots = sorted(robots_unsorted, reverse=True)

    for start_window in range(len(robots)):
        if robots[start_window] + robots[end_window] > max_weight:
            count += 1
        else:
            count += len(robots[count:]) // 2 + len(robots[count:]) % 2
            return count

    return count


robots_usr_input = input()
limit = int(input())
print(count_platforms(robots_usr_input, limit))



