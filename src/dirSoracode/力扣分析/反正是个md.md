# 你好

## 741.找到数组的中间位置
原题：
> 给你一个下标从 0 开始的整数数组 nums ，请你找到 最左边 的中间位置 middleIndex （也就是所有可能中间位置下标最小的一个）。  
> 中间位置 middleIndex 是满足 nums[0]+nums[1]+...+nums[middleIndex-1] == nums[middleIndex+1]+nums[middleIndex+2]+...+nums[nums.length-1] 的数组下标。  
> 如果middleIndex==0，左边部分的和定义为0。类似的，如果middleIndex == nums.length-1，右边部分的和定义为0。  
> 请你返回满足上述条件**最左边**的middleIndex，如果不存在这样的中间位置，请你返回-1。  
- 疏漏点：这个要返回的下标本身的值并不会参与比较，即下标两边的累加部分相等。
```c++
class Solution {
public:
    int findMiddleIndex(vector<int>& nums) {
        /**
        sum：用累加计算得出nums数组的全部值=12
        cur：当前已经累加的值
        i：所谓数组的中间位置下标。
         */
        int sum = accumulate(nums.begin(), nums.end(), 0);
        int cur = 0;

        /**
        能得出结果的情况：成功找到一个下标，他两边的累加部分相等
         */
        for (int i = 0; i < nums.size(); ++i) {
            if (cur * 2 + nums[i] == sum)
                return i;
            cur += nums[i];
        }

        return -1;
    }
};
```

## 35.搜索插入位置
原题：
> 给定一个升序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。  
> 请必须使用时间复杂度为 O(log n) 的算法。
- 疑惑点：对数时间复杂度就是说在循环过程中通过表达式可以减少原定的循环次数，因此本题不能够使用暴力枚举
```c++
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size()-1;
        while(left <= right)
        {
            // 我怎么如此愚蠢，不就是二分查找吗
            int mid = (right - left)/2+left;
            if(nums[mid] < target)
            {
                left = mid+1;
            }
            else if(nums[mid] > target)
            {
                right = mid-1;
            }
            else
            {
                return mid;
            }
        }
        return left;
    }
};
```

## 练习1.对角线遍历
原题：
> 给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素  
```c++
class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
        vector<int> ans;
        // 数组有可能是空的
        if(matrix.empty())
            return ans;
        // 重点在与行和列之间的组合，c代表当前列，r代表当前行
        int row = matrix.size(), col = matrix[0].size(), c = 0, r = 0;
        // 正矩形对角线长度=行数+列数-1
        for(int i=0;i < row+col-1;i++)
        {
            // 遍历的时候要分奇偶，值为偶朝上遍历，值为奇朝下遍历
            if(i % 2)
            {
                // i如果小于列数，说明当前还在左上三角
                // i大于列数，说明当前在右下三角区域，过了次对角线
                c = (i<col) ? i : col-1;
                r = i - c;
                // 上遍历和下遍历的情况相反，但有一点是可以确定的，两者要保证不越界，上遍历范围内是c不越下界，下遍历内是r不越下界
                while(c >= 0 && r < row)
                    ans.push_back(matrix[r++][c--]);
            }
            else
            {
                r = (i<row) ? i : row-1;
                c = i - r;
                while(c < col && r >= 0)
                    ans.push_back(matrix[r--][c++]);
            }
        }
        return ans;
        
    }
};
```

## 1.两数之和
原题：
> 给定一个整数数组nums和一个整数目标值target，请你在该数组中找出和为目标值target的那两个整数，并返回它们的数组下标。  
> 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。  
> 你可以按任意顺序返回答案。  
- 疏漏点：容易形成定势思维，不会用面向对象的新增类型配合，该题最好的方式就是搭配上哈希表，通过用哈希表记录下所有的数组元素，一定可以找到一对能够互补相加为target的元素
```