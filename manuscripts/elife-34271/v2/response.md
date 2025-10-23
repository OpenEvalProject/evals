# Author response - Round 1

Authors:
- Xiaochu Ma
- Maolin Lu
- Jason Gorman
- Daniel S Terry
- Xinyu Hong
- Zhou Zhou
- Hong Zhao
- Roger B Altman
- James Arthos
- Scott C Blanchard ([ORCID: 0000-0003-2717-9365](https://orcid.org/0000-0003-2717-9365))
- Peter D Kwong
- James B Munro
- Walther Mothes ([ORCID: 0000-0002-3367-7240](https://orcid.org/0000-0002-3367-7240))

## Response text

DOI: [10.7554/eLife.34271.022](https://doi.org/10.7554/eLife.34271.022)

The biophysical studies are an elegant mixture of single-molecule biophysics and challenging biochemistry/virology that deserves publication in eLife after changes that would greatly improve the presentation. However, our recommendation is that the EM structure should either be removed from this paper or extensively revised, which would require additional refinement and analyses of the structure.

We like to note up front that Peter Kwong and Priyamvada Acharya have agreed to remove the EM structure from the manuscript. Peter Kwong and Jason Gorman have supported our project on other aspects, and thus will remain authors. However, all authors involved in the structural work have agreed to be removed from the authors list, including Priyamvada Acharya.

We have the following suggestions for revising the smFRET part of the paper.

1) The authors use a challenging biochemical approach using orthogonal peptide tagging to allow double labeling of the individual protomers, combined with careful titration of unlabeled Env through co-expression. They have presented this approach previously, but it would have been useful for readers to know the extent of labeling efficiency for the virions. Also as described in the first paragraph of the subsection “State 3 corresponds to the gp120 conformation of the three-CD4-bound HIV-1 Env trimer”, the authors validate that insertion of the Q3 and A1 tags for fluorophore labeling did not affect Env functions using various assays, but it is not clear whether they tested labeled viruses in these assays, or viruses with just the peptide insertions. The peptide tag is just one component, and perhaps not the largest one, that distinguishes an unlabeled Env from a labeled Env. If it is not possible to do the validation assays using labeled viruses, then the authors should discuss caveats associated with possible steric occlusion from adding the dyes and whatever other components must be added to attach dyes to the peptide tags.

Each new HIV-1 isolate that is being introduced for smFRET imaging was carefully validated as shown in this manuscript for the BG505. This is done with the 100% tagged Env.

With respect to labeling efficiencies, we have previously determined the labeling efficiencies and found them to be 40% for the Q3 tag and 55% for the A1 tag (Munro et al., 2014). We are still using the same protocols and have not observed a drop in the number of labeled particles in each preparation. Given that labeling efficiencies are not 100%, it’s not valid to test the infectivity of “100% labeled” virus since there are several trimers on the surface of the virus and incomplete labeling leaves enough unlabeled Env to maintain similar infectivity as WT. Thus, the test of Q3 and A1 peptide insertion on virus infectivity was done solely on viruses carrying 100% labeling peptides, but not on fluorophore-labeled viruses. We now mention this in the last paragraph of the Materials and methods subsection “Preparation of labeled virions”. While dyes could affect the outcome, which we acknowledge in the last paragraph of the Materials and methods subsection “Infectivity measurements”, we have not observed anisotropy for singly labeled virions suggesting no trapping of dyes in specific environments. These dyes are highly hydrophilic (Zheng et al., 2014). They also do not interact with the viral membrane. The association of dyes with virions is entirely dependent on the presence of labeling tag (Munro et al., 2014).

For us most important have been the biological controls. The smFRET signal has been responsive to ligands, mutations in a manner that correlates with virological data (Munro et al., 2014; this paper; Herschhorn et al., 2016). Moreover, the Tier 2 viruses JR-FL and BG505 are more closed and less responsive to sCD4 than the Tier 1 lab-adapted HIV-1 isolate NL4-3 (Figures 1B, 1E and 1H).

2) The use of a dodecameric CD4 oligomer (sCD4D1D2-Igαtp) for capturing state 3 in NL4-3 is interesting and promotes different effects than sCD4 in the 3 trimers analyzed by smFRET. It is unclear, however, if the "high local CD4 density" resulting from the architecture of this dodecameric CD4 oligomer would geometrically allow multiple copies of CD4 to engage a single Env? A cartoon showing the structure of the construct used in these experiments demonstrating this is feasible would address this and support the results presented. Figure 1D indicates that sCD4D1D2-Igαtp stabilizes state 3 for HIV-1(NL4-3), which corresponds to the open conformation with 3 CD4 bound, whereas the authors also claim that a single CD4 bound to the mixed trimer 1 leads to the same result (Figure 2D). How can these results be reconciled? And were smFRET studies done using sCD4D1D2-Igαtp on mixed trimer 1 (labeled protomer that can bind CD4 with two protomers that can't bind CD4)? This would allow a direct comparison of sCD4D1D2-Igαtp effects on native HIV-1NL4-3 trimer and mixed HIV-1NL4-3 trimer 1. As shown in Figure 2—figure supplements 3-5, the effects of sCD4D1D2-Igαtp were evaluated for JR-FL and BG505 viruses but not for NL4-3. Minor suggestion: it would be easier to compare if Figure 2—figure supplements 3-5 were combined into one figure.

The dodecameric CD4 oligomer was generated and extensively studied by the group of James Arthos (Bennet et al., 2007; Arthos et al., 2002). The interaction of the sCD4D1D2-Igαtp with native virions has been directly visualized by Sriram Subramaniam using cryo-electron tomography. 12xCD4 was found to cover several gp120 subunits of the same trimer as well as neighboring trimers highlighting the strong avidity (Bennet et al., 2007). The off-rate for sCD4D1D2-Igαtp from viruses is basically zero (Arthos et al., 2002).

In Figure 2D, however, only one protomer in a trimer is capable of binding to CD4. This therefore leads to a single-CD4-bound asymmetric trimer, regardless of whether the ligand is a single D1D2 CD4 molecule or sCD4D1D2-Igαtp. Viruses carrying the D368R mutation are also resistant to sCD4D1D2-Igαtp (Figure 2—figure supplement 3). Thus, upon CD4 binding, this single gp120 adopts the conformation of State 3 that corresponds to the CD4-bound conformation.

The reason why we use either sCD4 or sCD4D1D2-Igαtp is because the Tier 1 lab-adapted HIV-1 isolate is highly responsive and sensitive to sCD4, whereas the Tier 2 viruses JR-FL and BG505 are not. To trigger the CD4 bound conformation, we have to use the more potent ligand 12xCD4 for both Tier 2 isolates. If we use sCD4D1D2-Igαtp on NL4-3, it would be more than 1000x above the inhibitory concentration. We are trying to image all ligands at ~10x above the IC90. It wouldn’t be wise to test one ligand at ~10x above an IC90 and another at 1000x above the IC90.

Upon request, we have combined Figure 2—figure supplements 3-5 into one single Figure 2—figure supplement 3 for better comparison. And have added the figure of 100% D368R NL4-3 in Figure 2—figure supplement 3A.

3) The schematics used in Figure 1, 2 and 3 are confusing. It is hard to see the donor and acceptor, and it's not clear why they should have different FRET values in the different conformational states. It's also hard to see the difference between closed and open on such a small figure. Maybe using axial lines for the 3 protomers, and making the dyes bigger (and their positions different in the states) would help. These are the key figures for understanding all the single-molecule data, so the authors should spend more time on presentation. In particular, in Figure 1K, the donor and acceptor dyes are shown as being the same distance apart whether they are on the closed or the open trimer. This is confusing, since the dyes would be separated by long distances in the low FRET State 1 but by shorter distances in the intermediate and high FRET states 3 and 2. There is little discussion in this paper as to whether it makes structural sense for the dyes to become closer together upon CD4 binding, which is especially important if the authors want to include the cryo-EM structure of Env in the same paper. In particular, this sentence, "Binding of a single CD4 may loosen interaction of the V1/V2 loops in the trimer association domain so that neighboring protomers can adopt a conformation in which the V1 and V4 loops are closer to each other." Is this consistent with what is known about the relative locations of V1 and V4 in closed and open Env structures?

We have modified the figures to schematically illustrate the changes in the dye distance. We can, however, not relate the FRET data to current structural models as it is not trivial and requires the determination of the FRET values observed in Env protein complexes characterized structurally, which requires a separate study. For this reason, we have also removed the EM structure from this manuscript.

4) Figure 3I. Why is 17b shown as binding to the protomers in a mixed trimer that can't bind CD4? 17b won't bind to most Envs in the absence of CD4. It seems reasonable that 17b could bind to the protomer(s) that can bind CD4 in a mixed trimer, but what evidence is there that 17b can also bind to the CD4-incompetent protomers in a mixed trimer?

Because the single protomer that engages CD4 in these asymmetric trimers is already in State 3 and there is no difference between the CD4-bound and the CD4/17b bound gp120 conformation, neither in our smFRET assay nor structurally in gp120 or in the SOSIP trimer in Ozorowski et al., 2017). Thus, 17b likely binds in trans to the neighboring protomers. Mechanistically 17b likely binds by capturing a preexisting State 3 conformation that is more frequently sampled in State 2 as compared to the more closed State 1. However, this is rather speculative. It could in principal be tested experimentally in mixed trimers by combining the D368R mutation with mutations that prevent 17b binding, but introducing several mutations into Env can lead to non-linear effects and phenotypes are increasingly difficult to interpret. We have therefore decided to stay away from this speculation.

Additional evidence can be found in previous publications such as (Herschhorn et al., 2016) demonstrating that Env mutants residing in State 2 more readily engage coreceptors, leading toward downstream conformations.

We have previously shown in the 2014 Munro paper that the frequently opening Tier 1 lab-adapted NL4-3 can open in response to 17b alone, while the more closed Tier 2 JR-FL needs CD4.

5) The authors should present prior measurements on CD4 affinity/kinetics wherever possible.

