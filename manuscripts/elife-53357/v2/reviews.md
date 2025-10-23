# Peer review - Round 1

Editors:
- Leon D Islas, Universidad Nacional Autónoma de México Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53357.sa1](https://doi.org/10.7554/eLife.53357.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript by White et al. describes a new statistical method for event detection in single-molecule biophysics. The performance of the new algorithm and workflow is higher than that of other well-established methods of single-molecule statistical analysis when probed against the same benchmarks. This new methodology combines a new top-down segmentation approach with other well-established event detection methods to yield a procedure that should accelerate and facilitate parameter extraction from single-molecule experiments.

Decision letter after peer review:

Thank you for submitting your article "High-Throughput Single-Molecule Analysis via Divisive Segmentation and Clustering" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Leon D Islas as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Olga Boudker as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Fred Sigworth (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors present us with a manuscript describing a new method to carry out idealization and parameter estimation of single-molecule data. The method merges several good-performing algorithms to segment the data and find transitions between states and finally discover the most probable number of states giving rise to the data. Importantly, they compare the performance of their DISC algorithm to other two well established methods and discover that DISC is faster and perhaps more accurate in certain experimental conditions.

The reviewers agree the DISC method is an important contribution to the arsenal of single-molecule trajectories analysis methods and the authors have provided a good characterization of its performance. The paper has merits and the method is an important contribution to the field, however, there are a number of important comments that were raised that need to be dealt with by the authors.

Essential revisions:

The paper needs to be rewritten in a manner that enough formal description of the method is given to allow the target readership (SM experimentalists, presumably) to understand how it works and what exactly it does. As it is, the paper reads more like an "advertisement" of an algorithm described in detail elsewhere.

1) The new Divisive Segmentation (DS) algorithm is described in general terms in the text but a formal description is not provided. A reasonable description of the CP analysis portion of DS is provided in Supplemental Note 2 (though a suitable pointer to this from the main text is not given). In the text you then note that you employ a modified k-means algorithm. The reader asks, what is the modification? The citations are unhelpful. Finally, the HAC part is also fairly well described in Supplemental Note 3. But the heart of the DS algorithm does not receive a similarly formal description. A similar problem arises with the mention of the Viterbi algorithm. We are told that you "use" it, but the only references are to the ion-channel and speech-recognition literature. Beside not explaining briefly what it does (for the naive reader's benefit), you do not explain what emission probability densities you use, nor how you set transition probabilities.

2) A question that arises regarding assumptions and parameters: how well does the DS/HSC perform for traces with rarely-visited states? Your selection of total fraction bound > 0.5 (subsection “Trace selection and analysis of binding activity”) suggests that your approach might be best for situations where the various states are roughly equi-probable. An important point to check is the performance of DISC as a function of the kinetics of the underlying process. How well does DISC estimates the number of states for fast kinetics, with a small number of data points in each state (short dwell-times)? One of the goals of single-molecule analysis is the determination not only of the most probable number of states, but also the dwell-times in each state and the transition rates between them. Was an effort made to include dwell-time estimation in DISC?

3) The authors need to be careful using the term high throughput as this means different things to different scientific fields. For instance, high throughput drug discovery often means looking at millions of compounds. Certainly 4000 molecules is relatively high throughput compared to a handful, but even the earliest single-molecule fluorescence papers included a hundred traces, so does a 40x increase justify the semantic transition to high throughput?

4) As authors show in the assessment of simulated traces in Figure 3, none of the methods compared work in a meaningful way when looking at SNR less than or equal to 3. The data simulated in the manuscript appears to be >10:1 according to a first approximation. So none of the methods assessed does a meaningful job revealing the 'true' number of states even when the data appear to be very good.

5) In the Introduction and Discussion sections, the authors downplay the general usefulness of existing Markov modeling methods. This is unfortunately misleading. The value of Markov modeling for time-series data analysis is proven in the extensive literature across a large number of fields using a variety of experimental approaches. While recent advancements in data throughput (e.g., sCMOS cameras) have put pressure on these algorithms to be efficient, this is a relatively minor problem that can be overcome by better implementations. Related to the above, Supplementary Note 1 includes a great deal of important introductory information that does a better job of placing DISC into the context of existing methods. This information belongs in the main text to substantively review the subject matter.

6) Given that the authors know (or should reasonably expect) that their experimental system has exactly five states, how does their "model free" approach compare to a traditional, model-based approach with a reasonable starting state (for example using SKM or any of the many HMM algorithms implemented in QuB, SPARTAN, or SMART)? This is important to justify the method being widely valuable, rather than just an incrementally better change-point algorithm.

7) The manuscript is lacking algorithm and implementation details. For example, the authors claim to use the Viterbi algorithm for idealization of time traces using the output of DISC, but the details of this step are never described. Looking at the code, it appears that the authors actually implemented the segmental k-means algorithm (SKM; Qin, 2004) using the state sequence from DISC as the input for the first iteration. SKM iteratively runs the Viterbi algorithm to identify the optimal state sequence followed by re-estimation of model parameters using this state sequence. Strictly speaking DISC does use Viterbi, but the description in the manuscript is not as novel as would appear. This is a critical point because it suggests that DISC just implements an existing, widely-used approach (SKM), and only differs in that it provides a means to initialize the starting model. If this is the case, it should simple be stated in this way. If this is not the case, then further clarity is definitely needed.

8) The SNR of the simulated traces in Figure 2A and Figure 3B seem to be far higher than specified. The most meaningful SNR, as it's usually defined, is the fluorescence intensity relative to the standard deviation of fluorescence background noise (or noise within the signal, if it is static). Correspondingly, SNR is a measure of experimental noise and is independent of the interpretation of the data. The authors instead define SNR in an unusual way that measures the noise in the signal relative to the separation between states (see Equation 2 in the Materials and methods). This may be a valuable metric, but it should not be called SNR. This is very misleading for the field. As used, it is also problematic because it has a circular dependence on the interpretation of the data.

9) In the system that was used to demonstrate the power of the DISC method the authors select for high SNR data and they know that there are five states. The question they sought to answer was whether or not the data exhibited random or cooperative transitions between states, hence, it is not clear that the data even needed to be idealized to assess this question. Gaussian fitting can be used to define the number of states – particularly when the SNR is this high; the idealization thus only provides access to kinetic information, which the authors do not appear as interested in. Hence, the biological question that appears to be of interest relates to the question of cooperativity potentially arising from the transmembrane domains, and this would have been a good way to showcase the method, but this assessment is not included.

10) Some important performance benchmarks are not discussed in the manuscript. For example, how well does it deal with changing or drifting baselines? It is a common feature of fluorescence measurements to be affected by steady reduction in the average fluorescence (drift). This is sometimes also encountered in other type of single-molecule experiments. It would be important for the authors to comment on the performance of DISC under such circumstances.
