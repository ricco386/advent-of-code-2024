# https://adventofcode.com/2024/day/3

memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

def find_all(mem, sub):
    start = 0

    while True:
        start = mem.find(sub, start)

        if start == -1: 
            return

        yield start

        start += len(sub)

def process_string(mem_dump):
    value = 0

    if mem_dump[3] == "(":
        end = mem_dump.find(")")
        divider = mem_dump.find(",")

        if end != -1 and divider != -1:
            first_number = mem_dump[4:divider]
            second_number = mem_dump[divider+1:end]

            value = int(first_number) * int(second_number)

    return value

def process_memory(mem):
    total = 0

    for index in find_all(mem, "mul"):
        total += process_string(mem[index:index+12])

    return total

print(process_memory(memory))
