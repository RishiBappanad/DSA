class Solution(object):
    def lengthLongestPath(self, input):
        stack = []
        best = 0
        i = 0
        n = len(input)
        
        while i < n:
            # Count tabs to find depth
            depth = 0
            while i < n and input[i] == '\t':
                depth += 1
                i += 1
                
            # Read the name of the file/folder until newline
            name_len = 0
            is_file = False
            while i < n and input[i] != '\n':
                if input[i] == '.':
                    is_file = True
                name_len += 1
                i += 1
                
            # Skip the newline character for the next iteration
            if i < n and input[i] == '\n':
                i += 1
                
            # Manage stack length based on current depth
            while len(stack) > depth:
                stack.pop()
                
            # Calculate total length (adding 1 for '/' separator if not root)
            parent_len = stack[-1] if stack else 0
            curr_len = parent_len + name_len + (1 if stack else 0)
            
            if is_file:
                best = max(best, curr_len)
            else:
                stack.append(curr_len)
                
        return best