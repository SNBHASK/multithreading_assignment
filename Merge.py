import threading
import time

def merge(a):
    if len(a) <= 1:
        return a
    m = len(a) // 2
    l = a[:m]
    r = a[m:]

    def sort_l():
        l[:] = merge(l)

    def sort_r():
        r[:] = merge(r)

    t1 = threading.Thread(target=sort_l)
    t2 = threading.Thread(target=sort_r)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    return combine(l, r)

def combine(l, r):
    o = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            o.append(l[i])
            i += 1
        else:
            o.append(r[j])
            j += 1
    o += l[i:]
    o += r[j:]
    return o

if __name__ == "__main__":
    a = [9, 2, 4, 7, 3, 6, 1, 5]
    print("Original:", a)
    t = time.time()
    a = merge(a)
    print("Sorted:", a)
    print("Time:", time.time() - t)
