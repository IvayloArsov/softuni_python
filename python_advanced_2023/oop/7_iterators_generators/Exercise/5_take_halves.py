def solution():
    def integers():
        i = 1
        while True:
            yield i
            i += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        taken = []
        for _ in range(n):
            taken.append(next(seq))
        return taken

    return (take, halves, integers)

