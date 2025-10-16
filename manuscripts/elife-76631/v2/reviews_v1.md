# Peer review - Round 1

Editors:
- Marcel P Goldschen-Ohm, https://ror.org/00hj54h04 University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76631.sa0](https://doi.org/10.7554/eLife.76631.sa0)

The authors present a method for measuring the average oligomerization state of fluorescently tagged membrane proteins by single-molecule localization microscopy (SMLM). In contrast to many other SMLM methods which aim to count subunits in membrane protein complexes, the authors aim to deduce the average oligomerization state from the probabilistic co-detection of at least 1 'reporter' fluorophore, which has relatively poor detection efficiency, with the detection of at least 1 fused 'marker' fluorophore. They calibrate the method against a set of proteins with known oligomerization states (validated against high-resolution clear native gel electrophoresis) and then apply it to convincingly clarify the oligomerization state of SLC26 and SLC17 family member membrane proteins. Although the approach is limited to measurements of the average oligomerization state, and as such is not suitable to measure a distribution of (higher) oligomerization states, it is nonetheless potentially very useful for identifying oligomerization states of unknown proteins in native cells, and furthermore works well with fluorophores that have poor detection efficiencies. The provided software should be sufficient to allow other researchers with some experience in Python to perform this analysis on their own data.


---

# Peer review - Round 1

Editors:
- Marcel P Goldschen-Ohm, https://ror.org/00hj54h04 University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76631.sa1](https://doi.org/10.7554/eLife.76631.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Determination of protein stoichiometries via dual-color colocalization with single molecule localization microscopy" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Marcel P Goldschen-Ohm as Reviewing Editor and Reviewer #1, and the evaluation has been overseen Richard Aldrich as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Please address all of the comments from both reviewers. In particular, pay close attention to the following points:

1) On the theory side, a rigorous probabilistic framework for the assignment of the most likely oligomerisation state is missing. This includes a sensitivity analysis of Equation 1 (or, better, of Equation 6) which highlights at which n or p this method is most sensitive. Also, no confidence intervals for fitted values of m and p were provided which could be used in such a sensitivity analysis. For example, it is clear that a high detection efficiency p renders the method insensitive. The optimal range p = 0.2-0.4 mentioned in the discussion is not substantiated. Also, the uncertainty of the experimentally determined values p and m could be accounted for by error propagation.

2) The SMLM detection/processing details are not state-of-the-art (PSF fit with fixed SD 2D Gaussian; not using maximum likelihood estimation for fitting; DBSCAN algorithm to group raw (single-frame) data). In conjunction with setting a minimum value of 6 (PAmCherry) and 10 (mVenus) for the number of localisations per cluster, these together might contribute to the poor detection efficiency for PAmCherry of 0.12, which is in contrast to the reported maturation efficiency of the protein, and which the authors attribute to protein misfolding. The detection, localisation and grouping of fluorescent events could be substantially improved by using maximum likelihood fitting of experimental point spread functions and post-filtering according to the log-likelihood ratio (LLR), as e.g. offered by the open source software SMAP (Ries, 2020, Nature Methods). This is expected to improve the detection of short fluorophore blinks while improving the rejection of background events. This may also impact the large variation observed from cell to cell, the limitations/requirements of which should be discussed.

3) The manuscript would also benefit from more discussion regarding the origin of the factor 'm'. Do HEK293T cells natively express any untagged protein corresponding to the transfected POIs? If not, it would be important to state this explicitly in the text. If yes, this violates the assumption of the analysis; in fact, it would be expected to contribute to the 'm' factor in equation 6 and lead to a significant variation of this factor from cell to cell, depending on the relative expression levels of tagged and untagged protein. Thus, a knock-out cell line needs first to be created before introducing the tagged POI. Also, it is unlikely that the author's attribution of the very low detection efficiency to a 'misfolded' fraction of proteins is the only possible explanation. For example, the coexistence of different oligomerisation states is expected to have a similar effect than terminated translation. This could be systematically explored by computer simulations to better justify the introduction of this factor and the limitations this implies for the calibration of the method. Finally, is Equation 6 even necessary to determine the oligomerization state?

4) The word stoichiometry in the title of the paper is misleading. Although the technique could be applied to measure the oligomerisation state of different subunits in independent samples using different expression constructs, and thus an average stoichiometry could be determined, it is not suitable to directly measure stoichiometries of different subunits in the same sample.

5) An open-source software tool would find wider-spread application and complement existing methods to measure the oligomerisation state of membrane proteins from monomers to tetramers using relatively standard PALM approaches.

6) Some of the semantics need to be better defined for a more general readership.

7) Regarding the fits to the data in Figure 4A, I assume that all of the (e.g., red) points were globally fit to the data for all 5 proteins with known stoichiometries using a single value of p. However, this is not stated in the text, which made it initially difficult for me to understand what the authors were doing here. Please describe the fitting in more detail in the text.

Reviewer #1 (Recommendations for the authors):

