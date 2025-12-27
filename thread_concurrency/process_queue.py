from multiprocessing import Process, Queue
import time

def prepare_chai(queue):
    queue.put("Masala Chai")

queue = Queue()

chai_maker = Process(target=prepare_chai, args=(queue, ))
chai_maker.start()
chai_maker.join()

print(f"Chai Prepared: {queue.get()}")