import math
import operator


def postman():
    x = 0
    data = []
    result = {}
    points = []
    while x != 228:
        print("В случае, если Вы хотите прекратить ввод координат, введите 228\nВведите значение координаты х:")
        x = int(input())
        if x != 228:
            print("Введите значение координаты у:")
            y = int(input())
            data.append([x,y])
    for i in data:
        for l in data:
            if i != l:
                point = f'({i})->({l})'
                if f'({l})->({i})' not in points:
                    points.append(point)
                    distance = math.sqrt(pow((l[0]-i[0]),2)+pow((l[1]-i[1]),2))
                    result[point] = distance
    result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
    result = {k: v for k, v in result}
    print(result)


if __name__ == '__main__':
    postman()
