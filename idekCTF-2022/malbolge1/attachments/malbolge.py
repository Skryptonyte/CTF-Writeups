from sys import stdin

CRAZY = [[1, 0, 0], [1, 0, 2], [2, 2, 1]]

ENCRYPT = "5z]&gqtyfr$(we4{WP)H-Zn,[%\\3dL+Q;>U!pJS72FhOA1CB6v^=I_0/8|jsb9m<.TVac`uY*MK'X~xDl}REokN:#?G\"i@"
ENCRYPT = list(map(ord, ENCRYPT))

with open("banner") as banner:
    print(*banner.readlines())


def crazy(a, b, bad):
    trits = CRAZY if bad is None else bad
    result = 0
    d = 1
    for _ in range(10):
        result += trits[b // d % 3][a // d % 3] * d
        d *= 3
    return result


def initialize(source, mem, bad):
    i = 0
    for c in source:
        print(c,ord(c)+i)
        assert (ord(c) + i) % 94 in {4, 5, 23, 39, 40, 62, 68, 81}
        mem[i] = ord(c)
        i += 1
    while i < 3**10:
        mem[i] = crazy(mem[i - 1], mem[i - 2], bad)
        i += 1


def interpret(mem, stdin_allowed, bad):
    output = ""
    # c: program counter
    # a: input register
    a, c, d = 0, 0, 0
    while True:
        if not 33 <= mem[c] <= 126:
            return output
        
        match (mem[c] + c) % 94:
            case 4:
                c = mem[d]
            case 5:  # Output char
                ch = chr(int(a % 256))
                print(ch, end="")
                output += ch
            case 23:   # Input single char
                if stdin_allowed:
                    try:
                        a = ord(stdin.read(1))
                    except TypeError:
                        return output
                else:
                    return output
            case 39:    # assign register a some crazy value
                a = mem[d] = 3**9 * (mem[d] % 3) + mem[d] // 3
            case 40:      # assign mem[d] to register d
                d = mem[d]
            case 62:
                a = mem[d] = crazy(a, mem[d], bad)
            case 81:
                return output

        if 33 <= mem[c] <= 126:     # Every byte gets encrypted
            mem[c] = ENCRYPT[mem[c] - 33]

        c = (c + 1) % 3**10
        d = (d + 1) % 3**10


def malbolge(program, stdin_allowed=True, a_bad_time=None):
    memory = [0] * 3**10
    initialize(program, memory, a_bad_time)
    return interpret(memory, stdin_allowed, a_bad_time)
