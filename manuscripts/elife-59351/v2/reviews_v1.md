# Peer review - Round 1

Editors:
- Patricia J Wittkopp, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59351.sa1](https://doi.org/10.7554/eLife.59351.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study uses creative approaches to examine sources of gene expression noise and the relationships among shadow enhancers in Drosophila embryos. A novel live imaging strategy is used to track expression of allele-specific expression that, combined with careful genetic analysis and manipulation of transcription factor levels, shows how the distinct regulation of different shadow enhancers reduces expression noise compared to identical copies of enhancers. Consequently, this work advances our understanding of how enhancers with largely overlapping functions interact and how variation in transcription factors relates to gene expression noise.

Decision letter after peer review:

Thank you for choosing to send your work, "Shadow enhancers suppress input transcription factor noise through distinct regulatory logic", for consideration at eLife.

All three reviewers found the premise of this work exciting and novel, with intriguing functional data. They also all appreciated the modeling work. However, they were also in unanimous agreement that additional experimental work is needed to elevate the impact of this work on the field to the level expected for publication in this particular journal. Because this work is expected to take longer than the typical 2 month revision timeline for eLife, I am rejecting this work, but encouraging resubmission of a version that addresses the issues raised. As one reviewer wrote during our discussion " It was frustrating to see great data, ideas, and analyses that were not critically tested." The reviewers' full comments are below.

The post-review discussion highlighted the following points as most critical:

1) Addressing the technical concerns raised in the reviews and clarifying methods. As one reviewer wrote "it's extremely hard to judge the quality of the current results (even in the Materials and methods)".

2) At a minimum, use smFISH to confirm the live imaging results/model predictions. Better would be to more directly measure fluctuations of input TFs (e.g., HaloTags or LlamaTags).

3) Functional data testing arguments emerging from the model. Specifically, analyzing enhancers with specific TF binding sites mutated/deleted and examining the impact of manipulating TFs were suggested as ways to further test the credibility of the conclusions presented.

Please note that we aim to publish articles with a single round of revision that would typically be accomplished within two months. This means that work that has potential, but in our judgment would need extensive additional work, will not be considered for in-depth review. We do not intend any criticism of the quality of the data or the rigor of the science. We wish you good luck with your work and we hope you will consider eLife for future submissions.

Reviewer #1:

In this manuscript, Waymack et al. investigate the control of transcriptional dynamics of the gap gene Kruppel in the Drosophila embryo via two independent shadow enhancers. I like the main experiment in Figure 1 and I think the results are clear. Measuring expression from two identical alleles shows higher correlation than when two different enhancers are used, suggesting A) the factors that provide input into each enhancer may be different, and B) that variations in local concentrations of upstream activators and repressors play a role in transcriptional activation/dynamics. All in one shot.

Presumably properties of the traces from each locus in the heterozygote could be used to predict whether expression from a particular site of transcription was driven by the proximal or distal enhancer. It might have been nice to use two different reporters (MS2 vs. PP7) to label the two alleles independently and unambiguously, but this would have required additional constructs and controls and I think the results should be basically the same. This is an elegant experiment using existing tools.

They go on to examine the amount of noise created by input transcription factor fluctuations using a largely modeling-based approach. This is one of the central claims of the paper, though the coefficient of variation is only very slightly improved. Though I'm not able to fully evaluate the model, the idea does make sense; if noise in activator A is independent from noise in activator B, under certain regimes one input and therefore output will remain accurate despite a certain amount of variability. It is nice to formalize this in a model and find it to be true at least some of the time. Importantly, results in Figure 3 begin to test their initial model and they find that identical pairs of enhancers together in the same construct do not buffer noise as well as a heterologous shadow enhancer pair. Doubling the number of enhancers does not reduce noise if the enhancers rely on the same inputs.

What I would have liked to see is additional experimental tests. 1) It would be great to know whether the upstream inputs do indeed differ, and if changing their contributions would modify the system in a predictable way based on the models. 2) It would be great to measure an upstream input directly and determine whether its fluctuations correlate with the observed output.

