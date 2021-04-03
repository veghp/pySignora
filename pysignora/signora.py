# Copyright 2019 Peter Vegh
#
# This file is part of pySignora.
#
# pySignora is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pySignora is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pySignora.  If not, see <https://www.gnu.org/licenses/>.


def signora(genelist, gps):
    import pandas as pd
    import scipy.stats as stats

    # M is the total number of objects (all GPSs)
    # n is the total number of Type I objects (GPSs of pathway)
    # N is drawn without replacement from the population (GPSs of genelist)
    # x is the number of Type I objects in N (GPSs of pathway in genelist)

    M = len(gps["g1"])  # constant

    genelist_which = gps["g1"].isin(genelist) & gps["g2"].isin(genelist)
    genelist_gps = gps[genelist_which]

    N = len(genelist_gps["g1"])  # constant

    # n_vector stores one n for each pathway:
    n_vector = gps["pwy"].value_counts()

    repo_pw = n_vector.index.tolist()  # gpsrepo pathways
    genelist_pw = list(set(genelist_gps["pwy"]))  # genelist-gpsrepo pathways

    # x_vector stores one x for each pathway:
    x_vector = [None] * len(n_vector)
    for counter, p in enumerate(repo_pw):
        x = genelist_pw.count(p)
        x_vector[counter] = x

    pvalues = [None] * len(repo_pw)
    for i, p in enumerate(repo_pw):
        pvalues[i] = 1 - stats.hypergeom.cdf(x_vector[i], M, n_vector[i], N)

    ntests = len(pvalues)
    bonferroni = pvalues * float(ntests)

    d = {
        "Pathway": pd.Series(repo_pw, index=repo_pw),
        "Pvalue": pd.Series(pvalues, index=repo_pw),
        "Pvalue_corr": pd.Series(bonferroni, index=repo_pw),
    }
    results = pd.DataFrame(d)

    return results
