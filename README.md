# OS Algorithm Simulator

A learning-focused project where I'm implementing **Operating System algorithms** while practicing **DSA concepts** alongside them.

The main goal is to understand how these algorithms work by implementing them myself, testing different inputs, and connecting the algorithms to a backend API.

## 🛠️ Technologies & Languages

* **Python** — Algorithm implementation and backend development
* **FastAPI** — Building the backend API
* **Pydantic** — Request data validation
* **Uvicorn** — Running the FastAPI application
* **Git & GitHub** — Version control and project management
* **Swagger / OpenAPI** — Testing and documenting the API

## ⚙️ CPU Scheduling

* FCFS (First Come First Serve)
* SJF (Shortest Job First)
* SRTF (Shortest Remaining Time First)
* Priority Scheduling (Non-Preemptive)
* Round Robin (Preemptive)

## 💿 Disk Scheduling

* FCFS (First Come First Serve)
* SSTF (Shortest Seek Time First)
* SCAN (Elevator Algorithm) — Standard & Professor's Version
* C-SCAN (Circular SCAN) — Standard & Professor's Version

## 🧠 Page Replacement

* FIFO (First In First Out)
* Optimal Page Replacement
* LRU (Least Recently Used)

## 🔒 Deadlock

* Banker's Algorithm
* Resource Allocation Graph (RAG)

## 🧩 DSA Concepts I'm Practicing

While implementing these algorithms, I'm also practicing:

* Arrays / Lists
* Queues
* Priority Queues
* Sorting
* Searching
* Heaps
* Graphs
* Resource Allocation
* Process Scheduling

## 🚀 Backend API

The algorithms are being connected to a **FastAPI backend** so they can be tested through API requests.

Current API sections:

```text
/api/cpu
/api/disk
```

FastAPI automatically provides interactive API documentation through **Swagger UI**, making it easier to test different inputs while developing the simulator.

## 📌 Project Status

### Completed

* CPU scheduling algorithms implemented
* CPU scheduling API endpoints
* Pydantic request validation
* Disk FCFS API
* Disk SSTF API
* Standard & professor-specific SCAN/C-SCAN logic
* Page replacement algorithms
* Deadlock algorithms
* Git/GitHub version control

### In Progress

* Connecting remaining disk algorithms to the API
* Expanding API structure for page replacement and deadlock algorithms

## 🔮 Future Improvements

As I learn more, I plan to gradually add:

* Interactive frontend for running algorithms
* Gantt chart visualization for CPU scheduling
* Disk head movement visualization
* Page replacement frame visualization
* Step-by-step algorithm execution
* More detailed performance metrics
* Better API structure and documentation
* Database integration for saving simulations
* User-friendly input forms
* Dockerization and deployment

## 🎯 Goal

This is mainly a **learning and practice project**.

I'm building it step by step while learning Operating Systems, DSA, backend development, and API design.

The project will continue to evolve as I learn and implement more concepts.
