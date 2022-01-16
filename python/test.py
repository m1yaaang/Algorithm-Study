def solution(participant, completion):
    one = list(participant)
    two = list(completion)
    for i in participant:
        print(i)
        if i in completion:
            one.remove(i)
            print(i)
            
    answer = one[0]
    print(type(completion))
    return answer

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))