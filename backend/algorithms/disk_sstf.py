def sstf(requests, head):
    """
    sstf (shortest seek time first)

    - the request closest to the current head is selected
    - after servicing a request, the head moves to that position
    - then the closest remaining request is selected
    """

    # make a copy so original list is not changed
    requests = requests.copy()

    current_head = head
    total_seek = 0
    sequence = [head]

    while requests:

        # find the request closest to current head
        closest = min(
            requests,
            key=lambda request: abs(request - current_head)
        )

        # calculate head movement
        movement = abs(closest - current_head)

        total_seek = total_seek + movement

        # move head to selected request
        current_head = closest

        sequence.append(closest)

        # remove the completed request
        requests.remove(closest)

    # calculate average seek
    if sequence:
        average_seek = total_seek / (len(sequence) - 1)
    else:
        average_seek = 0

    return {
        "sequence": sequence,
        "total_seek": total_seek,
        "average_seek": average_seek
    }


if __name__ == "__main__":

    # disk requests
    requests = [98, 183, 37, 122, 14, 124, 65, 67]

    # initial head position
    head = 53

    result = sstf(requests, head)

    print("\nSSTF DISK SCHEDULING")
    print("-" * 40)

    print("Initial Head:", head)

    print("\nRequest Sequence:")
    print(" -> ".join(map(str, result["sequence"])))

    print("\nTotal Seek Operations:", result["total_seek"])

    print(
        "Average Seek Operations:",
        f"{result['average_seek']:.2f}"
    )


"""
sstf

- sstf means shortest seek time first
- the closest request is selected first
- distance from the current head is checked
- the request with the smallest distance is selected
- after servicing it, the head moves to that request
- the process continues until all requests are completed

seek movement:

movement = abs(current head - selected request)

total seek = sum of all movements

average seek = total seek / number of requests
"""