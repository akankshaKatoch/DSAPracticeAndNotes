from k_sum_pairs_bug import max_operations

def run():
    assert max_operations([1,2,3,4], 5) == 2
    assert max_operations([3,1,3,4,3], 6) == 1
    assert max_operations([2,2,2,2], 4) == 2
    print("k-sum pairs tests passed")

if __name__ == "__main__":
    run()
