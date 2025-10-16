# Peer review - Round 1

Editors:
- Taekjip Ha, Johns Hopkins University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.35458.036](https://doi.org/10.7554/eLife.35458.036)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "FLAREs: Single-color, ratiometric biosensors for detecting signaling activities" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

- The concept is novel and the work is potentially a strong candidate for eLife. Observation of three different signaling events in parallel is important. However, a reviewer mentioned during the post-review discussion that three reporters in parallel is not by itself new.

- Testing was only done under signal optimal conditions. Example seems cherrypicked.

- Unclear how "usable" the technology will be. A more thorough characterization and comparison to current technology is needed.

- The MAPK sensor clearly should behave differently. The other sensors are also not well characterized.

- Cell population behaviors can be shown (e.g. multiple cell trajectories, average, stdev,.…). This would allow to get from anecdotal results to a real understanding of the robustness of the cell responses and biosensors.

The reviewers were generally positive about the approach but suggest a number of new experiments to validate the method and demonstrate the usability, and to characterize the reporters in more depth. Although I suspect not all the experiments are necessary to address their comments adequately.eLife. If a new manuscript is submitted that addresses the point in the future, we will be happy to consult the same reviewers.

Reviewer #1:

The authors re-engineer a number of classic FRET-based biosensors (PKA, ERK, PKC, MLCK, calcium, cAMP) biosensors using single color FPs that perform homo FRET, and that can be measured using fluorescence anisotropy measurements. Since each biosensor is based on only one color, this allows for multiplexed biosensor measurements in single living cells. It also allows to perform biosensor measurements in response to optogenetic activation. Finally, the authors perform some in vivo fluorescence anisotropy measurements using 2-photon microscopy.

The data somehow implies that a combination of mVenus and a cp mutant of Venus cp172-mVenus is the best pair for performing such anisoptropy measurements. It looks like that other pairs involving other color FPs perform much poorly. The authors propose that this can be a generalizable method to perform multiplexed imaging of multiple signaling activities in single living cells. While I like the concept, I think that the method might not be so easy to implement than as proposed. Multiplexed imaging has been performed using experiments that induce very robust signaling states. The poorest performing FP combination has been grafted on a calcium sensor that is known to be one of the most robust signaling modules available. The question is therefore if the approach has the full potential that the authors propose. This detracts my enthusiasm for the manuscript, and I do not think it is publishable in the present form.

Additional comments:

1) Throughout the paper, the authors analyse multiple cells for each respective experiment. Could the authors please show a representation of all of these curves with median, stdev, and accompanying statistics. That would really help the reader to get a sense of the robustness of the biosensor responses.

2) It would be helpful if the authors would calculate the SNR for all the biosensors, as they have performed for their AKAR-FLARE sensor. With 1. This would again give an idea about the robustness of the sensor.

3) The FLARE-EKAR EV sensor in Figure 2A displays sustained ERK activity in response to EGF stimulation, and is then switched off using a MEK inhibitor. This is contrary to another EKAR variant, EKAR2G, that displays a very transient ERK activity in the same HEK293T cells (PMID:23882122). Importantly, this is backed up with a phosphoERK western blot in this paper. What happens with this FLARE EKAR-EV version. Do the new FPs somehow influence the biosensor response, or is this due to the specific HEK293T cells/ experimental conditions used by the authors?

4) Figure 4A: from 9 cells, the authors imply that there are two dynamic signaling states in that experiment. I think that if they want to make a statement about something like this, they need to acquire much more cells, and avoid showing anecdotal data.

5) I think that one of the weaknesses of the paper is that they remain elusive about the microscopy setup, and the image analysis of the datasets. Obviously, all this information is published elsewhere. But this being a technology resource paper, I think that it would really make sense to discuss this in detail both of these aspects to make the reader more familiar with this imaging technology.

Reviewer #2:

The study of molecular dynamics in single cells has revealed unexpected complexity, only tractable by multiplexing molecular biosensors. Ross, et al. explore the use of fluorescence anisotropy to measure conformational changes in genetically encoded biosensors using a single color per sensor. The authors successfully use ratiometric measurements of polarized fluorescence to enable quantification of previously described FRET reporters. This is a very exciting idea as it could substantially increase multiplexing capabilities in single cells. The authors validate the use of FLAREs in a variety of individual sensors, multiplexed with optogenetic tools and in vivo. Although I find the concept and validation of great interest, the characterization of intramolecular fluorescence anisotropy and comparison to current methods is limited.

1) The authors should explore the use of fluorescence anisotropy to measure subcellular changes in activity. One of the advantages of FRET sensors is the ability to measure spatially restricted changes in protein activity (within cell compartments), however, the paper does not address whether local activities can be monitored also by fluorescence anisotropy. In fact, given the single color nature of FLAREs, single cell comparisons of FRET vs FLARE should be possible and helpful to define how these technologies compare quantitatively.

2) The novelty of this study relies on the use of intramolecular fluorescence anisotropy to measure conformational changes. However, the relationship between intramolecular distance (or orientation) and anisotropy is not explored. These experiments could be done by using linkers of different lengths or known proteins with different structures. In my opinion, a more thorough characterization of the parameters that affect intramolecular anisotropy is needed to understand the full spectrum of limitations and possibilities of this method.

