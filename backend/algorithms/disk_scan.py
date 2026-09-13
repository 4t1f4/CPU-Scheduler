def scan(requests, head, disk_size, direction="left", count_zero=True,
         professor_version=False, time_per_track=1):
    """
    scan (elevator algorithm)

    two versions:

    1. professor_version = False
       standard scan
       head goes to the disk boundary before reversing

    2. professor_version = True
       professor's version
       head does not go to 0/199 or 1/200
       unless that track is actually present in requests
    """

    requests = requests.copy()

    current_head = head
    total_movement = 0
    sequence = [head]

    # decide disk boundaries
    if count_zero:
        left_end = 0
        right_end = disk_size - 1
    else:
        left_end = 1
        right_end = disk_size

    # separate requests
    left_requests = sorted(
        [request for request in requests if request < head]
    )

    right_requests = sorted(
        [request for request in requests if request >= head]
    )

    # ------------------------------------------------
    # PROFESSOR VERSION
    # ------------------------------------------------

    if professor_version:

        if direction == "left":

            # service left requests in descending order
            order = sorted(left_requests, reverse=True)

            # then reverse and service right requests
            order = order + right_requests

        else:

            # service right requests in ascending order
            order = right_requests

            # then reverse and service left requests
            order = order + sorted(left_requests, reverse=True)

        # calculate movement only between requests
        for request in order:

            movement = abs(current_head - request)

            total_movement += movement

            current_head = request

            sequence.append(request)

    # ------------------------------------------------
    # STANDARD SCAN VERSION
    # ------------------------------------------------

    else:

        if direction == "left":

            # service left requests in descending order
            for request in reversed(left_requests):

                movement = abs(current_head - request)

                total_movement += movement

                current_head = request

                sequence.append(request)

            # move to left boundary
            if current_head != left_end:

                movement = abs(current_head - left_end)

                total_movement += movement

                current_head = left_end

                sequence.append(left_end)

            # reverse and service right requests
            for request in right_requests:

                movement = abs(current_head - request)

                total_movement += movement

                current_head = request

                sequence.append(request)

        else:

            # service right requests in ascending order
            for request in right_requests:

                movement = abs(current_head - request)

                total_movement += movement

                current_head = request

                sequence.append(request)

            # move to right boundary
            if current_head != right_end:

                movement = abs(current_head - right_end)

                total_movement += movement

                current_head = right_end

                sequence.append(right_end)

            # reverse and service left requests
            for request in reversed(left_requests):

                movement = abs(current_head - request)

                total_movement += movement

                current_head = request

                sequence.append(request)

    # calculate time
    total_time = total_movement * time_per_track

    return {
        "sequence": sequence,
        "total_movement": total_movement,
        "total_time": total_time
    }


if __name__ == "__main__":

    requests = [98, 185, 37, 122, 14, 124, 65, 67]

    head = 53

    disk_size = 200

    direction = "left"

    time_per_track = 1


    # =================================================
    # VERSION 1: STANDARD SCAN
    # =================================================

    print("\nSTANDARD SCAN")
    print("-" * 40)

    result_standard = scan(
        requests,
        head,
        disk_size,
        direction,
        True,
        False,
        time_per_track
    )

    print("Disk Tracks: 0 - 199")
    print("Initial Head:", head)
    print("Direction:", direction)

    print("\nSequence:")

    print(
        " -> ".join(
            map(str, result_standard["sequence"])
        )
    )

    print(
        "\nTotal Movement:",
        result_standard["total_movement"]
    )

    print(
        "Total Time:",
        result_standard["total_time"]
    )


    # =================================================
    # VERSION 2: PROFESSOR'S SCAN
    # =================================================

    print("\n\nPROFESSOR'S SCAN")
    print("-" * 40)

    result_professor = scan(
        requests,
        head,
        disk_size,
        direction,
        True,
        True,
        time_per_track
    )

    print("Disk Tracks: 0 - 199")
    print("Initial Head:", head)
    print("Direction:", direction)

    print("\nSequence:")

    print(
        " -> ".join(
            map(str, result_professor["sequence"])
        )
    )

    print(
        "\nTotal Movement:",
        result_professor["total_movement"]
    )

    print(
        "Total Time:",
        result_professor["total_time"]
    )


"""
scan (elevator algorithm)

standard scan:

- head moves in the selected direction
- requests in that direction are serviced
- head goes to the disk boundary
- then direction is reversed
- remaining requests are serviced

professor's version:

- head moves in the selected direction
- requests in that direction are serviced
- head does NOT move to disk boundary
- direction is reversed after the last request
- only requested tracks are included in movement

professor's logic:

left:
    left requests → descending
    right requests → ascending

right:
    right requests → ascending
    left requests → descending

movement:

movement = abs(current_head - next_request)

total movement:

total_movement = sum of all movements

time:

total_time = total_movement * time_per_track
"""