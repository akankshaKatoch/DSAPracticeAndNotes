from merge_intervals_bug import merge

def run():
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge([[1,4],[4,5]]) == [[1,5]]
    assert merge([]) == []
    print("merge intervals tests passed")

if __name__ == "__main__":
    run()
