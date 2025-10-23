# Peer review - Round 1

Editors:
- Alex Fornito, https://ror.org/02bfwt286 Monash University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73153.sa0](https://doi.org/10.7554/eLife.73153.sa0)

This paper describes a new open-access digital brain bank of post-mortem brains that have been scanned with high-resolution, multimodal magnetic resonance imaging and with select datasets accompanied by histological data. This valuable resource can be used to study healthy human brains, pathological human brains, and the brains of other species, opening new opportunities for comparative neuroanatomy and the biological validation of non-invasive neuroimaging signals.


---

# Peer review - Round 1

Editors:
- Alex Fornito, https://ror.org/02bfwt286 Monash University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73153.sa1](https://doi.org/10.7554/eLife.73153.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "The Digital Brain Bank, an open access platform for post-mortem datasets" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Büchel as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Ilona Lipp (Reviewer #1); Konrad Wagstyl (Reviewer #2); Timo Dickscheid (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Please modify the term "interactive data discovery and release platform" which, as used in the abstract, a little bit misleading. The interactivity is limited to viewing overlays of different images in a few of the datasets and the release option of one's own datasets is not established (yet).

2. Please add the resolution of all scans to Table 1.

3. Regarding the sentence "Although MRI hardware and acquisition protocols often need to be tailored to a specific domain, the signals measured in all these settings are fundamentally the same (Boon et al., 2019)." -> Please clarify the intention of this statement--is this an argument for using post-mortem MRI?

4. Please clarify: in Table 1, when it says structural MRI, is this always a T1w image?

5. Please clarify: From the text, it is not clear what diffusion data are made available exactly. Is this all diffusion-weighted images or just the estimated parameters, or does this depend on the database? ("To facilitate cross-dataset comparisons, the majority of diffusion datasets from the Digital Brain Bank provide derived diffusivity estimates in the form of diffusion tensor and/or ball and sticks model parameters (Behrens et al., 2007)). To reflect this, we primarily provide curated datasets to facilitate these analyses, as opposed to outputs associated with the results of specific projects (e.g. tractography-derived maps)…. Curated unprocessed data is additionally provided when there are clear routes of investigation (e.g. diffusion MRI volumes to investigate alternative diffusion models)."

6. Please clarify what you mean by 'tractography-derived maps' and 'clear routes of investigation'? (P.S.: "data are" not "data is")

7. The authors have chosen here to present the MRI data co-registered to the 2D histology and not vice versa. Sectioning can introduce morphological shifts in the tissue that might alter neuroanatomical findings relative to the original brain structure. Please add a note to explain why they chose to present the registration this way round.

8. The paper puts much emphasis on describing the postmortem MRI aquisition details, but the abstract suggests a clear focus on the neuroinformatics aspect. Please update the abstract to describe details about the postmortem acquisition component.

9. It would be very helpful if the publications that are listed for datasets were actual hyperlinks, so one could directly access them and need not copy-paste them in the browser.

10. Please specify how version control will be managed for future datasets. Given the nature of the data, more high-resolution scans might be added to existing datasets. How would users of the platform keep track of this?

11. Please place the paragraph on the Tensor Image Registration Library in the methods section rather than in the results.

Reviewer #1 (Recommendations for the authors):

It would help adding the resolution of all scans to Table 1, especially since the advantages of high resolution were so strongly advertised with Figure 1.

Regarding the sentence "Although MRI hardware and acquisition protocols often need to be tailored to a specific domain, the signals measured in all these settings are fundamentally the same (Boon et al., 2019)." -> I was not sure what you are trying to say here, is this an argument for using post-mortem MRI? If yes, this is not super clear from what comes before.

Table 1 very helpful, when it says structural MRI, is this always a T1w image?

From the text, it is not clear to me what diffusion data are made available exactly, is this all weighted images or just the estimated parameters, or does this depend on the database? ("To facilitate cross-dataset comparisons, the majority of diffusion datasets from the Digital Brain Bank provide derived diffusivity estimates in the form of diffusion tensor and/or ball and sticks model parameters (Behrens et al., 2007))…. To reflect this, we primarily provide curated datasets to facilitate these analyses, as opposed to outputs associated with the results of specific projects (e.g. tractography-derived maps)…. Curated unprocessed data is additionally provided when there are clear routes of investigation (e.g. diffusion MRI volumes to investigate alternative diffusion models)."

Also, could you please clarify what you mean by 'tractography-derived maps' and 'clear routes of investigation'? (P.S.: "data are" not "data is")

Reviewer #2 (Recommendations for the authors):

- It is currently unclear in table 1 which species have both structural and diffusion scans. These could be indicated with a symbol such as an asterisk.

Reviewer #3 (Recommendations for the authors):

– The paper puts much emphasis on describing the postmortem MRI aquisition details, but the abstract suggested to me a clear focus on the neuroinformatics aspect. I think this additional focus would be beneficial to point out more clearly in the abstract already.

– To me, the platform would benefit a lot from a visual (3D) overview illustrating where in each whole-brain dataset the additional microscopy datasets have been measured. This could even be a pre-computed cross-sectional view with markers.

– Figure 3: The caption "the digital pathologist" suggests to see the corresponding software interface, but the figure rather illustrates typical content.

– It would be very helpful if the publications that are listed for datasets were actual hyperlinks, so one could directly access them and need not copy-paste them in the browser.

– Do you foresee versioning of the datasets? Given the nature of the data, I imagine that e.g. more high-resolution scans might be added to existing datasets. How would users of the platform keep track of this?

– l. 525 ff: I would expect the paragraph on the Tensor Image Registration Library rather in the methods section than in the results.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The Digital Brain Bank, an open access platform for post-mortem datasets" for further consideration by eLife. Your revised article has been evaluated by Christian Büchel (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

– Re: R1 C1:

"established laboratory models" may sound like disease models, which is intuitive for the digital pathologist, but a bit restrictive for the digital anatomist. Please rephrase.

– Re: R1 C8:

"The signals measured in all these settings are fundamentally the same" is somewhat vague, as due to the same technology, the type of signal measured is the same, however, how to interpret and utilise the signal is quite different, which makes the "direct translation between domains" challenging. This paragraph of the manuscript can be slightly misleading. Please rephrase.

– in vivo is not spelled consistently across the manuscript (e.g. lines 75 and 77). Please amend

– The discussion with reviewer 3 on version control was important. While not raised in the initial round of reviewer comments, please consider adding DOIs to individual datasets. Typically, when datasets are shared through repositories they are assigned dataset DOIs (e.g. figshare, zenodo, University repos), which are essential for reproducible data science. Currently users of this platform can cite DOIs for the dataset's paper of origin and this platform. Perhaps within the future goals for version control, DOIs for specific version might also be added.

Reviewer #1 (Recommendations for the authors):

The authors have provided thorough explanations and amendments in response to my previously raised comments. I think that the manuscript has substantially improved now in terms of clarity. I have no more major comments.

Reviewer #2 (Recommendations for the authors):

The authors have responded in detail to the reviewer comments. The responses to my initial comments were addressed and overall the manuscript and description of the resource is improved.

Reviewer #3 (Recommendations for the authors):

Thank you for the detailed responses to the remarks on the first manuscript.

All my concerns have been clarified in detail in the author's response, and appropriately addressed in the revised text. Especially by toning down the platform aspect and putting more emphasis on the system as a data resource, I find the manuscript now very consistent.

From my perspective, it can be accepted in the present form.
