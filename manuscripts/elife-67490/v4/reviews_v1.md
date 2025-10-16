# Peer review - Round 1

Editors:
- Emilio Salinas, Wake Forest School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67490.sa1](https://doi.org/10.7554/eLife.67490.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This article will be of interest to neurophysiologists interested in identifying different neuronal types from extracellular recordings, which is a difficult computational task. It describes novel data-driven methods for functionally dissociating circuits in the primate brain: using a combination of unsupervised dimensionality reduction techniques and clustering methods to categorize extracellular spike waveform profiles (the signatures of different neuronal types), the authors identified cell types with distinct functional and neurophysiological properties in a dataset collected from the premotor cortex of two macaques. The authors went to great lengths to validate their results with clear and informative visualizations, and to outline the capabilities and limitations of this promising cell identification technique.

Decision letter after peer review:

Thank you for submitting your article "Non-linear Dimensionality Reduction on Extracellular Waveforms Reveals Cell Type Diversity in Premotor Cortex" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

1) One potential weakness is the technical presentation of the new technique in the Supplementary information, which although complete, does not allow the targeted audience to create an intuition of it, or be able to replicate the analysis. Describing the Uniform Manifold Approximation and Projection (UMAP) idea to an audience not versed in topology and category theory is not easy. Yet the manuscript would increase its already significant impact if a small effort was put to describe UMAP both technically (as it is nicely done) and more intuitively (maybe with the help of a schematic or two). Including specific computer code would also make these methods more accessible.

2) The reviewers noted a few additional analyses that would provide further validation of the methods and a better sense of how they would generalize to other datasets. Please address the individual commentaries listed in their additional recommendations.

3) Reviewer 1 also raised a few questions that would benefit from clarification and refinement (in additional recommendations). Although not critical, addressing them would benefit the presentation and should be straightforward.

Reviewer #1:

1. When discussing hyperparameter optimization and gridsearch, is the entire dataset used in deriving the best values? The authors acknowledge the data-leakage in conducting cross-validation, which seems sound given the questions pursued in this paper; however, the hyperparameters themselves would also be a potential source of leakage and should be addressed/discussed (primarily for UMAP and Louvain, random forests with lesser importance).

2. The sentence "This algorithm is also fairly deterministic (after fixing a random seed) …" was confusing with the context of fixing a random seed. If it is deterministic, then one wouldn't need to fix the random seed, correct?

3. When conducting classification using random forests, do the authors utilize the normalized waveforms (i.e., same input going into WaveMAP of 1.4ms at 30 kHz; 42 samples or features)? An explicit mention of vector length would be helpful to the reader.

4. Are there any special considerations when applying UMAP to time-series data? The canonical examples of UMAP do not contain the autoregressive aspects of spiking waveforms and it might be worthwhile to mention the implications, if any, on the effectiveness of the method.

5. It is not clear how many models are being trained/tested for the generation of confusion matrices (e.g. Figure 2C). Are the binary classifiers trained to distinguish between data points from 1 vs other 7 clusters or are there different models for classification between each possible pair of clusters?

6. The authors indicate that normalization was conducted as a preprocessing step. Are there any concerns on whether normalization might be removing a potential feature that may factor into further classification between spikes? Is it a possibility that adding amplitudes would aid the clustering procedure (e.g., by including the scaling parameter for each spike as an additional feature at the end of the feature vector) or is there a methodological constraint that renders non-normalized amplitudes useless?

7. The authors addressed the issue of stability of WaveMAP, as it pertains to applying different seeds on the entire data as well as the robustness of the 8-cluster solution on varying sizes of data. My understanding is that the authors did not confirm whether those 8-cluster solutions were indeed similar (i.e. spikes clustered with neighboring spikes from the 100% dataset model) when varying data size. A third test is needed that takes a subset of the dataset (e.g., 80%; a subset that would still on average produce an 8-cluster solution) and tests whether the spikes would consistently cluster with their neighbors in the 100% data model. While this test is posthoc and the full data are still incorporated in the remainder of analysis in the paper, this might help to demonstrate the stability of the solution.

Reviewer #2:

1. The results rest a lot on appropriate spike sorting. Given that the probe used will not allow any of the 'triangulation' spike-sorting based methods to work (too spaced out electrodes), it would be useful for the authors to provide a bit more information (maybe in their Methods section) as to how spike-sorting was achieved. Spike selection description I find adequate, but describing the spike-sorting method as "inspection of extracellular waveforms and subsequent offline spike sorting (Plexon Offline Sorter)" doesn't really allow the reader to form a picture of the likelihood of having 'single units' that are not really single. Particularly, nothing is mentioned about thresholding of spikes. I am not suggesting a thorough description of the spike sorting method but some information on the techniques used (within the Offline sorter and/or anything else) and a report on the authors' confidence of the single units produced (and how such confidence was evaluated). I understand that the literature utilising the types of probes used by the authors is also most of the times vague as to what spike-sorting really means, yet in most cases the assignment of spikes to single units does not bare the same significance to the subsequent results as in the case of this work, hence the above argument for some more clarity on the matter.

