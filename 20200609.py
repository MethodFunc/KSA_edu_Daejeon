def combinations(s):
    #mapper work
    if len(s) < 2:
        return s
    res = []
# 문자데이터 할때 위를 수정 sep = ' ' 힌트 -> 단어가 다 잘라진 상태의 배열을 만들고 비교함수

    # reduce work
    for i, c in enumerate(s):
        res.append(c)   #추가되는 부분 -> [ 'a', 'b', 'c', 'd']
        # print(i, c, res)
        #자기를 뺀 나머지를 비교
        for j in combinations(s[:i] + s[i+1:]):     # 재귀
            res.append(c+j)
            print(i, c, j, res)
    return res


if __name__ == "__main__":
    result = combinations("abcd")
    print(result)
    
    
#빅오 O(N^2) -> 2중 for문에 if문 포함
# O(2N) -> 2중 for문