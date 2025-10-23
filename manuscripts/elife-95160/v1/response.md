# Author response - Round 1

Authors:
- Jun Yang ([ORCID: 0000-0002-2484-2494](https://orcid.org/0000-0002-2484-2494))
- Hanqi Zhang
- Sukbin Lim ([ORCID: 0000-0001-9936-5293](https://orcid.org/0000-0001-9936-5293))

## Response text

DOI: [10.7554/eLife.95160.4.sa4](https://doi.org/10.7554/eLife.95160.4.sa4)

The following is the authors’ response to the previous reviews.

Reviewer #3:

I appreciate the revisions made by the author which address all of my concerns.

Nevertheless, I have some new questions when I read the paper again. These questions are not necessarily criticisms of the paper, which may reflect the gap in my understanding. Meanwhile, it also reflects the writing might be improved further.

- Fig. 1:

I understand that a critical assumption for generating the required result is that the oblique orientation has lower "energy" than the cardinal orientation (Fig. 1G). Meanwhile, I always have a concept that typically the energy is defined as the negative of log probability. If we take the log probability plotted in Fig. 1A, that will generate an energy landscape that is upside down compared with current Fig. 1G. How should I understand this discrepancy?

As the reviewer pointed out, a higher prior distribution near cardinal orientations causes cardinal attraction in typical Bayesian models, which can correspond to lower energy around these orientations. Additionally, in the context of learning natural statistics, Hebbian plasticity in excitatory connections strengthens recurrent connections and drives attraction toward more prevalent stimuli within neural circuits.

However, as demonstrated by Wei and Stocker (2015), Bayesian inference model can also produce cardinal repulsion when optimizing encoding efficiency. In our network, this efficient encoding is achieved through heterogeneous lateral connections and inhibitory Hebbian plasticity in the sensory module, resulting in lower energy near oblique orientations. Thus, the shape of prior distribution does not have a direct one-to-one correspondence with the bias pattern or the dynamic energy landscape.

- Fig. 3 and its corresponding text.

I understand and agree the Fig. 3B&C that neurons near cardinal orientations are shaper and denser. But why the stimulus representation around cardinal orientations are sparser compared with the oblique orientation? Isn't more neurons around cardinal orientation implying a less sparser representation?

Indeed, with sharper tuning curves, having more neurons can result in a sparser representation. Consider an extreme case where each orientation, discretized by 1°, is represented by only one active neuron with a tuning width of 1°. While this would require more neurons to represent overall stimuli compared to cases with wider tuning curves, each stimulus would be represented by fewer neurons, aligning with the traditional concept of sparse coding.

However, in Fig. 3 and corresponding text, we did not measure the sparseness of active neurons for each orientation. Instead, we used the term ‘sparser representation’ to describe the increased distance between representations of different stimuli near the cardinal orientations. Although this increased distance can be consistent with the traditional concept of sparse coding, to avoid any confusion, we have revised the term ‘sparser representation’ to ‘more dispersed representation’ in the 3rd paragraph in pg. 5 and the 3rd paragraph in pg. 6.
