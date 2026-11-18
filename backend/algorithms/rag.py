def check_deadlock(total_resources, allocation, requests):
    """
    Deadlock Detection Algorithm.

    Checks whether processes can complete
    using the currently available resources.
    """

    process_count = len(allocation)
    resource_count = len(total_resources)

    # calculate total allocated resources
    allocated = [0] * resource_count

    for i in range(process_count):

        for j in range(resource_count):

            allocated[j] += allocation[i][j]

    # calculate currently available resources
    available = []

    for j in range(resource_count):

        available.append(
            total_resources[j] - allocated[j]
        )

    initial_available = available.copy()

    # track which processes have completed
    finish = [False] * process_count

    safe_sequence = []

    # check whether processes can complete
    while True:

        found = False

        for i in range(process_count):

            if finish[i]:
                continue

            # check whether Request <= Available
            can_finish = True

            for j in range(resource_count):

                if requests[i][j] > available[j]:

                    can_finish = False
                    break

            if can_finish:

                finish[i] = True
                safe_sequence.append(i)

                # release resources after process completes
                for j in range(resource_count):

                    available[j] += allocation[i][j]

                found = True

        # stop if no more processes can complete
        if not found:
            break

    # identify processes that could not complete
    stuck = []

    for i in range(process_count):

        if not finish[i]:

            stuck.append(i)

    # deadlock exists if some processes remain unfinished
    deadlock = len(safe_sequence) != process_count

    return {
        "allocated": allocated,
        "initial_available": initial_available,
        "final_available": available,
        "safe_sequence": safe_sequence,
        "deadlock": deadlock,
        "stuck_processes": stuck
    }