def fifo_page_replacement(pages, frame_count):
    """
    FIFO Page Replacement Algorithm.

    Replaces the page that entered the frames first.
    """

    frames = []
    pointer = 0

    page_faults = 0
    page_hits = 0

    steps = []

    for page in pages:

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

                # replace the oldest page
                frames[pointer] = page

                # move to the next frame
                pointer = (pointer + 1) % frame_count

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