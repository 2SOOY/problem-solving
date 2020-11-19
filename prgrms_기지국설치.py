# 기지국 설치
# https://programmers.co.kr/learn/courses/30/lessons/12979

import math

def get_empty_section(n, stations, w):
    result = []
    first = stations[0]
    last = stations[-1]

    # 처음 구간
    if first - w > 0:
        result.append((0, first-w-1))

    # 중간 구간
    for i in range(len(stations) - 1):
        start = stations[i] + w + 1
        end = stations[i + 1] - w - 1
        result.append((start, end))

    # 마지막 구간
    if last + w < n - 1:
        result.append((last + w + 1, n - 1))

    return result


def build_station(n, w, sections):
    result = 0

    for start, end in sections:
        section_size = end - start + 1
        coverage = 2*w + 1 # 기지국을 세우면 본인포함 양옆으로 w만큼 적용
        result += math.ceil(section_size / coverage)

    return result


def solution(n, stations, w):
    answer = 0
    stations = [station - 1 for station in stations] # index 처리 편리하게 하기 위한 조작
    sections = get_empty_section(n, stations, w)
    answer = build_station(n, w, sections)

    return answer

n = 11
stations = [4, 11]
w = 1
print(solution(n, stations, w))