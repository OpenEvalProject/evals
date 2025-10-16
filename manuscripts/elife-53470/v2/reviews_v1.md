# Peer review - Round 1

Editors:
- Timothy E Behrens, University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53470.sa1](https://doi.org/10.7554/eLife.53470.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The paper demonstrates the efficacy of a new non-invasive method that is sensitive to histological features such as cell size. This is an important advance that opens up studies, for example, in other brain regions and clinical populations. It provides a new level of detail in our understanding of the microstructure of the human insula. The study is further unusual in providing comparison between human and nonhuman primate. This is important as much of our knowledge about the cytoarchitecture and connectivity in general, and in insula in particular, is derived from extrapolations from other primate species.

Decision letter after peer review:

Thank you for submitting your article "Microstructural organization of human insula is linked to its macrofunctional circuitry and predicts cognitive control" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Timothy Behrens as the Senior and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Matthew F Glasser (Reviewer #1); Leonardo Cerliani (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors provide an interesting analysis of the relationships between microstructure, functional connectivity and behavioural specialization for different regions of the human insular cortex. The most original finding relates to the distribution of a DWI-derived microstructural index denoted RTOP (Return to Origin Probability), which is sensitive to the volume and distribution of cell types in different cortical regions, and to the relationship of microstructural feature and functional specialization in insular and functionally connected cingulate regions, together representing the core of the Salience network. The major contributions of the work are a demonstration of sensitivity to histological features such as cell size in vivo with an innovative MR technique, a demonstration of how these features change in the human insular cortex, and a demonstration of the relationship between these features across distant, but connected, regions. The authors should also be commended for replicating the RTOP analysis in specimens of nonhuman primates, as most of our knowledge about insular cytoarchitecture and connectivity still relies on extrapolation from other primate species.

Essential revisions:

In the below, I have replicated comments from the original reviews, but I have previewed them with key elements of our discussion where we tried to clarify which comments should be addressed directly and which could be discussed.

Insular Parcellation:

Several concerns were raised about the insular cortex parcellation that you use. These concerns were about (i) the quality, and (2) the hemispheric asymmetry of the particular parcellation that you use, which could affect the results and (3) the group- rather than individual- nature of the parcellation, in the face of large reported individual differences. Reviewer comments are copied below. In the discussion, the reviewers agreed that it would be sufficient to reproduce key results using the HCP parcellation (described in first comment below), and to discuss the potential impact of individual variability in the discussion. It is hoped that the HCP parcellation (which does not contain the clear asymmetry present in the Deen parcellation) will improve some puzzles in the current results (eg pronounced asymmetry in Figure 2C). We hope that this will be straightforward as it simply requires running your existing pipeline on a new set of insular masks that are freely available.

Comment 1:

"The insular parcellation used by the authors appears of poor quality. For one thing, it is a volume-based parcellation generated from a small number of subjects (n=30) using a clustering algorithm (whose winner take all hard parcellation will be sensitive to noise when near the boundary) only on resting state data. The HCP has produced a much higher quality multi-modal parcellation of the whole cerebral cortex (Glasser et al., 2016 see Supplementary Neuroanatomical Results Figure 14), including the insula, from 210 HCP subjects and precisely replicated it in an additional 210 HCP subjects. The HCP recommends the use of this parcellation together with HCP data. Notably, this parcellation does not show the large hemispheric asymmetry found in the insular parcellation used by the authors in either the final parcellation or the multi-modal data it was defined from, despite the fact that such asymmetries could be found (and in fact were found) in some parts of the cortex in the HCP parcellation. Thus, any of the asymmetries found by the authors using the parcellation may result from idiosyncrasies of that parcellation (e.g. the failure to separate right dAI vs vAI, which I didn't see mentioned anywhere). That said, the three regions described by the authors might be reconstructed from the HCP's parcellation by grouping AAIC (vAI), AVI+MI(dAI), and Pol1+Pol2+Ig(PI) if desired. Depending on how the authors want to define the insular cortex, they might also include FOP3 and FOP2 in dAI and π respectively. Similarly, if the analysis were done with an HCP-Style approach (Glasser et al., 2016) the authors might find that their anterior cingulate regions match areas p24, a24pr, and p24pr (Glasser et al., 2016, see Supplementary Neuroanatomical Results Figure 19). Of note, the agranular to granular transition in the anterior cingulate cortex is much more pronounced in the inferior to superior direction than the anterior to posterior direction (Glasser et al., 2016 Supplementary Neuroanatomical Results section 19, Glasser and Van Essen, 2011, Journal of Neuroscience section on Cingulate Cortex)."

Comment 2: (Which should be addressed in discussion and not in new analyses.)

Interindividual variability and delimitation of insular regions.

The Authors state that "no consensus has yet emerged about their precise boundaries because of small sample sizes, limited insular divisions examined and high degree of variability across individuals". The first rationale of the statement – the small sample size of the histological samples – is not necessarily pertinent to accurately localize cytoarchitectonic transitions. For instance the transition between primary sensory and motor cortex is always very stablly localized, while other transitions – e.g. between BA44 and BA45 – are also clear at a microscopic examination, but present high intersubjective variability in terms of localization (cfr Amunts K et al., 1999 J Comp Neurology). In fact, the latter – rather than small sample sizes – could represent the main reason why also in the insula it is difficult to distinguish different architectural territories. Given this intersubjective variability – as mentioned by the Authors – it is peculiar that the present investigation relies on an insular parcellation which does not estimate such interindividual differences, as it was extracted from the mean connectivity matrix (cfr. Deen et al., 2010 p. 2).

In light of these considerations, I believe that the present analysis would have been much more compelling and data-driven if instead of using a predefined parcellation, the Authors would have carried out a tripartite parcellation of the insula in every individual using the rs-fMRI data at hand, even just with a simple k-means. Since the rs-fMRI data has already been preprocessed for the functional connectivity analysis, such procedure would have been quite easy to implement. I understand that this would probably be an excessive burden to carry out since the insular parcellation represents the very first step of the analysis, but I would like to ask the Authors to acknowledge the limitations the current choice.

Reference to prior work in insular parcellation:

There were several comments about your scholarship with reference to prior work in insular parcellation (some of this work is referenced in the comments above and others in the comments I have copied here)

"Further, there are multiple statements in the paper about lack of prior non-invasive mapping of the insula in the paper that must be toned down in the face of extensive prior literature."

"The Authors present the results by Deen, 2010 and Chang, 2012 as the reference for insular parcellation. They should mention that also other parcellations have been proposed based on similar data, e.g. Jakab et al., 2012; Cauda et al., 2010; Kelly et al., 2012. Importantly, most of these work do not report that a tripartite parcellation represents the best solution for the insula.

As a side note, reference work for human – vs other primates – insular parcellation are not cited. See e.g. the work of Rose and Brockhaus in the review by Nieuwenhuys."

"Correct the neuroanatomical statements in the paper, since they contain several claims which diverge from the reference literature.

"The dysgranular cortex has an intermediate profile that has been mainly observed in the dorsal anterior aspects of the insula". This is not entirely correct, and in this form it is misleading. The dysgranular architecture characterizes as well the central and ventral territory of the insula. Indeed, most of the insular cortex can be characterized as dysgranular. The results in the cited reference (Kurth et al., 2010) show that the ventral middle part of the insula has a dysgranular architecture, while they do not provide results regarding the anterior dorsal territory.

"The anterior insula is more strongly connected to brain areas important for cognitive control, most notably the dorsal anterior cingulate cortex (ACC) while the posterior insula has stronger links with subcortical and limbic regions important for emotion, including the amygdala and ventral striatum". This statement diverges from the reference literature: the amygdaloid complex and the ventral striatum are mostly connected with the ventral anterior insula (cfr. Amaral and Price, 1984 J Comp Neurol and Chikama et al., 1997, respectively), while these connections decrease along the antero-posterior axis."

Data processing:

The reviewers raised concerns that the data processing is not state of the art. This was a surprise as the HCP data that the authors have used is freely available in processed form with state of the art techniques. The relevant reviewer comment is copied below. In discussion, the reviewers agreed that we should strongly encourage the authors to redo analyses as described in the comment. We think this represents best practice. However, we realise that this means redoing the analyses from scratch and, although, we believe it would improve results and represent best practice, we do not think it would fundamentally change the key message of the paper. Hence, in line with eLife review policy, this is therefore a recommendation not a requirement for publication.

Reviewer comment:

"It has been replicated repeatedly that cross-subject cortical alignment and ability to localize signals to cortical areas is maximized by using surface-based intersubject registration instead of volume-based registration and, in particular, by avoiding 3D unconstrained volume-based smoothing (Reviewed Glasser et al., 2016 Nature Neuroscience; explicitly redemonstrated Coalson et al., 2018 PNAS). As such, the HCP has provided precisely aligned surface-based CIFTI resting state data (aligned with the MSMAll algorithm). Thus, it was puzzling to find that the authors choose to start from the less well aligned volume-based data and then smoothed the data with "a Gaussian kernel of 6mm FWHM was first applied to the minimal preprocessed data to improve signal-to noise ratio as well as anatomy correspondence between individuals." Importantly, the second statement is a common brain imaging misconception that has been decisively disproved by Coalson et al., 2018 PNAS. Further, the fMRI denoising approach chosen by the authors does not match HCP recommendations-rather they should use the data denoised by spatial ICA and the FIX classifier and do not need to remove movement regressors again. Temporal filtering is also discouraged by the HCP as it affects both signal and noise equally. Further, for the purposes of this study, the authors can easily make use of the publicly available group average MIGP resting state data, where the alignment, structured noise denoising, and significant unstructured noise denoising have already been taken care of-if they do not wish to worry about these methodological details. "

Reporting of methodological detail.

There were several concerns related to the reporting of methodological detail that need to be addressed.

The description of key imaging methods is inadequate. It is useful to restate the key aspects of the HCP diffusion acquisition and preprocessing for readers so they need not refer back to another paper. Additionally, the macaque data acquisition description, apparently new data acquired for the paper, is inadequate. For example, the resolution, TR/TE, b-shells, and preprocessing details are left unspecified. Of note the HCP data were acquired with a single spin echo sequence to enable minimizing the TE and maximizing the SNR. The preprocessing of the macaque diffusion data needs to be described. Further, no details are given as to how the surface-based maps of RTOP were created and any additional processing (e.g. spatial smoothing, cross-subject alignment) that was done on the HCP preprocessed diffusion data or derivatives of this. Depending on the preferred approach of the authors (ideally the one that worked the best) the RTOP data should have been computed in the individual subject's physical volume space and then mapped from between the individual's MSMAll aligned white matter and pial surface meshes onto the 32k MSMAll surface standard space without any spatial smoothing or after mapping the preprocessed diffusion data from between the individual's MSMAll aligned white matter and pial surface meshes onto the 32k MSMAll surface standard space without any spatial smoothing and then modeling RTOP. This data could then simply be averaged across subjects. With 449 subjects, smoothing is unlikely to be necessary for SNR purposes, but modest surface-based smoothing reduces precision much less than volume-based smoothing (Coalson et al., 2018 PNAS).

More information about the CCA analysis.

The association between RTOP and cognitive control measures represents an important part of the results. While the correlation between the left and right canonical vectors is significant and features a moderate effect size, I have some issues with the interpretation of the weights in the first component of the CCA, especially because I know little about this technique.

1) The right dorsal anterior insula has the highest weight, as expected and detailed in the Discussion. However it is a negative weight, while other weights, and notably the rvAI, are positive. What is the meaning of the sign and of the sign difference in the weights, in the interpretation of the microstructure-behavioural association?

2) The weights of the first behavioural canonical variate appear flat, and most of them are zero. What are the implications of this for the interpretations?

3) It would be useful to have a plot of the cumulative variance explained e.g. by the first N pairs of canonical variate, to assess whether a different combination of regional microstructur/behaviour adds a substatial amount of variance

4) Does the significance of the correlation between the first pair of canonical variates survive if permutation testing is used instead of parametric testing?

Introduce the RTOP measure more clearly to a non-specialised audience:

"Explain neuroanatomical correlates of RTOP, which is also useful to interpret the behavioural correlation with microstructure. Differences in insular microstructure are quantified using the RTOP DWI derivative. However I couldn't find an explanation of the microstructural properties that the RTOP targets in the Introduction or in the Results, with only one small mention at the end of the Supplementary Materials. Think e.g. about fractional anisotropy (FA): a neuroanatomist would like to know not only that there are localized differences in FA between samples of participants, but also how FA relates to the microstructure of axonal integrity and myelin sheet, in order to interpret those differences. Please include a brief description of the microstructural properties that RTOP allows to highlight, and the rationale that links these properties to the RTOP calculation. Preferably this should be present in the Introduction."
