def priority_scheduling(processes):
    """
    priority scheduling cpu scheduling

    each process has:
    - id
    - priority
    - burst

    smaller priority number means higher priority
    arrival time is considered 0 for all processes
    """

    # make a copy so the original process list is not changed
    processes = processes.copy()

    # sort by priority
    # python keeps the original order if priority is same
    processes.sort(key=lambda p: p["priority"])

    current_time = 0
    timeline = []
    results = []

    total_tat = 0
    total_wt = 0

    # run each process in priority order
    while processes:

        # take the first process
        process = processes.pop(0)

        pid = process["id"]
        priority = process["priority"]
        burst = process["burst"]

        # process starts at current time
        start_time = current_time

        # calculate completion time
        current_time = current_time + burst
        completion_time = current_time

        # arrival time is 0
        turnaround_time = completion_time

        # waiting time = turnaround time - burst time
        waiting_time = turnaround_time - burst

        # response time = start time because arrival time is 0
        response_time = start_time

        # add process to gantt chart
        timeline.append({
            "process": pid,
            "start": start_time,
            "end": completion_time
        })

        # save process result
        results.append({
            "id": pid,
            "priority": priority,
            "burst": burst,
            "completion": completion_time,
            "turnaround": turnaround_time,
            "waiting": waiting_time,
            "response": response_time
        })

        # add values to totals
        total_tat = total_tat + turnaround_time
        total_wt = total_wt + waiting_time

    # calculate average times
    number_of_processes = len(results)

    if number_of_processes > 0:
        average_tat = total_tat / number_of_processes
        average_wt = total_wt / number_of_processes
        average_response = sum(
            p["response"] for p in results
        ) / number_of_processes
    else:
        average_tat = 0
        average_wt = 0
        average_response = 0

    return {
        "timeline": timeline,
        "results": results,
        "averages": {
            "waiting": average_wt,
            "turnaround": average_tat,
            "response": average_response
        }
    }


if __name__ == "__main__":

    processes = [
        {
            "id": "P",
            "priority": 3,
            "burst": 5
        },
        {
            "id": "Q",
            "priority": 2,
            "burst": 4
        },
        {
            "id": "R",
            "priority": 1,
            "burst": 2
        },
        {
            "id": "S",
            "priority": 2,
            "burst": 4
        },
        {
            "id": "T",
            "priority": 1,
            "burst": 3
        }
    ]

    result = priority_scheduling(processes)

    print("\nGANTT CHART")
    print("-" * 40)

    for block in result["timeline"]:
        print(
            f"{block['process']}: "
            f"{block['start']} -> {block['end']}"
        )

    print("\nPROCESS RESULTS")
    print("-" * 40)

    for process in result["results"]:
        print(
            f"{process['id']} | "
            f"Priority: {process['priority']} | "
            f"BT: {process['burst']} | "
            f"CT: {process['completion']} | "
            f"TAT: {process['turnaround']} | "
            f"WT: {process['waiting']}"
        )

    print("\nAVERAGES")
    print("-" * 40)

    print(
        f"Average Waiting Time: "
        f"{result['averages']['waiting']:.2f}"
    )

    print(
        f"Average Turnaround Time: "
        f"{result['averages']['turnaround']:.2f}"
    )

    print(
        f"Average Response Time: "
        f"{result['averages']['response']:.2f}"
    )


"""
priority scheduling

- this version is non-preemptive
- smaller priority number means higher priority
- processes are sorted by priority
- if two processes have the same priority, original order is maintained
- all processes have arrival time 0
- once a process starts, it runs until it finishes
- a newly arrived process cannot interrupt the running process

time calculations:

completion time = previous completion time + burst time
turnaround time = completion time
waiting time = turnaround time - burst time
response time = start time
"""