2. A purported advantage of UMAP is that, in principle, it can deal with a very large number of features (better than t-SNE, which struggles with > 50 features or so). However, the technique is still new and this belief is largely anecdotal. It would be beneficial, to both the neuroscientific community and in general to anyone considering using UMAP, if the authors could make a comparison between using the raw data set in UMAP and using a dimensionality reduced one through PCA giving only the top PCs to UMAP. Practically provide some evidence to support your choice of using the raw data set. Also providing an idea of the "complexity" of the data set would be useful (maybe by mentioning the variance explained by different number of principal components after a PCA, even if you do not end up using the primary components generated).

3. The choice of the resolution parameter for the clustering algorithm (line 873 and Figure 2B) has rather important consequences in the subsequent analysis. The choice should be better justified.

a. The authors say they chose the resolution parameter at the elbow of the number of clusters, but that is not the case. The elbow point is the immediate next one (resolution of 2 and number of clusters probably 7).

b. The "number of clusters" value that was the most stable over the resolution is 5 (given resolutions between 3 and 5 if I read the graph properly), which might be another logical assumption for picking the used resolution.

c. So although the argument that choosing a smaller resolution leads to too many clusters with too few samples in them is a valid one, nonetheless there seems to be no real argument against choosing a resolution that would lead to a smaller number of clusters. Since this clustering impacts the whole of the subsequent analysis, it would be important to understand the authors' reasoning.

d. It would be interesting for example to see how a smaller number of WaveMAP generated clusters would fare in the learnability test shown by the authors (starting at line 188).

4. Comparison to t-SNE. This comment has been prompted by the phrase "While providing visualization, these methods are difficult to cluster upon because they return a different mapping on every initialization." (line 546). The authors provide reference 155 that actually directly contradicts this statement. Although the other comments about t-SNE and UMAP are valid (reverse mapping, and use of labels in training), I believe the first comment requires either removal or better further exploration. It would be very informative if the authors did a t-SNE embedding (on the data after PCA) and then used a DBSCAN to classify the cells. This would be rather straight forward to do at their data set size, even multiple times for different initialisations (but see Dimitriadis et al., 2018a for a GPU accelerated t-SNE algorithm and also for t-SNE and DBSCAN used in spike-sorting). That result can then also be contrasted to the WaveMAP and GMM methods using their random forest classifier. Even if the results from the t-SNE / DBSCAN clustering are comparative to WaveMAP the reverse mapping capability of UMAP is definitely a strength that is very nicely utilised in this work and which any other non-linear dimensionality reduction technique doesn't have. As a final point, in the comparison section the authors could also add that t-SNE is way slower than UMAP and this speed difference starts to be very obvious (minutes vs days) in sample sizes in the hundreds of thousands to millions (i.e. the regime of spike collection that high density probes collect Dimitriadis et al. 2018b and Steinmetz et al., 2018).

5. Number of waveform features used to classify the cells. The authors compare their WaveMAP to a seemingly standard technique in the macaque literature (or maybe in the literature that uses sparse electrode probes), that uses 3 features of the waveform to classify the cells. This is not the way things are done in most of the rodent electrophysiology (or works that use denser probes or tetrodes). The standard technique is to PCA each spike form and use the first 3 components per electrode. In the case of this work that would lead to the use of the same number of features, but (probably) much larger retention of information. See Harris et al., 2000 (and references therein) for how the PCA of the waveforms is used in tetrode recordings to do spike-sorting. More recent spike-sorting algorithms use template matching of the waveform. For instance, Kilosort (Pachitariu et al., 2016) omits spike detection and PCA, which can miss useful information. Instead, it relies on identifying template waveforms and their timing properties, in order to assign spikes (in the entirety of their waveform) to different cells. Also comparing the WaveMAP process to the clustering results (following the used Generalised Gaussian Models method, or other peak-density detection methods) of this feature set would be both more informative and more valid for the larger electrophysiology community.

1. Harris, K. D., Henze, D. A., Csicsvari, J., Hirase, H., and Buzsaki, G. (2000). Accuracy of tetrode spike separation as determined by simultaneous intracellular and extracellular measurements. Journal of neurophysiology, 84(1), 401-414.

2. Pachitariu, M., Steinmetz, N., Kadir, S., and Carandini, M. (2016). Kilosort: realtime spike-sorting for extracellular electrophysiology with hundreds of channels. BioRxiv, 061481.

3. Dimitriadis, G., Neto, J. P., and Kampff, A. R. (2018). T-SNE Visualization of Large-Scale Neural Recordings. Neural Computation, 30(7), 1750-1774. https://doi.org/10.1162/neco_a_01097

4. Dimitriadis, G., Neto, J. P., Aarts, A., Alexandru, A., Ballini, M., Battaglia, F., Calcaterra, L., David, F., Fiáth, R., Frazão, J., Geerts, J. P., Gentet, L. J., Helleputte, N. V., Holzhammer, T., Hoof, C. van, Horváth, D., Lopes, G., Lopez, C. M., Maris, E., … Kampff, A. R. (2018). Why not record from every channel with a CMOS scanning probe? BioRxiv, 275818. https://doi.org/10.1101/275818

5. Steinmetz, N. A., Zatka-Haas, P., Carandini, M., and Harris, K. D. (2018). Distributed correlates of visually-guided behavior across the mouse brain. BioRxiv, 474437. https://doi.org/10.1101/474437
