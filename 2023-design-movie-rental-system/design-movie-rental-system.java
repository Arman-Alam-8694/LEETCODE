import java.util.*;

class MovieRentingSystem {

    Map<String, Integer> getPrice = new HashMap<>();
    Map<Integer, TreeSet<int[]>> movieToShop = new HashMap<>();

    // Rented movies: [price, shop, movie], sorted by price -> shop
    TreeSet<int[]> rented = new TreeSet<>(
        (a, b) -> a[0] != b[0] ? a[0] - b[0] : (a[1] != b[1] ? a[1] - b[1] : a[2] - b[2])
    );

    public MovieRentingSystem(int n, int[][] entries) {
        for (int[] e : entries) {
            int shop = e[0], movie = e[1], price = e[2];
            String key = shop + "," + movie;
            getPrice.put(key, price);

            movieToShop.putIfAbsent(movie, new TreeSet<>(
                (a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]
            ));
            movieToShop.get(movie).add(new int[]{price, shop});
        }
    }

    public List<Integer> search(int movie) {
        List<Integer> res = new ArrayList<>();
        if (!movieToShop.containsKey(movie)) return res;

        int count = 0;
        for (int[] p : movieToShop.get(movie)) {
            res.add(p[1]);
            count++;
            if (count == 5) break;
        }
        return res;
    }

    public void rent(int shop, int movie) {
        String key = shop + "," + movie;
        int price = getPrice.get(key);

        rented.add(new int[]{price, shop, movie});
        movieToShop.get(movie).remove(new int[]{price, shop});
    }

    public void drop(int shop, int movie) {
        String key = shop + "," + movie;
        int price = getPrice.get(key);

        rented.remove(new int[]{price, shop, movie});
        movieToShop.get(movie).add(new int[]{price, shop});
    }

    public List<List<Integer>> report() {
        List<List<Integer>> res = new ArrayList<>();
        int count = 0;
        for (int[] p : rented) {
            res.add(Arrays.asList(p[1], p[2])); // [shop, movie]
            count++;
            if (count == 5) break;
        }
        return res;
    }
}
