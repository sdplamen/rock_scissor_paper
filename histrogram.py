def histrogram(nums):
    for x in nums:
        output = ''
        while x > 0:
            output = output + 'x'
            x = x - 1
        print(output)

histrogram([18, 11, 24, 5])

# with hist() function
def count_elements(seq) -> dict:
    # Tally elements from `seq`.
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist
counted = count_elements(histrogram)
counted
