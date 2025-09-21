import java.util.*;

class MovieRentingSystem {

    // Class to represent a movie copy (rented or unrented)
    static class Rental {
        int price, shop, movie;

        public Rental(int price, int shop, int movie) {
            this.price = price;
            this.shop = shop;
            this.movie = movie;
        }

        // equals() and hashCode() are still required for safe remove
        @Override
        public boolean equals(Object o) {
            if (!(o instanceof Rental)) return false;
            Rental r = (Rental) o;
            return this.price == r.price && this.shop == r.shop && this.movie == r.movie;
        }

        @Override
        public int hashCode() {
            return Objects.hash(price, shop, movie);
        }
    }

    Map<String, Integer> getPrice = new HashMap<>();
    
    // Unrented copies per movie, sorted by price -> shop
    Map<Integer, TreeSet<Rental>> movieToShop = new HashMap<>();
    
    // Rented movies, sorted by price -> shop -> movie
    TreeSet<Rental> rented = new TreeSet<>(
        Comparator.comparingInt((Rental r) -> r.price)
                  .thenComparingInt(r -> r.shop)
                  .thenComparingInt(r -> r.movie)
    );

    public MovieRentingSystem(int n, int[][] entries) {
        for (int[] e : entries) {
            int shop = e[0], movie = e[1], price = e[2];
            String key = shop + "," + movie;
            getPrice.put(key, price);

            movieToShop.putIfAbsent(movie, new TreeSet<>(
                Comparator.comparingInt((Rental r) -> r.price)
                          .thenComparingInt(r -> r.shop)
            ));
            movieToShop.get(movie).add(new Rental(price, shop, movie));
        }
    }

    public List<Integer> search(int movie) {
        List<Integer> res = new ArrayList<>();
        if (!movieToShop.containsKey(movie)) return res;

        int count = 0;
        for (Rental r : movieToShop.get(movie)) {
            res.add(r.shop);
            if (++count == 5) break;
        }
        return res;
    }

    public void rent(int shop, int movie) {
        String key = shop + "," + movie;
        int price = getPrice.get(key);
        Rental r = new Rental(price, shop, movie);

        rented.add(r);
        movieToShop.get(movie).remove(r); // safe because of equals() & hashCode()
    }

    public void drop(int shop, int movie) {
        String key = shop + "," + movie;
        int price = getPrice.get(key);
        Rental r = new Rental(price, shop, movie);

        rented.remove(r); // safe because of equals() & hashCode()
        movieToShop.get(movie).add(r);
    }

    public List<List<Integer>> report() {
        List<List<Integer>> res = new ArrayList<>();
        int count = 0;
        for (Rental r : rented) {
            res.add(Arrays.asList(r.shop, r.movie));
            if (++count == 5) break;
        }
        return res;
    }
}
