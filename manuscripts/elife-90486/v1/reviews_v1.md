# Peer review - Round 1

Editors:
- Sjors HW Scheres, MRC Laboratory of Molecular Biology United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90486.3.sa0](https://doi.org/10.7554/eLife.90486.3.sa0)

This is an important demonstration of how the false-positive rate of high-resolution 2D template matching to find particles of a given target structure in 2D cryo-EM images (2DTM) relates to overfitting the data towards the template. The authors present new methods to measure the amount of model bias that gets introduced in high-resolution features of such maps, with compelling evidence that high-resolution features that are not present in the template can still be reconstructed in 3D from images obtained by 2DTM.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90486.3.sa1](https://doi.org/10.7554/eLife.90486.3.sa1)

This work continues a series of recent publications from the Grigorieff lab (https://doi.org/10.7554/eLife.25648, https://doi.org/10.7554/eLife.68946, https://doi.org/10.7554/eLife.79272, https://doi.org/10.1073/pnas.2301852120) showcasing the development of high-resolution 2D template matching (2DTM) for detection and reconstruction of macromolecules in cryo-electron microscopy (cryo-EM) images of crowded cellular environments. It is well known in the field of cryo-EM that searching noisy images with a template can result in retrieval of the template itself when averaging the candidate particles detected, an effect known as "Einstein-from-noise" (https://doi.org/10.1073/pnas.1314449110). Briefly, this occurs because it is statistically likely to find a match to an arbitrary motif over a large noisy dataset just by chance. The effect can be mitigated for example by limiting the resolution of the template, but this prevents the accurate detection of macromolecules in a crowded environment, as their "fingerprint" lies in the high-resolution range (https://doi.org/10.7554/eLife.25648). Here, the authors show through several experiments on in vitro and in situ data that features as small as drug compounds and water molecules can be reliably retrieved by 2DTM if they are searched by a template (the "bait") that contains expected neighboring features but not the targets themselves.

The ideas are generally clearly presented with appropriate references to related work, and claims are well supported by the data. In particular, the experiments for verifying the density of the ribosomal protein L7A as well as the systematic removal of residuals from the template model to assess bias are particularly clever.

The revised version of the manuscript addresses essentially all of the concerns raised previously by this reviewer, with the addition of figures and extended discussion of the key concepts.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90486.3.sa2](https://doi.org/10.7554/eLife.90486.3.sa2)

This paper by Lucas et al follows on from earlier work by the same group. They use high-resolution 2D template matching (2DTM) to find particles of a given target structure in 2D cryo-EM images, either of in vitro single-particle samples or of more complicated samples, such as FIB-milled cells (which would otherwise perhaps be used for 3D electron tomography). One major concern for high-resolution template matching has been the amount of model bias that gets introduced into a reconstruction that is calculated straight from the orientations and positions identified by the projection matching algorithm. This paper assesses the amount of model bias that gets introduced in high-resolution features of such maps.

For a high-signal-to-noise in vitro single-particle cryo-EM data set, the authors show that their approach does not yield much model bias. This is probably not very surprising, as their method is basically a low false-positive particle picker, which works very well on such data. Still, I guess that is the whole point of it, and it is good to see that they can reconstruct density for a small-molecule compound that was not present in the original template.

For FIB-milled lamella of yeast cells with stalled ribosomes, the SNR is much lower and the dangers of model bias will be higher. This is also evidenced by the observation that further refinement of initial 2DTM identified orientations and positions worsens the map. This is obviously a more relevant SNR regime to assess their method. Still, they show convincing density for the GHX compound that was not present in the template, but was there in the reconstruction from the identified particles.

Quantification of the amount of model bias is then performed using omit maps, where every 20th residue in removed from the template and corresponding reconstructions are compared (for those residues) with the full-template reconstructions. As expected, model bias increases with lower thresholds for the picking. Some model bias (Omega=8%) remains even for very high thresholds. The authors state this may be due to overfitting of noise when template-matching true particles, instead of introducing false positive. Probably, that still represents some sort of problem. Especially because the authors then go on to show that their expectations of number of false positives do not always match the correct number of false positive, probably due to inaccuracies in the noise model for more complicated images, this may warrant further in-depth discussion in a revised manuscript.

Overall, I think this paper is well written and it has made me think differently (again) about the 2DTM technique and its usefulness in various applications, as outlined in the Discussion. Therefore, it will be a constructive contribution to the field.

After the first round of review, the authors addressed most points raised in a satisfying manner, which has led to a further (relatively minor) improvement of the manuscript.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90486.3.sa3](https://doi.org/10.7554/eLife.90486.3.sa3)

The authors evaluate the effect of high-resolution 2D template matching on template bias in reconstructions and provide a quantitative metric for overfitting. It is an interesting manuscript that made me reevaluate and correct some mistakes in my understanding of overfitting and template bias, and I'm sure it will be of great use to others in the field.

The revised version of this manuscript addresses all of my concerns. The newly added Figure 4 supplement 1 provides a sobering outlook for the fraction of the proteome we can hope to identify in situ.
