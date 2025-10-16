# Author response - Round 1

Authors:
- Prerna Srivastava ([ORCID: 0000-0002-3429-7039](https://orcid.org/0000-0002-3429-7039))
- Geoff de Rosenroll ([ORCID: 0000-0002-5431-2814](https://orcid.org/0000-0002-5431-2814))
- Akihiro Matsumoto
- Tracy Michaels
- Zachary Turple
- Varsha Jain
- Santhosh Sethuramanujam
- Benjamin L Murphy-Baum ([ORCID: 0000-0001-6746-3091](https://orcid.org/0000-0001-6746-3091))
- Keisuke Yonehara
- Gautam Bhagwan Awatramani ([ORCID: 0000-0002-0610-5271](https://orcid.org/0000-0002-0610-5271))

## Response text

DOI: [10.7554/eLife.81533.sa2](https://doi.org/10.7554/eLife.81533.sa2)

Reviewer #2 (Recommendations for the authors):

The BC7 and deconvolution experiments in Figures 3 and 5 are very nice, but they come across as a bit descriptive/anecdotal in the absence of analyzed pooled data.

We estimated the time-varying release rates by deconvolving the iGluSnFR signals (obtained by the experimental data) with the quantal signal. The release rates are pooled from the iGluSnFR experimental data and the comparisons with the Poisson trains are simply to represent that the estimated release rates can be used to generate the shape of the original iGluSnFR responses. To estimate the kinetics for our model BCs, we pooled data from 50 ROIs for proximal and distal sites (taken from, 6 retinas, 7 FOVs).

BC7 experiments were performed to bolster the idea that type 7 BCs are the primary source of sustained responses in the proximal dendritic region of SACs, which more effectively supports the ‘space-time’ wiring model.

Given the nature of the conclusions, it would seem appropriate to recognize in the Discussion Hassenstein and Reichardt (1956) and at least one of Barlow's papers on the subject.

Agreed! Thanks.

Reviewer #3 (Recommendations for the authors):

– In Suppl. Figure 2, the authors show that temporal response properties of type 7 bipolar cells do not change with signal to noise of the responses. They should also show the same analysis for the population data, together with the distribution of signal-to-noise ratios of proximal and distal ROIs. This will make sure that differences observed for proximal versus distal ROIs are unrelated to differences in response strength.

Agreed. The Sustained/transient index for proximal and distal ROIs is plotted against signal amplitude in Figure 3 —figure supplement 1. This plot shows that the kinetic properties are not confounded by signal-to-noise issues.

– The authors should provide more details in the Methods section regarding ROI detection, the rationale behind ROI sizes, and the fraction of ROIs that passed their threshold. In addition, I suggest not using the peak value, but instead a percentile for estimating the signal-to-noise ratio, as this is more robust against outliers.

In recent studies examining BC properties the spatial extent of ROIs has ranged from 5 µm (Franke et al., 2017) to ~50 µm (Gaynes et al., 2022). In most experiments we found using 10 µm x 10 µm or 5 x 5 µm ensured a large fraction of ROIs had SNR > 4. We found a weak relationship between response amplitude and kinetics (data now shown in Figure 3 —figure supplement 1). Since our estimates of iGluSnFR response kinetics did not appear to be seriously confounded by noise, we did not use the alternate method suggested by the Reviewer. We have described our methods more clearly in the text.

– In Figure 6C, the authors should indicate which velocities are significantly different between the two conditions.

We used a one-way ANOVA to demonstrate that there exists a group effect across all velocities i.e., changing the bipolar release profiles has a statistically significant effect. In the model data, subsequent pairwise comparisons at individual velocities are less informative and we simply state that the effects of BC kinetics dwindle at higher speeds (0.5 mm/s). For example, a statistically significant DS can be measured at all but the highest velocities for control conditions vs single BC input conditions, but above 500um/s this DS is tiny and less meaningful.

– The first sentence of the abstract reads like the space-time-wiring model is the main proposed mechanism underlying direction selectivity. I suggest the authors rephrase this sentence to illustrate that this is one of many, well-described other mechanisms.

We have now changed the text accordingly.

– In the Discussion section, the authors write: "Moreover, kinetic differences were discernable for stationary or slow-moving spots." I suggest rephrasing, as the slow-moving spot result was only predicted by their model.

We have changed the text as per the Reviewer’s suggestion.
