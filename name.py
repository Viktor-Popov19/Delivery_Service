#156840061
def min_platforms(robots: list, limit: int) -> int:
    """
    Вычисляет минимальное количество платформ для перевозки роботов.

    Параметры:
        robots: список весов роботов
        limit: грузоподъёмность одной платформы

    Возвращает:
        минимальное количество платформ
    """
    robots.sort()
    left = 0
    right = len(robots) - 1
    platforms = 0

    while left <= right:
        if robots[left] + robots[right] <= limit:
            left += 1
        right -= 1
        platforms += 1

    return platforms


if __name__ == "__main__":
    with open('input.txt', 'r', encoding='utf-8') as file_in:
        robots = list(map(int, file_in.readline().split()))
        limit = int(file_in.readline())

    result = min_platforms(robots, limit)

    with open('output.txt', 'w', encoding='utf-8') as file_out:
        file_out.write(str(result))