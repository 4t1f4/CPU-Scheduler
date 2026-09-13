def cscan(requests, head, disk_size, direction="right",
          count_zero=True, professor_version=False):
    """
    c-scan (circular scan)

    two versions:

    1. professor_version = False
       standard c-scan
       head moves to the disk end
       circular jump is not counted

    2. professor_version = True
       professor's version
       after finishing one side, directly calculate
       distance to the first request on the other side
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

    # =================================================
    # PROFESSOR'S VERSION
    # =================================================

    if professor_version:

        if direction == "right":

            # service right requests in ascending order
            for request in right_requests:

                movement = abs(current_head - request)

                total_movement += movement

                current_head = request

                sequence.append(request)

            # directly move to first left request
            # circular jump is not calculated separately
            if left_requests:

                first_left = left_requests[0]

                movement = abs(
                    current_head - first_left
                )

                total_movement += movement

                current_head = first_left

                sequence.append(first_left)

                # service remaining left requests
                for request in left_requests[1:]:

                    movement = abs(
                        current_head - request
                    )

                    total_movement += movement

                    current_head = request

                    sequence.append(request)

        else:

            # service left requests in descending order
            left_descending = sorted(
                left_requests,
                reverse=True
            )

            for request in left_descending:

                movement = abs(
                    current_head - request
                )

                total_movement += movement

                current_head = request

                sequence.append(request)

            # directly move to last right request
            if right_requests:

                first_right = right_requests[-1]

                movement = abs(
                    current_head - first_right
                )

                total_movement += movement

                current_head = first_right

                sequence.append(first_right)

                # service remaining right requests
                for request in reversed(
                    right_requests[:-1]
                ):

                    movement = abs(
                        current_head - request
                    )

                    total_movement += movement

                    current_head = request

                    sequence.append(request)

    # =================================================
    # STANDARD C-SCAN
    # =================================================

    else:

        if direction == "right":

            # service right requests
            for request in right_requests:

                movement = abs(
                    current_head - request
                )

                total_movement += movement

                current_head = request

                sequence.append(request)

            # move to right end
            if current_head != right_end:

                movement = abs(
                    current_head - right_end
                )

                total_movement += movement

                current_head = right_end

                sequence.append(right_end)

            # circular jump to left end
            # NOT counted
            current_head = left_end
            sequence.append(left_end)

            # service left requests in ascending order
            for request in left_requests:

                movement = abs(
                    current_head - request
                )

                total_movement += movement

                current_head = request

                sequence.append(request)

        else:

            # service left requests in descending order
            for request in reversed(left_requests):

                movement = abs(
                    current_head - request
                )

                total_movement += movement

                current_head = request

                sequence.append(request)

            # move to left end
            if current_head != left_end:

                movement = abs(
                    current_head - left_end
                )

                total_movement += movement

                current_head = left_end

                sequence.append(left_end)

            # circular jump to right end
            # NOT counted
            current_head = right_end
            sequence.append(right_end)

            # service right requests in descending order
            for request in reversed(right_requests):

                movement = abs(
                    current_head - request
                )

                total_movement += movement

                current_head = request

                sequence.append(request)

    return {
        "sequence": sequence,
        "total_movement": total_movement
    }


if __name__ == "__main__":

    requests = [ 98, 183, 37, 122, 14, 124, 65, 67 ]

    head = 53

    disk_size = 200

    direction = "right"


    # =================================================
    # VERSION 1: STANDARD C-SCAN
    # =================================================

    print("\nSTANDARD C-SCAN")
    print("-" * 40)

    result_standard = cscan(
        requests,
        head,
        disk_size,
        direction,
        True,
        False
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


    # =================================================
    # VERSION 2: PROFESSOR'S C-SCAN
    # =================================================

    print("\n\nPROFESSOR'S C-SCAN")
    print("-" * 40)

    result_professor = cscan(
        requests,
        head,
        disk_size,
        direction,
        True,
        True
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


"""
c-scan (circular scan)

standard version:

- service requests in one direction
- move to the disk boundary
- circular jump to the other boundary
- circular jump is not counted
- continue servicing requests in the same direction

professor's version:

- service requests in one direction
- do not separately calculate movement to 199/0
- do not calculate circular jump
- directly calculate distance between the
  last request on one side and the first
  request on the other side

right direction:

right requests -> ascending
then first left request
then remaining left requests -> ascending

left direction:

left requests -> descending
then last right request
then remaining right requests -> descending

movement:

movement = abs(current head - next request)
"""