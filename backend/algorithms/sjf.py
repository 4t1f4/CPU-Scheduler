def sjf(processes):
    """
    shortest job first cpu scheduling

    each process has:
    - id
    - arrival
    - burst
    - priority
    """

    # make a copy so the original process list is not changed
    processes = processes.copy()

    current_time = 0
    timeline = []
    results = []

    # keep running until all processes are completed
    while processes:

        # find processes that have already arrived
        available = [
            process for process in processes
            if process["arrival"] <= current_time
        ]

        # if no process has arrived yet, move cpu time forward
        if not available:
            next_arrival = min(process["arrival"] for process in processes)

            timeline.append({
                "process": "IDLE",
                "start": current_time,
                "end": next_arrival
            })

            current_time = next_arrival
            continue

        # choose the process with the shortest burst time
        process = min(
            available,
            key=lambda p: (p["burst"], p["arrival"])
        )

        pid = process["id"]
        arrival = process["arrival"]
        burst = process["burst"]

        # find when the process starts and finishes
        start_time = current_time
        completion_time = start_time + burst

        # calculate the scheduling times
        waiting_time = start_time - arrival
        turnaround_time = completion_time - arrival
        response_time = start_time - arrival

        # save this part for the gantt chart
        timeline.append({
            "process": pid,
            "start": start_time,
            "end": completion_time
        })

        # save all results for this process
        results.append({
            "id": pid,
            "arrival": arrival,
            "burst": burst,
            "priority": process["priority"],
            "start": start_time,
            "completion": completion_time,
            "waiting": waiting_time,
            "turnaround": turnaround_time,
            "response": response_time
        })

        # move the cpu time to when this process finishes
        current_time = completion_time

        # remove the completed process
        processes.remove(process)

    # calculate average times
    number_of_processes = len(results)

    if number_of_processes > 0:
        average_waiting = sum(
            p["waiting"] for p in results
        ) / number_of_processes

        average_turnaround = sum(
            p["turnaround"] for p in results
        ) / number_of_processes

        average_response = sum(
            p["response"] for p in results
        ) / number_of_processes
    else:
        average_waiting = 0
        average_turnaround = 0
        average_response = 0

    return {
        "timeline": timeline,
        "results": results,
        "averages": {
            "waiting": average_waiting,
            "turnaround": average_turnaround,
            "response": average_response
        }
    }


if __name__ == "__main__":

    processes = [
        {
            "id": "P1",
            "arrival": 1,
            "burst": 3,
            "priority": 4
        },
        {
            "id": "P2",
            "arrival": 2,
            "burst": 4,
            "priority": 3
        },
        {
            "id": "P3",
            "arrival": 1,
            "burst": 2,
            "priority": 1
        },
        {
            "id": "P4",
            "arrival": 4,
            "burst": 4,
            "priority": 2
        }
    ]

    result = sjf(processes)

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
            f"Waiting: {process['waiting']} | "
            f"Turnaround: {process['turnaround']} | "
            f"Response: {process['response']}"
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
sjf (shortest job first)

- the process with the shortest burst time gets the cpu first
- only processes that have already arrived can be selected
- once a process starts, it runs until it finishes
- no preemption means the process is not interrupted
- priority does not decide the order
- if no process has arrived, the cpu stays idle
- if two processes have the same burst time, arrival time is used

time calculations:
waiting time = start time - arrival time
turnaround time = completion time - arrival time
response time = first start time - arrival time
"""