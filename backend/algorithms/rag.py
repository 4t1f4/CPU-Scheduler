def check_deadlock(total_resources, allocation, requests):

    """
    Deadlock Detection Algorithm

    Checks whether processes can complete
    using currently available resources.

    total_resources = total instances of each resource
    allocation = resources currently allocated to processes
    requests = resources currently requested by processes
    """

    process_count = len(allocation)
    resource_count = len(total_resources)

    # calculate total allocated resources
    allocated = [0] * resource_count

    for i in range(process_count):

        for j in range(resource_count):

            allocated[j] += allocation[i][j]

    # calculate available resources
    available = []

    for j in range(resource_count):

        available.append(
            total_resources[j] - allocated[j]
        )

    initial_available = available.copy()

    # initially no process is finished
    finish = [False] * process_count

    # stores processes that can complete
    safe_sequence = []

    # check whether any process can complete
    while True:

        found = False

        for i in range(process_count):

            if finish[i]:
                continue

            can_finish = True

            # check Request <= Available
            for j in range(resource_count):

                if requests[i][j] > available[j]:

                    can_finish = False
                    break

            # process can complete
            if can_finish:

                finish[i] = True

                safe_sequence.append(i)

                # release allocated resources
                for j in range(resource_count):

                    available[j] += allocation[i][j]

                found = True

        # stop if no process can complete
        if not found:
            break

    # identify unfinished processes
    stuck = []

    for i in range(process_count):

        if not finish[i]:

            stuck.append(i)

    # check whether deadlock exists
    deadlock = len(safe_sequence) != process_count

    return {
        "allocated": allocated,
        "initial_available": initial_available,
        "final_available": available,
        "safe_sequence": safe_sequence,
        "deadlock": deadlock,
        "stuck_processes": stuck
    }