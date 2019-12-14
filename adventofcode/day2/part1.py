with open('input.txt', 'r') as fh:
    line = fh.readlines()

in_arr = line[0].split(',')
in_arr = [int(x) for x in in_arr]
print('array len = {}'.format(len(in_arr)))

idx = 0


def decode(arr, index):
    if arr[index] == 1:
        op = "add"
    elif arr[index] == 2:
        op = "mult"
    else:
        op = "terminate"
    if op == "add":
        sums = arr[index+1] + arr[index+2]
        mem_loc = arr[index+3]
        arr[mem_loc] = sums
        return 4
    if op == "mult":
        sums = arr[index+1] + arr[index+2]
        mem_loc = arr[index+3]
        arr[mem_loc] = sums
        return 4
    if op == "terminate":
        return -1


while idx <= len(in_arr):
    # opcode = in_arr[idx]
    incr = decode(in_arr, idx)
    if incr == -1:
        break
    idx += incr
    # print("elem = {}".format(elem))
print('final array = {}'.format(in_arr))