class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int n = nums.length;
        for(int i = 0; i < n-2; i ++){
            for(int j = i + 1; j < n-1; j ++){
                for(int k = j + 1; k < n; k ++){
                    int sum = nums[i] + nums[j] + nums[k];
                    int l;
                    for(l = (int)Math.sqrt(sum);l>1 ; l-- ) {
								if(sum%l==0) break;
                    }
                    if(l==1) answer++;
                }
            }
        }
        return answer;
    }
}
