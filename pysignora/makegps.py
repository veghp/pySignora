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


def makegps(repodf):
    # repodf is a pandas dataframe listing pathway-gene association with
    # 3 columns: pathway name/id, description, gene
    import pandas as pd

    repodf.columns = ["pwy", "desc", "gene"]
    repodf.drop_duplicates(inplace=True)

    # matrix format of bipartite graph:
    repomatrix = pd.crosstab(repodf.gene, repodf.pwy)

    # pwy_degree = repomatrix.sum(axis=0)
    # gene_degree = repomatrix.sum(axis=1)
    # pug = gene_degree[gene_degree == 1] # pathway-unique genes

    # gene-gene graph. Edge weight is the number of common pathways:
    repotransform = (repomatrix).dot(repomatrix.T)

    # this section converts the matrix into a gene-gene-weight format
    edgelist_genes = repotransform.unstack()
    edgelist_genes.index.names = ["g1", "g2"]
    edgelist_genes = edgelist_genes.reset_index()
    edgelist_genes.rename(columns={0: "weight"}, inplace=True)
    edgelist_genes = edgelist_genes[edgelist_genes.weight != 0].reset_index(drop=True)

    # gene-pair signatures (gps) are gene-pairs specific to 1 pathway:
    edgelist_genes_gp = edgelist_genes[edgelist_genes["weight"] == 1]
    edgelist_genes_gp = edgelist_genes_gp.reset_index(drop=True)

    # assign pathway to each gps:
    pwy_list = [None] * len(edgelist_genes_gp["g1"])
    for index in range(0, len(pwy_list)):  # range is [a, b[
        g1 = edgelist_genes_gp["g1"][index]
        g2 = edgelist_genes_gp["g2"][index]
        pwy_list[index] = repomatrix.columns[repomatrix.loc[[g1, g2]].sum(axis=0) == 2][
            0
        ]
        # part ...[0] retrieves the string

    edgelist_genes_gp["pwy"] = pwy_list

    return edgelist_genes_gp
