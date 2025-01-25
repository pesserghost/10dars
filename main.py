import redis

# 1. BLPOP funksiyasi
def blpop_example(redis_client, keys, timeout):
    return redis_client.blpop(keys, timeout=timeout)

# 2. BRPOP funksiyasi
def brpop_example(redis_client, keys, timeout):
    return redis_client.brpop(keys, timeout=timeout)

# 3. BRPOPLPUSH funksiyasi
def brpoplpush_example(redis_client, source, destination, timeout):
    return redis_client.brpoplpush(source, destination, timeout=timeout)

# 4. LINDEX funksiyasi
def lindex_example(redis_client, key, index):
    return redis_client.lindex(key, index)

# 5. LINSERT funksiyasi
def linsert_example(redis_client, key, where, pivot, value):
    return redis_client.linsert(key, where, pivot, value)

# 6. LLEN funksiyasi
def llen_example(redis_client, key):
    return redis_client.llen(key)

# 7. LPOP funksiyasi
def lpop_example(redis_client, key):
    return redis_client.lpop(key)

# 8. LPUSH funksiyasi
def lpush_example(redis_client, key, *values):
    return redis_client.lpush(key, *values)

# 9. LPUSHX funksiyasi
def lpushx_example(redis_client, key, value):
    return redis_client.lpushx(key, value)

# 10. LRANGE funksiyasi
def lrange_example(redis_client, key, start, end):
    return redis_client.lrange(key, start, end)

# 11. LREM funksiyasi
def lrem_example(redis_client, key, count, value):
    return redis_client.lrem(key, count, value)

# 12. LSET funksiyasi
def lset_example(redis_client, key, index, value):
    return redis_client.lset(key, index, value)

# 13. RPOP funksiyasi
def rpop_example(redis_client, key):
    return redis_client.rpop(key)

# 14. RPOPLPUSH funksiyasi
def rpoplpush_example(redis_client, source, destination):
    return redis_client.rpoplpush(source, destination)

# 15. RPUSH funksiyasi
def rpush_example(redis_client, key, *values):
    return redis_client.rpush(key, *values)

# 16. RPUSHX funksiyasi
def rpushx_example(redis_client, key, value):
    return redis_client.rpushx(key, value)

if __name__ == "__main__":
    # Redis serverga ulanish
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

    # 1. Ro'yxatni tozalash
    redis_client.delete("mylist")

    # 2. LPUSH orqali elementlarni qo'shish
    lpush_example(redis_client, "mylist", "a", "b", "c")  # ['c', 'b', 'a']

    # 3. BLPOP funksiyasini ishlatish
    print("BLPOP:", blpop_example(redis_client, ["mylist"], timeout=1))  # ('mylist', 'c')

    # 4. BRPOP funksiyasini ishlatish
    print("BRPOP:", brpop_example(redis_client, ["mylist"], timeout=1))  # ('mylist', 'a')

    # 5. RPUSH orqali elementlarni qo'shish
    rpush_example(redis_client, "mylist", "1", "2", "3")  # ['b', '1', '2', '3']

    # 6. LRANGE funksiyasini ishlatish
    print("LRANGE:", lrange_example(redis_client, "mylist", 0, -1))  # ['b', '1', '2', '3']

    # 7. LPOP funksiyasini ishlatish
    print("LPOP:", lpop_example(redis_client, "mylist"))  # 'b'

    # 8. LLEN funksiyasini ishlatish
    print("LLEN:", llen_example(redis_client, "mylist"))  # 3
