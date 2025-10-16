# Peer review - Round 1

Editors:
- Ihor Smal, https://ror.org/03r4m3349 Erasmus University Medical Center Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70169.sa0](https://doi.org/10.7554/eLife.70169.sa0)

This paper will be of interest to the cellular biologists who perform single-particle tracking experiments and develop new tracking methodologies. The authors investigate a new way of estimating an unknown number of diffusion states from short single-molecule trajectories. Ideas developed in the paper are likely to be used for further algorithm development. The authors give the users access to a repository on GitHub that contains comprehensive code that supports the paper.


---

# Peer review - Round 1

Editors:
- Ihor Smal, https://ror.org/03r4m3349 Erasmus University Medical Center Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70169.sa1](https://doi.org/10.7554/eLife.70169.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Recovering mixtures of fast diffusing states from short single particle trajectories" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Reviewing Editor and Anna Akhmanova as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Maarten Paul (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The authors are supposed to provide a point by point revision addressing the reviewers comments stated in this letter. The main directions for improvements can be summarized briefly as follows:

1) Rewriting or adding more information and explanations about the methodology, so it becomes accessible to a broader range of eLife readers.

2) Adding comparison with existing (alternative/similar) techniques mentioned by the reviewer as well as the case with non-Brownian motion.

3) Justifying the importance of the biologically relevant insights (see the reviewer’s comments) to fit the profile of the journal better.

Reviewer #1 (Recommendations for the authors):

The paper is well written and all the parts concerning the "regular" Brownian motion, as the authors also mention themselves, are validated with lots of experiments, covering all possible (parameter) dependencies. With the staring assumptions like that (the type of diffusion and the type of switching), it is difficult to ask for more. My concern is still about the applicability of these techniques to the data that contains anomalous diffusion. The typical experiments with H2B or any other protein binding events, where there is a switching between several types of motion, most of the time show that the "slow" components are always related to anomalous diffusion. In the typical cases, there are 2-3 components where only one most likely would correspond to the regular diffusion. With that respect, it would be interesting to know how the methods work (or break) with such data, for example in the simulations with 2-3 state fractional Brownian motions. The weakness that one can imagine is that the proposed techniques can distill the diffusion coefficients, but the bigger problem is that they cannot "split" the trajectories into the parts that correspond to those states with different parameter values. Such split is most of the time of a higher importance, because it allows for computation of residency times and other typical and intuitive parameters. Having the diffusion rates for the anomalous diffusion (which are only the "apparent" diffusion coefficients that do not have physical interpretation as clear as in the case of the regular Brownian motion). Also splitting trajectories in parts, according to different diffusion rates gives a possibility to create a spatial maps inside a cell/nucleus and observe, for example, where more transient binding is occurring. The attempt to present such type of information can be observed in Figure 5 but is it possible to compare these results with "more classical" approach (staring from SpotOn or any other techniques), that splits the trajectories into different parts, and see if the results produced by the proposed methods are unique and cannot be obtained otherwise. Splitting of the tracks with diffusion constants which are well separated (as in the paper) is not a big problem nowadays (see for example M. Arts, "Particle Mobility Analysis Using Deep Learning and the Moment Scaling Spectrum", or A. Vega "Multistep track segmentation and motion classification for transient mobility analysis"). Those already work better than simple MSD analysis that does not keep track on the order of displacements within a track.

Reviewer #2 (Recommendations for the authors):

1. Accuracy and precision are two different things. I would recommend that the authors look up the definition of accuracy (i.e. bias) and precision.

2. Introduction paragraph 3, "despite these advances several problems remain". This is very vague and I don't know what the authors tried to address with these advances. Please rephrase.

3. Introduction paragraph 3, "stroboscopic illumination", do the authors mean stroboscopic activation of excitation?

