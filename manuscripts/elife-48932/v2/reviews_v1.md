# Peer review - Round 1

Editors:
- Jonathan Erik Peelle, Washington University in St. Louis United States

Reviewers:
- Ingrid S Johnsrude, University of Western Ontario Canada

## Review text

DOI: [10.7554/eLife.48932.055](https://doi.org/10.7554/eLife.48932.055)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Mapping the human subcortical auditory system using histology, post mortem MRI and in vivo MRI at 7T" for consideration by eLife. Your article has been reviewed by four peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Marta Correia (Reviewer #4).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife. There was widespread appreciation of the amount of care and work that went into the analyses, and many of the results are impressive, particularly the ex vivo work. At the same time the in vivo part seemed less clear and potentially underpowered, and there was general concern about the correspondence between function and anatomy, especially for the lower brainstem structures.

If you are able to substantially add to the in vivo story and (as you've indicated) provide all of the maps for the broader community, we would consider a new submission under "tools and resources". However, this would need to be a substantially improved paper and would likely go to the same set of reviewers.

Reviewer #1:

This is a very nicely done atlas of subcortical auditory structures that includes histological identification and connectivity from MRI (post mortem and in vivo). Although the results are large confirmatory, this is a thoroughly impressive technical achievement and the release and publication of these atlases is likely to be impactful.

That being said, I understand the reasons for not making the segmentations and streamlines available yet, but the work is difficult to fully judge without seeing these (for example, to determine how accessible the formats are for other researchers). I think the data and code will need to be made available to the reviewers in some fashion before the work could be accepted.

Reviewer #2:

This is a helpful comparison of histological, postmortem MR, and in-vivo structural and functional approaches to localizing auditory brainstem and midbrain structures. The authors make use of previously acquired data and public atlases to align estimates of cochlear nuclei, olivary nuclei, inferior colliculi and medial geniculate nuclei across these different datasets, along with estimating the tract connections between them using DTI acquired ex- and in-vivo.

Clearly a lot of work has gone into the various components of this project and care has been taken with the analyses. What wasn't clear to me was what – if anything – was the 'message' of the paper, except maybe one that was not intended, e.g., that even when state-of-the-art techniques are used on high quality imaging data, it is extremely difficult to identify smaller auditory nuclei accurately in-vivo. Indeed, even the connectivity of the IC is not straightforward to map out despite much higher quality data than is usually available along with generally careful processing.

My major concerns were as follows (note that the authors do mention the majority of these as issues in the Discussion):

1) The fMRI-defined nuclei are clearly inaccurate in that they are up to an order of magnitude larger than the actual anatomical structures, and do not conform to the structures' shape. This must stem in part from the surprising decision to use a 3.3mm FWHM smoothing kernel on high-resolution data. It was also surprising that no unmasked group z maps were presented; I can understand the idea behind the conjunction maps (showing x of 10 subject with FDR-corrected activation there), but the pretty minimal overlap in the SOC (3 of 10 subjects) doesn't inspire too much confidence. I also wondered where the cluster threshold of 27 voxels came from (subsection “Functional MRI analysis”, last paragraph), and what the rest of the slices look like through the brainstem (e.g., how many splotches are there).

2) The similarity between the estimates of CN and SOC across the BigBrain, ex-vivo, and in-vivo segmentations is near or at zero (as shown by the dice coefficients). Since defining these smaller structures is really the main potential contribution of the paper (given IC and MGB have been previously identified by a number of groups), this is concerning.

3) The tractography results also essentially show that the known connections between any of the nuclei cannot be reliably reproduced, especially in-vivo. For instance, in the demonstration subject in Figure 6 as well as the matrix showing total streamlines, the IC is essentially being bypassed, despite the fact that it is (to my knowledge) the major source of input to the MGB. In the Figure 3—figure supplement 1 of the postmortem data, there are also a lot of streamlines that must be incorrect (most prominently, the large set of streamlines going inferiorly, but also the huge projections from around the SOC and CN seeds that seem to bypass the IC and go directly into the MGB). The large projections going inferiorly from the IOC seeds (Figure 4) are also rather mysterious. Particularly given the statements regarding the 'vastly improved estimation of white matter connections'.

In terms of overall contribution, having labelled nuclei in two publicly available postmortem datasets is helpful, and the fix to the incorrect MNI warp of bigbrain is also good to have. I'm less convinced about the contribution of the fMRI data (compared to the previously published studies that they come from), due to the way that they were processed and analyzed. If anything, the DTI tractography results seem to confirm the problems that Thomas et al., 2014, showed with even better diffusion data.

Reviewer #3:

This manuscript examines the structure of human auditory subcortical structures by recording in-vivo 7T functional magnetic resonance imaging (fMRI), structural MRI, and diffusion MRI (N=10). Ex-vivo 7T structural and diffusion MRI were also recorded in a single post-mortem subject. A subcortical atlas was created from the post-mortem structural MRI and publicly available histology data, and used to validate the functionally identified subcortical regions.

All four subcortical auditory structures (MGN, IC, SOC, CN) were successfully identified using ex-vivo structural MRI, while in-vivo structural MRI could only be used to identify the MGN and IC. Using functional data, the MGN and IC could be identified in majority of the participants, while the SOC and CN could only be identified in a small subset participants (n = 2-3). Ex-vivo tractography showed significant within-structure streamlines while the number of between-structure streamlines was quite modest. On the other hand, in-vivo diffusion imaging revealed significant streamlines between and within structures.

In general, the paper makes a useful contribution to the literature, and the figures are lovely. The Introduction, however, could be reorganized to more clearly indicate the gap in knowledge and the research question that this work was designed to address, since the general location of the main subcortical auditory processing nuclei is already well known in humans. One strength of the paper is that these findings replicate the authors' previous work (cited Discussion, ninth paragraph)-lending further credence to the idea that subcortical structures can be reliably identified from functional data. However, one limitation is that functional localization was not very strong in lower brainstem nuclei (i.e., SOC and CN) for majority of the participants (cf. Figure 5 left and middle panel and Figure 5—figure supplement 1). I do wonder if the in-vivo portion of the study is under powered. This issue could be addressed using additional commentary by the authors, although if the N is not supported by a power analysis (or some other logical explanation), the paper could be improved by recording data from a larger sample.

Reviewer #4:

I was asked to provide a review of the diffusion MRI methods used in this paper. The tractography methods used follow the current state-of-the-art and were implemented using the well validated tools within dipy. The authors are also cautious with their interpretation of results, in line with the known limitations of tractography methods.

I don't have any major concerns over the methods used.
