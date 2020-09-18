/**给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 */
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
/**原理
先将数组进行排序
从左侧开始，选定一个值为 定值 ，右侧进行求解，获取与其相加为 00 的两个值
类似于快排，定义首和尾
首尾与 定值 相加
等于 00，记录这三个值
小于 00，首部右移
大于 00，尾部左移
定值右移，重复该步骤

作者：githber
链接：https://leetcode-cn.com/problems/3sum/solution/three-sum-giftu-jie-by-githber/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。 */
var threeSum = function(nums) {
    // 最左侧值为定值，右侧所有值进行两边推进计算
    let res = [];
    nums.sort((a, b) => a - b);
    let size = nums.length;
    if (nums[0] <= 0 && nums[size - 1] >= 0) {
      // 保证有正数负数
      let i = 0;
      while (i < size - 2) {
        if (nums[i] > 0) break; // 最左侧大于0，无解
        let first = i + 1;
        let last = size - 1;
        while (first < last) {
          if (nums[i] * nums[last] > 0) break; // 三数同符号，无解
          let sum = nums[i] + nums[first] + nums[last];
          if (sum === 0) {
            res.push([nums[i], nums[first], nums[last]]);
          }
          if (sum <= 0) {
            // 负数过小，first右移
            while (nums[first] === nums[++first]) {} // 重复值跳过
          } else {
            while (nums[last] === nums[--last]) {} // 重复值跳过
          }
        }
        while (nums[i] === nums[++i]) {}
      }
    }
  
    return res;
  };

  /**标签：数组遍历
首先对数组进行排序，排序后固定一个数 nums[i]nums[i]，再使用左右指针指向 nums[i]nums[i]后面的两端，数字分别为 nums[L]nums[L] 和 nums[R]nums[R]，计算三个数的和 sumsum 判断是否满足为 00，满足则添加进结果集
如果 nums[i]nums[i]大于 00，则三数之和必然无法等于 00，结束循环
如果 nums[i]nums[i] == nums[i-1]nums[i−1]，则说明该数字重复，会导致结果重复，所以应该跳过
当 sumsum == 00 时，nums[L]nums[L] == nums[L+1]nums[L+1] 则会导致结果重复，应该跳过，L++L++
当 sumsum == 00 时，nums[R]nums[R] == nums[R-1]nums[R−1] 则会导致结果重复，应该跳过，R--R−−
时间复杂度：O(n^2)O(n 
2
 )，nn 为数组长度

作者：guanpengchn
链接：https://leetcode-cn.com/problems/3sum/solution/hua-jie-suan-fa-15-san-shu-zhi-he-by-guanpengchn/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。 */

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    let ans = [];
    const len = nums.length;
    if(nums == null || len < 3) return ans;
    nums.sort((a, b) => a - b); // 排序
    for (let i = 0; i < len ; i++) {
        if(nums[i] > 0) break; // 如果当前数字大于0，则三数之和一定大于0，所以结束循环
        if(i > 0 && nums[i] == nums[i-1]) continue; // 去重
        let L = i+1;
        let R = len-1;
        while(L < R){
            const sum = nums[i] + nums[L] + nums[R];
            if(sum == 0){
                ans.push([nums[i],nums[L],nums[R]]);
                while (L<R && nums[L] == nums[L+1]) L++; // 去重
                while (L<R && nums[R] == nums[R-1]) R--; // 去重
                L++;
                R--;
            }
            else if (sum < 0) L++;
            else if (sum > 0) R--;
        }
    }        
    return ans;
};

// 暴力法 时间复杂度：O(n^3)
var threeSum = function(nums) {
    var result = [];
    var repeatSet = new Set();
    var len = nums.length;
    for(var i = 0;i < len-2;i++){
        for(var j = i+1;j < len-1;j++){
            for(var k = j+1;k < len;k++){
                if(nums[i]+nums[j]+nums[k] == 0){
                    var tmpResult = [nums[i],nums[j],nums[k]];
                    var tmpSortStr = String(tmpResult.sort());
                    if(!repeatSet.has(tmpSortStr)){
                        result.push(tmpResult);
                        repeatSet.add(tmpSortStr)
                    }
                }
            }
        }
    }
    return result;
};
