# Peer review - Round 1

Editors:
- Anne-Florence Bitbol, Ecole Polytechnique Federale de Lausanne (EPFL) Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97330.3.sa0](https://doi.org/10.7554/eLife.97330.3.sa0)

This study presents a useful pipeline for de novo design of antimicrobial peptides active both against bacteria and viruses. The method is based on deep learning, using a GAN generator and a regression tasked to predict antimicrobial activity. The experimental evidence supporting the conclusions is solid, with 24 validated peptides, although some additional justifications of the computational strategy would be a plus. This work will be of interest to the community working on machine learning for biomedical applications and specifically on antimicrobial peptides.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97330.3.sa1](https://doi.org/10.7554/eLife.97330.3.sa1)

This manuscript presents a pipeline incorporating a deep generative model and peptide property predictors for the de novo design of peptide sequences with dual antimicrobial/antiviral functions. The authors synthesized and experimentally validated three peptides designed by the pipeline, demonstrating antimicrobial and antiviral activities, with one leading peptide exhibiting antimicrobial efficacy in animal models.

Overall, the authors have addressed each major comment through new experiments, particularly by validating 24 peptides, clarifying alignment methods, and demonstrating sequence novelty. These additions have strengthened the manuscript. To further refine the work, it would be helpful to briefly describe any steps taken to mitigate GAN pathologies (such as mode collapse), provide a short rationale for the use of five AVP classifiers and how they complement each other, and clearly present the expanded experimental data (including MIC values and antiviral results) in the main text. Finally, the authors should also compare their approach with recently described deep-learning-enabled antibiotic discovery methods.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97330.3.sa2](https://doi.org/10.7554/eLife.97330.3.sa2)

Summary:

This study marks a noteworthy advance in the targeted design of AMPs, leveraging a pioneering deep learning framework to generate potent bifunctional peptides with specificity against both bacteria and viruses. The introduction of a GAN for generation and a GCN-based AMPredictor for MIC predictions is methodologically robust and a major stride in computational biology. Experimental validation in vitro and in animal models, notably with the highly potent P076 against a multidrug-resistant bacterium and P002's broad-spectrum viral inhibition, underpins the strength of their evidence. The findings are significant, showcasing not just promising therapeutic candidates, but also demonstrating a replicable means to rapidly develop new antimicrobials against the threat of drug-resistant pathogens.

Strengths:

The de novo AMP design framework combines a generative adversarial network (GAN) with an AMP predictor (AMPredictor), which is a novel approach in the field. The integration of deep generative models and graph-encoding activity regressors for discovering bifunctional AMPs is cutting-edge and addresses the need for new antimicrobial agents against drug-resistant pathogens. The in vitro and in vivo experimental validations of the AMPs provide strong evidence to support the computational predictions. The successful inhibition of a spectrum of pathogens in vitro and in animal models gives credibility to the claims. The discovery of effective peptides, such as P076, which demonstrates potent bactericidal activity against multidrug-resistant A. baumannii with low cytotoxicity, is noteworthy. This could have far-reaching implications for addressing antibiotic resistance. The demonstrated activity of the peptides against both bacterial and viral pathogens suggests that the discovered AMPs have a wide therapeutic potential and could be effective against a range of pathogens.

Comments on revisions: I have no further comments on revisions.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97330.3.sa3](https://doi.org/10.7554/eLife.97330.3.sa3)

Summary:

Dong et al. described a deep learning-based framework of antimicrobial (AMP) generator and regressor to design and rank de novo antimicrobial peptides (AMPs). For generated AMPs, they predicted their minimum inhibitory concentration (MIC) using a model that combines the Morgan fingerprint, contact map and ESM language model. For their selected AMPs based on predicted MIC, they also use a combination of antiviral peptide (AVP) prediction models to select AMPs with potential antiviral activity. They experimentally validated 3 candidates for antimicrobial activity against S. aureus, A. baumannii, E. coli, and P. aeruginosa, and their toxicity on mouse blood and three human cell lines. The authors select their most promising AMP (P076) for in vivo experiments in A. baumannii-infected mice. They finally test the antiviral activity of their 3 AMPs against viruses.

Strengths:

- The development of de novo antimicrobial peptides (AMPs) with the novelty of being bifunctional (antimicrobial and antiviral activity).

- Novel, combined approach to AMP activity prediction from their amino acid sequence.

Weaknesses:

- I missed the justification for combined antiviral and antibacterial activities. As the authors responded, less than 10% of the training data has antiviral activity. Therefore, I do not understand how the high percentage of antiviral activities was achieved. Especially reading that the antiviral filtering did not have an influence on the number of antiviral peptides obtained.

- I had difficulty in reading the story because of the use of acronyms without referring to their full name for the first time, and incomplete information annotation in figures and captions.
