import time

def stop_watch():
    print("Stopwatch started. Press Ctrl+C to stop.")
    start_time = time.time()
    try:
        while True:
            elapsed_time = time.time() - start_time
            print(f"\rElapsed Time: {int(elapsed_time)} seconds", end="")
            time.sleep(1)
    except KeyboardInterrupt:   
        print(f"\nStopwatch stopped. time elapsed {round(elapsed_time)}, seconds")

stop_watch()





