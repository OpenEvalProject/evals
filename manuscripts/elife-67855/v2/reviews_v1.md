# Peer review - Round 1

Editors:
- Jesse H Goldberg, Cornell University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67855.sa1](https://doi.org/10.7554/eLife.67855.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Animal vocalizations are notoriously complex and difficult to categorize. Traditionally, sounds are transformed into spectrograms, which are then segmented into syllables and analyzed according to hand-selected features such as pitch, amplitude and frequency modulation. Here, the authors take a new approach: they use variational autoencoders to analyze vocalizations from songbirds and mice and find that they can quantify the similarity between distinct utterances. This approach will complement existing sound analysis methods to further our understanding of animal social behavior.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Low-dimensional learned feature spaces quantify individual and group differences in vocal repertoires" for consideration by eLife. Your article has been reviewed by 4 peer reviewers, including Jesse H Goldberg as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Ofer Tchernichovski (Reviewer #3); Scott W Linderman (Reviewer #4).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife (but note caveat below).

The reviewers mostly agreed that the VAE is a potentially interesting approach to categorizing vocalization data, and there was enthusiasm about the codebase available in github. Some major problems that arose in review were (1) lack of strong behavioral insights; (2) lack of clarity about data pre-processing – and how this would affect results; and (3) concern about novelty given the widespread use of VAEs for similar problems.

We would, in principle, be open to considering a revised version of this manuscript if the relatively long list of concerns by reviewers 2 and 4 were adequately addressed and if the VAE approach could perform similarity-score metrics (as requested by reviewer 3).

Reviewer #1:

The authors proposed the use of variational autoencoder (VAE) to vocal recordings of model organisms (mouse and zebra finch) to better capture the acoustic features that are missed by conventional acoustic metrics. This manuscript explores the effectiveness of the VAE approach from two perspectives: (i) a motifs based clustering which seeks to match the acoustics data against several predetermined template and (ii) an unsupervised clustering based on randomly segmented vocal recordings. These approaches involve the generation of a collection of images from spectrograms that are then fed to variational encoders to estimate the number of latent variables. With these latent variables, the authors then employed UMAP to visualize the variation within the dataset. The analyses are well conducted and will be useful for broad range of scientists investigating animal vocalizations.

i. From the zebra finch's discussion, this approach performs well in clustering the song syllables based on the four motifs predefined and at the same time could delineate the differences between directed and undirected songs as compared to previous acoustic metrics. While the authors provided a comparison between the ability of SAP acoustics features and VAE latent features in differentiating the directed and undirected birdsong, a comparison between the clustering of song syllables with the use of SAP features and VAE latent feature was not offered (Figure 5a). It would be interesting to see a side-by-side comparison of the 'Goodness of Clustering' metric in this VAE approach vs SAP.

ii. As for the randomly segmented vocal recordings, this method could generate a manifold where different acoustic features were situated in different regions and offer a continuous variability measure for all syllables. It is worth noting that the vocal recordings were randomly segmented based on the length of one syllable. What happens when the length is extended beyond that? Will the manifold produced look like the one shown in Figure 6?

iii. As for the mouse vocal recordings, the VAE approach generates a continuum-like points cloud that performs reasonably well in differentiating different acoustic features of the mouse vocalizations albeit the lack of boundaries in separating them. Could the smooth variation of points be due to the sampling rate? The mouse vocalizations were sampled at a much higher rate (10x) as compared to bird vocalizations. I would expect a greater resolution for the mouse data and thus the VAE can capture more subtle differences between the vocalizations, yielding a continuum-like points cloud. Of course these sampling rate differences are justified because of the different spectral properties of birdsong and mouse USVs – but a simple sentence or two about how sampling rates may affect these analyses would be useful..

Reviewer #2:

Authors introduce a new method for behavioral analysis of vocalizations that supposedly improves on weaknesses of handpicked features, which is that they miss variability and introduce undesirable correlations. They apply VAEs to bird and mouse vocalizations and perform analysis of the latent space. They show that VAEs outperform handpicked features on some simple analysis tasks including time-resolved analysis of variability.

Overall, even if it is correct that their method outperforms traditional-features based analysis, I don't think this insight is in any way relevant. Essentially, it is like saying: here is a bad way of doing things, and we offer one that is slightly better but still much worse than the gold standard. The problem is that there are many methods out there for doing things right from the start, so I cannot see a need for VAEs for the problems addressed. The problem with VAEs is that they are compressive (not representing all aspects of the data), which is why they are less desirable than methods that operate on equivalent representations of the raw data. If you are given money to buy groceries, why would you throw away part of it before you enter the store?

Overall it seems authors have not much to argue for other than their opposition to handpicked features. They pretend not much is out there other than these features for behavioral analysis, which does not reflect the wealth of methods out there. They have not even given appropriate credit to the real usefulness of the handpicked-feature approach, which is interpretability (which their method lacks). For example, one main utility of handpicked features is that some are learned. Songbirds have been shown to learn pitch from a tutor, so pitch is relevant. The same cannot be said about their latent features: which one of these do birds learn from a tutor?

Also, correlations among features that authors criticize as a bug can be seen as a feature, it provides insights into the aspects of their vocalizations that animals cannot control independently.

I could also not detect any new behavioral insights. The only real strength in their manuscript I could detect is that their method allows them to visually segregate directed from undirected song (Figure 4b), vocalizations from different mice strains (Figure 4f), and songbird syllables (Figure 5a). Thus, their method could be a suitable pre-processing for clustering efforts. Also, on a positive note, their method also produces some interesting looking plots (Figure 6b) of to-be identified utility.

L15 Authors claim that finding concise metrics remains a challenge, despite the large number of concise metrics ranging from Euclidean, Hamming, cosine, Wasserstein, Jensen-Shannon, Bhattacharia, Levenstein, ROUGE, etc. Surprisingly, their paper deals with the least concise metric imaginable, a deep autoencoder with thousands of parameters!

L17 Also not clear what would substantiate the claim that vocal behavior remains poorly understood.

L19 They mention several powerful approaches to enable automatic analysis of vocalizations but cite none.

L20 Given the wished-for generality of the problem they would like to study, it sounds strange that key to a successful approach would be a software package. Software packages are the last stage of analysis tool development.

L26 [10] did not discover overnight consolidation of learned birdsong as claimed, but instead 'inappropriate consolidation', which is challenged by a more recent analysis in [26].

L29 Authors criticize 'correlations among features', claiming these could result in redundant characterizations of vocalizations. Implicitly they argue for features that do not correlate, e.g. independent component analysis. But again, no citations, no following up on the embarked ideas. Correlations could actually be a feature of the behavior itself (and quite interesting to study).

I do not believe that mouse USV syllables form a continuum of syllables. Because authors did not find clusters, this does not mean that they are not there. Rather than trying to find shortcomings (e.g. of their method or the number of samples analyzed), authors generalize from a negative finding to inexistence. By their rejection of vocal clustering, they also ignore previous results showing such clustering [18, 4, 48, 6, 16]. Quite audacious. Is the moon still there when I close my eyes?

In the caption of Figure 2d, authors state 'an ideal representation would exhibit minimal off-diagonal correlation', i.e., ICA is ideal. Why do we need VAEs then if ICA is ideal?

Caption Figure 2e, the representational capacity will depend on the number of features, which is not reported. Same for Figure 2f, the more features used, the more principal components will be needed, so this may be a trivial effect of unequal number of features.

With regards to Figure 2f, it is not even clear from their analysis whether for a given fixed dimensionality, VAEs encode more variance than simple PCA, and if so, at what cost on memory (principal components vs auto-encoder network). For example, in the original Hinton paper in Science, the outcome of this analysis was rather surprising (VAEs are not clearly outperforming PCA in terms of representational capacity).

Last paragraph of Page 4, other than some pretty pictures (Figure S4) there is no (numerical) evidence for their claims of superiority of their latent features.

L115-125 and Figure 4: This is an ill-advised analysis. Why would one choose SAP features to detect changes in song? It is obvious that change detection requires the most sensitive analysis possible, so why would one perform compression beforehand? Same goes for their latent features. Even if it is better than SAP, why would one choose it and not the raw data itself (and a suitable standard metric)?

Same for L 126-L135 on data in mice.

L 173-L187: Authors argue about clustering failures of MUPET using UMAP representations, ignoring the fact that UMAP provides a faulty account of true distance. Their analysis of latent features is a step in the right direction, but falls short of analysis of the raw data (or an equivalent representation, e.g. https://asa.scitation.org/doi/abs/10.1121/1.4731466 and others).

L214: Their method is not useful for analyzing moment-by-moment variability of song, because they need to pre-process songs by 'warping each in time to account for well-documented differences in rhythm and tempo', which is the only problem that would complicate a more rigorous analysis.Reviewer #3:

This manuscript presents a new implementation of variational autoencoder machine learning algorithm (VAE) for the analysis of animal vocalization. The new method is impressive and powerful compared to existing methods. I also like the AVA Python program package, which is well documented. Results demonstrate that AVA can capture important biological differences between vocalization e.g., between directed and undirected songs in birds, and identify similar syllables in mouse song. It can clusters syllables to types in adult zebra finches. The evidence for the lack of clusters in the mouse song are strong and convincing, and of important implications.

The principal weakness of the manuscript, in its present form, is that only insufficient evidence are provided to allow judging how AVA can perform in more difficult tasks, for which software like SAP is often used. For example, can AVA perform robust tutor-pupil similarity measurement in zebra finches? Can it identify clusters in young zebra finches? There is also no serious attempt to show replicability across different training sets. Once these concerns are address I feel that the manuscript should be appropriate for publication.

1. Detecting similarly as in Figure S5 across random repetition of the same zebra finch syllable spectrograms is not convincing enough. It is important to show how well can AVA performs when comparing tutor and pupil zebra finch songs. This testing should include examples of tutor pupil zebra finch songs (some with high similarity and others with lower similarity) should be plotted using UMAP projection as in Figure 6b.

2. It is relatively easy to detect clusters in adult zebra finch songs, but to study song learning it is often needed to cluster song syllables in young birds. SAP can often detect clusters in 50-day old birds. I wonder if AVA can detect clusters even earlier? This would be a very convincing demonstration to the power and usability of the new approach. Again, it is critical to show how AVA behaves with presented with more challenging tasks.

3. One issue that bothers me a lot is how the specific training of the algorithm might affect the outcomes. Say for example that lab 1 trained AVA with one dataset, and lab 2 trained AVA with a second dataset. But assume that both datasets were randomly sampled from the same population of birds. How comparable the results would be? For example will a similarity measurement of the same tutor and pupil would be comparable across the labs who trained AVA independently?

4. I like the "higher representational capacity" of the new method, but sometimes "with much wisdom comes much sorrow": higher representation capacity can potentially cause trouble if it makes the method too sensitive to things we do not care about. At this level, I would like to see some evidence for robustness to noise. For example, it should be easy to test how sensitive AVA is for small differences in recording conditions, say, to recording with in a sound attenuation chamber while door is open or closed?

Reviewer #4:

Low-dimensional learned feature spaces quantify individual and group differences in vocal repertoires.

The authors use variational autoencoders (VAEs) to learn a low-dimensional representations to spectrograms of bird song an mouse unltrasonic vocalizations (USVs). They find these representations of vocal behavior to be useful for studying social interactions and differences between strains of mice. Further investigations suggest that mouse USVs do not cluster as nicely as previously thought, and rather span a continuous manifold in feature space. Finally, VAEs trained on random snippets of the spectrogram highlight variability (and stereotypy) in zebra finch songs, in contrast to the unstructured (or highly variable) space of mouse USVs.

The proposed model operates in the frequency domain, consuming snippets of time-warped spectrograms. Given that one of the central claims of this paper is the superiority of unsupervised methods for feature extraction, I think these preprocessing steps warrant further consideration. For example, the 2D convolutions in the VAE must implicitly leverage the fact that neighboring frequencies are adjacent in the 128x128 ``images,' but does the choice of frequency spacing (mel-spaced for song birds vs linearly-spaced for mouse USVs) affect the learned representations? How important is the time-warping to downstream representations and analyses? The spectral preprocessing also complicates the ``shotgun' analysis in Figure 6. Each point in the VAE latent space corresponds to a window of time rather than a single frame. How do the projections change as you vary the window size?

Motivated in part by these concerns, some recent approaches like WaveNet (van den Oord et al., 2016) have directly modeled raw waveform data. The sampling rates used for human speech and music (16kHz) are lower than those necessary for USVs, but the same principles should apply. For example, a pre-trained WaveNet with minimal fine-tuning for song bird or mouse USV could yield a very competitive generative model of vocalizations and offer a different representation of this behavior. The comparison may be beyond the scope of this paper, but I think it is worthy of discussion.

Overall, this paper offers a nice application of nonlinear latent variable models to vocal behavior data. The techniques themselves are not particularly novel – variational autoencoders have been widely used in the machine learning community for over five years now – and the finding that learned features can outperform handcrafted ones has been shown across many domains. Given the wealth of works on sequential VAEs for time-series data, I think the novelty of the shotgun VAE is somewhat overstated. In my view, the main contribution lies in the codebase (I looked through the Github repo and was quite impressed!), the analysis pipeline, and the proof-of-concept. That is why I think it is especially important to assess the sensitivity of these results to various design choices that went into the pipeline, including the very first choices about how to preprocess the raw waveform data into time-warped and windowed spectrograms.

Other comments:

– Figure 1a: It's not clear why the length 32 vector is appearing as a square matrix here.

– Please label which dataset (song bird or mouse) the point clouds and spectrograms are coming from in all of the figures. A consistent color scheme could help.

– Figure 2f only has three solid lines. Where is the plot of explained variance in MUPET features by VAE features?

– The paragraph starting on line 97 paints an overly optimistic view of VAEs. Designing deep generative models that can reliably disentangle latent factors is still an active area of research, as is model selection.

– Figures 3, S4, and S5 suggest that nearest neighbor reconstruction with DeepSqueak (and other handcrafted features) is surprisingly bad. Are you using just the Euclidean distance in DeepSqueak feature space? Did you whiten the DeepSqueak features before computing distances? Can you explain why it DeepSqueak is failing so dramatically?

– Throughout, the spectrograms fail to indicate the time window or frequency bands.

– Figure 4a+b aim to show that SAP do not separate directed and undirected vocalizations as well as latent features do, but is this information simply not present in the first two PCs? A classification accuracy assessment would be more convincing.

– The 2D embedding in Figure 4f is confusing to me. Why not just show the full distance matrix from Figure S8, but with the lines to indicate which rows/columns belong to each mouse? That figure gives considerably more information than the tSNE embedding, in my opinion. In particular, it looks like there is a solid group of C57 mice that are very similar to DBA mice, as measured by MMD. The use of tSNE seems rather arbitrary and lossy. Moreover, the colors in Figure 4f convey little information beyond identity, when there seems to be lots of extra info about strain that could be conveyed.

– There are no axis labels or titles in Figure 5a-c, just random clouds of points.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Low-dimensional learned feature spaces quantify individual and group differences in vocal repertoires" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Jesse H Goldberg as the Reviewing Editor and Reviewer #1. and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Ofer Tchernichovski (Reviewer #2); Scott W Linderman (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. This was deemed a strong resubmission and only one relatively minor issue related to Figure 7 is necessary for revision.

Essential revisions:

1. Figure 7 does not show clearly enough how the SG approach overcomes the problem of fused syllables (A and B). Figure 7c should somehow indicate the similarity in the fused AB vs A,B area. The issue is that it is not easy to see how the color code correspond to specific areas in the sonograms presented. An overlay panel could help here.

Reviewer #1:

In this paper, the authors addressed the reviewers' concerns and expanded extensively on the utility of variational autoencoder (VAE). The authors included an extra section discussing VAE 's capability in handling more complicated scenarios by studying the tutor and pupil song learning experiment. One can readily visualize the differences between tutor and pupil syllables via the latent embeddings. Although the latent features could be hard to interpret, one could view it as an initial exploratory analysis in identifying possible acoustic structure discrepancies. The authors also included additional data benchmarking latent features against conventional acoustics features for classification tasks and offered a more in-depth study comparing the clustering of song syllables using traditional acoustic features and VAE latent features. Moreover, they discussed the effect of time stretch and frequency spacing parameters on SAP features prediction and VAE's replicability issue for completeness.

The new Figure 7 showing tutor-pupil analyses is a welcome addition to the paper.

While it remains uncertain if this method will actually supersede others in quantifying finch and/or mouse datasets, this paper could, at minimum, provide a case study of advantages and disadvantages for using the VAE approach for vocalization datasets.

Reviewer #2:

This study applies an unsupervised learning approach for assessing acoustic similarity and for classifying animal vocalizations. Investigation focuses on mice vocalization and song learning in zebra finches. The method demonstrate an impressive capacity to map and compare vocal sounds in both species and to assess vocal learning. It has clear advantages upon existing methods. It is still an open question to what extent this approach can successfully capture vocal development during early stages of song learning. In particular, the learned latent features have no simple interpretation in production and perception of vocal sounds, which future studies will need to address.

Two remaining issues:

1. figure 7 does not show clearly enough how the SG approach overcomes the problem of fused syllables (A and B). Figure 7c should somehow indicate the similarity in the fused AB vs A,B area. The issue is that it is not easy to see how the color code correspond to specific areas in the sonograms presented. An overlay panel could help here.

2. The lack of song development analysis is still an issue.

Reviewer #3:

I thank the authors for their detailed responses. They have satisfactorily addressed all of my concerns.
