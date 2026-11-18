def priority_scheduling(processes):
    """
    Priority CPU Scheduling

    Smaller priority number means higher priority.
    All processes are considered to have arrival time 0.
    This is a non-preemptive scheduling algorithm.
    """

    # Make a copy so the original process list remains unchanged
    processes = processes.copy()

    # Sort processes according to priority
    # Python maintains the original order when priorities are equal
    processes.sort(key=lambda p: p["priority"])

    current_time = 0
    timeline = []
    results = []

    total_tat = 0
    total_wt = 0

    # Execute processes in priority order
    while processes:

        # Take the highest-priority process
        process = processes.pop(0)

        pid = process["id"]
        priority = process["priority"]
        burst = process["burst"]

        # Record when the process starts
        start_time = current_time

        # Calculate completion time
        current_time = current_time + burst
        completion_time = current_time

        # Since arrival time is 0, turnaround time equals completion time
        turnaround_time = completion_time

        # Calculate waiting and response times
        waiting_time = turnaround_time - burst
        response_time = start_time

        # Add the process to the Gantt chart timeline
        timeline.append({
            "process": pid,
            "start": start_time,
            "end": completion_time
        })

        # Store the completed process details
        results.append({
            "id": pid,
            "priority": priority,
            "burst": burst,
            "completion": completion_time,
            "turnaround": turnaround_time,
            "waiting": waiting_time,
            "response": response_time
        })

        # Keep track of total waiting and turnaround times
        total_tat += turnaround_time
        total_wt += waiting_time

    # Calculate average scheduling times
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