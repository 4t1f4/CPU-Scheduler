def sjf(processes):
    """
    Shortest Job First CPU Scheduling

    The process with the shortest burst time gets the CPU first.
    This is a non-preemptive scheduling algorithm.
    """

    # Make a copy so the original process list remains unchanged
    processes = processes.copy()

    current_time = 0
    timeline = []
    results = []

    # Continue until all processes are completed
    while processes:

        # Find processes that have already arrived
        available = [
            process for process in processes
            if process["arrival"] <= current_time
        ]

        # If no process is ready, move to the next arrival time
        if not available:

            next_arrival = min(
                process["arrival"] for process in processes
            )

            timeline.append({
                "process": "IDLE",
                "start": current_time,
                "end": next_arrival
            })

            current_time = next_arrival
            continue

        # Select the process with the shortest burst time
        # Arrival time is used to break ties
        process = min(
            available,
            key=lambda p: (p["burst"], p["arrival"])
        )

        pid = process["id"]
        arrival = process["arrival"]
        burst = process["burst"]

        # Calculate process start and completion times
        start_time = current_time
        completion_time = start_time + burst

        # Calculate scheduling times
        waiting_time = start_time - arrival
        turnaround_time = completion_time - arrival
        response_time = start_time - arrival

        # Add the process to the Gantt chart timeline
        timeline.append({
            "process": pid,
            "start": start_time,
            "end": completion_time
        })

        # Store the completed process details
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

        # Update CPU time and remove the completed process
        current_time = completion_time
        processes.remove(process)

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