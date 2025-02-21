/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
//  public class TreeNode {
//       int val;
//       TreeNode left;
//      TreeNode right;
//       TreeNode() {}
//       TreeNode(int val) { this.val = val; }
//       TreeNode(int val, TreeNode left, TreeNode right) {
//           this.val = val;
//           this.left = left;
//           this.right = right;
//       }
//   }

import java.util.*;
class FindElements {
    HashSet<Integer> seen=new HashSet<>();
    TreeNode root;
    int val=0;
    private void dfs(TreeNode node,int val){
            seen.add(val);
            if (node.left!=null){
                dfs(node.left,(val*2)+1);
            }
            if (node.right!=null){
                dfs(node.right,(val*2)+2);
            }

        }
    public FindElements(TreeNode root) {
        this.root=root;
        dfs(root,val);
        System.out.println(seen);

        
    }
        

    
    public boolean find(int target) {
        if(seen.contains(target)){
            return true;
        }
        else{
            return false;
        }

        
    }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements obj = new FindElements(root);
 * boolean param_1 = obj.find(target);
 */