# Peer review - Round 1

Editors:
- Graham Coop, University of California, Davis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54967.sa1](https://doi.org/10.7554/eLife.54967.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Simulations have long been central to population genetics. Population genomics has, in turn, become central to numerous areas of evolutionary biology and human genetics, and a vast array of different statistical methods have been developed. However, these methods are rarely ground-truthed in any truly reproducible manner. This paper takes an important set of steps in developing a flexible framework to standardize testing of population genetics software.

Decision letter after peer review:

Thank you for submitting your article "A community-maintained standard library of population genetic models" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: John Novembre (Reviewer #1); Arun Sethuraman (Reviewer #2); Sara Mathieson (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Simulations have long been central to population genetics. Population genomics has, in turn, become central to numerous areas of evolutionary biology and human genetics, and a vast array of different statistical methods have been developed. However, these methods are rarely ground-truthed in any truly reproducible manner. This paper takes an important set of steps in developing a flexible framework to standardize testing of population genetics software.

The reviewers' comments are all reasonably straight forward, often hit on similar points, and so most should be easily addressable. Please respond to each point in your response to reviews. In our online discussions with the reviewers three points came the fore:

1) Ensuring that the language about the models and parameters conveys the correct sense of uncertainty. Obviously the reviewers and the authors know that these just represent best guesses at the moment, but as this platform catches on we don't want these numbers and models to be seen as gospel.

2) We would like to see the SLIM integration demonstrated with an application that MsPrime doesn't cover. This could be, for example, a figure of the average value some summary statistics surrounding a selective under the human demographic model. The reviewers didn't want this to be a lot of work, e.g. it would be outside of the scope of the current paper to demonstrate the power of a range of selection methods. However, we felt that a simple demonstration of the functionality would substantially increase the scenarios easily available and imaginable by readers of the paper.

3) We felt that the Discussion would benefit from a discussion of the details not yet incorporated into the platform, e.g. sex-specific recombination, gene conversion, assembly error, structural variants etc. Such an addition might spur future development, and also give the authors an opportunity to discuss general ways forward on these issues.

4) We would be interested to see more of a discussion of the strengths and weakness of the various demographic inference methods.

Beyond testing methods, another major use axis that I can personally see for this platform is for empirical researchers to see whether patterns they see in their data are consistent with known demographic models. For example, demonstrating whether the frequency spectrum in larger samples lines up with previously inferred models. Having all of these models implemented in a central place will significantly lower the barrier of entry of empirical researchers into rigorous simulation frameworks.

Overall we are very excited to see this big move forward and welcome the authors' careful work in this important area.

Reviewer #1:

The manuscript describes a community effort to standardize population genetic simulations and it presents an example of the resource's utility for method's testing. This development answers a long-standing need in the population genetics community for greater standardization and ease-of-implementation of simulation protocols. As such, I expect it will be a well-used resource and it represents an important advance for the field's practices. From the test implementation included in the paper, it was remarkable to see how highly variable (and often poor) the performance of the demographic inference methods was, and those results add to the scientific contribution of this manuscript.

Some of the specific features that are nice about the work are the incorporation of inferred genetic maps where possible, the automated output of citation information, the use of long-term stable identifiers for models and genetic maps, and the outputting of provenance information in the tree sequence files.

1) Emphasize parameters are current best-guesses:

a) I am most worried about the fragility of the models over time and the misperception one might have that these models are "accurate" for a species. Genome assemblies change, recombination rates improve, mutation rates change, etc. I would like to see that uncertainty reflected more in the language used in the paper so that it's clear the catalog is a collection of inferred parameters that are subject to change over time. This is a subtle and cosmetic, but important I think. For example, "the library defines basic information about each species genome, including information about chromosome lengths, average mutation rates, and generation times." Yet, this is information we don't have – each of these parameters is actively under revision/discussion for even the best studied species. It would be great to hammer home these are all inferred values. (Also see sentence on "details on the physical organization of its genome"; the same comment applies, and an improvement might be something like "details on the physical organization of the latest reference genome assembled for the species").

b) On a related note, there is wording regarding ensuring "implemented models are accurate" – I think what is meant is that the "implemented models are faithful to the source publications from which they derive". As the second half of this paper makes clear, because of errors in inference, many of these models will not be accurate, in the sense of representing the true history of the species.

2) It would be wonderful to have a comments section for the models that would be either curated by a set of editors or crowd-sourced. I say this because overtime, models will proliferate, and some will come to be regarded as out-of-date. One can imagine those approaching the field afresh will be overwhelmed by the possible selections and possible implement models that become outdated. If the goal is standardization, how do we communicate that standards change? A comment system (or even star-rating system?) may be wise to implement now. Assuming it can be layered on top of the existing structure, it may be enough for this publication to note this as a future challenge that needs development/addressing.

