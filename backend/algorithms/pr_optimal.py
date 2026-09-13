def optimal_page_replacement(pages, frame_count):
    """
    Optimal Page Replacement Algorithm

    Optimal replaces the page that will be used
    farthest in the future.
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

                # find the page which will be used
                # farthest in the future
                farthest = -1
                page_to_replace = None

                for frame_page in frames:

                    # check where this page will be
                    # used next
                    if frame_page in pages[i + 1:]:

                        next_use = pages[i + 1:].index(
                            frame_page
                        )

                    else:

                        # page is not used again
                        next_use = float("inf")

                    # choose the page used farthest
                    # in the future
                    if next_use > farthest:

                        farthest = next_use
                        page_to_replace = frame_page

                # replace that page
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
    pages = [
        4, 3, 2, 1,
        4, 3, 5,
        4, 3, 2, 1, 5
    ]

    # number of frames
    frame_count = 3

    result = optimal_page_replacement(
        pages,
        frame_count
    )

    print("\nOPTIMAL PAGE REPLACEMENT")
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
OPTIMAL PAGE REPLACEMENT

Logic:

1. Check whether the page is already present.

2. If present:
   -> Hit

3. If not present:
   -> Page Fault

4. If an empty frame is available:
   -> Insert the new page.

5. If all frames are full:
   -> Look at future page references.

6. Find which page in the frames will be
   used farthest in the future.

7. Replace that page.

8. If a page will never be used again,
   replace that page immediately.

Example:

Frames = [4, 3, 2]

Suppose page 1 comes.

Look at the future:

4 -> used soon
3 -> used later
2 -> used farthest

So 2 can be replaced.

Optimal gives the minimum possible
number of page faults.

Page Fault Rate =
(Page Faults / Total Page References) * 100

Page Hit Rate =
(Page Hits / Total Page References) * 100

Important:

Optimal needs to know the future page references.

Therefore, it is mainly used as a benchmark
to compare other page replacement algorithms.

Unlike FIFO, Optimal does NOT suffer
from Belady's Anomaly.
"""