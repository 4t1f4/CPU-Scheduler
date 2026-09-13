def fifo_page_replacement(pages, frame_count):
    """
    FIFO Page Replacement Algorithm

    pages = page reference string
    frame_count = number of frames

    FIFO removes the page that entered first.
    """

    frames = []

    pointer = 0

    page_faults = 0
    page_hits = 0

    steps = []

    for page in pages:

        # check if page is already present
        if page in frames:

            page_hits += 1

            steps.append({
                "page": page,
                "frames": frames.copy(),
                "status": "Hit"
            })

        else:

            # page is not present
            page_faults += 1

            # if there is an empty frame
            if len(frames) < frame_count:

                frames.append(page)

            else:

                # replace the oldest page
                frames[pointer] = page

                # move pointer to next frame
                pointer = (pointer + 1) % frame_count

            steps.append({
                "page": page,
                "frames": frames.copy(),
                "status": "Page Fault"
            })

    # calculate page fault rate
    total_pages = len(pages)

    page_fault_rate = (page_faults / total_pages) * 100

    # calculate page hit rate
    page_hit_rate = (page_hits / total_pages) * 100

    return {
        "steps": steps,
        "page_faults": page_faults,
        "page_hits": page_hits,
        "page_fault_rate": page_fault_rate,
        "page_hit_rate": page_hit_rate
    }


if __name__ == "__main__":

    # page reference string
    pages = [
        4, 3, 2, 1,
        4, 3, 5,
        4, 3, 2, 1, 5
    ]

    # number of frames
    frame_count = 3

    result = fifo_page_replacement(
        pages,
        frame_count
    )

    print("\nFIFO PAGE REPLACEMENT")
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

    print("Page Fault Rate:",
          round(result["page_fault_rate"], 2),
          "%")

    print("Page Hit Rate:",
          round(result["page_hit_rate"], 2),
          "%")


"""
FIFO PAGE REPLACEMENT

Logic:

1. Check whether the page is already present.

2. If present:
   -> Hit

3. If not present:
   -> Page Fault

4. If an empty frame is available:
   -> Insert the new page.

5. If all frames are full:
   -> Replace the page that entered first.

6. Pointer moves to the next frame
   after replacement.

Page Fault Rate =
(Page Faults / Total Page References) * 100

Page Hit Rate =
(Page Hits / Total Page References) * 100

Page Fault Rate + Page Hit Rate = 100%

FIFO only checks which page entered first.
"""




"""
BELADY'S ANOMALY

Belady's Anomaly is a drawback of FIFO page replacement.

Normally, we expect:
More frames -> fewer page faults

But in FIFO, sometimes:
More frames -> MORE page faults

Example:

For some page reference strings:

3 frames  -> 9 page faults
4 frames  -> 10 page faults

So, increasing the number of frames
can unexpectedly increase page faults.

This happens because FIFO removes the page
that entered first, without considering
whether that page will be needed again.

Important:
Belady's Anomaly can occur in FIFO,
but it does not occur in Optimal or LRU.
"""
