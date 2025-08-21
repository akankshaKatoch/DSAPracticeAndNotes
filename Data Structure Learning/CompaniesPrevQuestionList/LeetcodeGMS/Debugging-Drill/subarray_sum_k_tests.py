from subarray_sum_k_bug import subarray_sum

def run():
    assert subarray_sum([1,1,1], 2) == 2
    assert subarray_sum([1,2,3], 3) == 2  # [1,2], [3]
    assert subarray_sum([0,0,0], 0) == 6  # many zeros
    assert subarray_sum([-1,-1,1], 0) == 1
    print("subarray_sum tests passed")

if __name__ == "__main__":
    run()
