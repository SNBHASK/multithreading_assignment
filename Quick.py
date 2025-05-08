import threading
import time

def q(a, l, r):
    if l < r:
        p = part(a, l, r)
        t1 = threading.Thread(target=q, args=(a, l, p - 1))
        t2 = threading.Thread(target=q, args=(a, p + 1, r))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

def part(a, l, r):
    x = a[r]
    i = l - 1
    for j in range(l, r):
        if a[j] < x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1

if __name__ == "__main__":
    a = [9, 2, 4, 7, 3, 6, 1, 5]
    print("Original:", a)
    t = time.time()
    q(a, 0, len(a) - 1)
    print("Sorted:", a)
    print("Time:", time.time() - t)
