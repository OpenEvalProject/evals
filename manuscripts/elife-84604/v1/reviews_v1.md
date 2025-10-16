# Peer review - Round 1

Editors:
- Michael B Eisen, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84604.3.sa0](https://doi.org/10.7554/eLife.84604.3.sa0)

This study makes valuable observations about the representation of "value" in the mouse brain, by using a nice task design and recording from an impressive number of brain regions. The combination of state-of-the-art imaging and electrophysiology data offer solid support for the authors' conclusions. The paper will be of interest to a broad audience of neuroscientists interested in reward processing in the brain.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.84604.3.sa1](https://doi.org/10.7554/eLife.84604.3.sa1)

Ottenheimer et al., present an interesting study looking at the neural representation of value in mice performing a pavlovian association task. The task is repeated in the same animals using two odor sets, allowing a distinction between odor identity coding and value coding. The authors use state-of-the-art electrophysiological techniques to record thousands of neurons from 11 frontal cortical regions to conclude that (1) licking is represented more strongly in dorsal frontal regions, (2) odor cues are represented more strongly in ventral frontal regions, (3) cue values are evenly distributed across regions. They separately perform a calcium imaging study to track coding across days and conclude that the representation of task features increments with learning and remains stable thereafter.Overall, these conclusions are interesting and well supported by the data.

The authors use reduced-rank kernel regression to characterize the 5332 recorded neurons on a cell-by-cell basis in terms of their responses to cues, licks, and reward, with a cell characterized as encoding one of these parameters if it accounts for at least 2% of the observed variance (while at first this seemed overly lenient, the authors present analyses demonstrating low false-positives at this threshold and that the results are robust to different cutoffs).

Having identified lick, reward, and cue cells, the authors next select the 24% of "cue-only" neurons and look for cells that specifically encode cue value. Because the animal's perception of stimulus value can't be measured directly, the authors created a linear model that predicts the amount of anticipatory licking in the interval between odor cue and reward presentations. The session-average-predicted lick rate by this model is used as an estimate of cue value and is used in the regression analysis that identified value cells. (Hence, the authors' definition of value is dependent on the average amount of anticipatory behavior ahead of a reward, which indicates that compared to the CS+, mice licked around 70% as much to the CS50 and 10% as much to the CS-.) The claim that this is an encoding of value is strengthened by the fact that cells show similar scaling of responses to two odor sets tested. Whereas the authors found more "lick" cells in motor regions and more "cue" cells in sensory regions, they find a consistent percentage of "value" cells (that is, cells found to be cue-only in the initial round of analysis that is subsequently found to encode anticipatory lick rate) across all 11 recorded regions, leading to their claim of a distributed code of value.

In subsequent sections, the authors expand their model of anticipatory-licking-as-value by incorporating trial and stimulus history terms into the model, allowing them to predict the anticipatory lick rate on individual trials within a session. They also use 2-photon imaging in PFC to demonstrate that neural coding of cue and lick are stable across three days of imaging, supported by two lines of evidence. First, they show that the correlation between cell responses on all periods except for the start of day 1 is more correlated with day 3 responses than expected by chance (although the correlation is low, the authors attribute this to inherent limitations of the data), and that response for a given neuron is substantially better correlated with its own activity across time than random neurons. Second, they show that cue identity is able to capture the highest unique fraction of variance (around 8%) in day 3 cue cells across three days of imaging, and similarly for lick behavior in lick cells and cue+lick in cue+lick cells. Nonetheless, their sample rasters for all imaged cells also indicate that representations are not perfectly stable, and it will be interesting to see what *does* change across the three days of imaging.
