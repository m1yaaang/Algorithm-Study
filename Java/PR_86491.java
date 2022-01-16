// 프로그래머스 위클리 챌린지 최소직사각형

public class PR_86491 {
    public static void main(String[] args) {
        Solution s = new Solution();
        int sizes[][] = new int[][] {{14, 4}, {19, 6}, {6, 16}, {18, 7}, {7, 11}};

        System.out.println(s.solution(sizes));
        
    }
}
class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
        int max_h, max_w;
        int tmp;

        for(int i=0;i<sizes.length;i++){
            if(sizes[i][0]<sizes[i][1]){
                tmp = 0;
                tmp = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = tmp;
            }
        }

        max_w = sizes[0][0];
        max_h = sizes[0][1];

        for(int i=1;i<sizes.length;i++){
            if(max_w<sizes[i][0])
                max_w = sizes[i][0];
            if(max_h<sizes[i][1])
                max_h = sizes[i][1];
        }

        answer=max_h*max_w;
        return answer;
    }
}