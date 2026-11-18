def bankers_algorithm(allocation, maximum, available):
    """
    Banker's Algorithm.

    Checks whether the system is in a safe state
    before allocating resources.
    """

    process_count = len(allocation)
    resource_count = len(available)

    # calculate Need = Maximum - Allocation
    need = []

    for i in range(process_count):

        row = []

        for j in range(resource_count):

            row.append(
                maximum[i][j] - allocation[i][j]
            )

        need.append(row)

    # Work represents currently available resources
    work = available.copy()

    # track which processes have completed
    finish = [False] * process_count

    safe_sequence = []

    # keep checking until all processes finish
    while len(safe_sequence) < process_count:

        found = False

        for i in range(process_count):

            # skip completed processes
            if finish[i]:
                continue

            # check whether Need <= Work
            can_execute = True

            for j in range(resource_count):

                if need[i][j] > work[j]:

                    can_execute = False
                    break

            if can_execute:

                # release resources after process completes
                for j in range(resource_count):

                    work[j] += allocation[i][j]

                finish[i] = True
                safe_sequence.append(i)

                found = True

        # stop if no process can execute
        if not found:
            break

    # check whether all processes completed
    safe = len(safe_sequence) == process_count

    return {
        "need": need,
        "safe_sequence": safe_sequence,
        "safe": safe
    }