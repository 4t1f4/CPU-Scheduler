def round_robin(processes, time_quantum):
    """
    round robin cpu scheduling

    each process has:
    - id
    - arrival
    - burst
    - priority

    time quantum decides how long a process can run
    before going back to the ready queue
    """

    # make a copy so the original process list is not changed
    processes = processes.copy()

    # add remaining burst time to each process
    for process in processes:
        process["remaining"] = process["burst"]

    current_time = 0
    timeline = []
    results = []

    # store the first time each process gets the cpu
    first_start = {}

    # ready queue
    ready_queue = []

    # keep track of processes that have been added to the queue
    added = set()

    # keep running until all processes are completed
    while len(results) < len(processes):

        # add newly arrived processes to the ready queue
        for process in processes:
            if (
                process["arrival"] <= current_time
                and process["id"] not in added
                and process["remaining"] > 0
            ):
                ready_queue.append(process)
                added.add(process["id"])

        # if the queue is empty, move cpu time to next arrival
        if not ready_queue:

            remaining_processes = [
                process for process in processes
                if process["remaining"] > 0
            ]

            next_arrival = min(
                process["arrival"]
                for process in remaining_processes
            )

            timeline.append({
                "process": "IDLE",
                "start": current_time,
                "end": next_arrival
            })

            current_time = next_arrival
            continue

        # take the first process from the ready queue
        process = ready_queue.pop(0)

        pid = process["id"]

        # record the first time the process gets the cpu
        if pid not in first_start:
            first_start[pid] = current_time

        # process can run for time quantum or until it finishes
        run_time = min(
            time_quantum,
            process["remaining"]
        )

        start_time = current_time
        current_time += run_time
        process["remaining"] -= run_time

        # save this part for the gantt chart
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

        # add any new processes that arrived while this process was running
        for new_process in processes:
            if (
                new_process["arrival"] <= current_time
                and new_process["id"] not in added
                and new_process["remaining"] > 0
            ):
                ready_queue.append(new_process)
                added.add(new_process["id"])

        # if process is not finished, put it back in the queue
        if process["remaining"] > 0:
            ready_queue.append(process)

        else:
            # calculate the scheduling times
            completion_time = current_time

            turnaround_time = (
                completion_time
                - process["arrival"]
            )

            waiting_time = (
                turnaround_time
                - process["burst"]
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
            "burst": 4,
            "priority": 3
        },
        {
            "id": "P3",
            "arrival": 2,
            "burst": 2,
            "priority": 1
        },
        {
            "id": "P4",
            "arrival": 4,
            "burst": 1,
            "priority": 2
        }
    ]

    time_quantum = 2

    result = round_robin(processes, time_quantum)

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
round robin (rr)

- each process gets the cpu for a fixed time
- this fixed time is called time quantum
- processes are handled using a ready queue
- if a process is not finished after its quantum, it goes back to the queue
- it is a preemptive scheduling algorithm
- processes are generally handled in circular order
- arrival time is considered when adding processes to the queue
- priority does not decide the order

time calculations:

waiting time = turnaround time - burst time
turnaround time = completion time - arrival time
response time = first start time - arrival time
"""