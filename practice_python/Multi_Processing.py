import requests
import time
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

url = "https://picsum.photos/5000/4000"

def downloadFile(url, name):
    print(f"The downloading process started for {name} file!!!")

    response = requests.get(url)
    open(f"images/image{name}.jpg", 'wb').write(response.content)

    print(f"The downloading process completed for {name} file!!!")


def normal_call(url):
    time_start = time.perf_counter()
    for i in range(5):
        downloadFile(url, i)
    time_end = time.perf_counter()

    print(f'Time taken to complete this process is {time_end - time_start}')

# normal_call(url)



def multiProcessing(url):
    time_start = time.perf_counter()
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=downloadFile, args=[url, i])
        p.start()
        processes.append(p)

    for pr in processes:
        pr.join()

    time_end  = time.perf_counter()
    print(f"Time taken for completing this process is {time_end-time_start}")

# if __name__== "__main__":
#     multiProcessing(url)






def processPoolExecuter(url):
    with ProcessPoolExecutor() as executer:
        list_url = [url for i in range(5)]
        list_name = [i for i in range(5)]

        results = executer.map(downloadFile, list_url, list_name)
        for res in results:
            print(res)
    
# if __name__=="__main__":
#     processPoolExecuter(url)

