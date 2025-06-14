import queue
import time
import random
import uuid # For unique IDs

# Create a request queue
request_queue = queue.Queue()

# Counter for simple IDs, if uuid is not needed
request_counter = 0

def generate_request():
    """
    Generates a new request and adds it to the queue.
    The request is identified by a unique ID.
    """
    global request_counter
    request_counter += 1
    request_id = f"Request #{request_counter}"
    request_data = {"id": request_id, "data": f"Details for request {request_id}"}
    
    request_queue.put(request_data)
    print(f"New request '{request_id}' added to the queue.")

def process_request():
    """
    Processes a request from the queue (if it is not empty).
    """
    if not request_queue.empty():
        # Remove a request from the queue
        current_request = request_queue.get()
        request_id = current_request["id"]
        print(f"Processing request '{request_id}'...")
        # Simulate processing
        time.sleep(random.uniform(0.5, 1.5)) # Simulate processing time
        print(f"Request '{request_id}' processed.")
        request_queue.task_done() # Mark the task as done (for join)
    else:
        print("The queue is empty. No requests to process.")

def main_simulation_loop_interactive():
    """Main program loop with interactive control."""
    print("Request processing system started.")
    print("Enter 'g' to generate a request, 'p' to process, 'q' to quit.")
    
    try:
        while True:
            user_input = input("Your command (g/p/q): ").strip().lower()
            
            if user_input == 'g':
                generate_request()
            elif user_input == 'p':
                process_request()
            elif user_input == 'q':
                print("Exiting the program.")
                break
            else:
                print("Unknown command. Try 'g', 'p' or 'q'.")
            
            print(f"Requests in queue: {request_queue.qsize()}")
            time.sleep(0.1) # Small wait for better perception
            
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    finally:
        # You can add logic to process remaining requests if needed
        if not request_queue.empty():
            print(f"There are {request_queue.qsize()} unprocessed requests left in the queue.")
        print("System operation completed.")

def main_simulation_loop_automatic():
    """Main program loop with automatic generation and processing."""
    print("Automatic request processing system started (Ctrl+C to exit).")
    
    try:
        while True:

            if random.random() < 0.7: # 70% chance to generate
                generate_request()
            
            # Process a request if there is something to process
            if not request_queue.empty():
                 # With a certain probability, if there are requests, process one
                if random.random() < 0.5 or request_queue.qsize() > 5: # 50% chance or if the queue is large
                    process_request()
            else:
                print("The queue is empty, waiting for new requests...")
            
            print(f"Requests in queue: {request_queue.qsize()}")
            time.sleep(random.uniform(0.5, 2)) # Pause between iterations

    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    finally:
        print("Automatic system operation completed.")
        print(f"Left in queue: {request_queue.qsize()}")


def run_automatic_demo(iterations=10):
    print("Demonstration of the automatic request processing system.")
    global request_counter # Reset the counter for a new run
    request_counter = 0
    while not request_queue.empty(): # Clear the queue if there is something
        request_queue.get()
        request_queue.task_done()

    for i in range(iterations):
        print(f"\n--- Iteration {i+1}/{iterations} ---")
        if random.random() < 0.8: # 80% chance to generate
            generate_request()
        
        if not request_queue.empty():
            if random.random() < 0.6 or request_queue.qsize() > 2:
                process_request()
        else:
            print("The queue is empty in this iteration.")
        
        print(f"Requests in queue: {request_queue.qsize()}")
        time.sleep(0.5)
    print("\nDemonstration completed.")
    print(f"Left in queue after demo: {request_queue.qsize()}")


print("--- Task 1: Request Processing Simulator ---")
run_automatic_demo(15) # Run the demo for 15 iterations