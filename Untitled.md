# Elimination Matrices — Structure, Mechanics, and Role in LU

## Core Idea

An **elimination matrix** performs a single, precise row operation:
> eliminate one entry below a pivot using a linear combination of rows

It is the matrix form of a Gaussian elimination step.

---

## 1. Definition

To eliminate \( a_{ij} \) using pivot \( a_{jj} \) (with \( i > j \)):

\[
\ell_{ij} = \frac{a_{ij}}{a_{jj}}
\]

The elimination matrix \( E_{ij} \) is:

\[
E_{ij} = I - \ell_{ij} \, e_i e_j^T
\]

Where:
- \( e_i \) = standard basis vector (1 at position \( i \), else 0)
- \( e_j^T \) = row selector

---

## 2. Operational Meaning

Left-multiplying by \( E_{ij} \):

\[
E_{ij} A
\]

performs:

\[
\text{Row}_i \leftarrow \text{Row}_i - \ell_{ij} \cdot \text{Row}_j
\]

👉 Exactly one elimination step

---

## 3. Concrete Example (3×3)

Let:

\[
A =
\begin{bmatrix}
2 & 1 & 1 \\
4 & -6 & 0 \\
-2 & 7 & 2
\end{bmatrix}
\]

### Step: Eliminate \( a_{21} = 4 \) using pivot \( a_{11} = 2 \)

\[
\ell_{21} = 4/2 = 2
\]

Elimination matrix:

\[
E_{21} =
\begin{bmatrix}
1 & 0 & 0 \\
-2 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\]

### Apply:

\[
E_{21} A =
\begin{bmatrix}
2 & 1 & 1 \\
0 & -8 & -2 \\
-2 & 7 & 2
\end{bmatrix}
\]

---

### Next: Eliminate \( a_{31} = -2 \)

\[
\ell_{31} = -2/2 = -1
\]

\[
E_{31} =
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
1 & 0 & 1
\end{bmatrix}
\]

Apply:

\[
E_{31} E_{21} A =
\begin{bmatrix}
2 & 1 & 1 \\
0 & -8 & -2 \\
0 & 8 & 3
\end{bmatrix}
\]

---

## 4. Structure of Elimination Matrices

General form:
- Identity matrix with **one modified off-diagonal entry**

For eliminating \( a_{ij} \):

- Entry at position \( (i, j) = -\ell_{ij} \)
- All diagonal entries = 1

👉 Sparse and structured

---

## 5. Sequence of Eliminations

Gaussian elimination = product of elimination matrices:

\[
E_k \cdots E_2 E_1 A = U
\]

Where:
- \( U \) = upper triangular matrix

---

## 6. Connection to LU Decomposition

Rewriting:

\[
A = E_1^{-1} E_2^{-1} \cdots E_k^{-1} U
\]

Define:

\[
L = E_1^{-1} E_2^{-1} \cdots E_k^{-1}
\]

👉 Then:

\[
A = LU
\]

---

## 7. Inverse of Elimination Matrix

\[
E_{ij}^{-1} = I + \ell_{ij} e_i e_j^T
\]

### Meaning:
\[
\text{Row}_i \leftarrow \text{Row}_i + \ell_{ij} \cdot \text{Row}_j
\]

👉 Undo the elimination step

---

## 8. Key Properties

| Property | Meaning |
|--------|--------|
| Sparse | Only one off-diagonal nonzero |
| Determinant | 1 |
| Invertible | Always (if pivot ≠ 0) |
| Structure | Lower triangular (for \( i > j \)) |

---

## 9. With Row Swaps (Pivoting)

If pivot = 0:
- Use permutation matrix \( P \)

\[
PA = LU
\]

👉 Elimination matrices alone are not enough when swapping is required

---

## 10. Mental Model

| Object | Interpretation |
|--------|--------------|
| \( E_{ij} \) | One elimination step |
| Product \( E_k \cdots E_1 \) | Full elimination process |
| Inverses | Build \( L \) |
| Result | Upper triangular \( U \) |

---

## Final Takeaway

Elimination matrices turn Gaussian elimination into **pure matrix multiplication**:
- Each step is encoded as a matrix
- The full process becomes structured and reversible
- This leads directly to **LU decomposition**

👉 They are the algebraic backbone of elimination.