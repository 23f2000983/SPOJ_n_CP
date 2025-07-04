# Arbitrage Detection using Floyd-Warshall
## 🔍 Problem Summary

Given:
- A list of currencies.
- A list of exchange rates between some pairs of currencies.

**Objective**: Detect whether it's possible to start with 1 unit of a currency and convert it through a sequence of exchanges **to end up with more than 1 unit of the same currency** — this is called **arbitrage**.

## 💡 Intuition

This problem maps directly to **graph theory**:

- Each **currency** is a **node**.
- Each **exchange rate** is a **directed edge** with a weight.
- If an exchange from `A → B` has rate `r`, then taking `log(r)` converts multiplication into addition.
- But instead of maximizing products (which is hard), we **transform the problem using negative logarithms**:
  - Set edge weights as `-log(r)`
  - Then arbitrage exists if there's a **cycle with total weight < 0**.

Thus, we’re looking for a **negative cycle** in a directed weighted graph.

## 🧠 Algorithm Used

### Floyd-Warshall Algorithm (All-Pairs Shortest Paths)

- Time Complexity: `O(n^3)`
- Used to compute shortest paths between every pair of currencies.
- After running it, we check for any currency `i` whether `dist[i][i] < 0`. This indicates a negative-weight cycle — and thus, arbitrage.

### Why `-log(r)`?

To turn: profit = r1 * r2 * r3 > 1 into  log(r1) + log(r2) + log(r3) > 0

So negating it, is just equivalent of negative graph cycle
### ✅ Key Concepts Practiced

- **Graph representation with real weights**
- **Transformation via logarithms**
- **Negative cycle detection**
- **All-pairs shortest paths (Floyd-Warshall)**
- **Floating-point precision handling**

### 📌 Edge Cases to Handle

- Currency names might not be connected to others.
- There might be multiple exchange rates between the same currencies — always take the **best** (maximum rate → minimum negative log).
- Floating-point errors — use an epsilon (`EPS = 1e-12`) to safely compare values near 0.
