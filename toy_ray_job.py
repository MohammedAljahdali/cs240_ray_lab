import ray
import time
import random


# Connect to the Ray cluster
# TODO: change this to the address of your Ray cluster. Otherwise it will create a local ray cluster
address = None  # E.g. "ray://52.57.207.94:10001"
ray.init(address)


@ray.remote(resources={"cpu": 1})
def my_task(x):
    time.sleep(x + 25)
    return x * x


futures = [my_task.remote(random.randint(5, 35)) for _ in range(6)]
print("Waiting for tasks to complete...")
while futures:
    # Wait for the next task to complete.
    done_id, futures = ray.wait(futures)
    print("Got result:", ray.get(done_id), "For task:", done_id)
    print(ray.get(done_id))

print(ray.get(futures))
