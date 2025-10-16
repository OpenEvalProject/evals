# Peer review - Round 1

Editors:
- Jennifer M Groh, Duke University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65566.sa0](https://doi.org/10.7554/eLife.65566.sa0)

How the auditory system encodes speech sounds is not well understood, and animal models have a lot to offer in investigating such questions. This study evaluated the representations of a variety of natural and synthetic sounds in both ferrets and humans, and reported that humans differed from ferrets in the manner in which speech and music were represented, despite controlling for the spectrotemporal content of the sounds. This work makes an important contribution to our understanding of how the coding of such sounds differs across species.


---

# Peer review - Round 1

Editors:
- Jennifer M Groh, Duke University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65566.sa1](https://doi.org/10.7554/eLife.65566.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Distinct higher-order representations of natural sounds in human and ferret auditory cortex" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Andrew King as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Greg Cogan (Reviewer #2); Tobias Overath (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Both reviewers found the work to be interesting and important, but the concerns about the reproducibility of the finding given the small number of animals tested weighed heavily. Given that both reviewers found merit in the work, we encourage a revised submission provided the concerns about reproducibility can be satisfactorily addressed.

Reviewer #2 (Recommendations for the authors):

1. Fig 2F: It would be useful here to quantify the slope as this appears to be a relevant feature of this figure.

2. Figure 2F: Are the distances for ferret vs. human chosen for a particular reason? Is it just a simple linear scaling based on brain size?

3. Is the unit size of one voxel a reasonable analysis size? If you average over all voxels in a particular region, do the results from figure 1A-D change?

4. Does the dimension reduction/component analysis (Figure 3) contain data from experiment 2 or just experiment 1? If only 1, do the results change by including the data from experiment 2?

5. While I am sure that the difference between methods of acquisition cannot fully explain your results (fUS vs. fMRI), is would be useful to comment on the relative SNR of the methods and how this would or would not influence your results.

Reviewer #3 (Recommendations for the authors):

1) Selectivity vs. sensitivity

The authors use the term selectivity, which implies exclusivity: e.g., response to a certain sound characteristic, but no response to any other sound characteristic. Given the actual data that the authors show, a more appropriate term to use would be sensitivity. For example, the f3 component's response profile in Figure S3 clearly shows the strongest response to speech sounds, but there is also substantial (though weaker) response to the other types of sounds. In that sense, f3 is not selective, but rather shows that it reflects maximal sensitivity to speech sounds (or, even more precisely, particular spectrotemporal characteristics of speech sounds). The authors should adjust the terminology accordingly throughout their manuscript.

2) Generalizing from 2 ferrets to all ferrets seems 'courageous' to me, especially given the replicability crisis in the human neuroimaging community. For what it's worth, the mean signal prior to denoising (Figure 1C) looks about as noisy as human fMRI data. I understand the invasive nature of fUS imaging, but I would feel much more comfortable seeing these results replicated in more animals.

3) Can the authors expand a bit on their reasoning for choosing a 3-11 s time window (line 701)? Looking at Figure 1c, it seems that this includes data from the initial rise period (which is not of interest), rather than just the (more) steady part of the response. I would have expected the authors to focus on the sustained, steady part response (e.g. 6-11 s), which presumably best reflects processing of the summary statistics of the input sound. The authors should show that their results are insensitive to (reasonable) variations in the time window.

4) NSE. I implemented the NSE formula in Matlab via

x = rand(1,40);

y = rand(1,40);

NSE = mean((x-y).^2) / (mean(x.^2) + mean(y.^2) – 2*mean(x)*mean(y))

However, the values I get for this implementation are not bounded between 0 and 1. Perhaps my implementation is wrong, or there is an error in the formula?

Also, after clarifying their NSE measure (or pointing out the mistake in the above implementation), can the authors elaborate on how NSE can distinguish between the cases (A) where a voxel has different response profiles for natural vs. model-matched sounds (e.g. x = 1:40; y = 40:-1:1;) vs. (B) where the response difference between natural and model-matched sounds is simply additive (or multiplicative) in nature (e.g. x = 1:40; y = x*2), vs. (C) when they are anticorrelated (x = [1 -1 1 -1]; y = [-1 1 -1 1])?