For 1): A main conclusion is that each enhancer has different inputs, which is suggested by the observed correlation between identical alleles but which breaks down comparing across alleles. Each enhancer is likely to share some inputs while others may vary; they are after all quite similar spatial patterns. These potential inputs are discussed only minimally and the authors do not attempt to test what they might be. Zld, Bcd, Hb, and Stat – all their predicted inputs – have nicely characterized binding sites. I would have liked to see a small number of constructs in which potential input factor binding sites have been mutagenized or added. This may reduce (or increase) expression levels or patterns, but the remaining pattern could be evaluated for dynamics and correlation. Zld binding sites, for instance, can often be removed without removing the pattern but with changes to expression dynamics. Or, Zld sites could be added to an enhancer missing them to make the enhancer pair more similar.

For 2): New methods are available to visualize protein live and compare it directly to RNA output. Since a major claim of the paper depends on variability of upstream input it would be fantastic to measure an input relative to output and see if that also fits the predictions about variability and noise, and to measure output using either identical or different enhancers. It is possible that fluctuations in local chromatin state, for example, or local changes in topology create noise and not TF concentrations. Measuring TFs directly would allow for direct attribution (or not!). This may be beyond the current scope, but this would have been a way to add impact and reinforce the central claims of the manuscript.

Overall the manuscript is a bit light on experimental data and does not attempt to validate their models or predictions other than fitting the original data, then testing pairs of the same enhancers. Seeing similar effects for a second gene would help, but 1) and/or 2) above would be even better. That said, I like the direction of the work and the data from Figure 1. Given the reluctance of eLife to recommend additional experiments and that reviewers should evaluate the work as it stands, I do like the manuscript, and I think the conclusions drawn are reasonably well supported by the data provided. I think stronger arguments could be made with additional experimental data. I am generally positive but a little on the fence on my recommendation and look forward to seeing what other reviewers think.

Reviewer #2:

In this manuscript, the authors interrogate the role of shadow enhancers. They use two apparently redundant enhancers of the Kr gene as a paradigm. They generated MS2<yellow transgenic reporters, driven either by the proximal or distal Kr enhancer, or a combination of both (referred to as shadow het or pair). The authors use an elegant approach to study the impact of fluctuations in TF inputs in single nuclei, by tracking biallelic transcription within a developmental pattern. By combining quantitative imaging with mathematical modeling, they show that a major function of the Kr shadow enhancers is to buffer transcriptional noise. This buffering is attributed to the natural variation in input regulators that is created by the presence of two separated enhancers.

To my knowledge, such in depth characterization of bi-allelic cross-correlation in transcriptional output has never been performed in vivo, and as such the results are novel and exciting. In particular, the question of noise buffering in an in vivo developmental context is fundamental and quantified in depth in this manuscript. However, I do have some concerns about the quantification methodology, in particular because the precise description underlying how this quantification was developed and the nature of its underlying assumptions is lacking. Moreover, given that noise buffering is among the key findings of the paper, I think that the authors should demonstrate it using an orthogonal approach. If the authors can address the major questions raised, I would recommend this work for publication.

General comments:

– Is there a particular reason to justify the usage of different transgenic lines for the allelic correlation aspect (Figure 1-2) and the noise quantification? It would be less confusing to quantify these two metrics using the same genetic paradigm.

In all figures:

• Dotted lines are too dim

• Error bars for experimental data should be added

• Numerical statistics (number of nuclei, number of videos) in each figure legend should be added instead of putting the information separately in Table 2.

To help understanding the similarities and distinctions of the two enhancers, the authors should provide a quantitative description of each enhancer alone, and the shadow heterozygote, in terms of

a) % of activation across A/P axis, with ideally still images at different time points in nc14 (and videos in supplemental data). This will clarify the mono- versus bi-allelic activation at the border of the pattern. This may help understand why measurements of the allelic correlation in the anterior most part of the embryo (20%-40% egg length) is only shown for “proximal”. Similarly, can the authors explain why the allelic correlation is measured at the posterior part only for “distal”? If this is due to the documented “shift” in Kr pattern (Jaeger 2004, El Sherif et al., 2016), the authors should comment on it.

b) Intensity profiles over time, at different positions of egg length (as in Scholes et al., 2019), and intensity per nucleus across the embryo length (similar to Bothma et al., 2014).

c) In the main text, the authors should be more explicit with the differential inputs: from the schematic in Figure 1, the distal enhancer seems to be regulated by the pioneer factor Zelda, while the proximal is not. Knowing that Zelda acts as a quantitative timer (Dufourt et al., 2018, Yamada et al., 2019), to what extent is noise buffering due to priming by a pioneer factor? Would the shadow pair still show low transcriptional noise in embryos depleted of maternal Zelda?

