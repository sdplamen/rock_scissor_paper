def histrogram(nums):
    for x in nums:
        output = ''
        while x > 0:
            output = output + 'x'
            x = x - 1
        print(output)

histrogram([18, 11, 24, 5])