1. I am under the impression that the approach requires identification of distinct proteins, hence the need for SMLM. The authors state that they achieve a 30nm radial resolution, so I assume that an inherent assumption here is that multiple proteins within 30nm of each other must be assumed to be rare? Even assuming this is ok, a 100nm cutoff is used for determining colocalization of spots in the two color channels. Why so much larger than 30nm? How do the authors ensure that only one protein is within each of these 100nm spots? Or can multiple PAmCherry spots be colocalized with the same mVenus spot, or vice-versa? This seems confusing to me. Or if this does not matter, please explain as the theory (e.g., Equation 3) requires counts of numbers of proteins. In the discussion, the authors suggest that their approach is actually not reliant on SMLM at all, and only requires "enough spatial resolution". Please define what "enough" means. And again, if resolving individual proteins is actually not required here, then this needs to be clarified.

2. Some of the semantics need to be better defined for a more general readership. What is a "localization"? Observation of a single fluorophore on a single frame, or the identified location of a single fluorophore across frames? Does a cluster of localizations represent a single protein, or a cluster of proteins? If it is the former, then requiring at least 3 localizations for a cluster to be analyzed (e.g., see Figure 5B) may limit background noise, but would also remove proteins where PAmCherry bleached within a couple of frames. What is the distribution of bleach times for PAmCherry, and what fraction are discarded by this cutoff? The authors suggest that this cutoff removes PAmCherry localizations that are likely to be background noise which do not colocalize with mVenus clusters. But if they do not colocalize, then how do they affect the computation at all, as I thought only colocalized clusters were considered? Overall, the methods should be described in more detail for a general readership.

3. I have some reservations regarding the use of Equation 6, which to some extent appears to be a fudge factor given that the data does not quite fit the initial simple theory (Equation 1). First, it is my understanding that p encompasses all of the things that can lead to a fluorophore not being observed. So why then are some ways in which this could occur such as misfolding or truncation treated separately? Second, Equation 6 needs to be better explained as to why it is appropriate to describe misfolding or truncation events. Third, I would like to see Figure 4C-N repeated without using the fudge factor m. Is Equation 6 really needed to reliably determine the stoichiometries of the tested exchangers/transporters? And lastly, why should we expect m to be the same for different proteins? It seems to me that misfolding or truncation may be highly protein dependent. If m does differ from protein to protein, then it seems like this entire approach is no longer robust, at least for monomers.

4. Equation 4 is introduced as a means to limit the contribution of background noise, but thereafter it appears that the authors just apply Equation 3 to their data. If so, what is the point of Equation 4, or is this a mistake in the text? Also, the variable N_CO in Equation 4 seems to be the same thing as N_MF in Equation 3? If so, please stick to one or the other, and if not please clarify.

5. Regarding the fits to the data in Figure 4A, I assume that all of the (e.g., red) points were globally fit to the data for all 5 proteins with known stoichiometries using a single value of p. However, this is not stated in the text, which made it initially difficult for me to understand what the authors were doing here. Please describe the fitting in more detail in the text.

6. The blue points in Figure 4A are hard to distinguish from the black points. Please choose a better representation. Also, for Figure 4A,B please show all of the data points rather than just box plots plus outliers. There are not so many data points to make this unreasonable in this case.

Reviewer #2 (Recommendations for the authors):

The detection, localisation and grouping of fluorescent events could be substantially improved by using maximum likelihood fitting of experimental point spread functions and post-filtering according to the log-likelihood ratio (LLR), as e.g. offered by the open source software SMAP (Ries, 2020, Nature Methods). This is expected to improve the detection of short fluorophore blinks while improving the rejection of background events.

The full potential, but also the limitations of the approach do not become clear because Equation 1 (or Equation 6) are not rigorously analysed with respect to their sensitivity/ability to differentiate different oligomerisation states. For example, it is clear that a high detection efficiency p renders the method insensitive. The optimal range p = 0.2-0.4 mentioned in the discussion is not substantiated. Also, the uncertainty of the experimentally determined values p and m could be accounted for by error propagation.

The manuscript would also benefit from more discussion regarding

– The origin of the factor 'm'. Do HEK293T cells natively express any untagged protein corresponding to the transfected POIs? If not, it would be important to state this explicitly in the text. If yes, this violates the assumption of the analysis; in fact, it would be expected to contribute to the 'm' factor in equation 6 and lead to a significant variation of this factor from cell to cell, depending on the relative expression levels of tagged and untagged protein. Thus, a knock-out cell line needs first to be created before introducing the tagged POI.

– The large variation observed from cell to cell. Figure 4, A and B, as well as Figure 4 —figure supplement 4 show substantial variation of the colocalization ratio P measured from cell to cell, as large as ranging from 0.15 to 0.45 (EAAT2) or 0.1 to 0.4 (CIC-2). The methods do not state how large the imaged/analysed FOV in a single cell was. According to Figure 1B, it was at least 5x5 µm2. With 1-2 clusters per µm2, this corresponds to 25-50 clusters. Together with the low detection efficiency p=0.12 for PAmCherry, this is expected to result in a substantial variability of P from measurement to measurement. This underlines how an improved detection efficiency, as could be achieved when using state-of-the-art SMLM, might translate in more accurate measurements.
