class Solution {

    public static int getLength(int[] nums, int left, int right){
        int ans=1;
        int l=nums.length;
        int start=-1;
        int prevEle=-1;
        for(int i=0; i<l; i++){
        	if(nums[i]==left || nums[i]==right) {
        		start=i;
        		prevEle=nums[i];
        		break;
        	}
        }
        for(int i=start+1; i<l; i++) {
        	if(nums[i]==left || nums[i]==right) {
        		if(prevEle==left) {
        			if(nums[i]==right) {
        				prevEle=nums[i];
        				ans++;
        			}
        		}else {
        			if(nums[i]==left) {
        				ans++;
        				prevEle=nums[i];
        			}
        		}
        	}
        }
        return ans;  
    }

    public int maximumLength(int[] nums, int k) {
        //First find the remainder and store
        int l = nums.length;
        int[] rem = new int[l];
        Set<Integer> set = new HashSet<Integer>();
        for(int i=0; i<l; i++){
            rem[i]=nums[i]%k;
            set.add(rem[i]);
        }
        // System.out.println(Arrays.toString(rem));

        //Find the cnts of each remainder
        int[] cnts = new int[k];
        int maxCntOfElement = 0;
        for(int i:rem){
            cnts[i]++;
            maxCntOfElement = Math.max(maxCntOfElement, cnts[i]);
        }

        List<Integer> lis = set.stream().collect(Collectors.toList());

        for(int i=0; i<lis.size(); i++){
            for(int j=i+1; j<lis.size(); j++){
                int left=lis.get(i);
                int right=lis.get(j);
                int res = getLength(rem, left, right);
                // System.out.println(left+"::"+right+"::"+res);
                maxCntOfElement=Math.max(res, maxCntOfElement);
            }
        }

        return maxCntOfElement;
        
    }
}
