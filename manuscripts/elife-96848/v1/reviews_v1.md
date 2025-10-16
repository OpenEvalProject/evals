# Peer review - Round 1

Editors:
- John R Huguenard, Stanford University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.96848.3.sa0](https://doi.org/10.7554/eLife.96848.3.sa0)

Hou and colleagues describe the the use of a previously characterized FRET sensor for use in determining γ-secretase activity in the brain of living mice. In an approach that targeted the sensor to neurons, they observe patterns of fluorescent sensor readout suggesting clustered regions of secretase activity. These results once validated would be valuable in the field of Alzheimer's Disease research, yet further validation of the approach is required, as the current evidence provided is inadequate to support the conclusions.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96848.3.sa1](https://doi.org/10.7554/eLife.96848.3.sa1)

Summary:

In their paper, Hou and co-workers explored the use of a FRET sensor for endogenous g-sec activity in vivo in the mouse brain. They used AAV to deliver the sensor to the brain for neuron specific expression and applied NIR in cranial windows to assess FRET activity; optimizing as well an imaging and segmentation protocol. In brief they observe clustered g-sec activity in neighboring cells arguing for a cell non-autonomous regulation of endogenous g-sec activity in vivo.

Strengths:

Mone.

Weaknesses:

Overall the authors provide a very limited data set and in fact only a proof of concept that their sensor can be applied in vivo. This is not really a research paper, but a technical note. With respect to their observation of clustered activity, they now provide an overview image, next to zoomed details. However, from these images one cannot conclude 'by eye' any clustering event. This aligns with the very low r values. All neurons in the field show variable activity and a clustering is not really evident from these examples. Even within a cluster, there is variability. The authors now confirm that expression levels are indeed variable but are independent from the ratio measurements. Further, they controlled for specificity by including DAPT treatments, but opposite to their own in vitro data (in primary neurons) the ratios increased. The authors argue that both distance and orientation can either decrease or increase ratios and that the use of this biosensor should be explored model-by-model. This doesn't really confer high confidence and may hinder other groups in using this sensor reliably.

Secondly, there is still no physiological relevance for this observation. The experiments are performed in wild-type mice, but it would be more relevant to compare this with a fadPSEN1 KI or a PSEN1cKO model to investigate the contribution of a gain of toxic function or LOF to the claimed cell non-autonomous activations. The authors acknowledge this shortcoming but argue that this is for a follow-up study.

For instance, they only monitor activity in cell bodies, and miss all info on g-sec activity in neurites and synapses: what is the relevance of the cell body associated g-sec and can it be used as a proxy for neuronal g-sec activity? If cells 'communicate' g-sec activities, I would expect to see hot spots of activity at synapses between neurons.

Without some more validation and physiologically relevant studies, it remains a single observation and rather a technical note paper, instead of a true research paper.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96848.3.sa2](https://doi.org/10.7554/eLife.96848.3.sa2)

Summary:

The manuscript by Hou et al is a short technical report which details the potential use of a recently developed FRET based biosensor for gamma-secretase activity (Houser et al 2020) for in vivo imaging in the mouse brain. Gamma-secretase plays a crucial role in Alzheimer's disease pathology and therefore developing methodologies for precise in vivo measurements would be highly valuable to better understand AD pathophysiology in animal models.

The current version of the sensor utilizes a pair of far-red fluorescent proteins fused to a substrate of the enzyme. Using live imaging, it was previously demonstrated it is possible to monitor gamma-secretase activity in cultured cells. Notably, this is a variant of a biosensor that was previously described using CFP-YFP variants FRET pair (Maesako et al, iScience. 2020). The main claim and hypothesis for the manuscript is that IR excitation and emission has considerable advantages in terms of depth of penetration, as well as reduction in autofluorescence. These properties would make this approach potentially suitable to monitor cellular level dynamics of Gama-secretase in vivo.

The authors use confocal microscopy and show it is possible to detect fluorescence from single cortical cells. The paper described in detail technical information regarding imaging and analysis. The data presented details analysis of FRET ratio (FR) measurements within populations of cells. The authors claim it is possible to obtain reliable measurements at the level of individual cells. They compare the FR values across cells and mice and find a spatial correlation among neighboring cells. This is compared with data obtained after inhibition of endogenous gamma-secretase activity, which abolishes this correlation.

Strengths:

The authors describe in detail their experimental design and analysis for in vivo imaging of the reporter. The idea of using a far-red FRET sensor for in vivo imaging is novel and potentially useful to circumvent many of the pitfalls associated with intensity-based FRET imaging in complex biological environments (such as autofluorescence and scattering).

Weaknesses:

There are several critical points regarding the validation of this approach:

(1) Regarding the variability and spatial correlation- the dynamic range of the sensor previously reported in vitro is in the range of 20-30% change (Houser et al 2020) whereas the range of FR detected in vivo is between cells is significantly larger in this MS. This raises considerable doubts for specific detection of cellular activity

(2) One direct way to test the dynamic range of the sensor in vivo, is to increase or decrease endogenous gamma-secretase activity and to ensure this experimental design allows to accurately monitor gamma-secretase activity. In the previous characterization of the reporter (Hauser et al 2020), DAPT application and inhibition of gamma-secretase activity results in increased FR (Figures 2 and 3 of Houser et al). This is in agreement with the design of the biosensor, since FR should be inversely correlated with enzymatic activity. Here, the authors repeated the experiment, and surprisingly found an opposite effect, in which DAPT significantly reduced FR.

The authors maintain that this result could be due to differences in cell-types, However, this experiment was previously performed in cultures cortical neurons and many different cell types, as noted by the authors in their rebuttal.

Instead, I would argue that these results further highlight the concerns of using FR in vivo, since based on their own data, there is no way to interpret this quantification. If DAPT reduces FR, does this mean we should now interpret the results of higher FR corresponds to higher g-sec activity? Given a number of papers from the authors claiming otherwise, I do not understand how one can interpret the results as indicating a cell-specific effect.

In conclusion, without any ground truth, it is impossible to assess and interpret what FR measurements of this sensor in vivo mean. Therefore, the use of this approach as a way to study g-sec activity in vivo seems premature.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96848.3.sa3](https://doi.org/10.7554/eLife.96848.3.sa3)

This paper builds on the authors' original development of a near infrared (NIR) FRET sensor by reporting in vivo real-time measurements for gamma-secretase activity in the mouse cortex. The in vivo application of the sensor using state-of-the-art techniques is supported by a clear description and straightforward data, and the project represents significant progress because so few biosensors work in vivo. Notably, the NIR biosensor is detectable to ~ 100 µm depth in the cortex. A minor limitation is that this sensor has a relatively modest ΔF as reported in Houser et al, which is an additional challenge for its use in vivo. Thus, the data is fully dependent on post-capture processing and computational analyses. This can unintentionally introduce biases but is not an insurmountable issue with the proper controls that the authors have performed here.

The following opportunity for improving the system didn't initially present itself until the authors performed an important test of the FRET sensor in vivo following DAPT treatment. The authors get credit for diligently reporting the unexpected decrease in 720/670 FRET ratio. In turn this has led to a suggestion that this sensor would benefit from a control that is insensitive to gamma-secretase activity. FRET influences that are independent of gamma-secretase activity could be distinguished by this control.

From previous results in cultured neurons, the authors expected an increase in FRET following DAPT treatment in vivo. These expectations fit with the sensor's mode-of-action because a block of gamma-secretase activity should retain the fluorophores in proximity. When the authors observed decreased FRET, the conclusion was that the sensor performs differently in different cellular contexts. However, a major concern is that mechanistically it is unclear how this could occur with this type of sensor. The relative orientation of fluorophores indeed can contribute to FRET efficiency in tension-based sensors. However, the proteolysis expected with gamma-secretase activity would release tension and orientation constraints. Thus, the major contributing FRET factor is expected to be distance, not orientation. Alternative possibilities that could inadvertently affect readouts include an additional DAPT target in vivo sequestering the inhibitor, secondary pH effects on FRET, photo-bleaching, or an unidentified fluorophore quencher in vivo stimulated by DAPT. Ultimately this new FRET sensor would benefit from a control that is insensitive to gamma-secretase activity. FRET influences that are independent of gamma-secretase activity could be distinguished by this control.
