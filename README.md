# OS Algorithm Simulator

A learning-focused project where I'm implementing **Operating System algorithms** while practicing **DSA concepts** alongside them.

The main goal is to understand how these algorithms work by implementing them myself, testing different inputs, and connecting them to a backend API.

## Technologies & Languages

- **Python** — Algorithm implementation and backend development
- **FastAPI** — Building the backend API
- **Pydantic** — Request data validation
- **Uvicorn** — Running the FastAPI application
- **Git & GitHub** — Version control and project management
- **Swagger / OpenAPI** — Testing and documenting API endpoints

## CPU Scheduling

- FCFS (First Come First Serve)
- SJF (Shortest Job First)
- SRTF (Shortest Remaining Time First)
- Priority Scheduling (Non-Preemptive)
- Round Robin (Preemptive)

## Disk Scheduling

- FCFS (First Come First Serve)
- SSTF (Shortest Seek Time First)
- SCAN (Elevator Algorithm) — Standard & Professor's Version
- C-SCAN (Circular SCAN) — Standard & Professor's Version

## Page Replacement

- FIFO (First In First Out)
- Optimal Page Replacement
- LRU (Least Recently Used)

## Deadlock

- Banker's Algorithm
- Resource Allocation Graph (RAG) — Matrix-based deadlock detection

## DSA Concepts I'm Practicing

While implementing these algorithms, I'm also practicing:

- Arrays / Lists
- Queues
- Priority Queues
- Sorting
- Searching
- Heaps
- Graphs
- Resource Allocation
- Process Scheduling

## Backend API

All the implemented algorithms are now connected to a **FastAPI backend**.

The API is divided into four sections:

```text
/api/cpu
/api/disk
/api/page-replacement
/api/deadlock
```

FastAPI automatically provides interactive API documentation through **Swagger UI**, where I can test different inputs and check the algorithm outputs.

To run the backend locally:

```bash
cd backend
.\venv\Scripts\activate
uvicorn main:app --reload
```

Open the following URL to access the API documentation:

```text
http://127.0.0.1:8000/docs
```

## Project Status

### Completed

- Implemented all CPU scheduling algorithms
- Connected CPU scheduling algorithms to API endpoints
- Implemented Pydantic request validation
- Implemented disk scheduling algorithms
- Added standard and professor-specific SCAN and C-SCAN logic
- Connected disk scheduling algorithms to API endpoints
- Implemented FIFO, Optimal and LRU page replacement
- Connected page replacement algorithms to API endpoints
- Implemented Banker's Algorithm
- Implemented matrix-based deadlock detection
- Connected deadlock algorithms to API endpoints
- Tested API endpoints using Swagger UI

### Next Steps

- Build an interactive frontend
- Connect the frontend to the FastAPI backend
- Add Gantt chart visualization for CPU scheduling
- Add disk head movement visualization
- Visualize page replacement using frames
- Show deadlock detection and safe sequences
- Add step-by-step algorithm execution
- Display performance metrics and comparisons

## Future Improvements

As I continue learning, I would also like to explore:

- Better input forms and validation
- Database integration for saving simulations
- Dockerization
- Deployment

## Goal

This is mainly a learning and practice project.

I'm building it step by step while learning Operating Systems, DSA, backend development, and API design.

There's still a lot I want to explore and improve, especially when it comes to visualizing how these algorithms actually work.
