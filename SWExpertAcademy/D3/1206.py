for i in range(10):
    T = int(input())
    apartment = list(map(int, input().split()))
    view = 0
    larger = 0
    for j in range(2, len(apartment)-2):
        larger = apartment[j] - max(apartment[j-2],
                                    apartment[j-1], apartment[j+1], apartment[j+2])
        if larger > 0:
            view += larger
    print("#{0} {1}".format(i+1, view))
