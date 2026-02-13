#156913842
def min_platforms(robots: list[int], limit: int) -> int:
    """
    Вычисляет минимальное количество платформ для перевозки роботов.

    Параметры:
        robots: список весов роботов
        limit: грузоподъёмность одной платформы

    Возвращает:
        минимальное количество платформ
    """
    sorted_robots = sorted(robots)
    left = 0
    right = len(sorted_robots) - 1
    platforms = 0

    while left <= right:
        if sorted_robots[left] + sorted_robots[right] <= limit:
            left += 1
        right -= 1
        platforms += 1

    return platforms


if __name__ == "__main__":
    robots: list[int] = list(map(int, input().split()))
    limit: int = int(input())

    result: int = min_platforms(robots, limit)
    print(result)