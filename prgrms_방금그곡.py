# 방금 그 곡
# https://programmers.co.kr/learn/courses/30/lessons/17683

IMPOSSIBLE = '(None)'
note_table = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a',}
TIME, TITLE, START, MELODY = 0, 1, 2, 3

# 재생시간 구하는 함수
# 분 단위로 계산 => 문제 조건
def get_play_time(start, end):
    answer = 0
    s_hour, s_min = start.split(':')
    e_hour, e_min = end.split(':')

    play_hour = int(e_hour) - int(s_hour)
    play_min = int(e_min) - int(s_min)

    answer = (play_hour * 60) + play_min # 1HOUR = 60MIN
    return answer


# []# 형태의 음표들 소문자로 변환하기
# replace를 활용하면 쉽게 바꿀 수 있다. (대신 #개수 만큼 반복해야함)
def transform_notes(notes):
    result = ''
    for i in range(len(notes) - 1):
        temp = notes[i: i+2] # 2개씩 묶어서 비교하기

        if temp in note_table:
            result += note_table[temp]
        else:
            if notes[i] == '#':
                continue
            result += notes[i]
    
    # 마지막 note에 대한 처리
    if notes[-1] != '#':
        result += notes[-1]

    return result


# 주어진 음악 정보 => 재생시간, 제목, 시작시간, 재생되는 음표
def transform_music_infos(music_infos):
    result = []

    for start, end, title, notes in music_infos:
        play_notes = '' # 해당 시간동안 재생되는 음표들
        play_time = get_play_time(start, end) # 재생시간
        notes = transform_notes(notes) # '#'붙은 음표들 변환
        start = int(''.join(start.split(':'))) # 시작시간 정보를 추가한 이유 => 동일한 재생시간 => 일찍 입력된 순서가 답
        
        for i in range(play_time):
            play_notes += notes[i % len(notes)]    

        result.append((play_time, title, start, play_notes))

    return result


# 기억 멜로디가 존재하는 음악 정보를 찾는 함수
def get_matched_music(memory, music_infos):
    result = []

    for music in music_infos:
        _, _, _, notes = music
        if memory in notes:
            result.append((music))

    return result


# MAIN
def solution(memory, music_infos):
    memory = transform_notes(memory)
    music_infos = [music.split(',') for music in music_infos]
    music_infos = transform_music_infos(music_infos)
    
    matched = get_matched_music(memory, music_infos)
    
    if not matched:
        return IMPOSSIBLE
    
    if len(matched) == 1:
        return matched[0][TITLE]

    # 가능한 후보들이 여러개 일때
    # 재생시간 긴 순 -> 입력 시간이 이른 순
    matched.sort(key= lambda x: (x[TIME], -x[START]))

    return matched[-1][TITLE]


memory = "ABC" 
music_infos = ["12:00,12:14,HELLO,CD#E#FGAB", "13:00,13:14,WORLD,ABCDEF"]
print(solution(memory, music_infos))