Allelic correlation:

To quantitatively compare the effect of each enhancer and the combined trans-heterozygote, they measure the correlation in allelic activity. This is the major result of Figure 1 and yet the authors don't explain clearly how they measure it. An explicative panel and a few sentences in the main text should help.

Moreover, they do not mention the presence of sister chromatids: if they observe transcription from duplicated sister chromatids, how does that affect the quantification analysis? Do they assume that replication occurs independently in both alleles? If so they should explicitly mention this.

Image analysis:

Does the procedure include an estimation of background intensities (free MCP-GFP), which varies substantially from embryo to embryo and within embryos? This is not mentioned in the Materials and methods.

Spot detection:

For each trace, how is the zero determined? This should be mentioned in the text.

Is spot detection performed in 2D (max projected Z-stacks) or in 3D?

Bursting:

The description of the burst calling algorithm is absent. If burst calling is arbitraty/manually determined, this should be clearly stated. This point is not critical for the results of this manuscript. However, authors should pay attention in clearly stating the assumptions for inferring promoter switching rates: indeed with a temporal resolution of 30 seconds, and without single molecule sensitivity, defining what is a clear “OFF” state (versus low activity below the threshold of detection) is difficult. Moreover in the Figure 5—figure supplement 1, can the author show raw traces instead of smoothened ones such as those depicted? The figure legend of this figure should be corrected: red circles should be the “on” promoters and not the black ones.

When comparing their model to the experimental data in Figure 1—figure supplement 2, error bars are present for the simulated data but absent from the experimental data. This should be corrected.

Calibration:

The authors mention Lammers et al. as the procedure they follow, but this paper is not referenced (and to my knowledge only deposited on Biorxiv, and thus has not been peer-reviewed). However Lammers at al. state clearly that their calibration procedure with the hb-MS2 transgene “should generalize to all measurements taken using the same microscope”.

Given that the authors use heterozygous MCP-GFP females (while Garcia et al., Lammers et al. use homozygous) and that imaging settings/laser power etc varies dramatically from one lab to another, I am concerned about this calibration, although I agree that this factor may not dramatically alter the results of the manuscript.

However, to have another independent assay and avoid increasing uncertainty with multiple obscure calibration steps, I recommend performing single molecule FISH experiments on their transgenes. It would then be relatively straightforward to convert integrated MCP-GFP traces to absolute mRNA counts. If the authors end up with a similar calibration factor, this orthogonal method will strengthen their conclusion. Moreover, single molecule experiments could be used to examine the effect of the two Kr enhancers on the variability of mRNA production (see below).

Quantification of noise:

The formula of the CV is wrong and is the opposite of what is described in the main text.

Figure 3: can the author explain how they found a 15% difference in CV for the shadow pair compared to the 2x distal transgene. Was this calculated at a particular %egg length?

Can the author discuss why the shadow pair does not demonstrate any minimal noise beyond 60% egg length? A similar trend is observed with the simulated data (Figure 4C).

These results suggest that the shadow enhancer pair buffers noise, but only under certain circumstances and only by a 15% difference. Thus, the authors should dampen their conclusions to better reflect the data presented.

A major finding of this manuscript is noise buffering is accomplished at least in part by the presence of shadow enhancers. Yet transcriptional noise is measured with only one approach, live imaging, from which image analysis part is critical and not well-described here. Therefore, the authors should confirm the observed differences in transcriptional noise with an orthogonal approach such as single molecule FISH, as performed in Little et al., 2013 or Boettiger, 2013. By assessing the production of each “pseudo-cell” in nc14 or alternatively within a “column” of nuclei at a given position of the A/P axis, the authors could then assess how variable is the production of mRNA in each of the genotypes. These experiments would also permit to discuss the effect of spatial and temporal averaging as mentioned by the authors.

Reviewer #3:

In their manuscript, "Shadow enhancers suppress input transcription factor noise through distinct regulatory logic," Waymack and colleagues explore how shadow enhancers drive consistent expression levels by buffering upstream noise through a separation of transcription factor inputs at individual enhancers. By measuring the transcriptional dynamics of several Kruppel shadow enhancer configurations in live Drosophila embryos, show that enhancers act largely independently. The authors suggest that TF fluctuations are an appreciable source of noise that the shadow enhancer pair can better buffer than duplicated enhancers. The authors demonstrate that shadow enhancer pairs are uniquely able to maintain low levels of expression noise across a wide range of temperatures. Finally, a stochastic model supports their conclusion that the separation of TF inputs is enough to explain these findings.

