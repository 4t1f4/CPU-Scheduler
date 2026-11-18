def scan(
    requests,
    head,
    disk_size,
    direction="left",
    count_zero=True,
    professor_version=False,
    time_per_track=1
):
    """
    SCAN (Elevator Algorithm)

    Standard version:
    The head moves to the disk boundary before reversing direction.

    Professor's version:
    The head reverses direction after the last request
    without travelling to the disk boundary.
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

    # Professor's version: reverse direction without visiting the boundary
    if professor_version:

        if direction == "left":

            # Service left requests first, moving towards lower tracks
            order = sorted(left_requests, reverse=True)

            # Then reverse direction and service right requests
            order += right_requests

        else:

            # Service right requests first, moving towards higher tracks
            order = right_requests.copy()

            # Then reverse direction and service left requests
            order += sorted(left_requests, reverse=True)

        # Calculate movement only between requested tracks
        for request in order:

            movement = abs(current_head - request)

            total_movement += movement

            current_head = request
            sequence.append(request)

    # Standard SCAN: visit the disk boundary before reversing
    else:

        if direction == "left":

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

            # Reverse direction and service right requests
            for request in right_requests:

                movement = abs(current_head - request)

                total_movement += movement

                current_head = request
                sequence.append(request)

        else:

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

            # Reverse direction and service left requests
            for request in reversed(left_requests):

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