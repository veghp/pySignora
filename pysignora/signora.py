def signora(genelist, gps):
    import pandas as pd
    import scipy.stats as stats
    # M is the total number of objects (all GPSs)
    # n is the total number of Type I objects (GPSs of pathway)
    # N is drawn without replacement from the population (GPSs of genelist)
    # x is the number of Type I objects in N (GPSs of pathway in genelist)

    M = len(gps['g1']) # constant

    genelist_which = gps['g1'].isin(genelist) & gps['g2'].isin(genelist)
    genelist_gps = gps[genelist_which]

    N = len(genelist_gps['g1']) # constant

    # n_vector stores one n for each pathway:
    n_vector = gps['pwy'].value_counts()

    repo_pw = n_vector.index.tolist() # gpsrepo pathways
    genelist_pw = list(set(genelist_gps['pwy'])) # genelist-gpsrepo pathways

    # x_vector stores one x for each pathway:
    x_vector = [None] * len(n_vector)
    for counter, p in enumerate(repo_pw):
        x = genelist_pw.count(p)
        x_vector[counter] = x

    pvalues = [None] * len(repo_pw)
    for i, p in enumerate(repo_pw):
        pvalues[i] = 1 - stats.hypergeom.cdf(x_vector[i], M, n_vector[i], N)

    d = {'Pathway': pd.Series(repo_pw, index=repo_pw),
         'Pvalue': pd.Series(pvalues, index=repo_pw)}
    results = pd.DataFrame(d)

    return results
