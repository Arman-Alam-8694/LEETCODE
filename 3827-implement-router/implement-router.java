import java.util.*;

public class Router {

    private static class Packet {
        int src, dst, ts;
        Packet(int s, int d, int t) { src = s; dst = d; ts = t; }
    }

    private final int memoryLimit;
    private final Deque<Packet> fifo;                 // global FIFO
    private final Set<String> seen;                   // duplicate check
    private final Map<Integer, ArrayList<Integer>> destTimestamps; // dst -> timestamps list
    private final Map<Integer, Integer> destHead;     // dst -> index of first valid element

    public Router(int memoryLimit) {
        this.memoryLimit = memoryLimit;
        this.fifo = new ArrayDeque<>();
        this.seen = new HashSet<>();
        this.destTimestamps = new HashMap<>();
        this.destHead = new HashMap<>();
    }

    public boolean addPacket(int source, int destination, int timestamp) {
        String key = makeKey(source, destination, timestamp);
        if (seen.contains(key)) return false;

        // Evict oldest if memory full
        if (fifo.size() == memoryLimit) {
            Packet old = fifo.pollFirst();
            String oldKey = makeKey(old.src, old.dst, old.ts);
            seen.remove(oldKey);

            ArrayList<Integer> oldList = destTimestamps.get(old.dst);
            int head = destHead.getOrDefault(old.dst, 0);

            // Advance the head index for that destination
            if (oldList != null && head < oldList.size()) {
                destHead.put(old.dst, head + 1);
                if (head + 1 >= oldList.size()) {
                    // list exhausted -> remove structures
                    destTimestamps.remove(old.dst);
                    destHead.remove(old.dst);
                }
            }
        }

        // Add new packet
        Packet p = new Packet(source, destination, timestamp);
        fifo.addLast(p);
        seen.add(key);

        destTimestamps.putIfAbsent(destination, new ArrayList<>());
        destHead.putIfAbsent(destination, 0);
        destTimestamps.get(destination).add(timestamp);

        return true;
    }

    public int[] forwardPacket() {
        if (fifo.isEmpty()) return new int[0];

        Packet p = fifo.pollFirst();
        String key = makeKey(p.src, p.dst, p.ts);
        seen.remove(key);

        ArrayList<Integer> list = destTimestamps.get(p.dst);
        int head = destHead.getOrDefault(p.dst, 0);

        if (list != null && head < list.size()) {
            destHead.put(p.dst, head + 1);
            if (head + 1 >= list.size()) {
                destTimestamps.remove(p.dst);
                destHead.remove(p.dst);
            }
        }

        return new int[]{p.src, p.dst, p.ts};
    }

    public int getCount(int destination, int startTime, int endTime) {
        ArrayList<Integer> list = destTimestamps.get(destination);
        if (list == null) return 0;
        int head = destHead.getOrDefault(destination, 0);
        int n = list.size();
        if (head >= n) return 0;

        // search in [head, n-1]
        int left = lowerBound(list, head, n - 1, startTime);
        int right = upperBound(list, head, n - 1, endTime);
        return Math.max(0, right - left);
    }

    // ---------- helpers ----------

    private String makeKey(int s, int d, int t) {
        return s + "," + d + "," + t;
    }

    // binary search for first index i in [l..r] with list.get(i) >= target
    private int lowerBound(ArrayList<Integer> list, int l, int r, int target) {
        int low = l, high = r + 1; // [low, high)
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (list.get(mid) >= target) high = mid;
            else low = mid + 1;
        }
        return low;
    }

    // binary search for first index i in [l..r] with list.get(i) > target
    private int upperBound(ArrayList<Integer> list, int l, int r, int target) {
        int low = l, high = r + 1; // [low, high)
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (list.get(mid) > target) high = mid;
            else low = mid + 1;
        }
        return low;
    }
}
