def srtf(processes):
    """
    Shortest Remaining Time First CPU Scheduling

    The process with the shortest remaining burst time gets the CPU.
    A running process can be interrupted if a shorter process arrives.
    """

    # Make a copy so the original process list remains unchanged
    processes = processes.copy()

    # Track how much execution time each process still needs
    for process in processes:
        process["remaining"] = process["burst"]

    current_time = 0
    timeline = []
    results = []

    # Store the first time each process gets the CPU
    first_start = {}

    # Continue until every process is completed
    while any(process["remaining"] > 0 for process in processes):

        # Find arrived processes that still need CPU time
        available = [
            process for process in processes
            if process["arrival"] <= current_time
            and process["remaining"] > 0
        ]

        # If no process is ready, move to the next arrival
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

        # Select the process with the shortest remaining time
        # Arrival time is used to break ties
        process = min(
            available,
            key=lambda p: (p["remaining"], p["arrival"])
        )

        pid = process["id"]

        # Record the first time this process gets the CPU
        if pid not in first_start:
            first_start[pid] = current_time

        # Execute the process for one time unit
        start_time = current_time
        current_time += 1
        process["remaining"] -= 1

        # Extend the previous timeline block if the same process continues
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

        # Check whether the process has finished
        if process["remaining"] == 0:

            completion_time = current_time

            # Calculate scheduling times
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