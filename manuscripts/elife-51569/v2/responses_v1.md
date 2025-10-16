# Author response - Round 1

Authors:
- David Hathcock ([ORCID: 0000-0003-4551-9239](https://orcid.org/0000-0003-4551-9239))
- Riina Tehver ([ORCID: 0000-0001-7406-3387](https://orcid.org/0000-0001-7406-3387))
- Michael Hinczewski ([ORCID: 0000-0003-2837-7697](https://orcid.org/0000-0003-2837-7697))
- D Thirumalai

## Response text

DOI: [10.7554/eLife.51569.sa2](https://doi.org/10.7554/eLife.51569.sa2)

Essential revisions:

1) The use of mean first-passage times as estimates for the binding reaction processes assumes that the reaction is taking place after a single collision (diffusion limit). While this might be the case, it is not proven in the case of motor proteins. I would add a caution at this point about the application of mean first-passage times. By the way, this might also be the reason why the theory does not work at large forces. Some discussion might be useful here. For example, authors should note that Dunn et al., 2007, Andrecka et al., 2015, and Veigel et al., 2002, all estimated the actual transit time from detachment of the trail head to its reattachment at a new forward position to be much greater than the theoretic first passage time.

The reviewers raise an important point that was not sufficiently clear in the original manuscript. Binding in our model is not simply diffusion-limited, but this was not discussed explicitly in the main text, and we did not show any binding time results. For that reason we have added a new section to the main text, “Probing the biological function of the joint constraint: effects on timing and consistency of stepping”. Part of this section is devoted to a detailed description of binding timescales, along with a new figure (Figure 6) that shows a comparison of diffusion, hydrolysis, and binding timescales as a function of load force. Quoting from that new section:

“As discussed above, binding in the model is more complex than just waiting for the head to diffuse within the capture radius a of a binding site on actin. […] Figure 6 shows tT versus tdiff as a function of applied force F, and we always see tT > tdiff, as expected from the above constraints.”

The discussion of the experimental estimates for transit times is later in the same section, and we quote it in response to the next reviewer comment.

2) Figure 5. The Veigel et al., 2002 paper showed evidence of stiffness changes at stall forces that may represent the proposal of trail head stomping. While the duration of these events were not quantified in this paper, lifetimes of 200—500 ms are shown in Figure 5 of that paper at 100 μm ATP. Could the authors comment on whether their model would predict such long lifetimes of single-headed attachment?

This is indeed an interesting experimental observation which we believe is linked to trailing leg stomping. We now discuss this experiment in our new section on timing that we have added to the main text. Quoting from that section:

“For small F the trailing leg kinetics is dominated by forward steps. tdiff < th in this regime, but even though the head can diffuse rapidly to forward binding sites, it does not bind until hydrolysis occurs. […] Here there is another experimental artifact in play: as discussed in Hinczewski et al.,2013, the drag from the gold nanoparticle can substantially increase diffusion times, with tT becoming much larger than th at F = 0 because of slow diffusion.”
