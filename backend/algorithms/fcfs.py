def fcfs(processes):
    """
    First Come First Serve CPU Scheduling

    The process that arrives first gets the CPU first.
    Once a process starts, it runs until completion.
    """

    # Arrange processes according to their arrival time
    processes = sorted(processes, key=lambda p: p["arrival"])

    current_time = 0
    timeline = []
    results = []

    # Execute each process in arrival order
    for process in processes:

        pid = process["id"]
        arrival = process["arrival"]
        burst = process["burst"]

        # CPU remains idle if the next process hasn't arrived
        if current_time < arrival:

            timeline.append({
                "process": "IDLE",
                "start": current_time,
                "end": arrival
            })

            current_time = arrival

        # Calculate process start and completion times
        start_time = current_time
        completion_time = start_time + burst

        # Calculate waiting, turnaround and response times
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

        # Move the CPU time forward
        current_time = completion_time

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