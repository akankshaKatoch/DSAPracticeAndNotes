from two_sum_bug import two_sum

def check(nums, target, expected_set):
    ans = two_sum(nums, target)
    assert set(ans) == set(expected_set), f"{nums}, {target}: got {ans}, expected indices {expected_set}"

if __name__ == "__main__":
    check([2,7,11,15], 9, [0,1])
    check([3,2,4], 6, [1,2])
    # Fails due to bug:
    check([3,3], 6, [0,1])
    print("two_sum tests passed")
