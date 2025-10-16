# Author response - Round 1

Authors:
- Mighten C Yip ([ORCID: 0000-0002-8463-0311](https://orcid.org/0000-0002-8463-0311))
- Mercedes M Gonzalez
- Colby F Lewallen
- Corey R Landry
- Ilya Kolb
- Bo Yang
- William M Stoy
- Ming-fai Fong ([ORCID: 0000-0002-2336-4531](https://orcid.org/0000-0002-2336-4531))
- Matthew JM Rowan
- Edward S Boyden ([ORCID: 0000-0002-0419-3351](https://orcid.org/0000-0002-0419-3351))
- Craig R Forest ([ORCID: 0000-0001-5343-1769](https://orcid.org/0000-0001-5343-1769))

## Response text

DOI: [10.7554/eLife.97399.3.sa4](https://doi.org/10.7554/eLife.97399.3.sa4)

The following is the authors’ response to the original reviews.

We thank the reviewers and editors for insightful feedback on how we could improve the manuscript. We have revised the manuscript and addressed the points raised.

Regarding the technical issues raised about the quality of patch clamp recordings (Reviewer 2), we acknowledge that the upper limit of the access resistance cutoff should be lower and that the accepted change should be 10-20%. To this end, we have revised the manuscript to more accurately detail the quality metrics used. The access resistance for the neurons in paired recordings were below 40 MΩ (similar to the metric used by Kolb et al. 2019), and if the access changed above 50 MΩ, we stopped recording from that neuron. Furthermore, the inclusion of neurons in the histogram with access resistance above 50 MΩ was to highlight the total number of neurons patched but not necessarily used in paired recordings. As this was done with an automated robotic system, the neurons would still undergo an initial voltage clamp and current clamp protocol before the pipette would release the neuron and patch another cell. To the point of Reviewer 2, this patch-walk protocol could also be alternatively implemented using manual recording approaches and this point has been included in the revised manuscript.

Regarding the spatial restrictions (Reviewer 3), we agree that the average intersomatic distance is higher than ideal. This was likely due to failed patch attempts; for instance, if one pipette successfully achieved whole cell, and the other pipette had several sequential failed patch attempts, the intersomatic distance (ISD) would increase with each failed attempt due to the user selected index of cells. Ideally, the pipettes would be walking across a slice with low ISD if the whole-cell success rate was closer to 100%. To overcome this challenge in future work, automated cell identification and tracking could enable the path planning to be continuously updated after each patch attempt. Given the whole-cell success rate efficiency for a given electrophysiologist, we believe that the automated robot could be improved in later versions to include routeplanning algorithms to minimize the distance between neurons. Alternatively, this patch-walk system could also be integrated to improve connectivity yields for manual recording approaches as well.

For the point raised about morphological identification, we believe that while important, morphological identification is out of the scope for this project. Future work will include neuronal reconstruction. Regarding the other points, we will amend the manuscript to highlight other key metrics such as maximum time we could hold a neuron under the whole-cell configuration. Additionally, we agree with Reviewer 3 that some of the current language may cause confusion, and we will amend it accordingly.

To all the reviewers, thank you for your time, understanding, and the opportunity to improve our manuscript.
