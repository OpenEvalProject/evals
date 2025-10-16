# Peer review - Round 1

Editors:
- Oliver Hobert, Howard Hughes Medical Institute, Columbia University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.20752.037](https://doi.org/10.7554/eLife.20752.037)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Decreased SMN causes deleterious increases in neuronal M2 muscarinic receptors due to microRNA misregulation" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The authors harness the power of C.elegans genetics to interrogate the defects incurred by loss of SMN on neuromuscular function. Using a series of approaches, the authors implicate the worm ortholog of Gemin3 (mel-46), the miR-2 and the M2 muscarinic receptor. The study demonstrates the power of a genetically tractable system to understand fundamental biology. Based on their data and previously published work, the authors propose the following:

1) SMN-1 acts genetically through MEL-46/Gemin3. Molecularly, SMN-1 is necessary to achieve normal levels of MEL-46/Gemin3.

2) Normal levels of Gemin3 are necessary for correct miRNA processing/function, including mir-2.

3) mir-2 is necessary to repress gar-2. GAR-2 is an M2 receptor that is predicted to inhibit synaptic release at cholinergic NMJs and thus needs to be kept at relatively low levels for optimal NMJ function

These conclusions are based on a number of relatively indirect measures, which are for the most part not sufficient to support all claims. In essence, a number of qPCR experiments are required to support a number of conclusions. Specifically:

1) The authors propose that reduction of SMN-1 results in lower levels of MEL-46. This is based on one genetic interaction: the fact that mel-46 overexpression rescues part of the defects observed in smn-1(lf) animals, most prominently, it suppresses the aldicarb resistance of smn-1(lf) animals. However, it does not rescue the pharyngeal defect of smn-1(lf), suggesting some kind of tissue specificity. Since the connection to miRNA processing/function is given by MEL-46/Gemin3, I think it's important to provide a more direct link and the authors need to measure mel-46 (RNA using qPCR and/or protein) in smn-1(lf).

This is important given that an alternative explanation is not satisfactorily rejected. Specifically, the authors discard an effect of MEL-46 in stabilizing the maternal contribution of SMN-1 by quantifying GFP fluorescence from a very nice SMN-1::GFP allele generated with Cas9, over whole worms, in wt animals with or without MEL-46 overexpression. However, given that in all phenotypic assays the effect of MEL-46 is only seen in the smn-1(lf) background but not in the wt background, it is not clear if one would expect to see any changes in SMN-1 abundance in wt animals. A more direct test would have been to look at the remaining GFP in the smn-1(lf) progeny from heterozygous mothers and see whether this changes with overexpression of MEL-46. Also, given the tissue specificity observed phenotypically, it may be more revealing to focus e.g. on motorneurons. Although if levels are too low to see GFP, a western blot against GFP may already provide some information.

2) The connection of SMN to miRNAs through Gemin3 is solely based on previous publications reporting the dysregulation of certain miRNAs when SMN or Gemin3 are decreased. There is no direct connection in this work between this pathway and mir-2, the miRNA the authors find to be important for NMJ function. Based on the data provided, mir-2 could be acting in the NMJs in a parallel pathway that has no connection to SMN-1 or MEL-46. To strengthen this link, the authors need to measure mir-2 levels in smn-1(lf), mel-46 mutants or overexpression strains. However, one has to wonder whether there is a connection at all: The authors claim to provide a link (although very indirect) with an epistasis analysis shown in Figure 4 where they look at a fluorescent reporter for gar-2, the predicted target of mir-2. The authors compare a reporter with the wt 3'UTR and one without the mir-2 binding site in wt animals or smn-1(lf). In wt animals, the fluorescence ratio between the two reporters is ~1 and in smn-1(lf) animals it goes up by 5% (to 1.05). The authors suggest this is consistent with mir-2 levels being lower in smn-1(lf) (because of lower mel-46/Gemin3, which is not shown) and that leads to gar-2 derepression. In addition to this being an extremely small effect that would need additional data to be convincing (e.g. qPCR of gar-2 mRNA in N2 v miR-2 mutant animals), there is a problem which is that the increase in ratio is not as one would expect from the reporter with the wt 3'UTR being derepressed (numerator going up) in smn-1(lf) but rather the reporter with the mutant 3'UTR is decreased in smn-1(lf) (denominator going down) (Figure 4—figure supplement 2, panels C and D). There is no other connection provided between the effect that smn-1 and mel-46 may have on the NMJ and whatever function mir-2 might have there as well.

3) The phenotypic and reporter analyses are consistent with gar-2 being a target of mir-2. Given the small magnitude of repression observed, this point could be made more convincingly, for example by mutating the mir-2 binding site in the 3'UTR of gar-2, which should not be too difficult given that the authors are able to generate alleles using Cas9.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Decreased microRNA levels lead to deleterious increases in neuronal M2 muscarinic receptors in Spinal Muscular Atrophy models" for further consideration at eLife. Your revised article has been favorably evaluated by a Senior Editor, a Reviewing Editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The authors have done a highly appreciated effort to incorporate the reviewers’ comments and suggestions and I think this has paid off in strengthening their model. However, one concern remains about a critical link in the story: The changes in mir2 measurements (Figure 5), an important and good addition, needs to be done with better controls. Currently, the authors report mir-2 levels relative to mir-60 levels. This is another miRNA that might also be affected by the manipulations done in this experiment. It is not clear at all from looking at the raw data provided whether in these experiments mir-2 is decreasing or mir-60 is increasing, in fact the latter seems more supported by the data. There is also a problem of reproducibility in this experiment, with variances of >10 Ct between replicates. It is strongly suggested that given the importance of this experiment, it should be repeated with additional normalization controls, which should include at least one non-miRNA RNA (U6, U18, 5S RNA). One suggestion for improving reproducibility is to use a remarkably well-working protocol published by Kien Ly, Suzanne J. Reid, Russell G. Snell as "Rapid RNA analysis of individual Caenorhabditis elegans" in MethodsX 2 (2015) 59-63.
