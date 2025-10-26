class Bank {
    private long[] cur_balance;
    private int n;

    public Bank(long[] balance) {
        n = balance.length;
        cur_balance = new long[n];
        for (int i = 0; i < n; i++) {
            cur_balance[i] = balance[i];
        }
    }

   
    public boolean check(int account) {
        return account >= 1 && account <= n;
    }

    public boolean transfer(int account1, int account2, long money) {
        if (!check(account1) || !check(account2)) {
            return false;
        }
        if (cur_balance[account1 - 1] < money) {
            return false;
        }
        cur_balance[account1 - 1] -= money;
        cur_balance[account2 - 1] += money;
        return true;
    }

    public boolean deposit(int account, long money) {
        if (!check(account)) {
            return false;
        }
        cur_balance[account - 1] += money;
        return true;
    }

    public boolean withdraw(int account, long money) {
        if (!check(account)) {
            return false;
        }
        if (cur_balance[account - 1] < money) {
            return false;
        }
        cur_balance[account - 1] -= money;
        return true;
    }
}
