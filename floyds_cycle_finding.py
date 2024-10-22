def floyd_cycle_detection(f, start):
    tortoise = start
    hare = start

    while True:
        tortoise = f[tortoise]
        hare = f[f[hare]]
        if tortoise == hare:
            break

    tortoise = start
    while tortoise != hare:
        tortoise = f[tortoise]
        hare = f[hare]

    cycle_start = tortoise

    cycle_length = 1
    hare = f[tortoise]
    while tortoise != hare:
        hare = f[hare]
        cycle_length += 1

    return cycle_start, cycle_length


if __name__ == '__main__':
    f = [6, 6, 0, 1, 4, 3, 6, 3, 0]
    start = 2

    cycle_start, cycle_length = floyd_cycle_detection(f, start)
    print(cycle_start, cycle_length)