3) The authors find that a circularly permutated Venus together with wt Venus is better at changing anisotropy, but then, the comparison to other FPs is done without any circular permutation. It is not clear, from the manuscript, what are the reasons for such comparison. If circular permutation affects anisotropy, other FPs should also be permuted.

4) Most experiments to test the reporting abilities of the sensor are done under chemical perturbation with chemicals that create non physiological states (i.e. Fsk, Ionomycin, PMA). To determine whether the reporting range of the sensor is appropriate for "real" conditions, a dose-response under physiological stimulation compared to other sensors should be done.

5) The choice of fluorescent proteins in the dual sensor experiment provided in Figure 4B is unfortunate. Venus and Cerulean3 are a FRET pair. This could be confusing the interpretation of the results. Using the Cherry version in one of the two sensors would be a more appropriate choice.

Overall, this study offers a novel strategy to enhance multiplexing capabilities when measuring single cell dynamics. Although the authors show multiple proof-of-principle experiments, the quantitative description of the parameters that affect intramolecular anisotropy and how it compares to FRET is poorly explored. Thus, I would encourage resubmission when these issues are addressed.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "FLAREs: Single-color, ratiometric biosensors for detecting signaling activities" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jonathan Cooper as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors re-engineered a number of classic FRET-based biosensors (PKA,ERK, PKC, MLCK, calcium, cAMP) using single color FP pairs that can perform homo FRET, which can be measured using fluorescence anisotropy measurements. Since each biosensor is based on only one color, this allows for multiplexed biosensor measurements in single living cells. It also allows them to perform biosensor measurements in combination with optogenetic activation systems. Finally, the authors perform some duo-color in vivo fluorescence anisotropy measurements using 2-photon microscopy. The data convincingly shows that (cp)mVenus and mCherry anistropy sensors can be multiplexed in complex cell types and in vivo measurements. The data also shows that the (cp) mCer-sensors performs a lot worse in comparison. Overall, the concept and experimental validation reported here are of great interest for the research community and the revision improved the quality of the work significantly. However, there are still significant concerns some of which may require some additional experiments to address.

Essential revisions:

1) The authors stress that their method provides a generalizable method for (triple) multiplex imaging, and state that "The fact that FLAREs only occupy a single color channel and are highly generalizable for different biosensors, as well as color variants, highlights their utility for multiplexed imaging applications".

With such a strong statement:

The authors should really show that the mCer3 based anisotropy measurements are usable in multiplex experiments beyond highly sensitive calcium sensor modules and / or under physiological conditions (e.g. histamine-induced response on FLARE-mCer3 probe).

2) The authors added (Figure 1—figure supplement 1) a convincing comparison of different linkers in mVenus-mVenus anisotropy measurements. Is this a general principle that can be applied to optimize anisotropy based biosensors? E.g. is this similar for mCherry/mCerulean based anisotropy sensors? This should at least be discussed (or better shown) to provide the readers with a basis to start utilising this technique. Similarly, it would greatly help the reader audience if the authors can discuss/speculate on the reason for different performance of the mVenus-pair over the other fluorescent protein pairs in anisotropy measurements.

3) One of the advantages of FRET sensors is the ability to measure spatially restricted changes in protein activity (within cell compartments), however, the paper does not address whether local activities can be resolved also by fluorescence anisotropy. In Figure 1—figure supplement 5 authors target the reporters to subcellular compartments and show changes in anisotropy, however, I think the authors should determine whether a local activity can be resolved using a non localized sensor. For instance Matsuda et al. (PMCID: PMC3226481) show that PKC in response to TPA is activated at the membrane edge. The authors should test the spatial resolution power of anisotropic probes using their FLARE CKAR.

4) All the experiments shown in this study have been done using transfection or electroporation which results in major overexpression of the biosensor. The authors should determine whether expression level determines the reporting ability of these sensors.

5) Although it may seem obvious I think the authors should determine whether the anisotropy change depends on the fluorescent proteins being in close proximity or just the conformational change itself. Mutating one chromophore could easily address this question.

6) Statistical methods and data reporting:

- Generally: Why are the average curves (including the variance measurements) in the supplemental figures? It would be much more informative and convincing for readers to show these in the main figures instead of the current "representative example curves".

- Unclear from which timepoints (or pooled timepoints?) the data in the boxplots in Figure 1B, C, 2A, B, C is calculated/compared.

- Unclear whether mean or median is represented in the boxplots in:

Figure 1B, C

Figure 2A, B, C

Figure 1—figure supplement 3 (also which variance measurement is used here?)

Figure 3—figure supplement 1B

Figure 3—figure supplement 3

Figure 4E (which variance measurement is used here, how is statistical significance calculated? -> descriptions missing in legend/main text).

- No (vehicle) controls in Figure 2B, C e.g. MLCK sensors can be activated by mechanical stress on cells from adding the experimental agents (it is also unclear from the "Materials and methods" section in what chamber cells were imaged, and how agents were added to the cells during experiments).
