def optimal_page_replacement(pages, frame_count):
    """
    Optimal Page Replacement Algorithm.

    Replaces the page that will be used farthest
    in the future.
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

                # find the page that will be used farthest ahead
                farthest = -1
                page_to_replace = None

                for frame_page in frames:

                    # check when this page will be needed again
                    if frame_page in pages[i + 1:]:

                        next_use = pages[i + 1:].index(frame_page)

                    else:

                        # replace the page if it will not be used again
                        next_use = float("inf")

                    # choose the page needed farthest in the future
                    if next_use > farthest:

                        farthest = next_use
                        page_to_replace = frame_page

                # replace the selected page
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