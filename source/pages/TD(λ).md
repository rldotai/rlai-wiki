

# Algorithm

## Pure Python Implementation

```python
def dot(a, b):
    """The dot product between `a` and `b`."""
    assert(len(a) == len(b))
    return sum([i*j for i, j in zip(a, b)])

class TD:
    def init(self, num_features):
        self.evec = [0 for i in range(num_features)]
        self.wvec = [0 for i in range(num_features)]

    def update(self, xvec, r, xvec_p, α, γ, λ):
        δ = r + γ*dot(self.wvec, xvec_p) - dot(self.wvec, xvec)
        self.evec = [x + (γ*λ)*e for x, e in zip(xvec, self.evec)]
        self.wvec = [w + alpha*δ*e for w, e in zip(self.wvec, self.evec)]

```