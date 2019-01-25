#p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
#g = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
#h = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333

#find x : h = g ^ x  in Zp. or x = log g (h) mod p
import gmpy2


def dlog(p, g, h, max_exp=40):
    b = gmpy2.mpz(2 ** (max_exp / 2))
    g = gmpy2.mpz(g)
    h = gmpy2.mpz(h)
    p = gmpy2.mpz(p)

    middle_dic = build_middle_map(b, g, h, p)
    return find_in_middle_dic_and_build_answer(b, g, middle_dic, p)


def find_in_middle_dic_and_build_answer(B, g, middle, p):
    for x0 in range(B):
        v = gmpy2.powmod(g, B * x0, p)
        if v in middle:
            x1 = middle[v]
            return B * x0 + x1
    return None


def build_middle_map(B, g, h, p):
    middle = {}
    for x1 in range(B):
        index = gmpy2.divm(h, gmpy2.powmod(g, x1, p), p)
        middle[index] = x1
    return middle

