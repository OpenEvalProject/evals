# Peer review - Round 1

Editors:
- Silke Hauf, Virginia Tech United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64592.sa1](https://doi.org/10.7554/eLife.64592.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Through technically impressive single-cell experiments and an array of genetic tools, this paper elegantly dissects the pathways that influence CDK1 activity and therefore cell cycle progression. A key question in this field is how cell size influences CDK1 activity, which allows cells to maintain their size. This work shows that CDK1 activity remains influenced by cell size when known pathways are eliminated and makes the novel observation that ploidy influences CDK1 activity.

Decision letter after peer review:

Thank you for submitting your article "Synergistic CDK control pathways maintain cell size homeostasis" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

In this paper, Patterson et al. use genetic techniques in fission yeast to understand how cell size impacts CDK activity and entry into mitosis. By disrupting several regulators of CDK activation and using single-cell readouts of cell size, CDK level, and CDK activity, they show that several layers of control synergistically contribute to making CDK activation dependent on cell size. Their data suggest that DNA concentration affects CDK activity and prevents entry into mitosis in cells that have not reached a certain size threshold.

The experiments' technical level is impressive. The authors have developed a novel sensor, synCut3-mCherry, as single-cell read-out for CDK1 activity, and, for the first time, experimentally demonstrate bistability of CDK regulation in fission yeast. The results will be of interest to researchers studying the cell cycle and cell size control.

The paper could be strengthened by directly examining size homeostasis (as is claimed in the title). In addition, the reviewers had some concerns that cell cycle state is not taken into account as one more variable that could influence the experimental results, and felt that the authors need to provide additional information both on their methods and on their interpretation of the results to make this paper understandable to a wider group of researchers.

Essential revisions:

(1) The authors do not mention that the cell cycle driven by phosphorylatable and non-phosphorylatable (AF) versions of cyclin-CDK fusion proteins could be very different. The data in Figure 1c/k strongly suggests that this is the case. This is also supported by prior findings (Figure 5 in Coudreuse and Nurse, 2010) despite some differences in the genetic background (CCP deletion). Overall, the data suggest that G1 phase is extended in the AF-carrying strain. For the experiments in Figure 2h, what is the cell cycle distribution (G1/S/G2) in the different size bins for the different strains, and does cell cycle state/DNA content (S vs. G2) influence the results?

At the very least, the differences in cell cycle structure between the strains need to be discussed. In addition, please specify which of the PP2A genes has been deleted, and how this influenced the cell cycle profile.

(2) Figure 4 shows that small diploid cells display a lower CDK activity than haploids of the same size. This suggests that a titration mechanism prevents the increase in CDK activity when DNA concentration is too high. These data would be strengthened by a direct readout of DNA content (e.g. DAPI) to measure the amount/concentration of DNA in single cells and its relation to CDK activity. Since DNA staining will also reveal cell cycle state (S phase vs. G2 phase), this would also allow it to exclude cell cycle effects by binning for G2 cells.

(3) PP2A has a dual effect on CDK activity, which is insufficiently discussed. PP2A regulates inhibitory phosphorylation of CDK through the feedback enzymes (Wee1 and Cdc25) as was shown by Chica et al., 2016 (which should be cited) and PP2A controls the phosphorylation state of CDK substrates. These two effects should be distinguished, because one of them influences the intrinsic CDK activity, while the second has an effect on net CDK phosphorylation of substrates. The authors need to check their text for statements that are not clear enough in that regard, e.g. in line 151 "PP2A and inhibitory tyrosine phosphorylation constitute two fundamentally different modes of lowering CDK activity" is not entirely correct.

(4) The major claim in the title is about cell size homeostasis, but size homeostasis is not examined directly. What is the cell size distribution at division in a C-CDK-AF PP2A-Δ strain and do these cells show size homeostasis (as judged by a "Fantes plot")? In the absence of any such data, the title would need to be revised.

(5) Showing the bistable behavior of CDK activity in Figure 2h is a beautiful experimental result. The authors show that the fusion-protein threshold to activate CDK is cell size dependent. But the authors do not explain why the CDK activity above the threshold is constant rather than increasing with the fusion-protein level on the x-axis. What is the limiting factor for CDK activity above the threshold? Does the sensor become saturated at high activity levels?

Furthermore, these important results would deserve a better presentation: calculating the mean CDK activity for a bimodal distribution seems meaningless and confusing. The main point here is at which threshold of fusion-protein levels the CDK activities bifurcate.

(6) In Figure 1j-o, the Pearson correlation coefficient should be provided to support the conclusions of the authors. On line 101, the authors mention that "C-CDK-AF cells… show size-dependent CDK activity scaling". Yet, in Figure 1m it does look like this dependency is significantly impaired. It is actually unclear why that is, knowing size scales with C-CDK level, and C-CDK levels correlate with CDK activity. Please discuss this.

(7) Either title or abstract should mention the experimental system being used.

(8) The paper is very dense and will be hard to understand for people not very familiar with this field. Please expand the introduction and discussion to make the text more accessible. It would be interesting if the authors could elaborate on the implications of their results regarding the mechanism(s) of size control, how their findings relate to (extensive) existing literature, and potentially other model systems in which these questions have been investigated. The introduction would benefit from citing one of the many excellent, recent reviews on the topic.

(9) More details need to be provided in the Methods section in order to allow other researchers to evaluate, and possibly reproduce, these experiments. For example:

– The authors should specify which of the two pp2a genes has been deleted and what effect it had on the cell cycle.

– The authors should explain how they measured the level (concentration) of the fusion protein which accumulates in the nucleus. It makes a huge difference whether the fluorescence is proportional to the concentration or the number of molecules of the fusion-protein.

– When referring to 'custom Matlab scripts', the authors should at least describe the steps that the scripts are executing.

– Please specify what 'our segmentation algorithm' is.

– Presumably FOV stands for 'field of view' – please spell out.

– Is there text missing between line 247 and 248? It is unclear what points 1 and 2 refer to.

– Which cdc2-as allele was used?

– Please provide the full genotype for "TetR1".

– Are the results based on a single strain for each genotype, or have several strains with identical genotype been analyzed? If so, how similar/different were the results?

– The diploid strains do not seem listed in the strain table. How were they generated?

– Figure 1l/n/m/o: When after release are the measurements taken? Please add information to the legend.
