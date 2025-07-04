# k‑Order Linear Recurrence (SPOJ SEQ style) – Matrix‑Exponentiation Solution
## 🚀 Problem Recap

For each test case you are given

* `k` – order of the recurrence (k ≤ 10)
* initial values **F(1)…F(k)**
* coefficients **c1…ck** defining  

  \[
      F(n) = c_1 F(n-1) + c_2 F(n-2) + \dots + c_k F(n-k)\quad (\bmod 10^9)
  \]

* a query index **n** (up to 2 000 000 000 or higher).

Print **F(n)**.

## 🧠 Intuition

This problem is solved using **matrix exponentiation**:

### Step 1: Build the transformation matrix

The recurrence relation can be expressed using a **k × k companion matrix** `T`:

\[
T =
\begin{bmatrix}
c_1 & c_2 & \dots & c_k \\
1   & 0   & \dots & 0   \\
0   & 1   & \dots & 0   \\
\vdots &   & \ddots & \vdots \\
0   & 0   & \dots & 1 \, 0
\end{bmatrix}
\]

This matrix, when multiplied with the state vector of the last `k` values, gives the next term.

### Step 2: Use fast exponentiation

To compute `F(n)`:
- Raise matrix `T` to power `(n - k)`
- Multiply it by the vector of initial values
- Return the top element of the resulting vector

---