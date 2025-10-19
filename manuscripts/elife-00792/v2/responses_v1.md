# Author response - Round 1

Authors:
- Mikhail Kudryashev
- Marco Stenta
- Stefan Schmelz
- Marlise Amstutz
- Ulrich Wiesand
- Daniel Castaño-Díez
- Matteo T Degiacomi
- Stefan Münnich
- Christopher KE Bleck
- Julia Kowal
- Andreas Diepold
- Dirk W Heinz
- Matteo Dal Peraro
- Guy R Cornelis
- Henning Stahlberg

## Response text

DOI: [10.7554/eLife.00792.018](https://doi.org/10.7554/eLife.00792.018)

We are aware of the significant risk of overfitting in the alignment of noisy data to a reference. As you point out, classical sub-tomogram averaging may produce such overfitting, while the “gold standard” procedure reduces this risk by splitting the dataset into two sub-sets and processes these completely independently. Unfortunately, applying this algorithm to sub-volume averaging is challenging if only a low number of sub-volume “particles” is available. We have now re-processed our injectisome sub-volumes, following the “gold standard” strategy with our “Dynamo” software. This resulted in a more conservative resolution estimate of 4 nm for our final injectisome structure. We now describe this “gold standard” processing approach in an additional section within the Materials and methods section and a panel in Figure 2—figure supplement 1D, and we have updated the manuscript accordingly.

The new, more reliable processing, however, did not affect our findings or the interpretation of the results: the positions of the rings in the injectisome structure, including the putative YscV ring, remained as before, and significant variations in the injectisome lengths after classification and averaging are observed as previously described. These dimensions are also supported by intermembrane distances measured at individual single injectisomes that we also show in Figure 2E.

As for the YscC structure, due to the small number of particles we could not achieve a reliable convergence with only half of the particles. The average from all available YscC sub-volumes, however, shows similar dimensions as the individual YscC sub-volumes showed before averaging, which leads us to believe that the sub-volume averaging reports a valid average structure within the specified resolution limits. To provide a reliable estimate of this resolution, we now used the more conservative threshold for the resolution (FSC=0.5), reporting a resolution of 3 nm. We have updated Figure 6 and the manuscript accordingly.
