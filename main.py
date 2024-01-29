import heapq


def main():
    cable_lenghts = [7, 3, 35, 12, 5, 15, 4, 9, 2, 10, 12, 2, 3, 25, 10]
    total_cost = 0

    print("Cable lengths: ", cable_lenghts)
    heapq.heapify(cable_lenghts)

    while len(cable_lenghts) > 1:
        first = heapq.heappop(cable_lenghts)
        second = heapq.heappop(cable_lenghts)
        new_cable_length = first + second

        total_cost += new_cable_length
        heapq.heappush(cable_lenghts, new_cable_length)

    print("Total cost: ", total_cost)
    print("Length of gotten cable: ", heapq.heappop(cable_lenghts))


if __name__ == "__main__":
    main()
