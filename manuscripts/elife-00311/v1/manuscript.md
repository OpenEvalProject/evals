# Modelling dynamics in protein crystal structures by ensemble refinement

## Authors

- B Tom Burnley<sup>1</sup>
- Pavel V Afonine<sup>2</sup>
- Paul D Adams<sup>2</sup>
- Piet Gros<sup>1</sup> †

### Affiliations

1. Crystal and Structural Chemistry, Bijvoet Center for Biomolecular Research, Department of Chemistry, Faculty of Science Utrecht University Utrecht The Netherlands
2. Lawrence Berkeley National Laboratory Berkeley United States
3. Department of Bioengineering University of California Berkeley Berkeley United States

† Corresponding author

## Abstract

Single-structure models derived from X-ray data do not adequately account for the inherent, functionally important dynamics of protein molecules. We generated ensembles of structures by time-averaged refinement, where local molecular vibrations were sampled by molecular-dynamics (MD) simulation whilst global disorder was partitioned into an underlying overall translation–libration–screw (TLS) model. Modeling of 20 protein datasets at 1.1–3.1 Å resolution reduced cross-validated Rfree values by 0.3–4.9%, indicating that ensemble models fit the X-ray data better than single structures. The ensembles revealed that, while most proteins display a well-ordered core, some proteins exhibit a ‘molten core’ likely supporting functionally important dynamics in ligand binding, enzyme activity and protomer assembly. Order–disorder changes in HIV protease indicate a mechanism of entropy compensation for ordering the catalytic residues upon ligand binding by disordering specific core residues. Thus, ensemble refinement extracts dynamical details from the X-ray data that allow a more comprehensive understanding of structure–dynamics–function relationships.

## Introduction

Since the dawn of structural biology there have been experimental observations of dynamic motion in proteins and other biomolecules (Linderstrøm-Lang and Schellman, 1959). Multiple biophysical methods have firmly established that such atomic ‘wigglings and jigglings’ (Feynman et al., 1963) play an inherent role in both protein structure and function; and, in conjunction with high-resolution structures insights into dynamics aid the understanding of biomolecular functions in catalysis, ligand or drug binding and macromolecular interactions. Presently X-ray diffraction and NMR spectroscopy are the primary source of data for high-resolution protein structures. Whereas microscopy methods may provide information regarding long-range conformational changes, NMR characterizes fluctuations at atomic detail. However, due to the challenging nature of such experiments the number of dynamics studies is relatively sparse in contrast with the wealth of structural information available in the Protein Data Bank (PDB) (Berman et al., 2000). The majority of entries in the PDB derived from X-ray diffraction data are presented as static, single, structures, although there is often extensive disorder resulting from protein dynamics and crystal-lattice distortions. Extracting atomic fluctuations from these diffraction data would dramatically increase the scope for dynamics studies of biomolecules and potentially reveal atomic details of structure–function–dynamic mechanisms that have previously been obscured.

The diffraction data of proteins are affected by multiple sources of disorder, notably arising from atomic vibrations, concerted motions of protein domains and inter-molecular lattice distortions. Structural models of proteins should account for both anisotropic and anharmonic distributions around the mean atomic positions to reproduce the observed Bragg intensities accurately (Vitkup et al., 2002; Furnham et al., 2006). However, explicit modelling of such distributions in macromolecules using current methods requires extensive parameterization inappropriate for the diffraction quality of a typical protein crystal. Multi-conformer structures represent both anisotropic and anharmonic disorder, but despite numerous attempts at automating the inclusion of minor conformations (DePristo et al., 2004; Levin et al., 2007; Terwilliger et al., 2007; Korostelev et al., 2009; van den Bedem et al., 2009; Lang et al., 2010), 95% of all protein residues in the Protein Data Bank (PDB) (Berman et al., 2000) derived from diffraction data are modelled with a single conformation (Lang et al., 2010). As opposed to multiple discrete models, a MD simulation with time-averaged restraints (Gros et al., 1990) results in a population of structures in which the individual models are interrelated by a Boltzmann-weighted energy function. This method introduced by Torda et al. (1989) and implemented in macromolecular crystallography by Gros et al. (1990), showed a reduction in R-value. However, cross-validation introduced subsequently (Brünger, 1992) revealed chronically over-fitted models (Burling and Brunger, 1994; Clarage and Phillips, 1994; Schiffer et al., 1995).

Here, we present an ensemble-refinement method that restricts the number of structures modelled and thereby prevents over-fitting of the data. We model large-scale motions, attributable to, for example, lattice distortions, by an underlying global disorder model. This approach allows MD simulations to sample local atomic fluctuations only, without the need for sampling large-scale global disorder. We show that the method yields reproducible ensembles with improved fit to the X-ray data, as validated by cross validation, Rfree (Brünger, 1992), and stereochemical analyses. Analyses of the ensembles show that detailed features are observed indicating atomic fluctuations that may be relevant for the biological function of the macromolecules.

## Results and discussion

### Ensemble refinement of 20 datasets from the PDB

We performed MD simulations, in which the model was restrained by a time-averaged X-ray (Gros et al., 1990), maximum-likelihood (Pannu and Read, 1996; Adams et al., 1997; Murshudov et al., 1997) target function (see ‘Materials and methods’). The X-ray restraint optimized 〈Fcalc(hkl)〉 against Fobs(hkl), where 〈Fcalc(hkl)〉 are computed as rolling averages from the structures in the MD trajectory, with the length of the averaging window determined by the relaxation time τx. This approach contrasts with the traditional crystallographic refinement approach, where Fcalc(hkl) are computed from a single structure and optimized against Fobs(hkl).

Prior to the simulations we approximated the large-scale disorder by an overall TLS model derived from the atomic B-factors of the refined single structure. Using one TLS group per protein molecule or domain, we iteratively fitted TLS parameters (Schomaker and Trueblood, 1968; Winn et al., 2001) to the atomic B-factors of the protein atoms excluding atoms with large deviations in B-factor from the TLS-derived B-factor (the parameter pTLS described the percentage of atoms included in TLS-fitting; see ‘Materials and methods’). The resulting TLS model was applied to all atoms throughout the simulation. Effectively, this TLS model of the protein core excludes the effects of hyper-flexible surface loops and, hence, describes the global disorder that may be attributed to inter-molecular lattice distortions and overall intra-molecular breathing or domain shifts.

Ensemble refinement was tested using 20 diffraction datasets from the PDB and started from either the PDB or PDB_REDO (Joosten et al., 2010) structures (‘Materials and methods’). Upper resolution limits of the datasets ranged from 1.1 to 3.1 Å resolution and structures had 50 to 1,004 amino-acid residues in the asymmetric unit (Table 1). The simulations were run at an effective temperature of 300 K for the protein atoms, using a temperature bath (Tbath) slightly below 300 K to allow for heating due to the non-conservative nature of the time-averaged X-ray restraint modulated by its weight wx-ray (‘Materials and methods’). Explicitly modelled solvent atoms were added and/or removed intermittently during the simulation dependent on the corresponding electron-density and difference maps (‘Materials and methods’). Bulk solvent effects were accounted for by an averaged Flat Bulk-Solvent Model (Jiang and Brünger, 1994; Afonine et al., 2005) (‘Materials and methods’). The parameters pTLS, τx and the Tbath and wx-ray pair were optimized in a grid search resulting in a shallow optimum scored by Rfree (Figure 1A). After a period of equilibration, the trajectory of structures was acquired over an extensive period of time (40 times τx).

**Table 1.**
 Ensemble refinement statistics for 20 datasets. Datasets were taken from the PDB or PDB_REDO and were re-refined using ensemble refinement and phenix.refine. The relaxation time τx used, the resulting number of structures in the final ensemble and Rwork and Rfree values are given. The ensemble models yield improved Rfree values for all datasets, ranging in improvement from 0.3% to 4.9% with a mean improvement of 1.8%. The PDB accession numbers are as follows: 1KZK (Reiling et al., 2002), 3K0M (Fraser et al., 2009), 3K0N (Fraser et al., 2009), 2PC0 (Heaslet et al., 2007), 1UOY (Olsen et al., 2004), 3CA7 (Klein et al., 2008), 2R8Q (Wang et al., 2007), 3QL0 (Bhabha et al., 2011), 1X6P (Dunlop et al., 2005), 1F2F (Kimber et al., 2000), 3QL3 (Bhabha et al., 2011), 1YTT (Burling et al., 1996), 3GWH (Rodríguez et al., 2009), 1BV1 (Gajhede et al., 1996), 1IEP (Nagar et al., 2002), 2XFA (Singh et al., 2011), 3ODU (Wu et al., 2010), 1M52 (Nagar et al., 2002), 3CM8 (He et al., 2008) and 3RZE (Shimamura et al., 2011)


