def lru_page_replacement(pages, frame_count):
    """
    LRU Page Replacement Algorithm.

    Replaces the page that has not been used
    for the longest time.
    """

    frames = []

    page_faults = 0
    page_hits = 0

    steps = []

    for i in range(len(pages)):

        page = pages[i]

        # check if the page is already in the frames
        if page in frames:

            page_hits += 1

            steps.append({
                "page": page,
                "frames": frames.copy(),
                "status": "Hit"
            })

        else:

            page_faults += 1

            # use an empty frame if available
            if len(frames) < frame_count:

                frames.append(page)

            else:

                # find the page that was used least recently
                least_recent = float("inf")
                page_to_replace = None

                for frame_page in frames:

                    # find the most recent previous use
                    previous_uses = [
                        j
                        for j in range(i)
                        if pages[j] == frame_page
                    ]

                    if len(previous_uses) == 0:

                        previous_use = -1

                    else:

                        previous_use = previous_uses[-1]

                    # choose the page used farthest in the past
                    if previous_use < least_recent:

                        least_recent = previous_use
                        page_to_replace = frame_page

                # replace the least recently used page
                replace_index = frames.index(page_to_replace)
                frames[replace_index] = page

            steps.append({
                "page": page,
                "frames": frames.copy(),
                "status": "Page Fault"
            })

    # calculate page fault and hit rates
    total_pages = len(pages)

    page_fault_rate = (page_faults / total_pages) * 100
    page_hit_rate = (page_hits / total_pages) * 100

    return {
        "steps": steps,
        "page_faults": page_faults,
        "page_hits": page_hits,
        "page_fault_rate": page_fault_rate,
        "page_hit_rate": page_hit_rate
    }