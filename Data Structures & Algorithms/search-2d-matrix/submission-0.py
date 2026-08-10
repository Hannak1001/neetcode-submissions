class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #go through each row and compare to target
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                #if in row, do binary search
                left = 0
                right = len(matrix[i]) - 1
                while left <= right:
                    middle = (left + right) // 2

                    if matrix[i][middle] == target:
                        return True
                    elif matrix[i][middle] > target:
                        right = middle - 1
                    else:
                        left = middle + 1
        return False