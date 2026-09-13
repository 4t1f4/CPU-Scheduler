def check_deadlock(total_resources, allocation, requests):

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

    print("Total Resources :", total_resources)
    print("Allocated       :", allocated)
    print("Available       :", available)

    # initially no process is finished
    finish = [False] * process_count

    safe_sequence = []

    # check whether any process can complete
    while True:

        found = False

        for i in range(process_count):

            if finish[i]:
                continue

            can_finish = True

            # check request <= available
            for j in range(resource_count):

                if requests[i][j] > available[j]:
                    can_finish = False
                    break

            if can_finish:

                # process completes
                finish[i] = True
                safe_sequence.append(i)

                # release allocated resources
                for j in range(resource_count):
                    available[j] += allocation[i][j]

                found = True

        if not found:
            break

    print("\nFinal Available:", available)

    if len(safe_sequence) == process_count:

        print("\nNo Deadlock")
        print(
            "Safe Sequence:",
            " -> ".join(
                "P" + str(i)
                for i in safe_sequence
            )
        )

    else:

        print("\nDeadlock Detected")

        stuck = []

        for i in range(process_count):
            if not finish[i]:
                stuck.append("P" + str(i))

        print("Processes stuck:", stuck)


# ==========================================
# Q1
# ==========================================

# Resource instances:
# R0 = 1
# R1 = 2
# R2 = 1
# R3 = 4

total_resources = [1, 2, 1, 4]


# Allocation Matrix
#
#        R0 R1 R2 R3
# P0     0  1  0  0
# P1     1  1  0  0
# P2     0  0  1  0

allocation = [
    [0, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 0]
]


# Request Matrix
#
#        R0 R1 R2 R3
# P0     1  0  0  0
# P1     0  0  1  0
# P2     0  1  0  0

requests = [
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0]
]


check_deadlock(
    total_resources,
    allocation,
    requests
)