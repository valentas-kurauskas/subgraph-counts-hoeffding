#Download the data and compute the lower bound for N from Corollary 5 of our paper.
import sys
import math
import argparse
import pandas as pd
import numpy as np

parser=argparse.ArgumentParser()
parser.add_argument("--h", type=int, help="number of vertices in H")
parser.add_argument("--i_T", type=int, help="number of internal vertices in T", default=1)
parser.add_argument("--epsilon", type=float, help="precision required (fraction of E D^{h-1})", default=0.1)
parser.add_argument("--p", type=float, help="1-p is the confidence required", default=0.05)
parser.add_argument("--n_vertices", type=int, help="number of vertices in G", default=0)
parser.add_argument("--min_n", type=int, help="number of vertices in G", default=10000)

args,filenames = parser.parse_known_args() 

n_practical = 0
n_total = 0

n=args.n_vertices

for filename in filenames:
    try:
        df=pd.read_csv(filename, names=["degree","freq"], skiprows=1, dtype={"degree": int, "freq": np.float32})
    except:
        print(f"Wrong format in file {filename}. Is it a CSV file containing two columns degree and freq?")
        continue
    if args.n_vertices == 0:
        n = df.freq.values.sum() 
    else:
        n = args.n_vertices
    if n < args.min_n:
        continue
    df = df.sort_values("degree", ascending=False).reset_index(drop=True)
    S = (df.degree**(args.h-1) * df.freq).cumsum() / df.freq.sum()

    #find minimum \Delta such that the empirical distribution of the degree \tilde{D}
    #satisfies \E \tilde{D}^{h-1} \mathbb{I}_{\tilde{D} \ge \Delta} < \epsilon \E \tilde{D}^{h-1}
    Delta = df.degree.values[np.where(S.values > args.epsilon * S.values[-1])[0][0]] + 1

    EDhm1 = S.values[-1]
    #use \lambda = \epsilon \E \tilde{D}^{h-1}
    lambd = args.epsilon * EDhm1 / args.i_T
    s = args.epsilon * EDhm1

    N_hoeffding = max(1,int(math.ceil(0.5 * math.exp(2 * (args.h-1) * math.log(Delta-1) - 2 * math.log(s)) * math.log(2/args.p))))
    if N_hoeffding <  n:
        n_practical += 1
    n_total += 1
    print(f"n = {n} N = {N_hoeffding} E D^{args.h-1} = {round(EDhm1,1)} max degree = {max(df.degree)} Delta = {Delta} {'practical' if N_hoeffding <  n else 'useless'} {filename}")

#Totals are printed in the end
print(f"h={args.h} n_practical={n_practical} n_total={n_total} ratio={None if n_total==0 else round(n_practical/n_total,2)}")
