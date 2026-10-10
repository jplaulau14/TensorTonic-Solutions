import heapq


def schedule_pipeline(tasks: list, resource_budget: int) -> list:
    by_name = {task["name"]: task for task in tasks}
    waiting = {name: len(set(task["depends_on"])) for name, task in by_name.items()}
    children = {name: [] for name in by_name}
    for task in tasks:
        for dep in set(task["depends_on"]):
            children[dep].append(task["name"])
    ready = [name for name, count in waiting.items() if count == 0]
    running = []
    schedule = []
    time = 0
    while ready or running:
        while running and running[0][0] <= time:
            _, name = heapq.heappop(running)
            for child in children[name]:
                waiting[child] -= 1
                if waiting[child] == 0:
                    ready.append(child)
        used = sum(by_name[name]["resources"] for _, name in running)
        skipped = []
        for name in sorted(ready):
            need = by_name[name]["resources"]
            if used + need <= resource_budget:
                used += need
                schedule.append({"task_name": name, "start_time": time})
                heapq.heappush(running, (time + by_name[name]["duration"], name))
            else:
                skipped.append(name)
        ready = skipped
        if running:
            time = running[0][0]
    return schedule