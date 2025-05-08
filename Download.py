import threading
import requests
import time

def d(u, i):
    r = requests.get(u)
    with open(f"file{i}.bin", "wb") as f:
        f.write(r.content)

if __name__ == "__main__":
    with open("urls.txt") as f:
        u = f.read().splitlines()

    t1 = time.time()
    for i, x in enumerate(u):
        d(x, i)
    print("Sequential Time:", time.time() - t1)

    t2 = time.time()
    ts = []
    for i, x in enumerate(u):
        t = threading.Thread(target=d, args=(x, i))
        ts.append(t)
        t.start()
    for t in ts:
        t.join()
    print("Concurrent Time:", time.time() - t2)
