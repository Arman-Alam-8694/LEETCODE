import java.util.*;

class Solution {
    
    public double calc(double p, double t) {
        return p / t;
    }


    public double gain(double p, double t) {
        return calc(p + 1, t + 1) - calc(p, t);
    }

    public double maxAverageRatio(int[][] classes, int extraStudents) {
       
        PriorityQueue<double[]> heap = new PriorityQueue<>(
            (a, b) -> Double.compare(b[0], a[0]) // sort by gain descending
        );

     
        for (int[] c : classes) {
            double pass = c[0];
            double total = c[1];
            heap.offer(new double[]{gain(pass, total), pass, total});
        }

      
        for (int i = 0; i < extraStudents; i++) {
            double[] top = heap.poll();  
            double pass = top[1] + 1;
            double total = top[2] + 1;
            heap.offer(new double[]{gain(pass, total), pass, total});
        }

      
        double sum = 0.0;
        while (!heap.isEmpty()) {
            double[] cur = heap.poll();
            sum += calc(cur[1], cur[2]);
        }

        return sum / classes.length;
    }
}
