def srtf(processes):
    """
    shortest remaining time first cpu scheduling

    each process has:
    - id
    - arrival
    - burst
    - priority
    """

    # make a copy so the original process list is not changed
    processes = processes.copy()

    # store remaining burst time for each process
    for process in processes:
        process["remaining"] = process["burst"]

    current_time = 0
    timeline = []
    results = []

    # store the first time each process gets the cpu
    first_start = {}

    # keep running until all processes are completed
    while any(process["remaining"] > 0 for process in processes):

        # find processes that have arrived and are not completed
        available = [
            process for process in processes
            if process["arrival"] <= current_time
            and process["remaining"] > 0
        ]

        # if no process has arrived yet, move cpu time forward
        if not available:
            next_arrival = min(
                process["arrival"]
                for process in processes
                if process["remaining"] > 0
                and process["arrival"] > current_time
            )

            timeline.append({
                "process": "IDLE",
                "start": current_time,
                "end": next_arrival
            })

            current_time = next_arrival
            continue

        # choose the process with the shortest remaining time
        process = min(
            available,
            key=lambda p: (p["remaining"], p["arrival"])
        )

        pid = process["id"]

        # record the first time the process gets the cpu
        if pid not in first_start:
            first_start[pid] = current_time

        # run the process for one unit of time
        start_time = current_time
        current_time += 1
        process["remaining"] -= 1

        # add this cpu time to the gantt chart
        if (
            timeline
            and timeline[-1]["process"] == pid
            and timeline[-1]["end"] == start_time
        ):
            timeline[-1]["end"] = current_time
        else:
            timeline.append({
                "process": pid,
                "start": start_time,
                "end": current_time
            })

        # check if the process has completed
        if process["remaining"] == 0:

            completion_time = current_time

            # calculate the scheduling times
            waiting_time = (
                completion_time
                - process["arrival"]
                - process["burst"]
            )

            turnaround_time = (
                completion_time
                - process["arrival"]
            )

            response_time = (
                first_start[pid]
                - process["arrival"]
            )

            # save all results for this process
            results.append({
                "id": pid,
                "arrival": process["arrival"],
                "burst": process["burst"],
                "priority": process["priority"],
                "start": first_start[pid],
                "completion": completion_time,
                "waiting": waiting_time,
                "turnaround": turnaround_time,
                "response": response_time
            })

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
            "arrival": 0,
            "burst": 5,
            "priority": 4
        },
        {
            "id": "P2",
            "arrival": 1,
            "burst": 3,
            "priority": 3
        },
        {
            "id": "P3",
            "arrival": 2,
            "burst": 4,
            "priority": 1
        },
        {
            "id": "P4",
            "arrival": 4,
            "burst": 1,
            "priority": 2
        }
    ]

    result = srtf(processes)

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
srtf (shortest remaining time first)

- the process with the shortest remaining burst time gets the cpu
- only processes that have already arrived can be selected
- it is the preemptive version of sjf
- a running process can be interrupted by a shorter process
- remaining burst time is checked whenever a new process arrives
- priority does not decide the order
- if no process has arrived, the cpu stays idle
- if two processes have the same remaining time, arrival time is used

time calculations:

waiting time = completion time - arrival time - burst time
turnaround time = completion time - arrival time
response time = first start time - arrival time
"""