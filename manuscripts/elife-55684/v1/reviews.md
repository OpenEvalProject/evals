# Peer review - Round 1

Editors:
- Michael Breakspear, QIMR Berghofer Medical Research Institute Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55684.sa1](https://doi.org/10.7554/eLife.55684.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper addresses circuit dysfunction in autism. In doing so, it nicely integrates computational (in silico) modelling with novel methods for the analysis of time series data, picking up on a recent thread on excitation-inhibition balance in neocortex. One very unique approach of the paper is the notion of a "behavioral camouflage" – that is, the ability mask social communicative difficulties through cognitive strategies: the authors find that a relatively intact E:I balance in medial prefrontal cortex may assist women with autism to recruit behavioural camouflage. This work obviously needs to be further nuanced with the various contributions of social gender roles, learning and cognitive strategies more broadly, as these pertain to persons with autism. This paper makes valuable contributions towards neurophysiological mechanisms of large-scale neurophysiological signals, the role of biophysical models in neuroscience, and our understanding of autism spectrum disorders.

Decision letter after peer review:

Thank you for submitting your article "Intrinsic excitation-inhibition imbalance affects medial prefrontal cortex differently in autistic men versus women" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Büchel as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Takamitsu Watanabe (Reviewer #1); Richard Gao (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This paper presents an impressive integration of in silico modelling, in-vivo rodent fMRI with chemogenetic manipulation and human fMRI. A number of key insights are advanced and integrated: the emerging and informative knowledge of time scale hierarchies in the brain; neurobiological and social aspects of autism spectrum disorder, including sex/gender considerations; and the role of computational models in linking micro- and macroscopic scales of investigation.

Revisions:

All three reviewers were impressed with the ambition and technical accuracy of the study. Their detailed technical suggestions are included below – all of which essentially request edits to the text (mainly Introduction and Discussion), more detailed appraisals of the data, and further visualizations. There are no new data acquisitions required and the additional analyses are suggested to improve the depth and quality of the presentation.

Reviewer 2 challenges the link between BOLD and LFPs versus spiking behaviour. Since the work of Logothetis and colleagues (and as confirmed subsequently), it is generally accepted that BOLD reflects broad spectrum LFP fluctuations more than spiking output, although this finding may be at times over-simplified. Therefore I suggest a brief discussion of this issue either in the Materials and methods (to justify the choice) or the Discussion (to acknowledge a partial limitation).

The reviewers' points are provided in full (because they are detailed and constructive), but where possible we will endeavour to rely on editorial discretion in appraising the revisions.

Reviewer #1:

In this work, the authors first demonstrated an association between E/I balance and Hurst component (H) by showing that [1] in a computational study, the Hurst component based on LFP was positively correlated with E/I balance, [2] also in-silico, the H based on BOLD signals was positively correlated with E/I balance –this part is predictable given prior work about the LFP-BOLD association – and [3] in vivo, the BOLD-based H was increased when neuronal excitability was enhanced.

Afterwards, they showed [4] MPFC was among human brain regions whose gene expression had both male-specific and autism-specific patterns, [5] in resting-state fMRI signals, a significant sex-diagnosis interaction effect was found in Hurst component in vMPFC and [6] only in the autistic female, the H was correlated with the camouflaging score.

Based on these observations, the authors claim that [A] Hurst component can be an index for the E/I balance and [B] the association between E/I balance and autism differs between sexes.

The theme (E/I balance, autism and sex difference) is important and each observation appears scientifically sound. In particular, the first half about the relationship between E/I balance and H (results [1]-[3] in above) is straight forward and looks solid. Relatively, the last half could be improved if the following concerns are addressed.

First, I think readers would like to know the spatial relationship between the MPFC found in the gene analysis and the vMPFC detected in the following rsfMRI analysis. In my understanding, if the authors want to say any link between sex-related genes and autism/sex-specific H changes, these two regions should be somewhat overlapped.

Second, I think readers would appreciate it if the authors supply some more information about associations between Hurst component in the vMFPC and behaviours/symptoms: at least, in both sexes, associations between H and symptom severity (total, social part and RRB component, respectively) in autistic individuals and those between H and AQ scores in both TD and autistic groups in both sexes. Such additional information would be quite helpful to re-interpret the function of the brain area in each sex and in TD and autism.

Reviewer #2:

In this study, Trakoshis, Martinez-Cañada and colleagues take a multi-scale approach to study how altered excitation-inhibition balance manifests in spectral features of the fMRI BOLD signal and apply it to study autism. Combining computational modeling of recurrent spiking neural networks, rodent chemogenetic experiments in-vivo, and sex- and autism-related gene expression in neuronal stem cells and post-mortem brain tissue, the authors relate changes in Hurst exponent (H) and 1/f exponent of the power spectrum to modulation of neuronal excitation specifically. With this link, they argue for a mechanistic interpretation of BOLD signal differences (in H) between autistic males and females, as well as the neural correlate of social camouflaging in females only.

The study is well-designed and logically presented, and I especially commend the multiscale approach that start with computational modeling to establish experimental hypotheses. Overall, I believe the paper is of quality and within the scope of eLife, as it integrates several levels of biology and thus appeals to a broad audience. Substantive concerns regarding modeling and analysis choices, as well as potentially problematic interpretations are listed below. I would recommend the manuscript for publication after those are addressed through additional analyses and writing changes, without collection of additional data.

Major comments:

1) I have two potential issues regarding the simulation of BOLD from LFP. First – and I do not claim domain expertise here whatsoever – it seems to me that BOLD should be simulated by convolving the HRF with the spiking output of the circuit, not the LFP. The LFP, as the authors note, is a combination of excitatory and inhibitory synaptic fluctuations. While taking the summation of the absolute value of those fluctuations will approximate local spiking, the latter is a true representation of the circuit's output, and is less affected by the strength of the inputs.

2) Second, and related, is that the authors draw attention to the frequency-dependent correlation between BOLD and LFP power, as correlation increases with frequency. But this pattern in correlation is essentially baked into the model itself, since a high-pass filter is applied after convolution with the HRF, imposing a higher correlation in higher frequencies. In addition, while this model partially recapitulates empirical data, it's also been shown that there is a negative correlation between LFP low-frequency power (e.g., α, 8-12 Hz) and BOLD (e.g., Mukamel et al., 2005). While it's good that the authors demonstrate changes in H to be unaltered by a conventional HRF-convolution model, I would like them to please comment on these two points, and whether the latter can be recapitulated in their model. If not, this is a good point of limitation to discuss.

