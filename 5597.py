# set이란 자료형은 무엇인가? -> 중복을 허용하지 않는 자료형
# list comprehension은 무엇인가? -> 반복 가능한 자료형을 간단하게 만들 수 있는 방법
students = {i for i in range(1, 31)}

for i in range(28):
    students.remove(int(input()))  # remove()는 set에서 특정 값을 제거하는 함수

# sorted()는 정렬된 리스트를 반환하는 함수
# map()은 두 개의 인자를 받아서 첫 번째 인자에 대해 두 번째 인자를 적용하는 함수
# join()은 문자열을 합치는 함수 (문자열.join(리스트))
print("\n".join(map(str, sorted(students))))
