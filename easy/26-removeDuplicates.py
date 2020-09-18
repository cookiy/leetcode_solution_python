"""
26. 删除排序数组中的重复项
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

 

示例 1:

给定数组 nums = [1,1,2], 

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
 

说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [:] 从左往右 循环体内数组本身会发生变化，所以用他的拷贝。这涉及到列表作为可变对象浅拷贝的问题
        for n in nums[:]:
            if nums.count(n) > 1: #
                nums.remove(n)
        return len(nums)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 因为python中的集合的自动排序是正数负数分开的，所以要用sorted排序
        # 如果等号左边是nums而不是nums[:]，那么nums只是指向了另一个列表而已，
        # 并没有原地修改列表，原来的列表也就没有变
        nums[:] = list(sorted(set(nums)))
        return len(nums)