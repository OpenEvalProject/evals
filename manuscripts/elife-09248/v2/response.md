# Author response - Round 1

Authors:
- Sergey Ovchinnikov
- Lisa Kinch
- Hahnbeom Park
- Yuxing Liao
- Jimin Pei
- David E Kim
- Hetunandan Kamisetty
- Nick V Grishin
- David Baker

## Response text

DOI: [10.7554/eLife.09248.031](https://doi.org/10.7554/eLife.09248.031)

Essential points to address:

1) While the results of CASP11 blind test are important and indicative, they cannot serve as a systematic and direct assessment of the accuracy of Rosetta-GREMLIN. It is necessary to directly compare the accuracy of Rosetta-GREMLIN with other leading methods, particularly EVFOLD. With such comparisons, the extent of progress in terms of prediction accuracy brought by this new method will be more clear and the authors' claims of unprecedented accuracy can be measured in specific metrics (e.g. Ca RMSD or TM score) and calibrated appropriately.

We did not argue in the original version of the paper that the Rosetta-GREMLIN method is better than those of Jones and Marks/Sander, because this is not the point of the paper. However, we appreciate the question of reviewer II about how much the increased computer time required for Rosetta structure predictions increases model accuracy, and more generally, the need for a more thorough comparison to existing methods, in particular EVFOLD. We have added to the manuscript a table comparing the Rosetta-GREMLIN method to the other methods for both the CASP targets and the membrane protein benchmark. For the CASP targets, we compare to the results of Jones who made submissions for the same targets for CASP. For EVFOLD, we used the excellent EVFOLD web server since EVFOLD did not officially participate in CASP11. For the membrane protein set, we do not compare to the benchmark/results of the previously published Evfold paper, as it would be unfair, given there were far less available sequences then and a less accurate contact prediction method (mfDCA) was used. For the comparison in the paper, the alignments we used were provided as input to the Evfold-webserver, and a contact prediction method very similar to GREMLIN (PLM) was selected. The EVFOLD web server returns 50 models, we computed the CA RMSD and GDT-TS for each of them, and selected the best one. The table compares this “best out of 50” selection to the single Rosetta-GREMLIN model chosen without knowledge of the correct structure as described in the text. We emphasize in the text that while the Rosetta models are more accurate, the EVFOLD models require orders of magnitude less computing time.

2) The angle and the motivation of this paper is reminiscent of the previous paper by Hopf et al. (Cell, 2012), which reported structure predictions, through exploiting evolutions covariance, for a relative larger number of membrane proteins without experimentally resolved structures. Of course the methodology is different here, but additional discussion of previous work along this line will help place the current work in an historical context. There have been structural predictions for some membrane proteins this paper discussed (e.g. adiponectin receptor and YeiH transporters). Briefly discussing these previous predictions and comparing them with the predictions by Rosetta-GREMLIN is needed.

We have added a sentence making this excellent point just before the discussion of the models. As described in the submitted manuscript, our adiponectin prediction is similar to the EVfold prediction, while in the other overlap case (EamA) the two models are quite different. We found no match of the YeiH transporter to any of those modelled in Hopf et al., 2012 nor the Evfold website.

3) The paragraphs in the Introduction describing the method are too long, too technical, and difficult to read. The Introduction should describe the method at a high level in a language accessible by a general audience and the technical details should be moved to the Methods. One reviewer summed up the new ingredients of this method as (A) making the distance restraint depended on the strength of the coevolution signal, (B) applying restrains between pairs of amino acids that are close in sequence first and adding restraints between remote residues later in the simulation to avoid trapping in wrong conformations, and (C) using the ROSETTA framework. This apt summary could be considered as a framework for a brief description of the method.

We have considerably simplified the multiple paragraph description of the method for identifying the families modeled in the paper and moved much of the detail to the Methods and table legend. The description of the method for generating the models is already quite brief (less than one paragraph), and it is difficult to shorten it further.

4) As one reviewer pointed out, much of the descriptive text concerning the specific structure models is too detailed with not enough motivation. A substantial portion of such text could go in a supplement so that the main discoveries are more visible. Alternatively, the text should be revised to be better connected to the main concern of the paper.

We have eliminated much of the descriptive text about specific conserved residues that are likely functional in the sections concerning specific structural model. We have emphasized in each individual case the gain from analyzing the coevolution data in the context of the three dimensional Rosetta-GREMLIN models over what could be gleaned from the co-evolution and conservation data alone.
