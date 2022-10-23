c = "125eade3ceb41b6cf53f5edb012024e2049568540d0b833323bed4946d66487e1f03439592e5bf12430a44be9b8f84fb00f33e62b2e85d5b20e74c276d75cf443a06e2ca37e9907445d9dc03a3f35056b87f0a8eccd2f83f1eccab055c919065"

from Crypto.Util.number import *
c = bytes.fromhex(c)


def iroot(k, n):
    hi = 1
    while pow(hi, k) < n:
        hi *= 2
    lo = hi // 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        midToK = pow(mid, k)
        if midToK < n:
            lo = mid
        elif n < midToK:
            hi = mid
        else:
            return mid
    if pow(hi, k) == n:
        return hi
    else:
        return lo


print(long_to_bytes(iroot(3, bytes_to_long(c))))
