import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

tmax = 10000
N = 10000

def one_walk(tmax):
    t = np.arange(0, tmax)
    x = np.zeros(tmax)
    a = 0

    for i in range(0, tmax):
        x[i] = a
        if(np.random.choice(2)):
            a += 1
        else:
            a -= 1
    return x

def make_supa(N, tmax):
    supa = np.zeros((N, tmax))
    for i in range(0, N):
        supa[i] = one_walk(tmax)
        plt.plot(np.arange(0, tmax), supa[i])
    return supa

def make_graph(N, tmax, supa):
    x = np.zeros(tmax)
    t = np.arange(0, tmax)

    for i in range(0, N):
        plt.plot(t, supa[i])

    for i in range(0, tmax):
        x[i] = np.mean(supa[:,i])
    x = np.power(x, 2)
    plt.plot(t, x, linewidth=3, c='black')

def make_hist(supa, ti):
    x = supa[:,ti]
    plt.hist(x, density=True, bins=30, ec='black')

    xmin, xmax = plt.xlim()
    mu, sig = norm.fit(x)
    l = np.linspace(xmin, xmax, 100)
    p = norm.pdf(l, mu, sig)
    plt.plot(l, p)

    plt.title(r'$\mu=$ {}, $\sigma=$ {}'.format(round(mu, 3), round(sig, 3)))
    plt.savefig(r'hist{}.pgf'.format(ti))
    return np.array([ti, mu, sig])

def make_tab(N, tmax, supa):
    vals = np.zeros((7, 3))
    mint = int(3*tmax/10)
    inct = int(tmax/10)
    for i in range(mint, tmax, inct):
        a = int(i/100 - 3)
        vals[a] = make_hist(supa, i)
    df = pd.DataFrame({
        'time':vals[:,0],
        'mu':vals[:,1],
        'sigma':vals[:,2],
    })
    df.to_csv('data.csv', index=False)

supa = make_supa(N, tmax)
plt.savefig('walks.pgf')
make_graph(N, tmax, supa)
plt.savefig('walks2.pgf')
make_tab(N, tmax, supa)
