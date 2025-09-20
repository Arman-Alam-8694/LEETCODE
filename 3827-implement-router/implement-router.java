import java.util.*;

class Router {

    class Packet {
        int src, dst, ts;
        public Packet(int s, int d, int t) {
            src = s; dst = d; ts = t;
        }
    }

    int memoryLimit;
    Queue<Packet> queue; // global FIFO
    Set<String> seen; // to check duplicates
    Map<Integer, ArrayList<Integer>> destMap; // destination -> timestamps

    public Router(int memoryLimit) {
        this.memoryLimit = memoryLimit;
        queue = new LinkedList<>();
        seen = new HashSet<>();
        destMap = new HashMap<>();
    }

    public boolean addPacket(int source, int destination, int timestamp) {
        String key = source + "," + destination + "," + timestamp;
        if (seen.contains(key)) return false;

        // Evict oldest if memory full
        if (queue.size() == memoryLimit) {
            Packet old = queue.poll();
            String oldKey = old.src + "," + old.dst + "," + old.ts;
            seen.remove(oldKey);

            ArrayList<Integer> list = destMap.get(old.dst);
            list.remove(0); // remove oldest timestamp
            if (list.isEmpty()) destMap.remove(old.dst);
        }

        // Add new packet
        Packet p = new Packet(source, destination, timestamp);
        queue.offer(p);
        seen.add(key);

        destMap.putIfAbsent(destination, new ArrayList<>());
        destMap.get(destination).add(timestamp); // append at end (timestamps increasing)
        return true;
    }

    public int[] forwardPacket() {
        if (queue.isEmpty()) return new int[0];
        Packet p = queue.poll();
        String key = p.src + "," + p.dst + "," + p.ts;
        seen.remove(key);

        ArrayList<Integer> list = destMap.get(p.dst);
        list.remove(0); // remove oldest timestamp
        if (list.isEmpty()) destMap.remove(p.dst);

        return new int[]{p.src, p.dst, p.ts};
    }

    public int getCount(int destination, int startTime, int endTime) {
        if (!destMap.containsKey(destination)) return 0;
        ArrayList<Integer> list = destMap.get(destination);

        // Binary search for lower and upper bounds
        int left = lowerBound(list, startTime);
        int right = upperBound(list, endTime);
        return right - left;
    }

    private int lowerBound(ArrayList<Integer> list, int target) {
        int l = 0, r = list.size();
        while (l < r) {
            int m = l + (r - l) / 2;
            if (list.get(m) >= target) r = m;
            else l = m + 1;
        }
        return l;
    }

    private int upperBound(ArrayList<Integer> list, int target) {
        int l = 0, r = list.size();
        while (l < r) {
            int m = l + (r - l) / 2;
            if (list.get(m) > target) r = m;
            else l = m + 1;
        }
        return l;
    }
}
