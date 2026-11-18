def disk_fcfs(requests, head):
    """
    Disk FCFS (First Come First Serve)

    Requests are handled in the same order they are received.
    The disk head moves directly from one request to the next.
    """

    current_head = head
    total_seek = 0
    sequence = [head]

    # Process each request in the given order
    for request in requests:

        # Calculate the distance between the current head and request
        movement = abs(request - current_head)

        total_seek += movement

        # Move the head to the requested track
        current_head = request
        sequence.append(request)

    # Calculate average seek operations
    average_seek = (
        total_seek / len(requests) if requests else 0
    )

    return {
        "sequence": sequence,
        "total_seek": total_seek,
        "average_seek": average_seek
    }