4. " but because camera integration times are never instantaneous, it cannot be removed entirely". Figure 1C should be supported with images from point spread functions (PSF) of real acquired single-molecules and histograms of intensity, background, and PSF width, which are related to the integration time of the camera to make this claim scientifically sound. Also for S1B, it would be easier to plot a 2D grid of pixels with a greyscale indicating the intensity (similar to Figure 1A, but zoomed-in). The paper misses too many details for their argumentation of the varying localization precision that the paper tries to address. This needs to be expanded so that the localization precision simulations match the reality.

5. The authors introduce a new acronym for sptPALM originally introduce in Manley, Nat. Meth, 2008. I don't see a reason for deviating from this.

6. The authors set out to address challenges by citing work from back in 2006 e.g. ref 19, 20. As the authors know a lot has happened since 2006, which should be discussed to describe an appropriate state-of-the-art. An example of this is the work from Linden Nat. Comm. 2017, which should be cited.

7. One of the major points of ref 30 is to be able to process short trajectories. Paragraph 4 suggests something else. Furthermore, a way to incorporate a changing localization precision over the field of view has been studied in the context of single-molecule kinetics Smith Nat. Com. 2019 and should be cited.

8. The paper contains a missing reference in figure S11 please correct it.

9. The authors introduce ref 30, but benchmark against much older ref 32. A comparison to the tracking methodology that was developed in the Elf lab would be useful for the general readership. The code is available on GitHub.

10. The authors make an approximation that is "strictly true when the localization precision is zero". When does this approximation break down, since this is not a valid assumption (e.g. Figure 1C)?

11. How does a user know from the output if they obtain discretization artifacts from SAs?

12. It would be useful if the authors could quantify the error in figure S2 i.e. add a graph with error vs the number of trajectories. Furthermore, it would be useful to see the impact of a broad distribution that realistically models a varying localization precision (see point 1).

13. Figure S6 shows two distinct diffusion states. My impression is that ref 30 would work on this perfectly fine. I recommend the authors to benchmark against this approach. It would be interesting two see a broad distribution of diffusion coefficients where ref 30 would fail. Here also it would be useful if the authors could quantify the error vs the number of trajectories.

14. Wouldn't it be easier to address defocalization using e.g. an astigmatic lens so that the z position can be estimated? Or would the varying localization precision still be a problem? It would be great if the authors could make this point in the discussion.

Reviewer #3 (Recommendations for the authors):

– The first paragraph of the results and first figure nicely describes single-molecule data as a mixture of molecules of different diffusive states and how image acquisition biases the results. In the second paragraph the authors present their new model and Bayesian approaches in a technical way. I think it would be useful at this point to explain their Bayesian approach in such a way that is easier to understand for biologists.

– Introduction; Page 3; "The central problem in spaSPT analysis…" I think it would be useful to add here that it is not only problem to recover the underlying set of dynamic states, but also the transitions between those states. Although this is not really the focus of this study I think it is a relevant aspect of single-particle tracking that should be considered.

– Figure 2A: It is difficult for me to understand these schemes. Possibly some additional description in the figure legend explaining the different terms would help.

– Figure 2C and D: It is unclear to me which of the two methods are used in these figures. A heading above the figures could possible clarify this.

– On page 6: paragraph "Performance of DPMMs and SAs on experimental spaSPT" here biological results are written clearly; however I do miss a description on the performance of (DPMMs and SAs) methods on the biological data and what new features are uncovered with their method.

– It seems to me that the SA method is most applicable for biological data as it considers variable localization error depending on the diffusion coefficient of the molecules, whereas the DPMM method work very well in simulations with known localization error, which is unfortunately is not very realistic in cellular experiments. Could the authors directly compare SA and DPMM for their biological dataset (Figure 4A) and discuss possible differences in the results.

– Could the authors indicate, other than possibly providing more accurate results, what new biological insights are revealed with their method, that are not possible to obtain with MSD analysis. Possibly the authors can compare their experimental results (Figure 4 and 5) to MSD and Spot-On analysis in terms of obtained diffusion rates and fraction of different states. It would be useful to know how big the differences would be, compared to these previous methods.

