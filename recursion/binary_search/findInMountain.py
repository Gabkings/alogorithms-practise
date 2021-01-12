class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        mountain_top, possible_solutions = self.find_top_of_mountain(mountain_arr, target)
        if possible_solutions and possible_solutions[0] < mountain_top:  
            # if the soultion was already found during the mountaion top search
            return possible_solutions[0]        
        
		# left side of mountain
        res = self.simple_binary_search(target, mountain_arr, 0, mountain_top, False)
        if res != -1:
            return res
        
		# right side of mountain
        if possible_solutions:
            return possible_solutions[0]
        return self.simple_binary_search(target, mountain_arr, mountain_top+1,                                                                                  mountain_arr.length() - 1, True)
                   
    
    def simple_binary_search(self, target, arr, start, end, is_decreasing):
        while start <= end:
            middle = start + int((end - start) / 2)
            val = arr.get(middle)
            
            if val == target:
                return middle
            elif val > target:
                if is_decreasing:
                    start = middle + 1    
                else:
                    end = middle - 1
            else:
                if is_decreasing:
                    end = middle - 1
                else:
                    start = middle + 1    
        return -1
    
    def find_top_of_mountain(self, arr, target):
        possible_solutions = set()
        start = 0
        end = arr.length() - 1
        while start < end:
            middle = start + int((end - start) / 2)
            middle_val = arr.get(middle)
            next_middle_val = arr.get(middle+1)
            
            if middle_val < next_middle_val:
                start = middle + 1
            else:
                end = middle            
            
            if middle_val == target:
                possible_solutions.add(middle)
            elif next_middle_val == target:
                possible_solutions.add(middle + 1)
            
        return start, list(possible_solutions)