# Trunk A — Lens / solenoid / circle-bundle construction

**AI disclaimer:** These construction notes are AI-assisted and AI-generated using Cursor, with Grok, Anthropic, and OpenAI models, under the direction of Alan J. Coppola.

**Plan:** [`../../plans/HM6_FINISH_LINE.md`](../../plans/HM6_FINISH_LINE.md)  
**Primary PDF:** [`../pdfs/1504.07277.pdf`](../pdfs/1504.07277.pdf) (Dranishnikov, essential lens sequence)

## Idea

Build the free $A_p$-space like a **solenoid**, but with **growing** odd-sphere dimension and Edwards–Walsh killing so the limit has $\dim_{\mathbb{Z}}=n$, not a $\mathbb{Z}[1/p]$ solenoid tail.

Each finite stage is a circle action:

\[
S^{1}\curvearrowright S^{2m_i-1}\subset\mathbb{C}^{m_i}
\quad\to\quad
L^{2m_i-1}(p^{k_i})=S^{2m_i-1}/C_{p^{k_i}}.
\]

## Stage recipe

1. Choose $m_i$ with $2m_i-1>n+1$ and $m_{i+1}>m_i$.  
2. Free linear $C_{p^{k_i}}\subset S^1$ on $S^{2m_i-1}$.  
3. Bonding on covers: coordinate $p$-power $\phi_i:S^{2m_{i+1}-1}\to S^{2m_i-1}$ (nullhomotopic as sphere maps when dims grow; essential on lens quotients for $K$-theory).  
4. Route integral top classes through EW / $K(\mathbb{Z},\cdot)$ so $\pi_{i+1}^*=0$ on $H^{q}$ for $q>n$.  
5. Inverse limit $E=\varprojlim S^{2m_i-1}$ carries free $A_p$; orbit $B=\varprojlim L^{\cdots}$.

## FAIL mode (document in harness G0)

Fixed $m_i\equiv m$: classical $p$-adic solenoid, $\check{H}^{2m-1}\cong\mathbb{Z}[1/p]$ — **not** an $n$-cm.

## Next concrete experiment

$n=5$, $p=3$, stages $i=0,1$: write cellular cochains for $S^5\to L^5(3)$ vs $S^7\to L^7(9)$ bonding and check ranks through degree $6$.
