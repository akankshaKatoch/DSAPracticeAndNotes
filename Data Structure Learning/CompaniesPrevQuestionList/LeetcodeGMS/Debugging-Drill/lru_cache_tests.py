from lru_cache_bug import LRUCache

def run():
    cache = LRUCache(2)
    cache.put(1,1)
    cache.put(2,2)
    assert cache.get(1) == 1
    cache.put(3,3)   # evicts key 2
    assert cache.get(2) == -1
    cache.put(4,4)   # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
    print("LRU tests passed")

if __name__ == "__main__":
    run()
