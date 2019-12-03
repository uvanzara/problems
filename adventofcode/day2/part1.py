with open('input.txt', 'r') as fh:
    line = fh.readlines()

in_arr = line[0].split(',')

print('array len = {}'.format(len(in_arr)))

idx = 0
while idx <= len(in_arr):
    # opcode = in_arr[idx]
    decode(in_arr, idx)
    # print("elem = {}".format(elem))

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
    if op == "mult":
        sums = arr[index+1] + arr[index+2]
        mem_loc = arr[index+3]
        arr[mem_loc] = sums