def lru_page_replacement(pages, frame_count):
    """
    LRU Page Replacement Algorithm

    LRU = Least Recently Used

    It replaces the page which has not been
    used for the longest time.
    """

    frames = []

    page_faults = 0
    page_hits = 0

    steps = []

    for i in range(len(pages)):

        page = pages[i]

        # check if page is already present
        if page in frames:

            page_hits += 1

            steps.append({
                "page": page,
                "frames": frames.copy(),
                "status": "Hit"
            })

        else:

            page_faults += 1

            # if there is an empty frame
            if len(frames) < frame_count:

                frames.append(page)

            else:

                # find the page that was used
                # least recently
                least_recent = float("inf")
                page_to_replace = None

                for frame_page in frames:

                    # find previous use of this page
                    previous_uses = [
                        j
                        for j in range(i)
                        if pages[j] == frame_page
                    ]

                    # choose page that was used
                    # farthest back
                    if len(previous_uses) == 0:

                        previous_use = -1

                    else:

                        previous_use = previous_uses[-1]

                    if previous_use < least_recent:

                        least_recent = previous_use
                        page_to_replace = frame_page

                # replace the least recently used page
                replace_index = frames.index(
                    page_to_replace
                )

                frames[replace_index] = page

            steps.append({
                "page": page,
                "frames": frames.copy(),
                "status": "Page Fault"
            })

    # calculate rates
    total_pages = len(pages)

    page_fault_rate = (
        page_faults / total_pages
    ) * 100

    page_hit_rate = (
        page_hits / total_pages
    ) * 100

    return {
        "steps": steps,
        "page_faults": page_faults,
        "page_hits": page_hits,
        "page_fault_rate": page_fault_rate,
        "page_hit_rate": page_hit_rate
    }


if __name__ == "__main__":

    # same page reference string as FIFO
    # and Optimal
    pages = [
        4, 3, 2, 1,
        4, 3, 5,
        4, 3, 2, 1, 5
    ]

    # number of frames
    frame_count = 3

    result = lru_page_replacement(
        pages,
        frame_count
    )

    print("\nLRU PAGE REPLACEMENT")
    print("-" * 50)

    print("Page Reference String:", pages)
    print("Number of Frames:", frame_count)

    print("\nPage\tFrames\t\tStatus")
    print("-" * 50)

    for step in result["steps"]:

        print(
            step["page"],
            "\t",
            step["frames"],
            "\t",
            step["status"]
        )

    print("\nTotal Page Faults:",
          result["page_faults"])

    print("Total Page Hits:",
          result["page_hits"])

    print(
        "Page Fault Rate:",
        round(result["page_fault_rate"], 2),
        "%"
    )

    print(
        "Page Hit Rate:",
        round(result["page_hit_rate"], 2),
        "%"
    )


"""
LRU PAGE REPLACEMENT

LRU = Least Recently Used

Logic:

1. Check whether the page is already present.

2. If present:
   -> Hit

3. If not present:
   -> Page Fault

4. If an empty frame is available:
   -> Insert the new page.

5. If all frames are full:
   -> Look at the previous page references.

6. Find the page which was used least recently.

7. Replace that page.

Example:

Frames = [4, 3, 2]

If a new page comes and:

4 -> used recently
3 -> used recently
2 -> not used for a long time

Then 2 is replaced.

LRU looks at the PAST.

Optimal looks at the FUTURE.

FIFO only looks at the ORDER in which
pages entered the frames.

Page Fault Rate =
(Page Faults / Total Page References) * 100

Page Hit Rate =
(Page Hits / Total Page References) * 100

Important:

LRU does NOT suffer from Belady's Anomaly.
"""