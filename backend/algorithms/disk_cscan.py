def cscan(
    requests,
    head,
    disk_size,
    direction="right",
    count_zero=True,
    professor_version=False,
    time_per_track=1
):
    """
    C-SCAN (Circular SCAN)

    Standard version:
    The head moves to the disk boundary, jumps to the other
    end and continues servicing requests in the same direction.
    The circular jump is not counted in total movement.

    Professor's version:
    The head directly calculates the distance between
    the last request on one side and the first request
    on the other side.
    """

    # Make a copy so the original request list remains unchanged
    requests = requests.copy()

    current_head = head
    total_movement = 0
    sequence = [head]

    # Set the first and last track of the disk
    if count_zero:
        left_end = 0
        right_end = disk_size - 1
    else:
        left_end = 1
        right_end = disk_size

    # Separate requests on the left and right of the head
    left_requests = sorted(
        [request for request in requests if request < head]
    )

    right_requests = sorted(
        [request for request in requests if request >= head]
    )

    # Professor's version
    if professor_version:

        if direction == "right":

            # Service right requests in ascending order
            for request in right_requests:

                movement = abs(current_head - request)

                total_movement += movement

                current_head = request
                sequence.append(request)

            # Directly move to the first left request
            if left_requests:

                first_left = left_requests[0]

                movement = abs(current_head - first_left)

                total_movement += movement

                current_head = first_left
                sequence.append(first_left)

                # Service the remaining left requests
                for request in left_requests[1:]:

                    movement = abs(current_head - request)

                    total_movement += movement

                    current_head = request
                    sequence.append(request)

        else:

            # Service left requests in descending order
            left_descending = sorted(
                left_requests,
                reverse=True
            )

            for request in left_descending:

                movement = abs(current_head - request)

                total_movement += movement

                current_head = request
                sequence.append(request)

            # Directly move to the last right request
            if right_requests:

                first_right = right_requests[-1]

                movement = abs(current_head - first_right)

                total_movement += movement

                current_head = first_right
                sequence.append(first_right)

                # Service the remaining right requests
                for request in reversed(right_requests[:-1]):

                    movement = abs(current_head - request)

                    total_movement += movement

                    current_head = request
                    sequence.append(request)

    # Standard C-SCAN
    else:

        if direction == "right":

            # Service right requests in ascending order
            for request in right_requests:

                movement = abs(current_head - request)

                total_movement += movement

                current_head = request
                sequence.append(request)

            # Move to the right boundary
            if current_head != right_end:

                movement = abs(current_head - right_end)

                total_movement += movement

                current_head = right_end
                sequence.append(right_end)

            # Jump to the left boundary
            # This circular jump is not included in total movement
            current_head = left_end
            sequence.append(left_end)

            # Continue servicing left requests in ascending order
            for request in left_requests:

                movement = abs(current_head - request)

                total_movement += movement

                current_head = request
                sequence.append(request)

        else:

            # Service left requests in descending order
            for request in reversed(left_requests):

                movement = abs(current_head - request)

                total_movement += movement

                current_head = request
                sequence.append(request)

            # Move to the left boundary
            if current_head != left_end:

                movement = abs(current_head - left_end)

                total_movement += movement

                current_head = left_end
                sequence.append(left_end)

            # Jump to the right boundary
            # This circular jump is not included in total movement
            current_head = right_end
            sequence.append(right_end)

            # Continue servicing right requests in descending order
            for request in reversed(right_requests):

                movement = abs(current_head - request)

                total_movement += movement

                current_head = request
                sequence.append(request)

    # Calculate total time using the time required per track
    total_time = total_movement * time_per_track

    return {
        "sequence": sequence,
        "total_movement": total_movement,
        "total_time": total_time
    }