– The authors mention in the discussion that their methods do not work well with non-Brownian motion. In many cases however confined motion types are relevant to describe the motion of proteins in cells, possibly also for the proteins they analyzed. Could the authors discuss in more detail how serious this limitation is, taking into account the types of anomalous diffusion that has been observed for several proteins for example in the cell nucleus.

– Unfortunately the software code from the State Array method was not available at the presented website (https://gitlab.com/alecheckert/saspt/). It is to praise that the authors plan to publish all their code and source data on publication, but it would be nice to have access this software during review. I think it is important to assure that the software is user-friendly and also accessible for biologists.

– If I understand correctly the experiments described in Figure 4B are done with cells expressing the different variants of RARA-HT from an exogenous promotor either transiently or by making use of stable cell lines. It would be useful if the authors indicate in the legend that this is different from the experiment in Figure 4A where they made use of a CRISPR/Cas9 knock-in. Additionally could the authors indicate the number of technical (cells) and biological replicates from these experiments.

– Finally, the paper is written rather technically, requiring at least some knowledge of Bayesian statistics. I do think it would be useful if the paper would be carefully evaluated to be more accessible for a broad audience and avoid technical terms whenever possible.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Recovering mixtures of fast diffusing states from short single particle trajectories" for further consideration by eLife. Your revised article has been evaluated by Anna Akhmanova (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Essential revisions:

All the reviewers agree that the paper is well written and presents a very valuable data analysis technique but also that the paper has a very strong focus on rather complex and methodological developments, which might be far from the expertise of a general eLife reader.

We ask the authors to take into account the comments of Reviewer #4 who has several suggestions on how to improve the readability of the paper and also mentions other recent works presenting similar methods for single trajectory characterisation.

Reviewer #1 (Recommendations for the authors):

The authors revised the manuscript very elaborately, taking into account all the comments and adding useful supporting explanations and experiments. The paper is now in very good shape, and even though the description of the methodology is improved, it can still be a difficult read for a general reader of eLife, but it is difficult to simplify that even more because the underlying theory is indeed quite complex.

Reviewer #3 (Recommendations for the authors):

I think the revised manuscript has improved significantly and become a useful paper addressing important aspects of single-molecule tracking with useful novel analysis methods. The additional simulations will help potential users of these methods to assess the appropriate approach to analyze their SPT data.

I found one typo on line 106 varable-> variable

Reviewer #4 (Recommendations for the authors):

I find the current manuscript clear and concise, correctly presenting the method developed as well as a variety of examples of use. The text is easily understandable and presents the different concepts and sections in a very ordered way. Also, the extensive number of figures helps to understand the extent of the method and its applicability to different experimental setups. Note that I have no background in Biology, hence my review is focused on the method and its application to simulated and experimental trajectories, and not on the details of the experimental setup (e.g. lines 257-268 and related figures/supplementary material).

My main concern relates to the benchmark of the method, as I miss an objective evaluation of the accuracy of the method. For instance, while the plots presented in Figure 3A, Figure 4A,…etc give a nice visual understanding of the power of SA, they do not allow for a rigorous comparison and evaluation of the method. In that sense, the plots presented in Figure 4 – Supplement2 C and D give a much better understanding of the accuracy of the method. Being this a rather technical paper focusing on a new method, giving a concise numerical metric (e.g. the mean absolute error) may be of interest to the community. It may also help compare objectively with other methods.

Another point which I found hard to understand was if the method was working at the 'single trajectory' level or in an ensemble of trajectories. From what I understand from line 296, the authors can give a prediction for every trajectory separately. I think that is an important and valuable feature, and perhaps should be highlighted earlier in the text. In this sense, it may also be worth pointing out in the text other recent works presenting similar methods for single trajectory characterization. Indeed, while the approach is slightly different, Ref A also proposes the use of Bayesian inference for extracting diffusion properties from trajectories. The use of machine learning has also been prominent recently for this purpose (see Ref C and the references therein) and may be worth adding a comment in the text. Indeed, in the latter reference, there are some approaches to trajectory segmentation, which may complement one of the flaws of the method stated in the text: dealing with transitions between states within a trajectory.
