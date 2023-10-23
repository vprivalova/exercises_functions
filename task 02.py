def fibonachi(n):
    nums = [1, 1]

    if n == 0:
        print('')

    elif n == 1:
        print(nums[0])

    else:
        for index in range(n-2):
            nums.append(nums[-1] + nums[-2])

        for element in nums:
            print(element, end=' ')


n_members = int(input())
fibonachi(n_members)
