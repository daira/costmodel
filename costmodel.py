#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Sequence, Tuple


@dataclass
class Cost:
    iFFTs: Sequence[int]
    FFTs: Sequence[int]
    MSMs: Sequence[int]


@dataclass
class Model:

    # Relation to Turbo-PLONK proposal <docs.zkproof.org/pages/standards/accepted-workshop3/proposal-turbo_plonk.pdf>
    # w = R+A
    # d = D
    # \ell = S

    rows: int                # N
    routable_columns: int    # R
    advice_columns: int      # A
    selector_columns: int    # S (including standard selectors maybe)
    max_degree: int          # D
    accessible: int          # number of accessible wires on the next row
    #standard_selectors: int  # 5 (q_L, q_R, q_O, q_M, q_C)

    def prover_cost(self):
        k = (rows-1).bit_length()
        n = 1 << k
        iffts = 0
        ffts = [R*rows,
                ???,         # "after some FFTs"
               ]
        msms = [rows,
                rows,        # permutation poly
                [R*rows]*R,  # "which it commits to in R separate commitments"
                [3]*(R+A) ?, # "openings for each wire at each location a gate queries it at"
                [rows],      # "opening polynomial to show these openings are correct"
                ???,         # "combined using random challenges and the prover opens it"
               ]
        return Cost(iffts, ffts, 0)

    def verifier_cost(self):
        msms = 0
        return Cost(0, 0, msms)


def main():
    k = 17
    N = 1<<k
    ...

    ecc = Block(advice, selector, ?)
    rescue = Block(..., ..., ?)
    app = Block(..., ..., ?)
    model = Model({ecc: ..., rescue: ..., app: ...})

    print("k:       ", k
    print("prover:  ", model.prover_cost())
    print("verifier:", model.verifier_cost())
    print("circuit: ", model)


main()
