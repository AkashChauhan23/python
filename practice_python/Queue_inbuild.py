from queue import Queue, LifoQueue, PriorityQueue


print("\nQueue >>>>> ")
q = Queue()
q.put("Akash")
q.put("Mahima")
q.put("Shaul")
q.put("Ditya")

while not q.empty():
    print(q.get())


print("\nLifoQueue >>>>> ")
lq = LifoQueue()
lq.put("Chauhan")
lq.put("Gupta")

while not lq.empty():
    print(lq.get())


print("\nPriorityQueue >>>>> ")
pq = PriorityQueue()
pq.put((2, "Akash"))
pq.put((3, "Varsha"))
pq.put((1, "Shalu"))
pq.put((0, "Chauhan"))

while not pq.empty():
    print(pq.get())