# Step-by-Step Flow of Asynchronous Execution
## Task Submission:

A task is defined in the Celery app using @shared_task or app.task.
The application submits the task to the broker:
python
Copy code
result = resize_image.delay('input.jpg', 'output.jpg', (300, 300))
Celery serializes the task (arguments, task name, etc.) and sends it to the broker as a message.

# Message Queuing:

The broker queues the task in a designated queue.
The queue acts as a buffer for pending tasks.

## Worker Retrieval:

A Celery worker listens to the queue for new messages.
When a task arrives, the worker retrieves the task, deserializes it, and executes it.
Task Execution:

The worker runs the task function (e.g., resize_image) with the provided arguments.
Execution happens independently of the task producer, so the main application remains free to continue processing other requests.



## Diagram

Main App          Message Broker           Worker
  |                    |                     |
  | .delay(task)       |                     |
  | -----------------> |                     |
  |                    |  Task Queued        |
  |                    | ----------------->  |
  |                    |                     | Task Executed
  |                    | <------------------ |
  |                    |                     | Result Sent to Backend
  |                    |                     |



# How Celery Achieves Asynchronous Execution
## Task Serialization:

When a task is submitted, Celery serializes the task name, arguments, and options into a message.
Default serialization formats: JSON or pickle.

## Concurrency with Workers:

Workers use concurrency mechanisms like threads, processes, or event loops (via libraries like gevent or eventlet).
Workers can handle multiple tasks simultaneously depending on the concurrency level.

## Non-blocking Nature:

The main application does not wait for task execution to complete.
Instead, it receives a task ID to track the task asynchronously.
Event Loop for Tasks:

Celery workers have an event loop that continuously listens for new tasks from the broker.
When a task is received, the event loop dispatches it to a worker thread or process.

## Scalability:

Multiple workers can listen to the same broker, enabling task distribution across multiple machines or processes.



# Why Asynchronous Execution is Important
## Non-blocking Operations:

The main application (e.g., a web server) can handle other user requests while tasks are processed in the background.
Improved Performance:

Asynchronous tasks prevent heavy computations from delaying critical user-facing operations.
## Scalability:

Celery allows you to scale task execution by adding more workers or machines.
Fault Tolerance:

If a task fails, it can be retried automatically without affecting the main application.

celery -A app worker --loglevel=info



redis-cli keys "*"

redis-cli GET "5174e4d6-ed93-4799-92d4-789d7757d7ec"