3) When simulating the effect of DREADD silencing, do the neurons still spike at very low leak potentials? If not, then the LFP is effectively driven by the statistics of the cortical and thalamic inputs, which would represent a different circuit regime from the recurrent interactions enabled by higher leak potentials. While this does not change the conclusion of the study drastically, it would implicate the non-recurrent inputs to be the key factor in shaping H in this instance, which can alter the interpretation of the DREADD data.

4) A related point: the spiking network model represents some local circuit that receives cortical inputs. When simulating the effect of DREADD, only EL is changed, but not the cortical inputs. How realistic is this assumption? In other words, how local is the effect of DREADD on the resting state activity in the PFC? Additionally, while the authors show changes in H (or the lack thereof) in the two DREADD experiments, does absolute amplitude of BOLD fluctuations change in the expected directions, e.g., an increase with excitation and decrease with silencing?

5) The rat is anesthetized prior to chemogenetic manipulation, which already shifts E:I balance. Without collecting data from pre-anesthesia periods, it's hard to say what those changes in H are, and how they compare relative to the DREADD manipulation. But the authors should at least discuss this point, and I would even suggest trying to simulate the additional effect of anesthesia to see if there is an interaction with DREADD (though this is not necessary).

6) E:I is interpreted to be normal in autistic females (no difference in H between TD and ASD females), but there is significant covariation with behavior, which is one of the main findings of the study. However, this begs the question: how much variation in H can be attributed to "healthy behavior-modulated variation", and how much to pathology? In Figure 5B, it looks like the range in H in the female autism cohort straddles the TD and ASD male cohorts, with comparable standard deviation. On the other hand, H does not correlate with the degree of social camouflaging in the male ASD cohort, yet there is still significant variation in the amount of camouflaging they are capable of. Is there a separate mechanism at play for camouflaging in males then? How do the authors settle these two seemingly contradictory findings?