<table>
  <thead>
    <tr>
      <th rowspan="2">PDB ID</th>
      <th rowspan="2">Resolution (Å)</th>
      <th colspan="4">Ensemble refinement</th>
      <th colspan="2">phenix.refine</th>
      <th colspan="2">Ensemble—phenix.refine</th>
    </tr>
    <tr>
      <th>τx (ps)</th>
      <th>No. of structures</th>
      <th>Rwork</th>
      <th>Rfree</th>
      <th>Rwork</th>
      <th>Rfree</th>
      <th>ΔRwork</th>
      <th>ΔRfree</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1KZK</td>
      <td>1.1</td>
      <td>1.5</td>
      <td>600</td>
      <td>0.125</td>
      <td>0.153</td>
      <td>0.136</td>
      <td>0.155</td>
      <td>−0.011</td>
      <td>−0.003</td>
    </tr>
    <tr>
      <td>3K0M</td>
      <td>1.3</td>
      <td>2.0</td>
      <td>250</td>
      <td>0.104</td>
      <td>0.129</td>
      <td>0.116</td>
      <td>0.132</td>
      <td>−0.012</td>
      <td>−0.003</td>
    </tr>
    <tr>
      <td>3K0N</td>
      <td>1.4</td>
      <td>1.0</td>
      <td>209</td>
      <td>0.115</td>
      <td>0.133</td>
      <td>0.119</td>
      <td>0.143</td>
      <td>−0.004</td>
      <td>−0.010</td>
    </tr>
    <tr>
      <td>2PC0</td>
      <td>1.4</td>
      <td>0.8</td>
      <td>250</td>
      <td>0.145</td>
      <td>0.188</td>
      <td>0.161</td>
      <td>0.193</td>
      <td>−0.016</td>
      <td>−0.005</td>
    </tr>
    <tr>
      <td>1UOY</td>
      <td>1.5</td>
      <td>1.0</td>
      <td>167</td>
      <td>0.104</td>
      <td>0.137</td>
      <td>0.155</td>
      <td>0.185</td>
      <td>−0.051</td>
      <td>−0.049</td>
    </tr>
    <tr>
      <td>3CA7</td>
      <td>1.5</td>
      <td>0.8</td>
      <td>40</td>
      <td>0.149</td>
      <td>0.184</td>
      <td>0.171</td>
      <td>0.212</td>
      <td>−0.022</td>
      <td>−0.029</td>
    </tr>
    <tr>
      <td>2R8Q</td>
      <td>1.5</td>
      <td>1.0</td>
      <td>200</td>
      <td>0.132</td>
      <td>0.162</td>
      <td>0.158</td>
      <td>0.178</td>
      <td>−0.026</td>
      <td>−0.016</td>
    </tr>
    <tr>
      <td>3QL0</td>
      <td>1.6</td>
      <td>0.5</td>
      <td>70</td>
      <td>0.204</td>
      <td>0.254</td>
      <td>0.229</td>
      <td>0.270</td>
      <td>−0.024</td>
      <td>−0.017</td>
    </tr>
    <tr>
      <td>1X6P</td>
      <td>1.6</td>
      <td>1.0</td>
      <td>400</td>
      <td>0.121</td>
      <td>0.149</td>
      <td>0.140</td>
      <td>0.175</td>
      <td>−0.019</td>
      <td>−0.026</td>
    </tr>
    <tr>
      <td>1F2F</td>
      <td>1.7</td>
      <td>0.8</td>
      <td>143</td>
      <td>0.128</td>
      <td>0.168</td>
      <td>0.160</td>
      <td>0.198</td>
      <td>−0.032</td>
      <td>−0.031</td>
    </tr>
    <tr>
      <td>3QL3</td>
      <td>1.8</td>
      <td>0.5</td>
      <td>80</td>
      <td>0.160</td>
      <td>0.208</td>
      <td>0.170</td>
      <td>0.221</td>
      <td>−0.010</td>
      <td>−0.013</td>
    </tr>
    <tr>
      <td>1YTT</td>
      <td>1.8</td>
      <td>0.3</td>
      <td>84</td>
      <td>0.139</td>
      <td>0.174</td>
      <td>0.166</td>
      <td>0.189</td>
      <td>−0.027</td>
      <td>−0.014</td>
    </tr>
    <tr>
      <td>3GWH</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>39</td>
      <td>0.160</td>
      <td>0.200</td>
      <td>0.187</td>
      <td>0.220</td>
      <td>−0.027</td>
      <td>−0.021</td>
    </tr>
    <tr>
      <td>1BV1</td>
      <td>2.0</td>
      <td>0.4</td>
      <td>78</td>
      <td>0.149</td>
      <td>0.182</td>
      <td>0.154</td>
      <td>0.205</td>
      <td>−0.005</td>
      <td>−0.023</td>
    </tr>
    <tr>
      <td>1IEP</td>
      <td>2.1</td>
      <td>0.5</td>
      <td>200</td>
      <td>0.183</td>
      <td>0.238</td>
      <td>0.196</td>
      <td>0.245</td>
      <td>−0.012</td>
      <td>−0.007</td>
    </tr>
    <tr>
      <td>2XFA</td>
      <td>2.1</td>
      <td>1.0</td>
      <td>100</td>
      <td>0.171</td>
      <td>0.217</td>
      <td>0.184</td>
      <td>0.244</td>
      <td>−0.013</td>
      <td>−0.027</td>
    </tr>
    <tr>
      <td>3ODU</td>
      <td>2.5</td>
      <td>0.3</td>
      <td>50</td>
      <td>0.208</td>
      <td>0.269</td>
      <td>0.219</td>
      <td>0.281</td>
      <td>−0.010</td>
      <td>−0.012</td>
    </tr>
    <tr>
      <td>1M52</td>
      <td>2.6</td>
      <td>0.5</td>
      <td>50</td>
      <td>0.161</td>
      <td>0.211</td>
      <td>0.168</td>
      <td>0.228</td>
      <td>−0.007</td>
      <td>−0.017</td>
    </tr>
    <tr>
      <td>3CM8</td>
      <td>2.9</td>
      <td>0.5</td>
      <td>67</td>
      <td>0.194</td>
      <td>0.235</td>
      <td>0.205</td>
      <td>0.248</td>
      <td>−0.011</td>
      <td>−0.013</td>
    </tr>
    <tr>
      <td>3RZE</td>
      <td>3.1</td>
      <td>0.1</td>
      <td>72</td>
      <td>0.210</td>
      <td>0.280</td>
      <td>0.210</td>
      <td>0.291</td>
      <td>0.000</td>
      <td>−0.011</td>
    </tr>
    <tr>
      <td rowspan="3" colspan="7"></td>
      <td>Max</td>
      <td>−0.051</td>
      <td>−0.049</td>
    </tr>
    <tr>
      <td>Min</td>
      <td>0.000</td>
      <td>−0.003</td>
    </tr>
    <tr>
      <td>Mean</td>
      <td>−0.018</td>
      <td>−0.018</td>
    </tr>
  </tbody>
</table>

