def round_robin(processes, time_quantum):
    """
    Round Robin CPU Scheduling

    Each process gets the CPU for a fixed amount of time
    called the time quantum.

    If a process is not completed, it goes back to the ready queue.
    """

    # Make a copy so the original process list remains unchanged
    processes = processes.copy()

    # Track the remaining burst time of each process
    for process in processes:
        process["remaining"] = process["burst"]

    current_time = 0
    timeline = []
    results = []

    # Store the first time each process gets the CPU
    first_start = {}

    # Ready queue stores processes waiting for CPU time
    ready_queue = []

    # Keep track of processes already added to the queue
    added = set()

    # Continue until all processes are completed
    while len(results) < len(processes):

        # Add newly arrived processes to the ready queue
        for process in processes:

            if (
                process["arrival"] <= current_time
                and process["id"] not in added
                and process["remaining"] > 0
            ):
                ready_queue.append(process)
                added.add(process["id"])

        # If the queue is empty, move to the next process arrival
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

        # Take the first process from the ready queue
        process = ready_queue.pop(0)

        pid = process["id"]

        # Record the first time the process gets the CPU
        if pid not in first_start:
            first_start[pid] = current_time

        # Run the process for one quantum or until it finishes
        run_time = min(
            time_quantum,
            process["remaining"]
        )

        start_time = current_time
        current_time += run_time
        process["remaining"] -= run_time

        # Add this execution to the Gantt chart timeline
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

        # Add processes that arrived while the current process was running
        for new_process in processes:

            if (
                new_process["arrival"] <= current_time
                and new_process["id"] not in added
                and new_process["remaining"] > 0
            ):
                ready_queue.append(new_process)
                added.add(new_process["id"])

        # If the process still needs CPU time, add it back to the queue
        if process["remaining"] > 0:

            ready_queue.append(process)

        else:
            # Calculate scheduling times for the completed process
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

            # Store the completed process details
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

    # Calculate average scheduling times
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