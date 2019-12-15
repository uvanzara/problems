def test(sum):
    path = [False]

    def helper(curr_sum):
        if curr_sum == 0:
            print('setting path to true')
            path[0] = True

    helper(0)
    return path


if __name__ == "__main__":
    print(test(10))