![Figure 1.](https://cdn.elifesciences.org/articles/00311/elife-00311-fig1-v1.jpg)

**Figure 1.:** Example of ensemble refinement for dataset 1UOY. (A) Optimisation of empirical ensemble refinement parameters (τx, pTLS and Tbath). Simulations are performed independently and in parallel. The plot shows effect of τx, pTLS on Rfree (each grid point corresponds to the lowest Rfree among all Tbath values). Optimum parameters are selected by Rfree. (B) R-values obtained during ensemble-refinement simulation, solid lines Rwork and dashed lines Rfree; high values are observed for instantaneous models (yellow) contrasting with the rolling average used in the target function (red) and the final ensemble (blue). (C) R-values are reduced throughout the resolution range for ensemble model (blue) compared with phenix.refine re-refined single structure (black); solid lines Rwork and dashed line Rfree. (D) Number of structures in the ensemble, reduced by equidistant selection, versus Rwork (solid line) and Rfree (dashed line). Final number of structures is selected as the minimum number required reproducing the Rfree + 0.1%; in this case resulting in an ensemble containing 167 structures. (E) Density difference maps for the ensemble structure (mFobs − DFmodel)exp[iφmodel], left-hand side, and the single structure right-hand side, contoured at 0.34 e/Å3 (equivalent to 3.0 σ for the ensemble model), positive and negative densities are coloured green and red respectively. All molecular graphics figures are drawn using PyMol (The PyMOL Molecular Graphics System, Schrödinger, LLC).

Figure 1B shows the R-values as they developed over the simulation time for a structure with PDB code 1UOY (Olsen et al., 2004), for which the largest improvement in Rfree was observed among the datasets tested (possibly due to the high degree of anisotropic and anharmonic side-chain motion for this case). The R-values started at a high value and remained high (∼35%) for the individual structures, which is in agreement with the observation that the derived global TLS B-factor model is not optimal for fitting a single structure to the data. Averaging the structure factors over the relaxation time τx of 1 ps (corresponding to the rolling average structure factors used in the X-ray restraint) dropped the Rwork and Rfree to ∼11% and ∼15% respectively. The Rwork and Rfree of the collected ensemble of structures (corresponding to unweighted averaged structure factors) monotonically decreased to 10.3 and 13.7% respectively. over the acquisition period of 40 ps. The improvement in R-values from the ensemble model with respect to the single-structure model spanned the entire resolution range of the data (Figure 1C). Acquisition over 40 times τx yielded a highly redundant set of structures. We reduced the number of structures by calculating the minimum number of structures, that is 167 in the case of 1UOY, required to reproduce the R-value of the trajectory (Figure 1D and ‘Materials and methods’).

Analysis of all 20 datasets showed that ensemble refinement improved the Rfree by between 0.3 and 4.9 percentage points compared to single structures re-refined using the same program package, that is Phenix (Afonine et al., 2012), with a mean improvement of 1.8% in Rfree values (Table 1, Figure 2A). The effect of the starting structure on ensemble refinement was assessed by using alternative refinement programs, phenix.refine, Refmac (Vagin et al., 2004), and Buster (Bricogne et al., 2009), to generate varying input models. No significant differences were observed due to the different starting models (Tables 3 and 4). The improvement in Rfree, number of structures in the final ensemble and the averaging time τx tended to increase with resolution (Figure 2A–C). The optimum values for the parameters pTLS and Tbath are not correlated with resolution (Figure 2D,E). Concomitant with the reduction in R-values, the ensemble models reduced electron-density differences, decreasing rms fluctuations in difference maps by 0 to 41% with an average of 12% improvement (Table 2). The difference electron-density maps for the single-structure and ensemble models indicated improvements throughout the asymmetric unit cell, as exemplified in Figure 1E.

![Figure 2.](https://cdn.elifesciences.org/articles/00311/elife-00311-fig2-v1.jpg)

**Figure 2.:** Ensemble refinement parameters and results as function of resolution of the datasets. (A) Gain in Rfree of ensemble refinement compared with re-refinement using phenix.refine, (B) number of structures in the final ensemble model, (C) optimum relaxation time, τx, (D) optimum pTLS and (E) optimum Tbath plotted as function of resolution of the dataset.

**Table 2.**
 Rms (mFobs − DFmodel)exp[iφmodel] difference densities obtained from ensemble refinement and re-refinement in phenix.refine


<table>
  <thead>
    <tr>
      <th rowspan="2">PDB ID</th>
      <th rowspan="2">Resolution (Å)</th>
      <th colspan="2">σmFo−DFc (e/Å3)</th>
    </tr>
    <tr>
      <th>Ensemble</th>
      <th>phenix.refine</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1KZK</td>
      <td>1.1</td>
      <td>0.138</td>
      <td>0.161</td>
    </tr>
    <tr>
      <td>3K0M</td>
      <td>1.3</td>
      <td>0.016</td>
      <td>0.018</td>
    </tr>
    <tr>
      <td>3K0N</td>
      <td>1.4</td>
      <td>0.007</td>
      <td>0.008</td>
    </tr>
    <tr>
      <td>2PCO</td>
      <td>1.4</td>
      <td>0.099</td>
      <td>0.099</td>
    </tr>
    <tr>
      <td>1UOY</td>
      <td>1.5</td>
      <td>0.115</td>
      <td>0.162</td>
    </tr>
    <tr>
      <td>3CA7</td>
      <td>1.5</td>
      <td>0.132</td>
      <td>0.148</td>
    </tr>
    <tr>
      <td>2R8Q</td>
      <td>1.5</td>
      <td>0.104</td>
      <td>0.118</td>
    </tr>
    <tr>
      <td>3QL0</td>
      <td>1.6</td>
      <td>0.124</td>
      <td>0.138</td>
    </tr>
    <tr>
      <td>1X6P</td>
      <td>1.6</td>
      <td>0.098</td>
      <td>0.105</td>
    </tr>
    <tr>
      <td>1F2F</td>
      <td>1.7</td>
      <td>0.104</td>
      <td>0.126</td>
    </tr>
    <tr>
      <td>3QL3</td>
      <td>1.8</td>
      <td>0.131</td>
      <td>0.139</td>
    </tr>
    <tr>
      <td>1YTT</td>
      <td>1.8</td>
      <td>0.170</td>
      <td>0.215</td>
    </tr>
    <tr>
      <td>3GWH</td>
      <td>2.0</td>
      <td>0.125</td>
      <td>0.138</td>
    </tr>
    <tr>
      <td>1BV1</td>
      <td>2.0</td>
      <td>0.109</td>
      <td>0.119</td>
    </tr>
    <tr>
      <td>1IEP</td>
      <td>2.1</td>
      <td>0.084</td>
      <td>0.091</td>
    </tr>
    <tr>
      <td>2XFA</td>
      <td>2.1</td>
      <td>0.069</td>
      <td>0.074</td>
    </tr>
    <tr>
      <td>3ODU</td>
      <td>2.5</td>
      <td>0.105</td>
      <td>0.113</td>
    </tr>
    <tr>
      <td>1M52</td>
      <td>2.6</td>
      <td>0.088</td>
      <td>0.093</td>
    </tr>
    <tr>
      <td>3CM8</td>
      <td>2.9</td>
      <td>0.036</td>
      <td>0.036</td>
    </tr>
    <tr>
      <td>3RZE</td>
      <td>3.1</td>
      <td>0.070</td>
      <td>0.070</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Effect of input structure on ensemble refinement. For three datasets ensemble refinement was performed using a starting structure from three different refinement programs. For each structure three random number seed repeats of ensemble refinement were performed and the R-factors are shown to be highly similar


<table>
  <thead>
    <tr>
      <th rowspan="3">PDB</th>
      <th rowspan="2" colspan="3">Re-refinement</th>
      <th colspan="8">Ensemble refinement</th>
    </tr>
    <tr>
      <th colspan="2">Repeat 1</th>
      <th colspan="2">Repeat 2</th>
      <th colspan="2">Repeat 3</th>
      <th colspan="2">Mean</th>
    </tr>
    <tr>
      <th>Program</th>
      <th>Rwork</th>
      <th>Rfree</th>
      <th>Rwork</th>
      <th>Rfree</th>
      <th>Rwork</th>
      <th>Rfree</th>
      <th>Rwork</th>
      <th>Rfree</th>
      <th>Rwork</th>
      <th>Rfree</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">1UOY</td>
      <td>Buster</td>
      <td>0.167</td>
      <td>0.196</td>
      <td>0.108</td>
      <td>0.144</td>
      <td>0.112</td>
      <td>0.145</td>
      <td>0.110</td>
      <td>0.146</td>
      <td>0.110</td>
      <td>0.145</td>
    </tr>
    <tr>
      <td>Refmac</td>
      <td>0.147</td>
      <td>0.170</td>
      <td>0.104</td>
      <td>0.137</td>
      <td>0.103</td>
      <td>0.140</td>
      <td>0.105</td>
      <td>0.144</td>
      <td>0.104</td>
      <td>0.140</td>
    </tr>
    <tr>
      <td>Phenix</td>
      <td>0.155</td>
      <td>0.185</td>
      <td>0.109</td>
      <td>0.142</td>
      <td>0.109</td>
      <td>0.147</td>
      <td>0.111</td>
      <td>0.149</td>
      <td>0.110</td>
      <td>0.146</td>
    </tr>
    <tr>
      <td rowspan="3">3CA7</td>
      <td>Buster</td>
      <td>0.177</td>
      <td>0.208</td>
      <td>0.137</td>
      <td>0.186</td>
      <td>0.137</td>
      <td>0.192</td>
      <td>0.141</td>
      <td>0.197</td>
      <td>0.138</td>
      <td>0.192</td>
    </tr>
    <tr>
      <td>Refmac</td>
      <td>0.170</td>
      <td>0.205</td>
      <td>0.139</td>
      <td>0.187</td>
      <td>0.135</td>
      <td>0.189</td>
      <td>0.138</td>
      <td>0.193</td>
      <td>0.137</td>
      <td>0.189</td>
    </tr>
    <tr>
      <td>Phenix</td>
      <td>0.171</td>
      <td>0.212</td>
      <td>0.138</td>
      <td>0.180</td>
      <td>0.142</td>
      <td>0.189</td>
      <td>0.148</td>
      <td>0.193</td>
      <td>0.142</td>
      <td>0.187</td>
    </tr>
    <tr>
      <td rowspan="3">1BV1</td>
      <td>Buster</td>
      <td>0.161</td>
      <td>0.204</td>
      <td>0.137</td>
      <td>0.184</td>
      <td>0.138</td>
      <td>0.185</td>
      <td>0.137</td>
      <td>0.186</td>
      <td>0.138</td>
      <td>0.185</td>
    </tr>
    <tr>
      <td>Refmac</td>
      <td>0.178</td>
      <td>0.231</td>
      <td>0.140</td>
      <td>0.182</td>
      <td>0.143</td>
      <td>0.184</td>
      <td>0.143</td>
      <td>0.189</td>
      <td>0.142</td>
      <td>0.185</td>
    </tr>
    <tr>
      <td>Phenix</td>
      <td>0.154</td>
      <td>0.205</td>
      <td>0.139</td>
      <td>0.188</td>
      <td>0.138</td>
      <td>0.189</td>
      <td>0.140</td>
      <td>0.189</td>
      <td>0.139</td>
      <td>0.189</td>
    </tr>
  </tbody>
</table>

**Table 4.**
 Fmodel cross-correlation scores for ensembles generated with different input models. Three different refinement programs generated alternative starting structures, see Table 3. The best ensemble was selected as judged by Rfree. Fmodel cross correlation scores are >0.99 for all pairs of ensemble structures for all three datasets


<table>
  <thead>
    <tr>
      <th rowspan="2">PDB</th>
      <th colspan="2">Ensemble pair</th>
      <th rowspan="2">CC</th>
    </tr>
    <tr>
      <th>Re-refined input</th>
      <th>Re-refined input</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">1UOY</td>
      <td>Refmac</td>
      <td>Buster</td>
      <td>0.997</td>
    </tr>
    <tr>
      <td>Refmac</td>
      <td>Phenix</td>
      <td>0.997</td>
    </tr>
    <tr>
      <td>Buster</td>
      <td>Phenix</td>
      <td>0.999</td>
    </tr>
    <tr>
      <td rowspan="3">3CA7</td>
      <td>Refmac</td>
      <td>Buster</td>
      <td>0.993</td>
    </tr>
    <tr>
      <td>Refmac</td>
      <td>Phenix</td>
      <td>0.992</td>
    </tr>
    <tr>
      <td>Buster</td>
      <td>Phenix</td>
      <td>0.996</td>
    </tr>
    <tr>
      <td rowspan="3">1BV1</td>
      <td>Refmac</td>
      <td>Buster</td>
      <td>0.992</td>
    </tr>
    <tr>
      <td>Refmac</td>
      <td>Phenix</td>
      <td>0.990</td>
    </tr>
    <tr>
      <td>Buster</td>
      <td>Phenix</td>
      <td>0.992</td>
    </tr>
  </tbody>
</table>

### Validation of ensemble refinement

We used the high-quality experimental phases available to high resolution for 1YTT of mannose-binding protein (Burling et al., 1996) to validate the ensemble-refinement method. The overall correlation coefficient between the electron-density map from the ensemble model (obtained without experimental phases) and the experimentally phased electron-density map was 0.903, compared with 0.873 and 0.895 for the published and re-refined single structures. These seemingly small improvements in overall quality indicators allow for significant local improvements. Real-space correlation coefficients (Brändén and Jones, 1990) highlighted marked local improvements for flexible residues in particular (Figure 3A) with 11 residues improving by more than 0.1 in correlation coefficient. This observation was consistent with local improvements in electron-density differences in regions of flexible or disordered side chains (Figure 3B). Moreover, the ensemble model contained structural details previously identified in a multiple-model approach by Burling et al. (1996), as shown for the anisotropic distribution for the side chain of Phe121 (Figure 3C) and diffuse water shells around hydrophobic residues (Figure 3D). Figure 3E shows that the most occupied water sites in the ensemble correlated with low atomic B-factors for waters in the single-structure model.

![Figure 3.](https://cdn.elifesciences.org/articles/00311/elife-00311-fig3-v1.jpg)

**Figure 3.:** Validation of ensemble refinement using dataset 1YTT with exceptionally high quality experimental phases. (A) Real space cross-correlation of experimentally phased electron density map (|Fobs|exp[iφobs]) and model map (|Fmodel|exp[iφmodel]) for the single-structure (black) and ensemble model (chain A and B, blue and red respectively) shows improvements particularly for disordered areas (atomic B-factors from the re-refined single structure are shown in grey dashed lines). (B) Example of improved vector-difference map (|Fobs|exp[iφobs] − |Fmodel|exp[iφmodel]), contoured at 0.71 e/Å3 equivalent to 2.5 σ for the single structure for Gln167, chain A, for single (left-hand side) and ensemble structure (right-hand side). (C) Conformer distribution of Phe121 (chain A) with the experimental phased map (|Fobs|exp[iφobs]) contoured at 1.4 σ is highly similar to the multi-conformer shown in Figure 1c in Burling et al. (1996). (D) Partially disordered solvent shell (red) around residue Leu203 (chain A) as anticipated in Burling et al. (1996). Ensemble structure with experimental phased experimental map (|Fobs|exp[iφobs]) contoured at 1.4 σ (left side) and 0.7 σ (right side), as shown in Figure 2b in Burling et al. (1996). (E) Scatter plot showing the anti-correlation between the B-factor of explicit solvent molecules in the re-refined single-structure and the relative occupancy of water molecules at that same position (within 0.5-Å distance) in the ensemble model. Due to the difficulty in differentiating between disorder (B-factor) and occupancy for explicitly modelled water atoms in single structures a high B-factor is likely to correspond to a partially occupied site.

Next, we analysed the stereochemistry of the computed ensemble models. The robustness of the observed atomic distributions was tested by repeating ensemble refinements 10 times using different random starting velocities. Figure 4A shows that the observed distributions are highly reproducible. With data extending to 1.5-Å resolution correlations above 0.99 were observed between residue distributions from separate runs. At lower resolutions, the majority of residues showed correlations above 0.95, with occasionally correlations dropping below 0.8 in very flexible regions (see Figure 4B,C). Clearly, the ensembles contain multiple values for each geometrical term that form a distribution, instead of a single stereochemical value obtained from a single structure; Figure 5A–D presents examples of side-chain distributions (by χ1 and χ2 angles) observed in the ensembles along with standard deviations computed from the 10 repeats. Averaged over all 20 cases, the rms deviations from idealized bond lengths, bond angles and dihedral angles for the re-refined single-structures were 0.010 Å, 1.26° and 15.2° respectively. (Figure 6—source data 1). These deviations decreased for the ensemble models by 0.002 Å, 0.26° and 6.6° respectively, when considering the centroids of the observed stereochemical distributions. Taking all fluctuations around the centroids (i.e. complete distributions) into account, these values increased by 0.002 Å, 0.33° and 4.0° respectively compared to the statistics from single structures. This indicates high stereochemical quality for the ensemble model, but that the ensemble of structures contained fluctuations exhibiting larger deviations from ideality. Figure 6A,B shows that high-energy conformations, as indicated by for example non-favourable Ramachandran φ,ψ-angle combinations, occurred transiently and were concentrated in regions of structural flexibility. Counting the most frequent Ramachandran classification for each φ,ψ-angle showed that the ensembles have a similar percentage for ‘allowed’ and an increased number of ‘outliers’ compared to the single structures (Figure 6C and Figure 6—source data 2). These analyses illustrate that in ensemble refinement conformations were sampled, rather than optimized to a single configuration as in single-structure refinement. Similar to Brünger (Brünger, 1992), we observe that lower Rfree values correlate with better quality of the Ramachandran statistics (Figure 6D).

![Figure 4.](https://cdn.elifesciences.org/articles/00311/elife-00311-fig4-v1.jpg)

**Figure 4.:** Sampling reproducibility of ensemble refinement. (A) Cross-correlations (CC) calculated for all pairs from 10 random-number seed repeat ensemble refinements of the 1UOY dataset extending to 1.5-Å resolution. (B) Cross correlations computed for 1BV1 (2.0-Å resolution); and, (C) for 3CM8 (2.9-Å resolution). Mean CC shown in solid blue (black error bars indicate ±1 σ). Cross correlations were computed from real-space Fmodel electron-density map correlations (Brändén and Jones, 1990). B-factors from the single structures refined using phenix.refine are shown in dotted grey lines.

![Figure 5.](https://cdn.elifesciences.org/articles/00311/elife-00311-fig5-v1.jpg)

**Figure 5.:** Reproducibility of side-chain rotamer distributions. Mean χ1 and χ2 distributions of four side-chains from the 10 repeats, with error bars ±1 σ, are shown for 1UOY. The four residues presented are those with the two highest CC values (see Figure 4A), (A) Gln11 (0.9999) and (B) Arg32 (0.9999), and the two lowest CC values, (C) Lys39 (0.9976) and (D) Arg13 (0.9966).

![Figure 6.](https://cdn.elifesciences.org/articles/00311/elife-00311-fig6-v1.jpg)

**Figure 6.:** Ramachandran analysis. Distribution of Ramachandran torsion angles classified as outliers (red) and allowed (blue) for ensemble models, 1UOY (A) and 1BV1 (B). Plot shows percentage of classification per residue (i.e. relative number of times a φ,ψ-torsion angle combination is scored as outlier or allowed as defined by phenix.ramalyze). Structure inserts show (left-hand side) the location of the non-favourable torsion angles, outliers (red) and allowed (blue), and (right-hand side) a B-factor putty representation for the single structure refined with phenix.refine. (C) Overall Ramachandran statistics for ensemble and re-refined models. The Ramachandran statistics for the ensemble models are calculated in two ways: blue shows the percentage of outliers (left side) or allowed (right side) from all structures in the ensemble (cf. ‘whole distribution’ in Figure 6—source data 1), whereas red shows these percentages based on the most frequent occurring classification of each φ,ψ combination (cf. ‘centroid distribution’). The grey lines show the percentage of allowed (left side) and outliers (right side) for the re-refined single structures. Ramachandran statistics per re-refined single structure and ensemble are given in Figure 6—source data 2. (D) Correlation of Ramachandran statistics with Rfree values obtained from ensemble refinement. Three ensemble refinements were performed for the dataset 1UOY using different random-number seeds at Tbath values of 220, 260, 280, 290 and 295 K. Shown are the number of Ramachandran outliers (left side) and allowed (right side) in the ensemble as function of the Rfree value.

The presence of non-crystallographic symmetry (NCS) allowed for crystallographically-independent observations of atomic fluctuations in multiple copies of a protein molecule (Figure 7A–C). In some cases, the applied global TLS models differed significantly between NCS-related copies (Figure 7B). Nevertheless, we observed atomic fluctuations similar both in magnitude and location for related copies in areas not affected by crystal packing (Figure 7B,C; additional cases of NCS are presented in Figure 7—figure supplement 1–4). Apparently, variations in overall disorder arising from packing differences of NCS copies (as indicated by different B-factor distributions) were well accounted for by the applied global TLS models. Similarly, a global increase in disorder present in a dataset collected at ambient temperature vs an isomorphous dataset collected under cryo-conditions was fully accounted for by an increase in global TLS (Figure 8A). These data indicate that the derived atomic fluctuations are molecular traits and that the global TLS model accounts for overall disorder, which includes for example lattice or packing effects.

![Figure 7.](https://cdn.elifesciences.org/articles/00311/elife-00311-fig7-v1.jpg)

**Figure 7.:** Comparison of atomic fluctuations for non-crystallographic symmetry related protein copies for dataset 1M52. (A) Cα trace of the re-refined single structure coloured by B-factor (from blue to red with increasing B-factor) for the two chains (left) and the B-factors plotted per residue number for protein chain A (blue) and B (red) (right). (B) B-factors from the basal TLS model (left) and rms atomic fluctuations (right) in the ensemble model averaged per residue. Differences in crystal packing restrict the flexibility of chain B around residue 47. (C) Comparison (left) and superposition (right) of a region of the protein (indicated by black box in (A)) of the ensemble of structures observed for protein copy A (blue) and B (red). Analogous analyses for 2R8Q, 1YTT, 1IEP and 2XFA are shown in Figure 7—figure supplements 1–4. The protein copies in 3GWH and 3ODU showed backbone shifts greater than 4.5 Å and were left out of this analysis.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/00311/elife-00311-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** Comparison of atomic fluctuations for NCS related protein copies for dataset 2R8Q.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/00311/elife-00311-fig7-figsupp2-v1.jpg)

**Figure 7—figure supplement 2.:** Comparison of atomic fluctuations for NCS related protein copies for dataset 1YTT.

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/00311/elife-00311-fig7-figsupp3-v1.jpg)

**Figure 7—figure supplement 3.:** Comparison of atomic fluctuations for NCS related protein copies for dataset 1IEP.

![Figure 7—figure supplement 4.](https://cdn.elifesciences.org/articles/00311/elife-00311-fig7-figsupp4-v1.jpg)

**Figure 7—figure supplement 4.:** Comparison of atomic fluctuations for NCS related protein copies for dataset 2XFA.

![Figure 8.](https://cdn.elifesciences.org/articles/00311/elife-00311-fig8-v1.jpg)

**Figure 8.:** Ensemble refinement of two isomorphous proline isomerase datasets collected at 100 K and 288 K. (A) Left, basal TLS B-factors of ensemble models for 100 K and 288 K datasets (blue and green, respectively). Right, atomic rms fluctuations of ensemble models for 100 K and 288 K datasets (blue and green, respectively). (B) Re-refined single-structure (left) and ensemble model (right) for 100 K dataset. (C) Re-refined single-structure and ensemble model for 288 K dataset. In (B) and (C) atoms are coloured by B-factor (5 to 25 Å2). As with the published single structure refinement (Fraser et al., 2009) alternative conformations were not found for residues Leu98, Ser99 and Phe113 at 100K.

### Functional dynamics revealed by ensemble refinement

Inspection of the obtained ensembles showed that most proteins, as expected, are characterized by well-ordered residues in the protein core and flexible residue side chains and loops on the outside (an example is given in Figure 9A). However, three cases exhibited marked flexibility of residue side chains on the inside of the molecule. 1BV1 (Gajhede et al., 1996), major birch pollen allergen, has a large forked solvent channel with multiple disordered side chains and a diffuse water network (Figure 9B). The cavity is consistent with its putative role as a general plant steroid carrier (Marković-Housley et al., 2003). Presumably, the flexible internal residues play a role in binding the diverse ligands. More surprising are the disordered cores in 1X6P of PAK pilin (Dunlop et al., 2005) (Figure 9C) and 3K0N of the enzyme proline isomerase (Fraser et al., 2009) (Figure 9D); in both these cases, the datasets were recorded at ambient temperatures. Multiple (16) aliphatic and aromatic side chains are highly flexible, forming a molten core in the pilin molecule. These flexible residues, which are extremely well conserved in the type IV pilin family, create the central interface between the characteristic long α-helix and β-sheet of this protein fold (Hazes et al., 2000). We hypothesize that this monomeric pilin structure represents an intermediate molten state, which becomes stabilized upon protomer filament formation. The third case with flexible residues on the interior is 3K0N of proline isomerase (Fraser et al., 2009). As with the pilin structure, several (11) aromatic and aliphatic residues showed large side chain fluctuations, yielding a molten core of the protein structure. However, the same protein under cryogenic conditions (3K0M) (Fraser et al., 2009) showed mostly well-ordered side chains in the ensemble (Figure 9D, right-hand side), indicating that at cryogenic conditions the molten core has been annealed to its ground state configuration. As discussed in more detail in the next paragraph, the observed flexibility of the core residues at ambient temperature is likely of functional relevance for the enzyme. Thus, the computed ensemble models highlighted a hitherto unnoticed phenomenon of molten cores in folded proteins, which are likely relevant for the biological function of these molecules.

![Figure 9.](https://cdn.elifesciences.org/articles/00311/elife-00311-fig9-v1.jpg)

**Figure 9.:** Overview of side-chain dynamics in ensemble structures. Atoms are coloured by their relative probability in the ensemble (see ‘Materials and methods’), reflecting the degree of disorder (ranging from well-ordered in blue to disordered in red). Bottom left insert shows secondary structure cartoon. Three datasets exhibit disordered interior sides chains forming a molten core region. (A) 3CA7 shows an ordered core with disordered hydrophilic side chains on the outside and is typical of the majority of the datasets. (B) 1BV1, the major pollen allergen and putative plant steroid transporter, has a disordered central cavity (location of cavity show with dotted lines). (C) 1X6P in the monomeric form of the fibril forming PAK pilin shows multiple disordered aliphatic and aromatic side chains in the interface between the N-terminal α-helix and the four stranded β-sheet domain. (D) Proline isomerase exhibits a molten core at 288 K, 3K0N (left); however, these interior dynamics are frozen-out at 100 K, 3K0M (right).

NMR spectroscopy has previously revealed specific dynamics for active-site residues of proline isomerase (Eisenmesser et al., 2005). The solvent-exposed residues Arg55 and Met61 in the active site showed disorder in 3K0M (Fraser et al., 2009), where data were collected at 100 K. For 3K0N collected at 288 K, a number of additional residues with multiple conformations were observed (Figure 8A,B). These included Ser99, Phe113, which are part of the substrate-binding pocket together with Arg55 and Met61 (Figure 10A), and Leu98, which neighbours the flexible residue Ser99 but points into the hydrophobic core (Fraser et al., 2009). Ensemble refinement of the 288 K data revealed a large number of residue side chains in the core to be flexible. This flexibility in the core appears to be linked to the dynamics of active-site residues through the intervening β-sheet. In particular, the main-chain H-bonding network (C=O·HN) of neighbouring β-strands within the sheet was flexible, as indicated by anisotropy in the C=O bonds of residues 55-62-113-98 (with the largest anisotropy observed for 55 and 62; see Figure 10B). Analysis of the side-chain conformations for the active-site residues Arg55, Met61, Ser99 and Phe113 showed a 10% minor conformation for the four active-site residues (Figure 10C), which is in good agreement with NMR relaxation data (see Figure 2 in Eisenmesser et al., 2005). Mutation of Ser99 to Thr (>14 Å away from the catalytic Arg55) affects the side-chain distributions and lowers the activity ∼300-fold, similar to an Arg55Lys mutation of the catalytic residue (Eisenmesser et al., 2005; Fraser et al., 2009). Thus, the ensemble refinement results support the notion put forward by Eisenmesser et al. and Fraser et al. that side chain dynamics play a critical role in the enzymatic function of proline isomerase and, moreover, expand upon this theme to reveal mechanistic insights arising from the underlying detailed dynamics.

![Figure 10.](https://cdn.elifesciences.org/articles/00311/elife-00311-fig10-v1.jpg)

**Figure 10.:** Dynamics in the binding pocket of proline isomerase at 288 K. (A) The location of the binding pocket comprised of residues Arg55, Met61, Ser99 and Phe113. (B) Zoom in of binding pocket (as dotted lines in (A)) showing flexible β-sheet for C=O·HN network of residues 55-62-113-98 in neighbouring β-strands. (C) All four residues show a ∼9:1 ratio between major and minor conformations which is in good agreement with NMR relaxation dispersion data collected a similar temperature (Eisenmesser et al., 2005). Histograms show mean χ1 angles generated from 10 random number repeats of ensemble refinement (error bars ±1 σ). Inserts show the relevant side chains, coloured by atomic probability (see ‘Materials and methods’), as observed in the ensemble reported in Table 1.

Ligand binding to HIV protease is known to have marked effects on the enzyme structure (Heaslet et al., 2007). We compared HIV protease in its apo form, 2PC0 (Heaslet et al., 2007), and bound to ligand JE-2147, 1KZK (Reiling et al., 2002). As for proline isomerase, HIV protease exhibited flexible, moldable, substrate-binding pockets in the apo state. Enthalpic and entropic binding of the ligand with high affinity (KD = 41 pM) (Velazquez-Campoy et al., 2001) reduced the flexibility in the substrate binding pockets by protein–ligand H-bond interactions and van der Waals stacking (Figure 11A,B). Upon ligand binding, Asp90 became ordered through H-bonding with the ligand in P2, whereas its dimeric partner lacked a H-bonding partner in P2′ and remained flexible as in the unbound state. The canonical aspartic protease catalytic residues, Asp25 of both monomers, became ordered upon ligand binding. Concomitantly, we observed significant changes in dynamics of specific core residues (Figure 11C). Some residues, most notably Thr26, ‘froze’ (Thr26 is part of the conserved Asp25-Thr26-Gly-27 sequence). In contrast, the side chains of other residues, most notably Cys95 and Leu97 opposite of Thr26, became highly disordered in the bound state, whereas they were relatively ordered in the unbound state. This observation supports NMR data that showed that conformational variability increases upon inhibitor binding for Leu97 amongst others (Torchia and Ishima, 2003). These data suggest that the entropy lost by the catalytic aspartates upon ligand binding is compensated with an increase in disorder of specific core residue side chains. This type of dynamic modulation was also observed for Ca2+ binding to calmodulin, where this effect was dubbed entropy compensation (Lee et al., 2000). Similar to the molten core dynamics for proline isomerase, the structure ensembles generated by the ensemble refinement method revealed specific core dynamics for HIV protease, in particular a conformational exchange that is likely functionally relevant.

![Figure 11.](https://cdn.elifesciences.org/articles/00311/elife-00311-fig11-v1.jpg)

**Figure 11.:** Comparison of ensemble structures of bound and unbound forms of HIV protease. (A) Residues in the P1 binding sites are disordered in the unbound HIV protease (2PC0), left-hand side, with carbon atoms shown in cyan, oxygen red and nitrogen blue. These residues become ordered in HIV protease in complex with a high affinity inhibitor, JE-2147 (1KZK), right-hand side with carbon atoms of the protease shown in green and of the inhibitor in purple. In 1KZK the two chains of the functional dimer are present in the asymmetric unit, whereas in 2PC0 a monomer is present in the asymmetric unit and the dimer is drawn using the crystallographic twofold axis. (B) Shows an alternative orientation showing the P2 binding site. (C) The catalytic Asp25 becomes ordered upon binding of the inhibitor, forming a hydrogen bond with the P1 carbonyl and hydroxyl of JE-2147. In contrast, the distal residues Cys95 and Leu97 at the dimer interface become less ordered upon binding.

The development of new small molecule therapeutics is often supported by the use of macromolecular structure, typically X-ray crystallography of complexes between target proteins and drug candidates. These complexes are typically interpreted as static structures, and the impact of dynamics, if considered at all, is probed using computational methods. Our new ensemble refinement approach makes it possible to study the role of dynamics in drug–target complexes in the context of the experimental data. Therefore, we analysed two structures of Abl kinase in complex with Imatinib (also known as Gleevec), that is 1IEP, and PD173955, that is 1M52 (Nagar et al., 2002). These compounds bind the Abl kinase with high affinity, 37 nM (Schindler et al., 2000) and 100 nM respectively (Nagar et al., 2002). The ensembles provide insights into the flexibility of the protein residues and the ligand moieties in the complex. Figure 12A shows the variation in H-bonding observed in Abl kinase–Imatinib. Variable H-bonding interactions were observed for the hydrophilic N-methylpiperazine moiety with the backbone carbonyl atoms of Ile360 and His361. In contrast, the ensemble displayed a well-ordered H-bond between the anilino-NH and Thr315 ‘gatekeeper’ side-chain. Moreover, the ordered water network between Glu286, Lys271 and the pyrimidine moiety of Imatinib (Nagar et al., 2002) was reproduced in the ensemble model (Figure 12B). We observed that the Abl kinase adopts two different states in these crystal structures. In the Imatinib complex the activation loop, residues 381–402, is highly disordered (Figure 12C), which was confirmed by comparison to previously published NMR data (Vajpai et al., 2008). In general, the ensemble models indicate details of tight and highly ordered drug–target interactions on one side vs disordered interactions elsewhere, which are indicative of less tight interactions, that may suggest which sites to modify in a drug-optimization cycle.

![Figure 12.](https://cdn.elifesciences.org/articles/00311/elife-00311-fig12-v1.jpg)

**Figure 12.:** ABL-kinase Imatinib binding site. (A) Imatinib binding site in chain A of the 1IEP dataset showing distribution of the six protein–ligand hydrogen bonds in chain A and chain B (red and blue respectively). (B) Hydrogen bond network of ordered water network observed in the re-refined single structure, left, and the ensemble model, right. (C) The activation loop (shown in pink) is disordered when ABL-kinase is complexed with Imatinib (shown in cyan) as observed previously in solution (Vajpai et al., 2008).

## Conclusions

We have shown that far more structural information can be reliably extracted from protein diffraction data than is achieved to date by traditional single-structure modelling methods. Our ensemble refinement method samples distributions that reflect structural details of protein dynamics. The resulting ensemble models provide a more comprehensive description of the molecules and allow interpretation of the molecular function in terms of both the three-dimensional arrangements of the protein residues and their flexibilities. Moreover, ensemble models minimize the risk of structural over-interpretation associated with the seemingly rigid single-structure models. We found comparative analyses of protein molecules in different states to be very useful for identifying detailed changes in structural dynamics that may be mechanistically relevant for the molecular function.

Partitioning large-scale disorder into a global model separates intermolecular variations of protein packing in the crystal from the detailed intra-molecular atomic fluctuations. Effectively, the X-ray gradient dictates the MD sampling to yield featureless, (mFobs−DFmodel)exp[iφmodel], electron-density difference maps, while the global disorder model is accounted for by taking BTLS into account when computing the atomic densities. In this way, the ensemble of structures is generated to model the anisotropic and anharmonic electron-density distributions precisely, while being restrained by the bonded and non-bonded energy terms used in the MD simulation. The separation of global disorder and local atomic fluctuations contrasts the original approach by Gros et al. (1990), where the MD sampling had to account for both the large scale global disorder and local fluctuations leading to very long relaxation times τx of 16 ps. In the current work much shorter relaxation times of 0.25–2 ps can be used, thereby limiting potential over-fitting markedly. The method is applicable to data with a wide range of upper resolution limits. We see marked improvements in Rfree for datasets ranging from 1.5 to 2.6-Å upper-resolution limit. A detailed interpretation of the ensembles is allowed, supported by the very high local correlations between independent ensemble refinements. However, at lower resolution limits and for highly disordered loops the local correlation between independent runs drops and detailed interpretation is not feasible. Thus, even though the number of independent parameters in an ensemble model is not clearly defined (and therefore the parameter-to-observation ratio is unclear), the gain in Rfree and the very high local correlations between independent runs indicate a high reliability of the ensemble models. However, the method is not a panacea for highly disordered protein regions. In the absence of ordered conformations for a certain region of the protein (as implicitly defined by the diffraction data) the ensemble refinement will sample diverse conformations in order to prevent the build up of negative peaks in the electron-density difference map. In other words, if the data ‘says’ that a region is disordered, ensemble refinement will generate diverse conformations for that region. Furthermore, dataset pathologies caused, for example, by radiation damage may have confounded effects that obscure the dynamics inherent to the protein molecule. Thus, perhaps somewhat counter-intuitively, this modelling method that accounts for inherent protein dynamics does not help to resolve structural details of disordered regions, but is particularly suited to resolve dynamical fluctuations in ordered parts of the protein structure.

Ensemble refinement of 20 protein datasets highlighted global dynamics features of protein molecules. Surprisingly, in some cases the ensembles indicated the existence of folded protein structures that display molten cores. Most likely, such molten cores may indicate intermediates of protein molecules that function in larger complexes (such as PAK pilin), or alternatively these molten cores support dynamical fluctuations that are needed for ligand binding and enzyme functioning (as for birch pollen allergen and proline isomerase respectively). Furthermore, the ensembles show details of specific order–disorder transitions, or conformational exchanges, between active site and core residues (as for HIV protease in the unbound and bound state) that suggest a mechanism of entropy compensation to support the enzymatic activity. The difference in dynamics observed between the ensembles of proline isomerase at cryo and ambient temperatures indicates that flash freezing of a crystal anneals local conformational fluctuations and thereby removes protein dynamics that may be functionally relevant.

In conclusion, this new method of modelling X-ray diffraction data reveals a wealth of detailed information about the dynamics of biomolecules that complements the high-resolution structural information already available from the crystallographic experiment. In depth understanding of structure–dynamics in biomolecules will enhance our insights into the molecular mechanisms that underlie biological processes.

## Materials and methods

The method of ensemble refinement was implemented in the Phenix software (Adams et al., 2010). Adaptations and new procedures developed for ensemble refinement are given in section ‘Ensemble refinement methods’. Simulations were performed as described in section ‘Ensemble refinement protocol’. Details of the single-structure re-refinements used for comparison with the ensemble models are given in section ‘Single structure re-refinements’. Validation of the global disorder TLS model, the dependency of ensemble refinement on the starting structure and additional ensemble refinement calculations are given in ‘Additional ensemble refinement calculations’.

Ensemble refinement was performed using phenix.ensemble_refinement, as will be made available in the next release of Phenix.

### Ensemble refinement methods

#### Time-averaged restraints

The overall model structure factors are calculated as (1), defined by Afonine et al. (2005), incorporating overall anisotropic scaling (Sheriff and Hendrickson, 1987) and bulk solvent contributions (Jiang and Brünger, 1994).

$$
F_{model}=ke^{(−\frac{h^{T}A^{−1}B_{cart}(A^{−1})^{T}h}{4})}(F_{calc}+k_{sol}e^{(−\frac{B_{sol}s^{2}}{4})}F_{mask}),
$$

where, k is the overall scale factor, h is the column vector with Miller indices, A is the orthogonalisation matrix, Bcart is the anisotropic scale matrix, Fcalc is the structure factors calculated from atomic model, ksol and Bsol are the parameters for the flat bulk solvent model and Fmask are the structure factors calculated from bulk solvent mask.

In order to restrain the instantaneous structures produced during the MD simulation with time and spatially averaged X-ray data, time-averaged restraints are used (Gros et al., 1990). This produces time-averaged (or rolling-average) structure factors such that (1) becomes (2).

$$
F_{model}^{t}=ke^{(−\frac{h^{T}A^{−1}B_{cart}(A^{−1})^{T}h}{4})}(〈F_{calc}〉_{t}+k_{sol}e^{(−\frac{B_{sol}s^{2}}{4})}〈F_{mask}〉_{t}).
$$

This is a time-dependent memory function, that is a ‘rolling’ average, where the size of the averaging window is controlled by the τx parameter (typically 1 ps). This averaging function is updated with the current individual structure every 10 time-steps (∆t) during the simulation and is implemented as in (3).

$$
〈F_{calc}〉_{t}=e^{−Δt/\tau_{x}}〈F_{calc}〉_{t−Δt}+(1−e^{−Δt/\tau_{x}})F_{calc}^{t}.
$$

#### Dual explicit-bulk solvent model

Due to the stochastic behaviour of solvent molecules and the number of partially disordered or low occupancy sites, explicitly modelled solvent atoms are repositioned every 250 time-steps. Electron-density and difference density maps are generated using Fmodelt, excluding reflections in the free R set. Water oxygen atoms with an electron-density peak >1.0 σ in the 2mFobs − DFmodel map or a peak >3.0 σ in the mFobs − DFmodel map are preserved, otherwise the atom is removed. New water atoms are added for positions which have a 2mFobs − DFmodel peak >1.0 σ and a mFobs − DFmodel peak >3.0 σ, and are between 1.8–3.0 Å in distance to an existing atom. For high-resolution cases these criteria are adjusted to include mFobs − DFmodel map peaks >2.5 σ. Newly positioned atoms are assigned a random, Boltzmann-weighted, velocity. Explicitly modelled solvent atoms contribute to the atomic model (Fcalc).

Bulk solvent is modelled using a solvent mask (Afonine et al., 2005). The mask structure factors (Fmask) are averaged in the same manner as the atomic model (Fcalc) (4).

$$
〈F_{mask}〉_{t}=e^{−Δt/\tau_{x}}〈F_{mask}〉_{t−Δt}+(1−e^{−Δt/\tau_{x}})F_{mask}^{t}.
$$

The ksol and Bsol bulk solvent parameters and Bcart scaling parameters used for the duration of the simulation are calculated from the starting structure as described previously (Afonine et al., 2005), they are re-optimized for the final ensemble.

#### Constrained target functions

The overall scale factor, k, is constrained during the simulation. For the maximum-likelihood target function, as shown for acentric reflections, (5) during normalisation (6), the sum of the rolling-average structure factor array (2) is scaled to the sum of the structure factor array from the starting model (Fref) as shown in (7).

$$
P_{x-ray}=\frac{2E_{obs}}{1−\sigma_{A}^{2}}exp(−\frac{E_{obs}^{2}+\sigma_{A}^{2}E_{model}^{t}}{1−\sigma_{A}^{2}})I_{0}(\frac{2E_{obs}\sigma_{A}E_{model}^{t}}{1−\sigma_{A}^{2}}),
$$



$$
E_{model}^{t}=\frac{kF_{model}^{t}}{\sqrt{\epsilon Σ_{N}}},
$$



$$
k=\frac{ΣhklF_{ref}}{ΣhklF_{model}^{t}},
$$

where, Eobs and Emodel are the normalised structure factors, σA is the Sigma-A weighting factor, I0 is a modified Bessel function of order 0 and ε is the expected intensity factor.

#### Temperature bath and X-ray weight

The simulations are performed such that the non-solvent atoms are at a target temperature (Ttarget) of 300 K, where the simulation is coupled to a velocity-scaled temperature-bath (Berendsen et al., 1984). The temperature bath is set to a value less than 300 K, typically 295–298 K. Because the X-ray restraints are computed from a time-dependent memory function, the X-ray energy term is non-conservative and thus heating occurs. During the equilibration phase the X-ray weight (wx-ray) is modulated by the temperature of the protein atoms (Tprotein) every 10 time-steps (∆t), such that the non-solvent atoms sample consistently at the target temperature (8).

$$
w_{x-ray}^{t}=w_{x-ray}^{t−Δt}\frac{T_{target}}{T_{protein}}.
$$

Thus, the thermostat offset controls the X-ray weight in a system independent manner whilst maintaining the target temperature. In the acquisition phase the X-ray weight is fixed to the averaged value used in the equilibration phase.

#### TLS approximation of the global disorder

The partitioning of inter-molecular disorder is performed before the start of the simulation using ADPs from the traditionally refined starting structure. TLS groups are assigned per molecule or domain as appropriate to model global packing disorder. For each group, TLS parameters are fitted to the ADPs of the starting structure for all non-solvent, non-hydrogen atoms. The agreement of the isotropic equivalents for the fitted TLS ADPs (Btls) and the reference ADPs (Bref) is scored as (9) for all non-solvent, non-hydrogen atoms.

$$
R_{i}=|B_{ref}^{i}−B_{tls}^{i}|.
$$

A percentile of atoms with the poorest fitting ADPs (pTLS) are excluded from the next round of TLS parameter fitting and repeated until the fitted TLS parameters converge. The converged TLS parameters are then applied to all atoms within that group for the duration of the simulation. Solvent atoms are assigned to the TLS group of the closest non-water atom, this assignment is updated every 250 time-steps. This TLS model produced lower R-values than using the ADP values from the re-refined single structure or using the one overall isotropic B-factor for all atoms in the model (Table 5).

**Table 5.**
 Comparison of three B-factor models for ensemble refinement. Burling et al. (Burling and Brunger, 1994) had shown previously that the choice of ADPs for ensemble refinement can affect the resultant structures. Three alternative ADP models were tested for seven datasets. (1) ‘Global isotropic B-factor’, one overall isotropic B-factor applied to all atoms in the simulation. Multiple trials were performed to establish the optimum single value. For comparison the Wilson B-factor of the data is listed. (2) ‘Refined ADPs', ADPs from the refined single-structures. Best results were obtained by multiplying the refined ADPs by given scale factor. (3) ‘Fitted TLS ADPs', fitted TLS model obtained as described in ‘Materials and methods’


<table>
  <thead>
    <tr>
      <th rowspan="2">PDB</th>
      <th rowspan="2">Resolution (Å)</th>
      <th colspan="4">Global isotropic B-factor</th>
      <th colspan="3">Refined ADPs</th>
      <th colspan="3">Fitted TLS ADPs</th>
    </tr>
    <tr>
      <th>Rwork</th>
      <th>Rfree</th>
      <th>Wilson B-factor (Å2)</th>
      <th>Global B-factor (Å2)</th>
      <th>Rwork</th>
      <th>Rfree</th>
      <th>Scale factor</th>
      <th>Rwork</th>
      <th>Rfree</th>
      <th>pTLS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3K0M</td>
      <td>1.3</td>
      <td>0.117</td>
      <td>0.147</td>
      <td>12.0</td>
      <td>12.0</td>
      <td>0.125</td>
      <td>0.146</td>
      <td>0.9</td>
      <td>0.103</td>
      <td>0.130</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>3K0N</td>
      <td>1.4</td>
      <td>0.121</td>
      <td>0.153</td>
      <td>19.1</td>
      <td>19.1</td>
      <td>0.126</td>
      <td>0.153</td>
      <td>0.9</td>
      <td>0.114</td>
      <td>0.133</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td>1UOY</td>
      <td>1.5</td>
      <td>0.103</td>
      <td>0.148</td>
      <td>10.4</td>
      <td>9.4</td>
      <td>0.107</td>
      <td>0.144</td>
      <td>0.9</td>
      <td>0.101</td>
      <td>0.136</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>3CA7</td>
      <td>1.5</td>
      <td>0.129</td>
      <td>0.194</td>
      <td>16.8</td>
      <td>13.4</td>
      <td>0.142</td>
      <td>0.192</td>
      <td>0.9</td>
      <td>0.142</td>
      <td>0.190</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>1X6P</td>
      <td>1.6</td>
      <td>0.108</td>
      <td>0.158</td>
      <td>15.9</td>
      <td>12.7</td>
      <td>0.113</td>
      <td>0.152</td>
      <td>0.8</td>
      <td>0.121</td>
      <td>0.150</td>
      <td>0.8</td>
    </tr>
    <tr>
      <td>1F2F</td>
      <td>1.7</td>
      <td>0.116</td>
      <td>0.184</td>
      <td>15.6</td>
      <td>14.8</td>
      <td>0.123</td>
      <td>0.167</td>
      <td>0.8</td>
      <td>0.126</td>
      <td>0.167</td>
      <td>0.7</td>
    </tr>
    <tr>
      <td>1BV1</td>
      <td>2.0</td>
      <td>0.125</td>
      <td>0.192</td>
      <td>22.6</td>
      <td>18.1</td>
      <td>0.135</td>
      <td>0.191</td>
      <td>0.8</td>
      <td>0.145</td>
      <td>0.182</td>
      <td>0.6</td>
    </tr>
    <tr>
      <td>Mean</td>
      <td>-</td>
      <td>0.117</td>
      <td>0.168</td>
      <td>-</td>
      <td>-</td>
      <td>0.125</td>
      <td>0.164</td>
      <td>-</td>
      <td>0.122</td>
      <td>0.155</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

#### Generation of the final ensemble

Structure factors for the final ensemble are calculated from the population of collected structure as in (2) where Fcalc and Fmask are defined as (10) and (11).

$$
〈F_{calc}〉_{final}=\frac{1}{n}\sumi=1nF_{calc}^{i},
$$



$$
〈F_{mask}〉_{final}=\frac{1}{n}\sumi=1nF_{mask}^{i}.
$$

The acquisition phase is split into several time blocks, in each of which 250 structures are typically stored. The R-values of all possible contiguous time blocks are calculated and the periods with the lowest Rwork are selected. This selection reduces the Rwork by 0–1.0% (mean improvement in 0.3%). For the 1YTT dataset with high quality experimental phases, the block selection for lowest Rwork corresponds well with the overall map correlation coefficient computed between the experimentally phased map and the map derived from the ensemble model (Figure 13). Next, to reduce the redundancy in the number of structures in the final ensemble (during the simulation thousands of structures are collected), we calculate the smallest number of structures that reproduce the Rfree within 0.1%. This is performed by iteratively parsing the stored structures with increasing time spacing (see Figure 1D). The overall and bulk-solvent scale factors are optimised for the final ensemble. The ensembles of structures are stored using the standard PDB format for multiple models, with B-factors listed as computed from the TLS model and overall B-factor scaling contributions.

![Figure 13.](https://cdn.elifesciences.org/articles/00311/elife-00311-fig13-v1.jpg)

**Figure 13.:** Correlation of R-values and overall map correlation coefficient for the 1YTT dataset in the block selection procedure. The correlation coefficients are calculated between the experimentally phased electron density map (|Fobs|exp[iφobs]) and ensemble model maps (|Fmodel|exp[iφmodel]) computed for different blocks of consecutive simulation times; blue squares indicate Rwork and red squares indicate Rfree.

#### Calculation of atomic positional probability

All atoms comprising the ensemble are assigned a probability (Pi) based on the positional likelihood of atom i in a given model relative to the complete ensemble of models. Fcalc electron-density maps are calculated for each model in the ensemble and 〈Fcalc〉 electron-density map is calculated for the complete ensemble as (10). Pi is calculated as (12).

$$
P_{i}=\frac{ρ_{〈F_{calc}〉}^{i}}{ρ_{F_{calc}}^{i}}.
$$

Calculating from an electron-density function allows for non-Gaussian distributions unlike RMSF, which is calculated from mean atomic position. These probabilities aid the visual inspection of the ensemble models and allow the observer to control the level of detail displayed (Figure 14).

![Figure 14.](https://cdn.elifesciences.org/articles/00311/elife-00311-fig14-v1.jpg)

**Figure 14.:** Interpretation of global and local details of 1UOY ensemble model is aided by relative atomic probability (as described in ‘Materials and methods’). Ensemble models, left and centre, are colour by individual atom probability (0–1) from red to blue. Single structures, right, are coloured by individual atomic B-factor as refined in phenix.refine. (A) Global structure, selecting different probability ranges highlights partially ordered water positions. (B) Atomic probabilities of loop regain features correlate with B-factors in single structure. Anharmonic motion of Ser5 can be observed as well as anisotropic motion at Tyr7, which is shown in more detail in (C).

### Ensemble refinement protocol

#### Preparing the starting model

The starting structures were taken from the PDB server or from the PDB_REDO server if the Rfree was <0.25% than the equivalent PDB structure. We removed alternative positions and set corresponding occupancies to one. Overall anisotropic scale factors and solvent scale and B-factor (ksol and Bsol) were calculated based on these traditional single-structures (i.e. using the refined B-factor models). Next, the atomic B-factors were substituted by B-factors derived the global TLS disorder model (‘Materials and methods’—TLS approximation of the global disorder).

#### X-ray restrained MD simulation

At t = 0 〈Fcalc〉 and 〈Fsol〉 are set to Fcalc and Fsol. Boltzmann-weighted velocities are assigned to the atoms, corresponding to T = 300 K. The bath temperature Tbath used for velocity scaling is coupled to the X-ray weight (wx-ray) calculation, resulting in a temperature of 300 K for all non-solvent atoms. The simulation time-step used is 0.5 fs and the force-field parameterisation is as described (Grosse-Kunstleve et al., 2004). Simulations are started in parallel with varying values of pTLS (e.g. 0.2, 0.6, 0.8, 0.9, 1.0), τx (e.g. 0.25, 0.5 and 1.0 ps) and Tbath (e.g. 295 and 299 K). Water positions are picked according to electron-density criteria and updated every 250 steps. Every 10 time-steps rolling average structure factors, 〈Fcalc〉 and 〈Fsol〉, are updated for use in the time-averaged X-ray restraints. σA Values are updated if the Rfree of the rolling average model improves by >0.25%. The simulations have an equilibration phase (20τx) in which the temperature, X-ray weight and averaged structure factors stabilize. This is followed by an acquisition phase (40τx) where the values for wx-ray and σA are fixed and the structures for the final ensemble model are collected.

#### CPU time

CPU time for a dataset at 2.0-Å resolution with 199 residues in the asymmetric unit is 25 hr for each simulation using a 1.9 GHz processor.

### Single structure re-refinements

The single structure re-refinements used the same starting structure as the ensemble refinements (alternative conformations were not removed) and were re-refined using phenix.refine (version 1.7.1) (Afonine et al., 2012) and Buster (version 2.10.0) (Bricogne et al., 2009). Standard parameters were used with the exception of optimizing the target weights and increasing the number of macro-cycles to 8 in phenix.refine. Explicit water refinement was performed, anisotropic ADPs were used if present in starting structure and TLS parameters were defined as used in the starting structure. PDB_REDO (Joosten et al., 2010) models were used as deposited.

### Additional ensemble refinement calculations

#### Testing B-factor model in ensemble refinement

Burling et al. (Burling and Brunger, 1994) had previously shown that the choice of ADPs for ensemble refinement can affect the resultant structures. Three alternative ADP models were tested for seven datasets, as shown in Table 5. ADP model 1, ‘Global isotropic B-factor’, uses one overall isotropic B-factor applied to all atoms in the simulation. Multiple trials were performed to establish the optimum single value. For comparison the Wilson B-factor of the data is listed. ADP model 2, ‘Refined ADPs’, uses the ADPs from the refined single-structures. Best results were obtained by multiplying the refined ADPs by given scale factor. ADP model 3, ‘Basal TLS ADPs’, uses the basal TLS model with one TLS group per chain (including all non-hydrogen, non-solvent atoms) obtained as described in ‘Materials and methods’—TLS approximation of the global disorder, where pTLS is the percentage of atoms included the iterative fitting procedure. The basal TLS model returns the lowest Rfree values in all test cases.

#### Effect of starting model on ensemble refinement

To test the effect of the starting structure three datasets (1UOY, 3CA7 and 1BV1) were re-refined with Buster, phenix.refine and Refmac as given by the PDB_REDO server. Each of these re-refined structures was used as the input structure for ensemble refinement, using the same run-time parameters. Each ensemble refinement was repeated three times using a different random number to generate the initial atomic velocities. The results are shown in Table 3. The mean Rfree (averaged over the random number seed repeats) of the resulting ensembles from the three different input structures are within 0.5%. The Fmodel cross correlation of ensemble pairs (best representative from each program, selected by Rfree) was calculated and is shown in Table 4. All ensemble pairs exhibit a cross correlation of greater than 0.99.

#### Partial occupancies

Because occupancy and B-factor are strongly coupled in a traditional refinement, the occupancies of bound ligands and ions are typically set to unity, while the corresponding B-factors are refined in a single-structure refinement. In ensemble refinement, the B-factors are not refined, but are derived from the global TLS model and the atomic fluctuations.

All simulations were initially performed with full occupancy for bound ligands and ions. In several cases, this resulted in excessive sampling of the ligand or ion, as seen when inspecting the ensemble and reported by the kinetic energies during the simulation, which were far in excess of neighbouring protein atoms. These observations indicate that the corresponding occupancy of the bound ligand or ion is less than one. In these cases the occupancies were lowered and the simulations repeated until the kinetic energy of the ligand or ion were equivalent to the proximal protein components.
