# Peer review - Round 1

Editors:
- Axel T Brunger, Howard Hughes Medical Institute, Stanford University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.16105.056](https://doi.org/10.7554/eLife.16105.056)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Ensemble-based model refinement and validation with Resolution Exchange MDFF for sub-5 Å cryo-electron microscopy maps" for consideration by eLife. Your article has been favorably evaluated by John Kuriyan (Senior editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The novelty of this paper lies in the combination of a variety of tools and concepts, none of which individually are new. Moreover, the authors published work on MDFF fitting of EM maps. However, this new combination (MD-based fitting of EM maps, combined with replica exchange and gradual resolution increase) works very well in the test cases that are presented in this work. The radius of convergence is impressive.

The main application of this combined method is for cases where the initial model is very far from the EM map. However, in practice the applications of their method may be somewhat limited since either (a) the EM map is near atomic resolution (3.5 A or better) allowing ab initio tracing, or (b) the map is lower resolution in which case higher resolution structures of fragments are generally needed in order to have confidence in the final model. The new method is probably most useful in the resolution range 4-7 A where ab initio fitting to the maps is not possible and when high-resolution structures are available of all components, but these components undergo large conformational changes.

Along similar lines, the advantages of cMDFF/ReMDFF over 'direct' MDFF are clearly demonstrated for high-resolution, although it would be helpful to know if there are also advantages of using cMDFF/ReMDFF over direct MDFF at moderate resolutions (lower than 4 A resolution).

Essential revisions:

1) A common practice in the EM field is to perform refinements against half maps to judge the degree over-fitting. Assuming that the authors have access to the EM data for one of the test cases, such over-fitting test should be performed – as shown in DiMaio, et al. (2013) Protein Sci, 22, 865-868 or Amunts, et al. (2014) Science 343, 1485-1489.

2) It was unclear how well the protocols work at the second step – ensuring an accurate model that sufficiently describes the density at the side chain level. In the absence of figures demonstrating the fit of side chains to density (an omission that should be corrected), one of the reviewers compared the provided model coordinates (source data to Table 1) with the deposited structure of β-galactosidase (PDB accession code 3J7H). This revealed substantial problems with the model. There are a large number of Ramachandran outliers (~10%); more than 1% of non-prolines are in cis-configurations (less than 0.05% are expected); the backbone of the region around the galactoside binding site is incorrect, and many of the side chains are not in their correct density. The authors themselves note 'even if the backbone is correctly placed, the MD force fields […] are incapable of providing sidechain geometries consistent with the map'. This may represent a considerable limitation to using cMDFF/ReMDFF to refine atomic models against sub 5 Å EM maps. It would be helpful if the authors could demonstrate that cMDFF/ReMDFF is capable of refining good starting models without disrupting backbone and side chain geometries. This would more accurately reflect the starting model for many of the potential users of cMDFF/ReMDFF. For example, the deposited model for β-galactosidase should be refined with cMDFF and ReMDFF and not just direct MDFF. The manuscript should provide guidance on how to preserve side chain geometries and the prevent cis-peptide bond formation during refinement. This would improve the utility of cMDFF/ReMDFF as a method of fitting a well-refined structure to classes of different conformational states that can range from high to mid resolution – a good test case might be CorA (Matthies et al. 2016. Cell, 164(4):747-756). Further statistics should be provided to demonstrate the quality of the model after cMDFF/ReMDFF. For example, root-mean-square deviations for bond lengths and bond angles and Ramachandran statistics, which are typically minimal requirements when reporting the quality of structural models. These should be added to Table 1.

3) The authors propose per-residue root mean square fluctuation (RMSF) values as a way of specifying the precision of atom positions. These are shown to correlate with local map quality, suggesting they can be used for model-to-map validation. In many ways RMSF values appear to be analogous to atomic B factors. It would be helpful to see a side-by-side comparison of a protein structure colored by local resolution, atomic B factors and RMSF (an expansion of Figure 3). One would expect them to correlate in a way that EMRinger and local correlation coefficient do not (Figure 4—figure supplement 2). What are the advantages of RMSF over B factors, which are a more established measure? Do the authors actually recommend depositing ensembles?

4) It is unclear what advantages are to be gained by utilizing RMSF values to determine the B factor for sharpening the map (which involves multiple simulations) compared to Guinier analysis performed during the standard post-processing procedure when both provide the same, or similar, values (Figure 5—figure supplement 2). Could RMSF values be calculated for different parts of the model to generate locally sharpened maps that subsequently improve refinement (although one suspects that applying a mask during post-processing would result in a similar effect)?

5) There is no relation of the presented method with "phase extension" approaches in crystallography where phase experimental phase information is generally much less accurate than amplitude information, and phase extension method make use of the inherently higher accuracy of the amplitude information along with approaches such as solvent flattening of map averaging. The cMDFF and ReMDFF approaches do not actually improve the EM map, they just use filtered less rugged density maps for better convergence of the global conformational changes. Please avoid this analogy.

6) The title is a bit misleading, reading "Ensemble-based refinement…". One might expect an ensemble refinement method, which this is not. Similar with the expression "ensemble-based flexible fitting" (end of Discussion): the flexible fitting itself is not "ensemble-based". Ensemble-based here simply refers to the calculation of RMSF value from the trajectory.

7) Figure 5: The plot describes map sharpening. Sharpening implies applying a negative B-factor, therefore one expects negative B-factor values on the x-axis.

8) This sentence – "well within the structural uncertainty represented by the 3 Å resolution limit of the crystallographic data" –, in the Results, is a bit misleading, since it sounds as if the structural uncertainty for 3 Angstroms data is 3 Å, which is not the case but unfortunately a common misconception. The accuracy of atomic positions is usually considerably higher than the limiting resolution of a crystal. Please remove or reword this sentence.

9) The authors should discuss in more detail the limitations and potential applications of their method as suggested in the summary above.

10) Overall, the manuscript should be edited to remove repetition (cloud computing is described as being cost-effective four times in the paper) and inaccuracies. The Materials and methods section is almost indistinguishable in style from the Results section and could be shortened considerably, with some of the more insightful descriptions moved to the Results (for example the first paragraph of the subsection “Fluctuation Analysis”). Additionally, many of the reference choices seem unnecessary. For example, in the first paragraph of the Introduction, describing how cryo-EM has evolved, the authors cite papers on NMR methods for complexes over 20 kDa (Clore and Gronenborn), membrane proteins by XFEL (Neutze et al.) and ribosome structures at mid-resolution (the papers by Rawat et al.). It would be better to cite one of the recent reviews on cryo EM, for example 'Cheng, Y. 2015. Single-particle cryo-EM at Crystallographic resolution. Cell, 161(3):450-7.

11) All starting and refined models should be provided as supplementary data files.
