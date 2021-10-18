def solution(sizes):
    h = []
    w = []
    for a,b in sizes:
        if a>=b:
            h.append(a)
            w.append(b)
        else:
            h.append(b)
            w.append(a)
        

    maxH = max(h)
    maxW = max(w)

    answer = maxH*maxW
    return answer

sizes =[[60, 50], [30, 70], [60, 30], [80, 40]]
solution(sizes)
