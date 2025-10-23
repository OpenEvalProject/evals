# Peer review - Round 1

Editors:
- Yuval Elhanati, https://ror.org/02yrq0923 Memorial Sloan Kettering Cancer Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82786.sa0](https://doi.org/10.7554/eLife.82786.sa0)

This study presents a valuable mathematical model for the adaptive dynamics of cancer evolution in response to immune recognition. The mathematical analysis is rigorous and convincing, and overall the framework presented could be used in the future as a solid base for analytically tracking tumor evasion strategies. The work will be of interest to evolutionary cancer biologists and potentially may also have implications for the design of clinical interventions.


---

# Peer review - Round 1

Editors:
- Yuval Elhanati, https://ror.org/02yrq0923 Memorial Sloan Kettering Cancer Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82786.sa1](https://doi.org/10.7554/eLife.82786.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Optimal Cancer Evasion in a Dynamic Immune Microenvironment Generates Diverse Post-Escape Tumor Antigenicity Profiles" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

As you can see below, the scope and mathematical effort in your manuscript were greatly appreciated by all reviewers. The model is mathematically rigorous and addresses an important and timely problem. There were some doubts about the applicability of your model to cancer evolution in real situations, but as a conceptual paper, it can contribute much to the advancement of the field. Even then, it needs some more work to be truly beneficial for the community.

1) Clarity of the paper should be improved. This includes a better discussion of the underlying assumptions, less technical terms and clearer ones, and a tighter exploration of the important parameters of the model, possibly with a phase diagram or similar graphical aid.

2) The process of Clonal cancer evolution should be better discussed in relation to the model, which describes the dynamics of mutations but does not follow clones.

3) The claim that the cancer cells are sensing the immune system is a bold and intriguing one, and as such need to be better supported, or otherwise, it is hard to justify.

Reviewer #1 (Recommendations for the authors):

The actual evolutionary process in the tumor happens on the level of cells and clones. Tumor clones proliferate and compete, each with its own fitness under the changing selection pressure from the immune system. However, the model here does not address tumor cells or clones, but rather the presented antigens as independent particles. While this is not an unreasonable choice, it does require better discussion and justification.

A major ingredient of the model is the penalty for immune evasion – in which while evading immune recognition of certain TAAs, a tumor will develop new ones as potential new targets for the immune system. This is presented in an opaque way, with several assumptions and specific mathematical forms. There should be some tradeoff between immune escape and loss of function, that would lead to such a penalty, and it should be made more concrete and transparent.

The idea that cancer can sense and respond to the immune system and the tumor microenvironment is exciting and intriguing but therefore requires stronger evidence. It would be valuable to make more connections to known observations to support this type of model. This is especially true since some of the model "predictions", like the correlation between lower immune surveillance and tumor mutational burden, are known from simpler principles.

And more generally, language and notation should be improved throughout the manuscript, making it easier to follow. Some jargon should be discouraged or explained, like "date-n" or "mean evolution dynamics" (section 3.1). A phase-space-like diagram of the different parameters' regimens of the model (maybe β and q?) would also be extremely useful.

The definition of eta is confusing. The manuscript states: 'eta may be interpreted as the probability of the complement of the following event: "recognition occurs without matched evasion for a single antigen". In other words, eta is the probability of a tie at a single antigen position.' But the complement of that event also includes the probability of no recognition, on top of a tie, unless I misunderstood what tie means. Regardless, tie is a confusing term here and should at least be explained better.

Reviewer #2 (Recommendations for the authors):

Reviewer #3 (Recommendations for the authors):

Developing such conceptual models is important and has the potential to inspire the wider field. However, I fear that some of that full potential might not be reached without additional work rewriting the text for greater clarity and precision. The following are some suggestions that might be helpful in that regard.

To start with, I had a hard time following some of the terminology. There are some instances where different terms are used to refer to the same concept. For instance, in Figure 1C the terminology changes between the legend (evasion rate) and plot (optimal downregulation attempt probability). Furthermore, the terminology seems overloaded: π is referred to as an evasion probability, but maybe one would want to reserve this term for the complete evasion of immune recognition by cancer. π might be more simply referred to as a rate of antigen loss, or similar. I was also wondering whether it would make sense to directly include β in Eq.1 and separate it from the penalty term. I understood penalty to refer to the increase in antigen creation rate when π is higher. From the equation, β instead could be more aptly named a basal rate of antigen creation. Lastly, notations should be uniformized. Specifically, I noted that in the methods the rate at which TAAs are lost is denoted by p instead of pi, if I understand correctly, which can cause confusion for the reader.
