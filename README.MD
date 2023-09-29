
In these codes,  a trajectory of a 40ns long MD simulation of calmodulin (CaM) is given as an example.x

# PRS
This code enables the monitoring of conformational changes  and facilitates the study of the mechanisms underlying these shifts in conformation.(Atilgan & Atilgan, 2009)
### Code works as follows,
1. In this Jupyter Notebook code, PDB and DCD files of the initial structure should be provided.(In this example, initial.pdb and initial.dcd) 
2. Carbon alpha atoms should be selected as "calpha"
3. Final PDB structure should be placed. (In this example, final.pdb)
4. The script perturbs 200 times for each Carbon alpha residue in initial structure
6. This code operates with both the Covariance and Hessian matrices. As a result, it calculates overlaps and correlation coefficients between the final and initial structures twice.("corr_coeff.dat", "avg_overlap_anm.dat" outputs belong to Covariance matrix; "maximum_overlap_anm.dat","corr_coeff_anm.dat" belong to Hessian matrix)
7. The output files of this code should include overlap, correlation coefficients, and RMSD of the mean initial structure. (In this example: "avg_overlap.dat", "maximum_overlap.dat", "corr_coeff.dat", "avg_overlap_anm.dat", "maximum_overlap_anm.dat","corr_coeff_anm.dat")   


# Mode Analysis

This code facilitates the calculation of dominant motions with principal component analysis.(Bakan & Bahar, 2011)
### This code made by using Jupyter Notebook and works as follows,

1. PDB and DCD files should be placed to parse PDB file and parse DCD file on it. (In this example, input files are: initial.pdb and initial.dcd) 
2. Carbon alpha atoms should be selected as "calpha"
2. This code provides both calculation of normal modes and generation of cross correlation matrix to use further analysis.
3. The output files of this code should include cross correlation plot, nmd and eigenvalue contribution files. (In this example, cross_corr.dat, protein_pca.nmd, protein_eigvals_contribution.dat, protein_correlation.png)
4. Modes can be visualised using the VMD plugin(Normal Mode wizard) with nmd output. 

