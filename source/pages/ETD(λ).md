

# Algorithm

\begin{align}
\theta_{t+1} &= \theta_{t} + \alpha_{t} \delta_{t} e_{t} \\
\delta_{t} &= R_{t+1} + \gamma_{t+1}\theta_{t}^{\top} \phi_{t+1} - \theta_{t}^{\top}\phi_{t} \\
e_{t} &= \rho_{t}(\gamma_{t} \lambda_{t} e_{t-1} + M_{t} \phi_{t}) \\
M_{t} &= \lambda_{t} I_{t} + (1 - \lambda_{t}) F_{t} \\
F_{t} &= \rho_{t-1} \gamma_{t} F_{t-1} + I_{t}
\end{align}

# Analysis

The expected eligibility trace can be defined as 

$$
e(s) = d_{\mu}(s) \mathbb{E}[\gamma_{t} \lambda_{t} e_{t-1} + M_{t}\phi_{t} | S_{t} = s]
$$

Represented as a matrix with $e(s)$ on the diagonal, $[E]_{ii} = e(s_i)$. 

\begin{align}
E^{\top} &= \Phi^{\top} M + E^{\top} P_{\pi} \Gamma \Lambda \\
&= \Phi^{\top} M (I - P_{\pi} \Gamma \Lambda)^{-1}
\end{align}

The expected followon trace can be defined as:

$$
f(s) = d_{\mu}(s) \mathbb{E}_{\mu} [F_{t} | S_{t} = s] 
$$

The expected emphasis can be defined as:

$$
m(s) = d_{\mu}(s) \mathbb{E}_{\mu} [ M_t | S_t = s]
$$

The expected update can be expressed as:

$$
\bar{\theta}_{t+1} = \bar{\theta}_{t} 
+ \alpha \Phi^{\top} M (I - P_{\pi} \Gamma \Lambda)^{-1} r_{\pi}
- \alpha \Phi^{\top} M (I - P_{\pi} \Gamma \Lambda)^{-1} (I - P_{\pi} \Gamma) \Phi \bar{\theta}_{t}
$$

The fixed point (the weights that the algorithm converges to) has a similar form to TD, and can be computed as follows

\begin{align}
w_{\infty} &= A^{-1} b \\
A &= \Phi^{\top} M (I - P_{\pi} \Gamma \Lambda)^{-1} (I - P_{\pi} \Gamma) \Phi\\
b &= \Phi^{\top}M(I - P_{\pi} \Gamma \Lambda)^{-1} r_{\pi}
\end{align}

# Example Code

## Python Implementation

```python

```