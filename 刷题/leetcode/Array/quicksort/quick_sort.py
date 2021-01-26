def quicksort(nums, left, right):
    if left < right:
        position = partition(nums, left, right)
        quicksort(nums, left, position - 1)
        quicksort(nums, position + 1, right)
def partition(nums, left, right):
    pivot = nums[right]
    i = left
    for j in range(left,right):
        if nums[j] < pivot:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    nums[right], nums[i] = nums[i], nums[right]
    return i


def quick_sort(nums, start, end):
    if start > end:
        return
    left = start
    right = end - 1
    pivot = nums[end]
    while left <= right:
        # 直到找到 一个不合法的left， 也就是不大于等于 pivot 的
        while left <= right and nums[left] >= pivot:
            left += 1
        # 找到一个不合法的right
        while left <= right and nums[right] <= pivot:
            right -= 1
        # 不想等时 进行交换
        if left < right:
            swap(nums, left, right)
    # left 就是 pivot 的位置
    swap(nums, left, end)
    quick_sort(nums, left + 1, end)
    quick_sort(nums, start, left - 1)

def swap(nums, a, b):
    nums[a], nums[b] = nums[b], nums[a]

def main():
    A = [5,4,1,7,2,3,5]
    left = 0
    right = len(A) - 1
    quick_sort(A, left, right)
    print(A)
main()
'''
quick sort 原理
当left 《 right 时
我们先把整个数组做一个 partition
partition 意思是每一次 把数组最后一个作为pivot，i 指针指向的位置是必须比pivot 小的位置，每一次如果发现j 指向的元素比pivot 小的话，
那么就跟i 交换位置，并且i += 1， 如果j 指向的位置比pivot大的话 那么我们就不动
最后 我们再把 pivot 放在 i的位置， 这样就形成 pivot 左边都是比pivot 小的， 右边都是比pivot大的
然后再把 i return
昨晚partition，我们就知道 partition 已经把 nums 化成两部分， 以position为划分
左边比position 小， 右边比position大
然后 我们再把左边那一部分  跟右边部分 分别quick sort 一次
最终 我们会得到 sort好的 array
'''