def bankers_algorithm(allocation, maximum, available):
    """
    Banker's Algorithm

    Used for deadlock avoidance.

    allocation = resources currently allocated
    maximum = maximum resources each process may need
    available = resources currently available
    """

    process_count = len(allocation)
    resource_count = len(available)

    # calculate Need matrix
    # Need = Maximum - Allocation
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

    # keeps track of completed processes
    finish = [False] * process_count

    # stores safe sequence
    safe_sequence = []

    # keep checking processes
    while len(safe_sequence) < process_count:

        found = False

        for i in range(process_count):

            # skip if process is already completed
            if finish[i]:
                continue

            # check whether Need <= Work
            can_execute = True

            for j in range(resource_count):

                if need[i][j] > work[j]:

                    can_execute = False
                    break

            # process can execute
            if can_execute:

                # after process finishes,
                # its allocated resources are released
                for j in range(resource_count):

                    work[j] += allocation[i][j]

                finish[i] = True

                safe_sequence.append(i)

                found = True

        # if no process can execute,
        # system is unsafe
        if not found:
            break

    # check whether all processes finished
    safe = len(safe_sequence) == process_count

    return {
        "need": need,
        "safe_sequence": safe_sequence,
        "safe": safe
    }


if __name__ == "__main__":

    # Allocation Matrix
    allocation = [
        [0, 6, 3, 2],
        [0, 0, 1, 2],
        [1, 0, 0, 0],
        [1, 3, 5, 4],
        [0, 0, 1, 4]
    ]

    # Maximum Matrix
    maximum = [
        [0, 6, 5, 2],
        [0, 0, 1, 2],
        [1, 7, 5, 0],
        [2, 3, 5, 6],
        [0, 6, 5, 6]
    ]

    # Total resources available in the system
    total_resources = [3, 14, 12, 12]

    # calculate total allocated resources
    allocated_total = []

    for j in range(len(total_resources)):

        total = 0

        for i in range(len(allocation)):

            total += allocation[i][j]

        allocated_total.append(total)

    # Available = Total Resources - Allocated Resources
    available = []

    for j in range(len(total_resources)):

        available.append(
            total_resources[j] - allocated_total[j]
        )

    # run Banker's Algorithm
    result = bankers_algorithm(
        allocation,
        maximum,
        available
    )

    print("\nBANKER'S ALGORITHM")
    print("-" * 50)

    print("\nAllocation Matrix:")

    for row in allocation:
        print(row)

    print("\nMaximum Matrix:")

    for row in maximum:
        print(row)

    print("\nTotal Resources:")
    print(total_resources)

    print("\nAllocated Resources:")
    print(allocated_total)

    print("\nAvailable Resources:")
    print(available)

    print("\nNeed Matrix:")

    for i, row in enumerate(result["need"]):

        print(
            "P" + str(i),
            "->",
            row
        )

    # check result
    if result["safe"]:

        print("\nSystem is in SAFE STATE.")

        print("\nSafe Sequence:")

        print(
            " -> ".join(
                "P" + str(i)
                for i in result["safe_sequence"]
            )
        )

    else:

        print("\nSystem is in UNSAFE STATE.")

        print("No safe sequence exists.")


"""
BANKER'S ALGORITHM

Banker's Algorithm is used for
DEADLOCK AVOIDANCE.

It checks whether the system can
allocate resources safely without
entering a deadlock situation.


IMPORTANT FORMULAS:

Need = Maximum - Allocation

Available = Total Resources - Allocated Resources


STEPS:

1. Calculate the total allocated
   resources column-wise.

2. Calculate Available:

   Available = Total - Allocated

3. Calculate Need:

   Need = Maximum - Allocation

4. Find a process whose:

   Need <= Available

5. Assume that the process completes.

6. When the process completes,
   its allocated resources are released.

7. Add those resources to Available.

8. Continue checking other processes.

9. If all processes can finish:

   -> SAFE STATE

10. If no process can proceed:

   -> UNSAFE STATE


FOR THIS EXAMPLE:

Total Resources:

[3, 14, 12, 12]

Allocated Resources:

[2, 9, 10, 12]

Available:

[1, 5, 2, 0]


Need Matrix:

P0 -> [0, 0, 2, 0]
P1 -> [0, 0, 0, 0]
P2 -> [0, 7, 5, 0]
P3 -> [1, 0, 0, 2]
P4 -> [0, 6, 4, 2]


SAFE SEQUENCE:

P1 -> P3 -> P4 -> P0 -> P2


SAFE STATE:

All processes can complete without
causing deadlock.


IMPORTANT:

Unsafe state does NOT always mean
deadlock has already happened.

It means that the system cannot
guarantee safe completion of all
processes with the current resources.

Banker's Algorithm is a
DEADLOCK AVOIDANCE algorithm.
"""