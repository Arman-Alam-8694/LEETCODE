class Solution {
public double largestTriangleArea(int[][] points) {
double res = 0.0;

    for (int[] x : points) {
        for (int[] y : points) {
            for (int[] z : points) {
                double area = Math.abs(
                    x[0] * (y[1] - z[1]) +
                    y[0] * (z[1] - x[1]) +
                    z[0] * (x[1] - y[1])
                ) / 2.0;
                res = Math.max(res, area);
            }
        }
    }
    return res;
}


}
