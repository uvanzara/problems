def nqueens(n):
    result = []
    nums = [j for j in range(n)]
    # print("nums = {}".format(nums))

    def helper(n, i, slate):
        lastq = len(slate) - 1
        for earlierq in range(lastq):
            rowdiff = abs(lastq - earlierq)
            coldiff = abs(slate[lastq] - slate[earlierq])
            if rowdiff == coldiff:
                return
        
        if i == n:
            tmp_array = []            
            for index in slate:
                array_2d = ["."] * n
                array_2d[index] = "q"
                tmp_array.append(''.join(array_2d))
            result.append(tmp_array)

        for pick in range(i, len(nums)):
            nums[i], nums[pick] = nums[pick], nums[i]
            slate.append(nums[i])
            # print("calling helper with slate = {}".format(slate))
            helper(n, i + 1, slate)
            slate.pop()
            nums[i], nums[pick] = nums[pick], nums[i]
    helper(n, 0, [])
    return result

if __name__ == "__main__":
    for n in [4]:
        answer = nqueens(n)
        print(answer)