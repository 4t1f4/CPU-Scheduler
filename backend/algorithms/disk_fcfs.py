def disk_fcfs(requests, head):
    """
    disk fcfs (first come first served)

    - disk requests are handled in the order they are given
    - there is no sorting
    - head moves directly from one request to the next
    """

    current_head = head
    total_seek = 0
    sequence = [head]

    for request in requests:

        # calculate how far the disk head has to move
        movement = abs(request - current_head)

        total_seek = total_seek + movement

        # move head to the requested track
        current_head = request

        sequence.append(request)

    return {
        "sequence": sequence,
        "total_seek": total_seek,
        "average_seek": total_seek / len(requests) if requests else 0
    }


if __name__ == "__main__":

    # disk requests
    requests = [98, 183, 37, 122, 14, 124, 65, 67]

    # initial head position
    head = 53

    result = disk_fcfs(requests, head)

    print("\nDISK FCFS")
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
disk fcfs

- fcfs means first come first served
- requests are handled in the same order as given
- there is no sorting
- disk head moves from the current position to each request
- total seek time is the total distance travelled by the head

seek movement:

movement = abs(current head - requested track)

total seek = sum of all movements

average seek = total seek / number of requests
"""