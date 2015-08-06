# General Value Functions

$$
v_{\pi}(s) = \mathbb{E} \left[ \sum_{t=0}^{\infty} R_{t+1} \prod_{k=1}^{t} \gamma_{k}| S_0 = s, A_t \sim \pi( \cdot | S_t), \forall t \right]
$$

## n-Step Return

Let $G_{t}^{n}$ (sometimes written as $G_{t}^{(k)}$) denote the n-step return following time step $t$. 

$$
G^{n}_{t} = \sum_{k=1}^{n} R_{t+k} \gamma^{k-1}  + \gamma^{n}v(S_{t+n})
$$

The general version of such functions can be expressed as

$$
G^{n}_{t} = \sum_{k=1}^{n} R_{t+k} \prod_{j=1}^{k-1} \gamma_{t+j} + \prod_{k=1}^{n} \gamma_{t+k} v(S_{t+n})
$$



## Lambda Return

The lambda return at time $t$ is denoted $G^{\lambda}_t$ and expressed as

$$
G_{t}^{\lambda} = (1-\lambda)\sum_{n=1}^{\infty} \lambda^{n-1} G_{t}^{n}
$$

The general form of the function is expressed as

$$
G_{t}^{\lambda} = (1-\lambda_{t}) \sum_{n=1}^{\infty} G_t^{n} \prod_{k=1}^{n-1} \lambda_{t+k}
$$