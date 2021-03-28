class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return heapq.nlargest(k,nums)[-1]
        #Quickselect - O(N) time and O(1) space
        def partition(left, right, pivot):
            
            pivot_val = nums[pivot]
            nums[right], nums[pivot] = nums[pivot], nums[right]
            
            partition_index = left
            for ii in range(left, right):
                if nums[ii] < pivot_val:
                    nums[ii], nums[partition_index], = nums[partition_index], nums[ii]
                    partition_index += 1
            nums[partition_index], nums[right] = nums[right], nums[partition_index]
            
            return partition_index
        
        def search(left, right, k_smallest):
            
            if left == right:
                return nums[left]
            
            index = random.randint(left,right)
            part_index = partition(left,right, index)
            
            if part_index == k_smallest:
                return nums[part_index]
            elif part_index > k_smallest:
                return search(left, part_index - 1, k_smallest)
            else:
                return search(part_index + 1, right, k_smallest)
                

        return search(0, len(nums) - 1, len(nums) - k)
        