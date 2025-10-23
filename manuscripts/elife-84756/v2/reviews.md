# Peer review - Round 1

Editors:
- Christian R Landry, https://ror.org/04sjchr03 Université Laval Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84756.sa0](https://doi.org/10.7554/eLife.84756.sa0)

Predicting the evolutionary path towards resistance through successive mutations is an important problem. This valuable study reports on the evolution of resistance to antifolates using computational predictions of changes in drug binding affinity. The findings generally rely on solid analyses although some of the claims are only partially supported because the computational predictions on the effects of mutations are only partially validated by prior experimental data. This study will be of interest to microbiologists interested in the evolution of drug resistance.


---

# Peer review - Round 1

Editors:
- Christian R Landry, https://ror.org/04sjchr03 Université Laval Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84756.sa1](https://doi.org/10.7554/eLife.84756.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A computational method for predicting the most likely evolutionary trajectories in the stepwise accumulation of resistance mutations" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Landry as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Adrian Serohijos (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Reviewer 1: It would be important to demonstrate how robust the results are given that the number of mutations and pathways being considered are limited. Reviewer 3 also mentions the lack of quantification of the performance of the method.

Reviewers 1 and 2 bring several points regarding the statistical analyses (p-values missing, model not converging, distribution of ddG values considered), the calculation relating fitness to the fraction of protein unbound by the drug, and the performance of Rosetta to estimate ddG. These elements would need to be corrected and the performance of Rosetta quantified and demonstrated.

Reviewer 2 suggested better dissecting the cases of epistasis to differentiate trivial cases due to the non-linearities inherent to the system, from other epistasis.

Reviewer 1 remarked that some evolutionary trajectories may not be independent of each other due to the possibility of gene flow.

Many relevant papers by Ogbunugafor and colleagues on studying epistasis and evolutionary trajectories on the same enzymes and in plasmodium were not considered here. It would seem important to cite this body of work and see how your results relate to their approaches and results. For example:

Ogbunugafor CB, Wylie CS, Diakite I, Weinreich DM, Hartl DL. Adaptive landscape by environment interactions dictates evolutionary dynamics in models of drug resistance. PLoS computational biology. 2016 Jan 25;12(1):e1004710.

Ogbunugafor CB, Hartl D. A pivot mutation impedes reverse evolution across an adaptive landscape for drug resistance in Plasmodium vivax. Malaria journal. 2016 Dec;15(1):1-0.

Ogbunugafor CB. The mutation effect reaction norm (mu‐rn) highlights environmentally dependent mutation effects and epistatic interactions. Evolution. 2022 Feb;76(S1):37-48.

Ogbunugafor CB, Eppstein MJ. Competition along trajectories governs adaptation rates towards antimicrobial resistance. Nature ecology and evolution. 2016 Nov 21;1(1):1-8.

Reviewer #1 (Recommendations for the authors):

1. There are five instances of incorrectly referenced figures throughout the text, "… (Figure ??) … ".

2. Appendix-figure 4 caption: "… gradient of the average…" Please clarify if this was a running average and over what interval window.

Reviewer #2 (Recommendations for the authors):

In this work the authors use a simple biophysical model to predict evolutionary trajectories of resistance to pyrimethamine – inhibitor of PfDHFR from P. falciparum and PvDHFR from P. vivax – pathogens causing malaria which presents a worldwide health concern. The authors use a simple fitness model that posits that selection coefficient -relative change in fitness between WT and mutant strains is determined by the fraction of unbound (to antibiotic inhibitor) DHFR. The population genetics simulations use the Kimura formula which is applicable to low mutation high selection regime where populations are monoclonal. The authors use computational tool Rosetta Flex ddG to assess binding of the antibiotic ligand to WT and mutant protein and compare their predicted evolutionary trajectories with lab evolution and data on naturally evolved variants worldwide and find semi-quantitative agreement, albeit sith significamt variation in detail.

The paper is of potential interest as it presents one of the first (but not the first) attempts to compare evolutionary dynamics based on biophysics inspired fitness model with laboratory evolution and natural data for very important problem of emergence and fixation of antibiotic resistant alleles. As such it can be a useful starting point for more detailed and biophysically realistic models of evolution of resistance against anti-DHFR drugs.

There are a number of issues – mostly technical but important – which limit potential impact and predictive power of this work. Let me list them in order of importance:

1) The fitness model whereby fitness of a variant is proportional to the fraction of free DHFR (and hence selection coefficient in Kimura formula is defined as relative difference in this quantity) is very simplistic. In fact earlier studies by Kaczer and Burns, Dean and Hartl and Rodrigues et al. (2016) cited here show that selection coefficient with respect to variation of DHFR is a more complex non-linear function of DHFR abundance, activity and – importantly – other enzymes in the folate metabolism pathway. Recent paper PMID: 26484862 established a proper fitness model for DHFR variation.

2) Rosetta ddG Flex does a mediocre job, to say the least in predicting binding free energy.

Table 1 shows that predictions in many cases are off quite substantially.

