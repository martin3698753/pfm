import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd
from scipy.optimize import curve_fit as cf

#matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

tmax = 1000
N = 1000

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
        print(r"Created {}. curve of supa".format(i))
        plt.plot(np.arange(0, tmax), supa[i])
    return supa

def make_graph(N, tmax, supa):
    x = np.zeros(tmax)
    t = np.arange(0, tmax)
###############################################################################################################################################################
    for i in range(0, tmax): ##### Tady to dělá tu křivku <x^2>
        x[i] = np.mean(supa[:,i]) ### Beru všechny budy z křivek a dávám je do průměru (format podobny jako v Matlabu)
    x = np.power(x, 2) ##### Umocní to celý array čísel na 2 mocninu
    plt.plot(t, x, linewidth=3, c='black')
####################################################################################################################3

def make_hist(supa, ti, a):
    ti = int(ti)
    x = supa[:,ti]
    plt.hist(x, density=True, bins=30, ec='black') #denisty = normalizace

    xmin, xmax = plt.xlim()
    mu, sig = norm.fit(x) #automaticky najde mu a sigma hodnoty
    l = np.linspace(xmin, xmax, 100)
    p = norm.pdf(l, mu, sig)
    plt.plot(l, p)

    plt.title(r'$\mu=$ {}, $\sigma=$ {}, $t_i =$ {}'.format(round(mu, 3), round(sig, 3), ti))
    plt.savefig(r'hist{}.pdf'.format(a))
    print("created hist with time cut {}".format(ti))
    plt.clf()
    return np.array([ti, mu, sig])

def func(t, a, b, c):
    return a*t**b+c

def make_tab(N, tmax, supa):
    vals = np.zeros((18, 3))
    mint = int(3*tmax/10)
    rg = np.random.uniform(mint, tmax, 18)
    a = 0
    for i in rg:
        vals[a] = make_hist(supa, i, a)
        a += 1

    x = vals[:,0]
    y = vals[:,2]
    nx = np.linspace(min(x), max(x), 2000)

    plt.scatter(x, y, label='sigma(t)')
    popt, pcov = cf(func, x, y)
    u, v, w = round(popt[0],2), round(popt[1],2), round(popt[2],2)
    print('------------------------------------')
    print('a = ', u)
    print('b = ', v)
    print('c = ', w)
    print('------------------------------------')
    plt.plot(nx, func(nx, popt[0], popt[1], popt[2]))
    plt.savefig('lin.pdf')

    df = pd.DataFrame({
        'time':x,
        'mu':vals[:,1],
        'sigma':y,
    })
    df = df.round(3)
    df.to_csv('data.csv', index=False)

supa = make_supa(N, tmax)
print("Created supa")
plt.savefig('walks.pdf')
plt.clf()
print("Making graph")
make_graph(N, tmax, supa)
print("Created graph")
plt.savefig('walks2.pdf')
plt.clf()
print("Creating hists")
make_tab(N, tmax, supa)
print("Dun")
