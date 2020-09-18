"""
给你一个整数数组 nums，将该数组升序排列。

 

示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
 

提示：

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

"""

十大排序方法：

https://blog.csdn.net/MobiusStrip/article/details/83785159?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task%E4%BD%9C%E8%80%85%EF%BC%9Apowcai%E9%93%BE%E6%8E%A5%EF%BC%9Ahttps://leetcode-cn.com/problems/sort-an-array/solution/python-shi-xian-de-shi-da-jing-dian-pai-xu-suan-fa/%E6%9D%A5%E6%BA%90%EF%BC%9A%E5%8A%9B%E6%89%A3%EF%BC%88LeetCode%EF%BC%89%E8%91%97%E4%BD%9C%E6%9D%83%E5%BD%92%E4%BD%9C%E8%80%85%E6%89%80%E6%9C%89%E3%80%82%E5%95%86%E4%B8%9A%E8%BD%AC%E8%BD%BD%E8%AF%B7%E8%81%94%E7%B3%BB%E4%BD%9C%E8%80%85%E8%8E%B7%E5%BE%97%E6%8E%88%E6%9D%83%EF%BC%8C%E9%9D%9E%E5%95%86%E4%B8%9A%E8%BD%AC%E8%BD%BD%E8%AF%B7%E6%B3%A8%E6%98%8E%E5%87%BA%E5%A4%84%E3%80%82
"""

"""
归并排序
归并排序利用了分治的思想来对序列进行排序。对一个长为 n 的待排序的序列，我们将其分解成两个长度为 n/2的子序列。每次先递归调用函数使两个子序列有序，然后我们再线性合并两个有序的子序列使整个序列有序
"""
class Solution:
    
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: 
            return nums
        mid = len(nums) // 2
        return merge(self.sortArray(nums[:mid]), self.sortArray(nums[mid:]))

    def merge(self, left, right):
        res = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        res += left
        res += right
        return res    


"""
快速排序
"""
class Solution:
    def partition(self, nums, l, r):
        pivot = nums[l]
        while l < r:
            while l < r and pivot <= nums[r]:
                r -= 1
            nums[l] = nums[r] 
            while l < r and nums[l] <= pivot:
                l += 1 
            nums[r] = nums[l]
        nums[l] = pivot
        return l
    def random_partition(self, nums, l, r):
        i = random.randint(l, r)
        nums[i], nums[r] = nums[r], nums[i]  
        return self.partition(nums, l, r)
    def quickSort(self, nums, l, r):
        if l < r:
            k = self.random_partition(nums, l, r)
            self.quickSort(nums, l, k-1)
            self.quickSort(nums, k+1, r)
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1 )
        return nums