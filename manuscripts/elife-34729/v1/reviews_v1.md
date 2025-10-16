# Peer review - Round 1

Editors:
- Nir Ben-Tal, Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.34729.018](https://doi.org/10.7554/eLife.34729.018)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Rational Design of Thermostabilizing Point Mutations for G-Protein Coupled Receptors" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Arup Chakraborty as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Dmitry Veprintsev (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript describes a computational approach to the thermostabilisation of GPCRs. Prediction of thermo-stabilizing mutations is highly desirable because GPCRs that cannot be crystallized, are probably too unstable, and adding thermo-stabilizing mutations would make structure determination possible. The authors use the 5HT2c receptor as their target, because the structure had not been determined, and also there are close 5HT receptor homologs whose structures have been published (and therefore provide the best possible start for computational modelling). The program devised (CompoMug) is unique in that it takes into account four sources of information, whereas previous computational approaches normally considered only one. The four modules, knowledge-based, sequence-based, structure-based and machine learning, independently predicted point mutations that would thermo-stabilize the 5HT2c receptor. Sometimes, more than one module predicted the same mutation, but usually there was little overlap between the predictions. A total of 39 mutations were computationally predicted as being thermo-stabilizing, so these were expressed and purified, and the thermo-stability tested experimentally in the presence or absence of various ligands. Ten of the mutations (25%) were found to be thermo-stabilizing and were combined to make a triple mutant that was highly expressed and stable, and the structure was subsequently determined (accompanying manuscript).

There are two key features that sets this paper apart from previously published papers on predicting thermo-stabilizing mutations. Firstly, this manuscript considers and compares four different sources of information for predicting thermo-stabilizing mutations. Secondly, the predicted mutations were shown to be useful in generating a structure (reported in a separate paper). We appreciate that other GPCR structures have been published containing thermo-stabilizing mutations, but in many instances the authors have been less than candid about the approaches used to predict the mutations.

Essential revisions:

1) There are two numbers quoted for improved thermo-stability that are used throughout the paper to extol the virtues of the approaches developed, namely a 9˚C increase for a single mutation (C360N) and a 19˚C increase for a triple mutant. It appears that these numbers came from the graph in Figure 6 where the ΔTm is plotted for each of the constructs. However, the comparison is being made to the apo receptor, so the bar that gives the 9˚C increase is a C360N mutant receptor bound to ritanserin. The apo receptor containing the C360N mutation appears to have a ΔTm of 4˚C. However, this does not correspond to the data in Table 2 where the same mutation is shown with an apparent Tm increase of 8.6˚C. There cannot be two different numbers given for the same data. The 19˚C increase in apparent Tm seems to be of the mesulergine-bound mutant compared to the apo receptor. If it was compared to the wild type receptor bound to mesulergine, then the Tm difference would be about 5˚C lower. If the apo receptor is compared, the triple mutant would be about 10˚C more stable than the parental receptor. This graph needs to be re-drawn so that the increase in Tm is calculated between the parental receptor and mutant receptor when bound to the same ligand. This will give a true reflection on the improvement in apparent Tm. Secondly, all the actual Tms measured to create the data in Figure 6 must be included as a table in supplementary (or in the text). It is still worth putting in the bar graph as depicted in Figure 6, because it shows the absolute scale of thermo-stability and is therefore most useful in assessing the possibility of crystallizing a given mutant with a particular ligand. Error bars should also be put on both graphs.

2) The claims of Tm increases throughout the manuscript must be changed in the light of point 1.

3) The computational methods should be made available as scripts and/or web-server so that others can apply them to systems of interest.

4) It was unclear whether the method is transferable to other GPCRs. For generality, we recommend: (a) that the authors "retrospectively" predict stabilizing mutations used in crystal structures published by Heptares, and/or (b) that the authors implement their computational method (no additional experiments needed) to at least five other GPCRs of known structure and provide tables of suggested point mutations. Without this, the paper stands on only one example, although it claims a general method. We stress this point because two of the four modules the authors implement (knowledge based and structure based) may substantially narrow the scope.

5) In addition, the authors should include a brief discussion of potential applications of this algorithm to other classes of α-helical membrane proteins.

6) The authors claim that 25% hit rate is high. What are they comparing to? Alanine scan is obviously much lower, but structure based and especially consensus-based approaches have shown success rates of ~50% in soluble proteins.

7) Equation 1 is difficult to understand. It's essentially a way to quantify whether positions diverge from the family sequence consensus. We recommend carefully rephrasing the explanation of this equation taking care to correctly label the indices for each term (for instance, it seems that Cmax should be Ckmax).

8) The sequence alignment can have a dramatic effect on prediction success, especially in divergent sequence families like GPCRs. Could the authors provide more details about sequence cutoffs and sources of information for the sequences? Ideally, they would provide the sequence ID of each sequence that went into each of the MSAs they used.