3) In terms of the maturity of the examples developed for the initial release, I would have liked to see at least one simulation model with a selective sweep, one with background selection, and one with spatial stepping-stone structure. Each of these would be helpful test cases to implement to be sure that the existing catalog framework has the breadth/flexibility necessary to accommodate future use cases. I do not think this is a requirement for publication, but it would add great value to this initial release of the resource.

4) The approach of masking "low-recombination" portions of the chromosomes seems like an incomplete/indirect attempt to model the inherent limitations of sequencing to an "accessible" genome.

a) Shouldn't the approach instead be to drop "low complexity" regions (e.g., as defined by an excessive number of "N"'s in the reference, low mapability scores, or via tools like RepeatMasker?). This part of the pipeline seems open to refinement.

b) Are the "masks" a separate configuration file for the simulations? It seems that it would be preferable for them to be separate from the recombination rate files – right now it reads as if the mask applied is a function of the genetic map file, but this seems too inflexible for users who prefer an alternative approach to masking.

Reviewer #2:

The authors in this manuscript describe the implementation of a publicly curated, open source simulation package called stdpopsim – equipped with commonly utilized population genetic demographic models in humans, Drosophila melanogaster, and Arabidopsis thaliana. I am in awe of what these authors have achieved, in terms of benchmarking these standard models in an effort to avoid duplication of effort, and possibility of erroneous inference. The package is currently equipped with several "in-built" models that allow the simulation of trees with msprime and SLiM. The authors explain the application of these models by simulating and benchmarking estimates of Ne under a couple of scenarios. The manuscript is also well written, and use popular tools like dadi and smc++ to estimate and benchmark the simulations under a variety of models. Across all simulated scenarios (except under more complex models), the simulations seem relatively accurate.

Despite a little hiccup with python version mismatch prior to me successfully installing stdpopsim, I was able to successfully get the tutorials running within minutes after. I have one recommendation however for the tutorials – it would definitely help if the CLI versus python tutorials were kept separate. I found it a little confusing since they are all listed on the same page (https://stdpopsim.readthedocs.io/en/latest/tutorial.html). The simulations, testing models, calculating divergences, plotting ran without a hitch, and I am impressed and excited to play around with more models in coming days. Having also developed similar libraries/pipelines, I have also found it extremely useful for developers to provide some more detailed documentation/tutorials via Jupyter notebooks, or some similar platform. I did however notice that the authors have provided their analyses as Snakemake files in the interest of replication. I did not replicate their analyses, but I trust that the documentation for these analyses are detailed enough to aid readers/users in establishing similar analysis pipelines for stdpopsim simulated data.

I thoroughly enjoyed reading this manuscript, and learning of all the new features that have been written into stdpopsim, and believe that this will be an invaluable contribution to the population genomics community.

Reviewer #3:

The authors present a standardized framework for creating reproducible population genetic simulations. This resource will allow researchers to create models for new species/scenarios, and easily compare methods on the same dataset. The authors are correct that the current state of benchmarking in population genetics causes inconsistency, duplicated effort, and confusion about the performance of different methods. The authors highlight that creating a realistic and meaningful simulation study is a barrier to entering this field, and I absolutely agree. I will be passing this resource on to my students and look forward to using it myself. Stdpopsim is a crucial step forward. The manuscript itself is well-written and describes an extensive comparison of demography methods in a variety of species/scenarios. I have a few comments.

1) The authors mention that SLiM can be used as an alternative backend, which would presumably allow for simulations with selection. Although I don't think an extensive comparison of selection methods is necessary for this paper, it would be ideal if the authors can give some idea of how this would work (example command line, etc). There are also a myriad of methods for detecting/quantifying selection, and these simulations are not consistent either.

2) I like the inclusion of the "zigzag" history, as well as generic piecewise constant models and IM models (subsection “The Species Catalog”). I wonder if these could be included in a separate section (not organism specific) in the documentation and software (and then in Table 1). Right now the zigzag model is under humans in the catalog.

3) In the subsection “Use case: comparing methods of demographic inference”, the authors set up notation for the number of replicates (R), number of chromosomes (C), and sample size (n), but don't seem to use it afterward (or use it inconsistently). It would be helpful if all the figure legends and main text included this notation (I am guessing the number of replicates is 3 based on the images, but this should be clarified). The authors use N in the Materials and methods (i.e. subsection “Workflow for analysis of simulated data”) to refer to population size (which makes sense), but then also say "In all cases we set the sample size of the focal population to N = 50 chromosomes." For MSMC, the sample size was set to n=2,8 which suggests haploid samples, but the "Calculating coalescence rates" section says that n is the diploid sample size.

4) "Calculating coalescence rates" section needs a read through. Reword first sentence and add some citations (especially regarding computing p(t) and p(z,t)). It was unclear to me how the "mean coalescence times" were used (the rate was used to compute the ground truth over time). This section is also referred to as the Appendix in the main text.