7) Subsection “Human fMRI data analysis” appears to state that the mean of the BOLD timeseries across voxel is taken first, from which H is computed. Doesn't it make more sense to compute H for each voxel and then average after? How different are these two situations? I don't have an intuition for how averaging timeseries affect H, but an analogous situation in spectral analysis is destructive interference, where two high-amplitude oscillations may combine to a flat signal due to a phase difference.

8) Another method question: why not fit PLS directly with the 2-column matrix (CF1 and CF2) directly, since PLS is capable of outputting a single explanatory component, instead of performing PCA first. They should be similar?

9) Similarly (and maybe I'm not understanding something here), why not fit PLS or mass univariate over the entire cortex for camouflaging as well, as the authors did to find spatial specificity for the sex*diagnosis contrast, instead of only regressing in vMPFC specifically?

10) Lastly, while I appreciate the ample reference to Gao et al., 2017, I suggest the authors check out Lombardi et al., 2017 as well, as they also look at how 1/f changes as a result of E:I shifts, but with a recurrent and interacting-E:I spiking model that is arguably more similar to the model in this manuscript. However, their finding is in contrast to Gao et al., 2017, where 1/f flattens for increasing inhibition. This is worth referencing and noting in the discussions.

Reviewer #3:

This is an impressive piece of work combining multi-level methods and different modalities using both mouse and human data that substantially enhances our understanding of E:I imbalance in autism. The authors demonstrate and extend the link between E:I balance and the Hurst component and 1/f slope in local field potentials and rsfMRI data using a biologically more plausible network model than prior work. They further establish the spatial distribution of autism-linked genes associated with excitation and androgen-sensitive genes that coincide with the sex-differential region associated with the H-component in the human rsfMRI data. Interestingly, this region also shows a sex-differential relationship to camouflaging behavior. This is an impressive set of analyses with elaborate and thorough methodological steps. Listed below are some minor comments that can help increase the clarity of the manuscript and interpretation of the results.

1) The authors start the Introduction with the sentence that E:I imbalance affects many disorders. This calls for at least a short mention in the Discussion how findings are specific to autism.

2) The Introduction lacks a bit of a red line to my taste. It would be clearer to read if sub-paragraphs were linked to each other. The different sections make sense – however it is left to the reader to link them to each other. Given the complexity and many aspects touched on, I think the flow of the Introduction could still be improved a bit.

3) Could authors explain in more details what “in silico” refers to in this context? This might not be clear to a broad readership.

4) How was mean frame-wise displacement calculated? Power? Jenkinson?

5) In Table 3, could authors also report differences in symptom scores and camouflaging between autistic males and females.

6) What is the justification for the use of PLS on top? What additional information is revealed?

7) A large part of the results is in mouse data. The Introduction should thus also include a section introducing how E:I imbalance can be investigated in animal models. Right now, the Introduction refers solely to human participants, whereas the entire first Result section does not.

8) Given the results first format, it should be pointed out briefly which dataset was used for which set of results. The first section should clearly state that this is done in the mouse data for example.

9) The sex-differential results in humans are intriguing. However, when looking at Figure 5B, I wonder whether a gender-incoherent pattern is evident here? Could authors further discuss this? Also, in line with this, I wonder whether authors could refine this part of the Discussion stating: "Thus, one potential explanation for the male-specific reduction of H in vMPFC could have to do with early developmental and androgen-sensitive upregulation of genes that play central roles in excitatory neuron cell types, and thus ultimately affecting downstream E:I imbalance. Such effects may be sex-differential and thus less critical in human females, serving an important basis of sex-differential human brain development and explaining the sex-based heterogeneity and qualitative sex differences of autism neurobiology in human." Do authors refer to typical females here? The results look like TD females show a similar pattern to autistic males. So how do authors explain the differential pattern in TD females and autistic females.

10) I like the link to the camouflaging behavior. However, the question arises whether there is also a sex-differential link to core autistic symptoms such as for example repetitive behaviors that have also been shown to differ across autistic males and females?

11) Could authors include information on the age range of autistic subjects (currently, I can't see the age range anywhere) and discuss the potential effect of age on their results from a neurodevelopmental perspective?
