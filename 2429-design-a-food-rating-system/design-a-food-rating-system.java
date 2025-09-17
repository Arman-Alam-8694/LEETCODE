import java.util.*;

public class FoodRatings {
    private static class Entry {
        String name;
        int rating;
        Entry(String name, int rating) {
            this.name = name;
            this.rating = rating;
        }
    }

    private final Map<String, String> foodToCuisine = new HashMap<>();
    private final Map<String, Integer> foodToRating = new HashMap<>();
    private final Map<String, PriorityQueue<Entry>> cuisineToPQ = new HashMap<>();

    // comparator: higher rating first, then lexicographically smaller name
    private final Comparator<Entry> comp = (a, b) -> {
        if (a.rating != b.rating) return b.rating - a.rating;
        return a.name.compareTo(b.name);
    };

    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        for (int i = 0; i < foods.length; i++) {
            String f = foods[i];
            String c = cuisines[i];
            int r = ratings[i];

            foodToCuisine.put(f, c);
            foodToRating.put(f, r);
            cuisineToPQ
                .computeIfAbsent(c, k -> new PriorityQueue<>(comp))
                .add(new Entry(f, r));
        }
    }

    public void changeRating(String food, int newRating) {
        // update the canonical rating
        foodToRating.put(food, newRating);
        // push a new Entry (lazy deletion of old entries)
        String cuisine = foodToCuisine.get(food);
        cuisineToPQ.get(cuisine).add(new Entry(food, newRating));
    }

    public String highestRated(String cuisine) {
        PriorityQueue<Entry> pq = cuisineToPQ.get(cuisine);
        if (pq == null) return ""; // or throw if invalid cuisine

        // lazy cleanup: remove stale entries until top matches current rating
        while (true) {
            Entry top = pq.peek();
            if (top == null) return ""; // should not happen if input guarantees at least one food
            int current = foodToRating.get(top.name);
            if (current == top.rating) return top.name;
            pq.poll(); // stale entry, remove and continue
        }
    }
}