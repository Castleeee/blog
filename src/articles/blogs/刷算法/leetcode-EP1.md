---
title: leetcode-EP1
date: 2022-10-11 22:28:02
category:
- 刷算法
tag:
- leetcode
---

<!-- more -->

<div align="center" style="font-size:1.4em;"><h2><strong> leetcode-EP1</strong></h2></div>


## leetcode-EP1
### 二分查找
#### 分类
leetcode题号: 704. 二分查找
代码随想录视频[链接](https://www.bilibili.com/video/BV1fA4y1o715)
时间：37min
#### 代码

::: details Click to see more

```python
def search(nums, target: int) -> int:  
    result = -1  
    right = len(nums) - 1  
    left = 0  
    middle = int(right / 2)  
    while True:  
        if left == right:  
            if target == nums[middle]:  
                result = middle  
            break  
        if target == nums[middle]:  
            result = middle  
            break  
        elif target > nums[middle]:  
            left = middle + 1  
            middle = int((left + right) / 2)  
        elif target < nums[middle]:  
            if middle==left: # 处理边界条件，例如两个元素，为什右边不会有这个情况  
                right = middle  
            else:  
                right = middle - 1  
            middle = int((left + right) / 2)  
    return result  
  
if __name__ == '__main__':  
    print(search([2,3,4,5,6],7))
```
运行结果
```
PASS 44ms
```
:::

#### 注意的点:
- 注意边界条件开闭情况，一般是左闭右开或左闭右闭，在中间处理的时候也遵循这个
- 二分要在有序序列中查找
- 其他：None

### 删除元素
#### 分类
leetcode题号:27
代码随想录视频[链接](https://www.bilibili.com/video/BV12A4y1Z7LP/)
时间：45min
#### 代码

::: details Click to see more

```python


    def removeElement(self, nums: List[int], val: int) -> int:  
    '''
    双指针法
    '''
        f=0
        s=0

        while (f<=len(nums)-1):
            if nums[f]==val:
                f+=1
                continue
            else:
                nums[s]=nums[f]
                f+=1
                s+=1
        return len(nums[:s])

    def removeElement(self, nums: List[int], val: int) -> int:  
    ‘‘‘
    暴力移除
    '''
        i = 0
        while (i < len(nums)):
            if nums[i] == val:
                for j in range(i, len(nums) - 1):
                    nums[j] = nums[j + 1]
                del(nums[-1])
            else:
                i += 1
        return len(nums)

```
运行结果
```
PASS
```
:::

#### 注意的点:
- 主要就是处理边界条件，双指针fast一直拿最新的数据，slow就管着存，注意最后一个元素和重复元素的处理
- 其他：None

