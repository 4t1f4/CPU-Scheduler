def sstf(requests, head):
    """
    SSTF (Shortest Seek Time First)

    The request closest to the current head is selected first.
    After servicing a request, the head moves to that track.
    """

    # Make a copy so the original request list remains unchanged
    requests = requests.copy()

    current_head = head
    total_seek = 0
    sequence = [head]

    # Continue until all requests have been serviced
    while requests:

        # Find the request closest to the current head
        closest = min(
            requests,
            key=lambda request: abs(request - current_head)
        )

        # Calculate the head movement
        movement = abs(closest - current_head)

        total_seek += movement

        # Move the head to the selected request
        current_head = closest
        sequence.append(closest)

        # Remove the completed request
        requests.remove(closest)

    # Calculate average seek operations
    average_seek = (
        total_seek / (len(sequence) - 1)
        if len(sequence) > 1 else 0
    )

    return {
        "sequence": sequence,
        "total_seek": total_seek,
        "average_seek": average_seek
    }