3) Equation 1 to predict fraction of unbound protein is not entirely accurate. The correct set of equations to determine this quantity is:

Lfree+LfreePfreeKd=L0

Pfree+LfreePfreeKd=P0

Lfree=L0+(Pfree−P0)

Pfree+(L0+(Pfree−P0))PfreeKd=P0

Pfree2Kd+Pfree(1+L0−P0Kd)−P0=0

Pfree=Kd2(−1−L0−P0Kd±(1+L0−P0Kd)+4P0K2)

=Kd2(−1−L0−P0Kd+1+2(L0+P0)Kd+(L0−P0Kd))

Where Pfree and Lfree are concentration of free (monomeric, unbound) protein and antibiotic Where ligand in solution and P0 and L0 are their total concentrations. Under certain conditions this full result reduces to Equation 1 but it is important that the authors assess whether these conditions are indeed met in realistic cellular scenarios. In essence Equation 1 assumes that Lfree | L0 but it is not clear whether this is a realistic condition.

4) Given that there are so many caveats and limitations to the underlying analysis the authors should revisit their results and discuss why some of the predictions are robust to these limitations and where the predictions fail due to the limitations of the analysis.

5) The authors point out to many cases when epistasis is observed but it can be a “trivial” epistasis due to the fact that Kd that determines fraction of free proteins is related to 'G in a non-linear way, see e.g. PMID: 21610162. It might be interesting to outline cases where epistasis is “trivial” and where it is related to effective interactions between mutation sites.

In summary this is an interesting work with some potential implications for predicting evolution of antibiotic resistance but technical concerns need to be addressed to make the foundation of the study more solid.

Reviewer #3 (Recommendations for the authors):

Major points and suggestions:

1. The comparison between the computational results and previous studies is done in a case-by-case manner. This is certainly informative. But it is somewhat dissatisfactory that a single summary metric (or a small number of them) is not provided as an overall performance measure of the computational method.

2. The presentation will benefit hugely if a fitness graph (based on hypercube representations, see for e.g. de Visser and Krug 2014, Figure 1c) is provided based on the free-energy change estimates from the computational method.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A computational method for predicting the most likely evolutionary trajectories in the stepwise accumulation of resistance mutations" for further consideration by eLife. Your revised article has been evaluated by Christian Landry (Senior Editor) and a Reviewing Editor.

The manuscript has been improved, but some remaining issues must be addressed, as outlined below. Following the submission of their respective reviews, we discussed with the reviewers, and the consensus is that the two significant points that follow remain problematic. Overall, the reviewers are excited about the development of computational tools to predict resistance. Still, at the same time, there remain major concerns about the actual data and model used to make predictions.

1) As raised by one of the reviewers in the initial review process, the RosettaFoldDDG poorly matches experimentally measured parameters. You now include a measure of correlation that confirms this poor accuracy. It, therefore, remains challenging to understand how the methods would work if the predicted measures do not reflect actual physical parameters. The reviewers would minimally require that the predictions of binding affinities are validated using alternative methods (computational or experimental).

2) One of the papers that are cited (2016 PNAS) to support the work actually shows that resistance, at least in bacteria, is very poorly predicted from the same parameters used here when considering a full fitness model. It would therefore be necessary that the authors use a fitness model to show that binding affinities are indeed predictive of resistance or that the values that are predicted using RosettaFoldDDG are indeed predictive.

Reviewer #1 (Recommendations for the authors):

The authors satisfactorily addressed my comments and concerns.

Reviewer #2 (Recommendations for the authors):

The authors addressed many editorial concerns raised by all reviewers.

I am still of the opinion that the premise of the study – to use biophysical model to explore evolutionary dynamics of resistant variants – is worthwhile and timely.

Nevertheless, my two most important essential concerns have not been addressed adequately making me question the technical validity of the study.

1) The authors completely misrepresent the key conclusion of the study of Rodrigues ate al 2016 PNAS. They suggest that Rodrigues et al. claimed that inhibitor binding to DHFR is the most important and predictive biophysical trait that determines fitness and more specifically IC50. In fact, the direct opposite is true – Fig, S8 of Rodrigues et al. showed that binding affinity to antibiotic is THE LEAST predictive of IC50 biophysical property and that there is no statistically significant correlation between Ki alone and IC50 for many variants and conditions explored in the 2016 Rodrigues at al PNAS. Essentially these authors showed that ignoring the effect of mutations on catalytic activity and proteins stability/abundance completely eliminates the predictive power of the biophysical model. This is the key conclusion of the 2016 paper which is completely misinterpreted in the present work. The authors of course may disagree with the conclusions of the 2016 study but in this case, they MUST present evidence of the validity of their simplified, naive biophysical model.

2) Table 1 still shows that there is no relationship between ddG predictions and reality and the authors themselves admit that the correlation is not statistically significant. Their justification of using Rosetta that there is no other method that provides prediction of binding affinities is both incorrect and disingenuous. Using such inaccurate predictions of the only parameter in their fitness model makes the approach devoid of predictive power.
