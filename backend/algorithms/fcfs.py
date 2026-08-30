def fcfs(processes):
    """
    first come first serve cpu scheduling

    each process has:
    - id
    - arrival
    - burst
    - priority
    """

    # sort processes according to arrival time
    processes = sorted(processes, key=lambda p: p["arrival"])

    current_time = 0
    timeline = []
    results = []

    # go through each process one by one
    for process in processes:
        pid = process["id"]
        arrival = process["arrival"]
        burst = process["burst"]

        # check if the cpu has to wait for the next process
        if current_time < arrival:
            timeline.append({
                "process": "IDLE",
                "start": current_time,
                "end": arrival
            })

            current_time = arrival

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

    # calculate average times
    number_of_processes = len(results)

    if number_of_processes > 0:
        average_waiting = sum(p["waiting"] for p in results) / number_of_processes
        average_turnaround = sum(p["turnaround"] for p in results) / number_of_processes
        average_response = sum(p["response"] for p in results) / number_of_processes
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
            "burst": 2,
            "priority": 4
        },
        {
            "id": "P2",
            "arrival": 1,
            "burst": 2,
            "priority": 3
        },
        {
            "id": "P3",
            "arrival": 5,
            "burst": 3,
            "priority": 1
        },
        {
            "id": "P4",
            "arrival": 6,
            "burst": 4,
            "priority": 2
        }
    ]

    result = fcfs(processes)

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

    print(f"Average Waiting Time: {result['averages']['waiting']:.2f}")
    print(f"Average Turnaround Time: {result['averages']['turnaround']:.2f}")
    print(f"Average Response Time: {result['averages']['response']:.2f}")




"""
fcfs (first come first serve)

- the process that arrives first gets the cpu first
- processes are arranged according to arrival time
- once a process starts, it runs until it finishes
- no preemption means no interruption between a process
- priority and burst time do not decide the order
- if no process is available, the cpu stays idle

time calculations:
waiting time = start time - arrival time
turnaround time = completion time - arrival time
response time = first start time - arrival time
"""