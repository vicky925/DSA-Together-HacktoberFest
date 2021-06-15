#https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root) :
      
      def helper(node , mini ,maxi):
        
        if not node:
          return True
        if(node.val <= mini):
          return False
        if(node.val >= maxi):
          return False
        
        return helper(node.left , mini , node.val) and helper(node.right , node.val , maxi)
      
      
      return helper(root , float("-inf") , float("inf"))
      
      
        
        