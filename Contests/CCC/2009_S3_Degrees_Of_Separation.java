import java.util.*;

class Question1 {
    static final Map<Integer, List<Integer>> friends = new HashMap<>();

    public static void main(String[] args) {
        setupGraph();

        Scanner input = new Scanner(System.in);
        while (true) {
            String command = input.nextLine();
            int x, y;
            switch (command) {
                case "i": {
                    x = Integer.parseInt(input.nextLine());
                    y = Integer.parseInt(input.nextLine());
                    addFriend(x, y);
                    break;
                }
                case "d": {
                    x = Integer.parseInt(input.nextLine());
                    y = Integer.parseInt(input.nextLine());
                    deleteFriend(x, y);
                    break;
                }
                case "n": {
                    x = Integer.parseInt(input.nextLine());
                    System.out.println(numFriends(x));
                    break;
                }
                case "f":
                    x = Integer.parseInt(input.nextLine());
                    System.out.println(numFriendsOfFriends(x));
                    break;
                case "s":
                    x = Integer.parseInt(input.nextLine());
                    y = Integer.parseInt(input.nextLine());
                    int result = degreeOfSep(x, y);
                    if (result == -1) {
                        System.out.println("Not connected");
                    } else {
                        System.out.println(result);
                    }
                    break;
                case "q":
                    input.close();
                    return;
            }
        }
    }

    public static void addFriend(int x, int y) {
        if (!friends.containsKey(x)) {
            friends.put(x, listFromIntArr(new int[] { y }));
        } else if (!friends.get(x).contains(y)) {
            friends.get(x).add(y);
        }

        if (!friends.containsKey(y)) {
            friends.put(y, listFromIntArr(new int[] { x }));
        } else if (!friends.get(y).contains(x)) {
            friends.get(y).add(x);
        }
    }

    public static void deleteFriend(int x, int y) {
        if (friends.containsKey(x) && friends.get(x).contains(y)) {
            friends.get(x).remove((Integer) y);
        }

        if (friends.containsKey(y) && friends.get(y).contains(x)) {
            friends.get(y).remove((Integer) x);
        }
    }

    public static int numFriends(int x) {
        if (friends.containsKey(x)) {
            return friends.get(x).size();
        } else {
            return 0;
        }
    }

    public static int numFriendsOfFriends(int x) {
        Set<Integer> friendOfFriends = new HashSet<>();
        if (friends.containsKey(x)) {
            for (int friend : friends.get(x)) {
                friendOfFriends.addAll(friends.get(friend));
            }
            Set<Integer> newFriendOfFriends = new HashSet<>();
            for (int elem : friendOfFriends) {
                if (!(elem == x) && !friends.get(x).contains(elem)) {
                    newFriendOfFriends.add(elem);
                }
            }
            return newFriendOfFriends.size();
        } else {
            return 0;
        }
    }

    public static int degreeOfSep(int x, int y) {
        Map<Integer, Integer> dist = new HashMap<>();
        Set<Integer> visited = new HashSet<>();
        List<Integer> queue = new ArrayList<>();
        queue.add(x);

        while (queue.size() > 0) {
            int vertex = queue.remove(0);
            if (vertex == y) {
                return dist.get(vertex);
            }
            for (int neighbour : friends.get(vertex)) {
                if (!visited.contains(neighbour)) {
                    if (dist.containsKey(vertex)) {
                        dist.put(neighbour, dist.get(vertex) + 1);
                    } else {
                        dist.put(neighbour, 1);
                    }
                    visited.add(neighbour);
                    queue.add(neighbour);
                }
            }
        }
        return -1;
    }

    public static void setupGraph() {
        friends.put(1, listFromIntArr(new int[] { 6 }));
        friends.put(2, listFromIntArr(new int[] { 6 }));
        friends.put(3, listFromIntArr(new int[] { 4, 5, 6, 15 }));
        friends.put(4, listFromIntArr(new int[] { 3, 5, 6 }));
        friends.put(5, listFromIntArr(new int[] { 3, 4, 6 }));
        friends.put(6, listFromIntArr(new int[] { 1, 2, 3, 4, 5, 7 }));
        friends.put(7, listFromIntArr(new int[] { 6, 8 }));
        friends.put(8, listFromIntArr(new int[] { 7, 9 }));
        friends.put(9, listFromIntArr(new int[] { 8, 10, 12 }));
        friends.put(10, listFromIntArr(new int[] { 9, 11 }));
        friends.put(11, listFromIntArr(new int[] { 10, 12 }));
        friends.put(12, listFromIntArr(new int[] { 9, 11, 13 }));
        friends.put(13, listFromIntArr(new int[] { 12, 14, 15 }));
        friends.put(14, listFromIntArr(new int[] { 13 }));
        friends.put(15, listFromIntArr(new int[] { 3, 13 }));
        friends.put(16, listFromIntArr(new int[] { 17, 18 }));
        friends.put(17, listFromIntArr(new int[] { 16, 18 }));
        friends.put(18, listFromIntArr(new int[] { 16, 17 }));
    }

    public static List<Integer> listFromIntArr(int[] arr) {
        List<Integer> list = new ArrayList<>();
        for (int elem : arr) {
            list.add(elem);
        }
        return list;
    }
}
