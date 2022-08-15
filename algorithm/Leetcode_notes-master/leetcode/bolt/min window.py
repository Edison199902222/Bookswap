def helper(nums, prev_value, sums, index, path):
    if len(nums) == 1 or len(nums) == 0:
        return set(nums)
    if index == len(nums):
        temp = set()
        temp.add(sums)
        print(temp, path)
        return temp
    result = set()
    i = index
    if i == 0:
        result |= helper(nums, nums[i], nums[i], i + 1, str(nums[i]))
    else:
        result |= helper(nums, nums[i], sums + nums[i], i + 1, path + "+" + str(nums[i]))
        result |= helper(nums, - nums[i], sums - nums[i], i + 1, path + "-" + str(nums[i]))
        result |= helper(nums, prev_value * nums[i], sums - prev_value + prev_value * nums[i], i + 1, path + "*" + str(nums[i]))
        if nums[i] != 0:
            result |= helper(nums, prev_value / nums[i], sums - prev_value + prev_value / nums[i], i + 1, path + "/" + str(nums[i]))
    return result

def main():
    string = [5,1,1]
    result = helper(string, 1, 0, 0, "")
    print(result)


main()
