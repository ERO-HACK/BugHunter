import time
import sys

def show_timer(total_steps, task_name="Task"):
    estimated_time = total_steps * 0.5
    print(f"{task_name} in progress... Estimated time: {estimated_time:.1f} seconds")
    for i in range(total_steps):
        sys.stdout.write(f"\rProgress: {i+1}/{total_steps}")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\n")