We are working with native virions and measure infectivity, not affinities for recombinant proteins. We present the neutralization curves for CD4 and sCD4D1D2-Igαtp for all three HIV-1 isolates (Figures 2A, 2F and 2I; Figure 1—figure supplement 3). We now include a table with the calculated IC50 (Table 2), but we cannot include affinities.

6) Figure 1 legend. Why are the authors using standard errors here instead of standard deviations as they used for other error analyses?

Standard error= standard deviation/ (square root of sample size). We chose standard error for the estimation of data quality of histograms because it is more important for such a big number of data points that both reflect the mean and the accuracy of mean, which standard error takes into account. While for neutralization curves, there are only about 10 data points for each sample mean, therefore it is more important to present how each individual data point is different from the mean, which is reflected by standard deviation.

7) For FRET traces, it would be nice to show with lines the high, medium, and low states in each trace.

We have added lines indicating Low-, Intermediate- and High-FRET states in the FRET trace with Hidden Markov Modeling idealization (Figure 1A).

8) Materials and methods subsection “Preparation of labeled virions”. The protocol for use of the enzyme AcpS for labeling of one of the peptide tags should be cited.

We have added lines indicating Low-, Intermediate- and High-FRET states in the FRET trace with Hidden Markov Modeling idealization (Figure 1A).

9)Discussion, fifth paragraph. The authors say they have compared smFRET values for labeled BG505 virus and labeled BG505 SOSIP in a paper cited as Lu, Ma et al., 2017, under review. As the current submitted paper includes smFRET data for BG505 virus and an EM structure of a BG505 SOSIP, the paper under review is directly relevant to evaluating the submitted paper and should be given to the reviewers.

We have removed any reference to the Lu manuscript since the EM structure has been removed from this manuscript.

Cryo-EM structure

The structure itself (both results and methods) is problematic, and there is little effort to correlate the EM and smFRET results. We can't figure out why the authors think that the EM structure validates the smFRET results because the EM methods are inadequately described and/or possibly done incorrectly, the figures are poor quality, and the description of the structure is vague. We think this paper would stand alone as an important contribution without the EM structure, but if the authors want to include the EM, the following issues must be addressed before publication in any journal.

We have removed the EM structure from the manuscript.
