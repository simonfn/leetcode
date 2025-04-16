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
class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        Stack<TreeNode> qRoot = new Stack<>();
        qRoot.push(root);
        TreeNode headRoot;
        while(!qRoot.empty()){
            headRoot = qRoot.pop();
            if(headRoot.val == subRoot.val){
                Stack<TreeNode> qScan = new Stack<>();
                Stack<TreeNode> qSub = new Stack<>();
                TreeNode headScan, headSub;
                boolean isSame = true;
                qScan.push(headRoot);
                qSub.push(subRoot);
                while(!qSub.empty() && !qScan.empty()){
                    headScan = qScan.pop();
                    headSub = qSub.pop();
                    if(headScan.val != headSub.val){
                        isSame = false;
                        break;
                    }
                    // check for asymmetry (containing null)
                    if((headScan.left == null) != (headSub.left == null) || 
                        (headScan.right == null) != (headSub.right == null)){
                        isSame = false;
                        break;
                    }
                    if(headScan.left != null){
                        qScan.push(headScan.left);
                        qSub.push(headSub.left);
                    }
                    if(headScan.right != null){
                        qScan.push(headScan.right);
                        qSub.push(headSub.right);
                    }
                }
                // no other children and last node check also true
                if(qSub.empty() && qScan.empty() && isSame){
                    return true;
                }
            }
            if(headRoot.left != null)
                qRoot.push(headRoot.left);
            if(headRoot.right != null)
                qRoot.push(headRoot.right);
        }
        return false;
    }
}