Overall, this was a great paper and is exploring an important question in the field. It is well controlled with thoughtful experiments and modeling.

That said, I have some suggestions that could help the authors solidify their conclusions. Namely, one of the main conclusions is that TF fluctuations are the main source of noise that is suppressed by enhancers with different inputs. The authors go on to explore how shadow enhancers suppress noise across a wide range of temperatures. However, this does not test the effects of TF fluctuations and how they impact transcription directly. It would be great if they could test this though perturbations at either binding sites in the enhancers, or better still, through transient increases or decreases in the varying TF inputs. This could be done, for example, by noisy promoters driving the TFs in early embryos (HS::Hb or another variant), or by playing with copy number, etc. The authors could also image the distribution of the factors around the sites of transcription (Tsai et al., 2017, 2019). Again, this would explore how TF fluctuations impact shadow enhancers in a more direct way.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Shadow enhancers can suppress input transcription factor noise through distinct regulatory logic" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Patricia Wittkopp as the Senior and Reviewing Editor. The following individual involved in review of your submission has agreed to reveal their identity: Justin Crocker (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This study uses creative approaches to examine sources of gene expression noise. As reviewers wrote: The quantification of noise in a multicellular organism with live imaging is very elegant and has, to my knowledge, never been performed by this bi-allelic approach in Drosophila embryos. The Kr system with its set of two types of enhancers is very well adapted to the question. GFP-tagged Bcd was also used to measure Bicoid fluctuations and enhancer activity (shadow pair or distal enhancer) in the same nucleus, which showed that changes in the activity of the shadow pair were less correlated with Bcd levels than changes in the activity of the distal enhancer.

Overall, the reviewers were very pleased with the revisions and new data added directly visualizing transcription factor input alongside mRNA response. They were also all enthusiastic about this work being suitable for eLife. One reviewer, however, had some reservations about Bcd experiment and thus strength of one element of the conclusions. I've included this reviewer’s concerns (which were supported by the other two reviewers during the discussion phase) below. I anticipate that these concerns can be addressed with only text revisions to moderate the strength of conclusions drawn in one part of the manuscript and to add missing information about the copy number of Bcd-GFP

Revisions:

I think the data presented in the manuscript strongly support the first part of the title : “Shadow enhancers can suppress input TF noise”. However, more experimental data are needed to support the conclusion that noise buffering is achieved via “distinct regulatory logic”.

I appreciate the efforts of the authors to quantify Bicoid fluctuations while assessing transcriptional output dictated by the distal enhancer or the shadow pair (new Figure 3). However, I think that these data should be interpreted with caution.

First, the quantification are performed in a 3Xbicoid background (unless the authors introduced Bcd-GFP in a Bcdnull background, but this is not mentioned). Thus, the statement that half the Bcd proteins were labeled would not be strictly rigourous. If indeed there are 3 copies of Bcd, the shape of the Bcd gradient might be affected. Moreover, I would expect that fluctuations in this TF activator would be higher if Bcd was solely produced by the transgene Bcd-GFP. If there are indeed only two copies of Bcd, this should be clarified in text.

Second and most importantly, knowing that Bcd nuclear distribution is not homogeneous (as alluded to in the Discussion) (Mir, 2017, Mir et al., 2018), Bcd concentration should have been measured at the Transcription Site, as performed in Tsai, 2017 or Yamada, 2018, not across the entire nucleus.

Additionally, the difference in the correlation of Bcd-MS2 between the two transgenes (shadow pair vs distal) presented in Figure 3F is relatively modest. This panel would benefit from the control proximal alone.

I understand that with the current pandemic, it is quite difficult to perform experiments. However, to claim that noise buffering is achieved via distinct responses to TF fluctuations, the paper would need more data (such as smFISH, imaging new transgenes with TF mutations, and perturbing TF concentrations with heterozygous mutants in trans).

Having said that, I believe that a re-written manuscript with less emphasis on the cause of noise buffering would be a of great value that clearly deserve publication in eLife. I would build the manuscript around the solid finding that shadow enhancers buffer noise and perhaps end the paper with the possible explanation of noise buffering (actual Figure 3 results revised, see comments above). This may also help to clarify the manuscript, as the text itself is highly complex and could be well-served by simplifying the structure to highlight a single key advance per sentence.
