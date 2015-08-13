
# Single Chain MDP

This is one of the simplest MDPs to analyze, and occasionally illustrates surprising properties of the various algorithms.
 
We can compute the fixed point of the weight updates pretty easily. 

Let $\Delta_t = \delta_{t} e_{t}$. 
At convergence, $\sum_{t=1}^{T} \Delta_{t} = 0$, so we can solve for the value of $\theta$ at which this occurs.

## Two State Version

- $\gamma_t = 1$ for $S_t$ nonterminal
- $R_{t+1} = r(s_t) = r_t$
- $\phi(s_1) = 1$, $\phi(s_2) = c$
- $\rho_t = 1 \forall t$, i.e. the on-policy setting.

### TD Analysis

The TD algorithm is defined via:

\begin{align}
\theta_{t+1} &= \theta_{t} + \alpha \delta_t e_t 
\\
\delta_{t} &= (R_{t+1} + \gamma_{t} \theta_{t}^{\top} \phi_{t+1} - \theta_{t}^{\top} \phi_{t})
\\
e_{t} &= \gamma_t \lambda_t e_{t-1} + \phi_{t}  
\end{align} 

We can keep track of the variables in the updating scheme,

\begin{align}
\delta_{1} &= r_1 + c\theta - \theta \\
\delta_{2} &= r_2 - c\theta 
\end{align}

\begin{align}
e_{1} &= 1 \\
e_{2} &= \lambda + c
\end{align}

\begin{align}
\Delta_1 &= r_1 + (c - 1)\theta \\
\Delta_2 &= (r_2 - c \theta)(\lambda + c) \\
&= (\lambda + c) r_2 - (c^2 + c\lambda) \theta 
\end{align}

So, we get

\begin{align}
0 &= \Delta_1 + \Delta_2 \\
(c^2 + c\lambda + 1 - c)\theta &= r_1 + (\lambda + c)r_2\\
\theta &= \frac{r_1 + (\lambda + c)r_2}{(c^2 + c\lambda + 1 - c)}  \\
\theta &= \frac{r_1 + (\lambda + c)r_2}{(c^2 + c(\lambda - 1) + 1)}
\end{align}

#### Lambda = 1

For $\lambda = 1$, we get

\begin{align}
\theta &= \frac{r_1 + r_2 (1 + c)}{c^2 + 1}
\end{align}

Which is the same as we find solving the problem with least squares.

#### Lambda = 0

For $\lambda = 0$, we get

\begin{align}
\theta &= \frac{r_1 + c r_2}{c^2 - c + 1}
\end{align}

### ETD Analysis

\begin{align}
e_{t} &= \rho_t (\gamma_t \lambda_t e_{t-1} + M_t \phi_t) \\
F_{t} &= \rho_{t-1} \gamma F_{t-1} + I_t \\
M_{t} &= \lambda_t I_t + (1 - \lambda_t) F_t
\end{align}

The $\delta_t$ values are the same as in TD, but we need to keep track of the followon trace and the emphasis.

\begin{align}
\delta_{1} &= r_1 + c\theta - \theta \\
\delta_{2} &= r_2 - c\theta 
\end{align}

For $\gamma(s) = 1$ if $s$ is nonterminal, $F_t = \sum_{k=1}^{t} I_k$, and so 

\begin{align}
M_1 &= \lambda I_1 + (1 - \lambda)I_1 = I_1\\
M_2 &= \lambda I_2 + (1 - \lambda)(I_1 + I_2) = I_2 + (1-\lambda) I_1 
\end{align}

If we assume that interest is constant and equal to one (a valid scenario for comparing with TD), we get

\begin{align}
M_1 &= 1 \\
M_2 &= 2 - \lambda 
\end{align}

And so the eligibility traces become

\begin{align}
e_{1} &= 1 \\
e_{2} &= \lambda + c(2 - \lambda)
\end{align}

\begin{align}
\Delta_1 &= r_1 + c \theta - \theta \\
\Delta_2 &= (r_2 - c \theta)(\lambda + c(2 - \lambda)) \\
&= r_2(\lambda + 2c - \lambda c) - \theta (\lambda c + 2c^2 - \lambda c^2)
\end{align}

And therefore

\begin{align}
0 &= \Delta_1 + \Delta_2 \\
0 &= r_1 + c \theta - \theta + r_2(\lambda + 2c - \lambda c) - \theta (\lambda c + 2c^2 - \lambda c^2) \\
\theta (\lambda c + 2c^2 - \lambda c^2 - c + 1) &=  r_1 + r_2(\lambda + 2c - \lambda c) \\
\theta ( \lambda c (1 - c) + 2c^2 - c + 1) &= r_1 + 2c r_2 + \lambda r_2 (1-c) \\
\end{align}

Therefore,

$$
\theta = \frac{r_1 + 2c r_2 + \lambda r_2 (1-c)}{\lambda c (1 - c) + 2c^2 - c + 1}
$$

This leads to the interesting observation that for $c = 1$ (i.e., identical features), $\lambda$ doesn't affect the overall result.

For $c \neq 1$, we can set $\lambda = 1$ and get

\begin{align}
\theta &= \frac{r_1 + 2c r_2 + r_2 (1-c)}{c (1 - c) + 2c^2 - c + 1} \\
&= \frac{r_1 + r_2(1 + c)}{c^2 + 1}
\end{align}

For $c \neq 1$, we can set $\lambda = 0$ and get

\begin{align}
\theta &= \frac{r_1 + 2c r_2}{2c^2 - c + 1} \\
\end{align}

Note that this is not the same solution as found under TD(0).

