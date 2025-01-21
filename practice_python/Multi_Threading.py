import threading
import time
from concurrent.futures import ThreadPoolExecutor

def resturentOrder(dish = 'Paneer Lababdar', timeinterval = 30):
    print(f'Item {dish} will ready in {timeinterval} seconds')
    time.sleep(timeinterval)

def normal_call():
    time_start = time.perf_counter()

    resturentOrder("Paneer Batar masala", 10)
    resturentOrder("Dalmakhni", 5)
    resturentOrder("Butter naan", 4)
    resturentOrder("Laccha Paratha", 6)
    print("All items are ready!!!")

    time_end = time.perf_counter()
    print(f"Total time taken to complete the order is {time_end -time_start}")

# Normally time taken for complete the full order
# normal_call()



def Call_using_thread():
    time_start = time.perf_counter()

    thread1  = threading.Thread(target=resturentOrder, args=["Paneer Batar masala", 10])
    thread2 = threading.Thread(target=resturentOrder, args=["Dalmakhni", 5])
    thread3 = threading.Thread(target=resturentOrder, args=["Butter naan", 4])
    thread4 = threading.Thread(target=resturentOrder, args=["Laccha Paratha", 6])

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    print("All items are ready!!!")

    time_end = time.perf_counter()
    print(f"Total time taken to complete the order is {time_end -time_start}")

# Time taken for complete the full order using Thread
# Call_using_thread()


def call_using_concurrent_future():
    time_start = time.perf_counter()

    with ThreadPoolExecutor() as executer:
        future1 = executer.submit(resturentOrder, "Paneer Batar masala", 10)
        future2 = executer.submit(resturentOrder, "Dalmakhni", 5)
        future3 = executer.submit(resturentOrder, "Butter naan", 4)
        future4 = executer.submit(resturentOrder, "Laccha Paratha", 6)
        future1.result()
        future2.result()
        future3.result()
        future4.result()

    print("All items are ready!!!")

    time_end = time.perf_counter()
    print(f"Total time taken to complete the order is {time_end -time_start}")
    


# Time taken for complete the full order using Concurrent future
# call_using_concurrent_future()



def call_concurrent_future_using_map():
    time_start = time.perf_counter()

    with ThreadPoolExecutor() as executer:
        items_list = ["Paneer Batar masala", "Dalmakhni", "Butter naan", "Laccha Paratha"]
        items_time_taken_list = [10, 5,4,6]
        # executer.map(resturentOrder, items_list, items_time_taken_list)

        results = executer.map(resturentOrder, items_list, items_time_taken_list)
        for i, _ in enumerate(results):
            print(f"Item {items_list[i]} is Ready")

    print("All items are ready!!!")

    time_end = time.perf_counter()
    print(f"Total time taken to complete the order is {time_end -time_start}")
    


# Time taken for complete the full order using Concurrent future
# call_concurrent_future_using_map()