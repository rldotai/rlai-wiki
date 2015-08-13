
Value function of MDP.

\begin{align}
V_{\pi} &= \mathbb{E}_{\pi} \left[\sum_{k=1}^{\infty} R_{t+k} \right] \\ 
&= r_{\pi} + \gamma P_{\pi} V_{\pi}
\end{align}

Transition matrix

$$
[P_{\pi}]_{ij} = \sum_{k}p(s{t+1} = s_{j}| a_{t} = a_k, s_{t} = s_{i}) \pi(a_{k} | s_{i})
$$

Limiting distribution

$$
d_{\pi}(s) = \mathbb{E}_{\pi} \left[ \sum_{t=0}^{\infty} 1_{s_t = s} \right]
$$