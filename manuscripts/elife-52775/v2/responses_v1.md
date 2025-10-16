# Author response - Round 1

Authors:
- Samuel G Usher ([ORCID: 0000-0002-2487-6547](https://orcid.org/0000-0002-2487-6547))
- Frances M Ashcroft ([ORCID: 0000-0002-6970-1767](https://orcid.org/0000-0002-6970-1767))
- Michael C Puljung ([ORCID: 0000-0002-9335-0936](https://orcid.org/0000-0002-9335-0936))

## Response text

DOI: [10.7554/eLife.52775.sa2](https://doi.org/10.7554/eLife.52775.sa2)

Essential revisions:

1) Please address the discrepancy between your conclusion that inhibition by TNP-ATP is weak and incomplete for the C166S mutation, and previous reports that (unmodified) ATP at 10 mM produces complete inhibition of this mutant (for instance, in pmid 11159439 and other papers). Your raw data in Figure 3D are compatible with strong inhibition at high concentration, but your model results are not (Figure 3D/E). It seems important that you address this, ideally with some new data at higher [TNP-ATP], but at the very least by discussion and perhaps additional modeling to learn how more complete inhibition would affect the conclusions.

There have been numerous previous studies examining the effect of amino acid substitutions at Kir6.2-C166 on the sensitivity of KATP to nucleotide inhibition. Some report complete inhibition at high ATP concentrations (Kir6.2,N160D,C166S + SUR1, Enkvetchakul et al., 2000) whereas others only report partial inhibition (Kir6.2,C166S-△C26, Kir6.2,C166S + SUR1, Trapp et al., 1998; Kir6.2,C166A-GFP + SUR1, Ribalet et al., 2006). The maximal block at high nucleotide concentrations appears to be background dependent.

To directly address this issue in our construct, Kir6.2*,C166S-GFP + SUR1, we applied 10 mM ATP to excised patches and observed only partial inhibition. We have added these data to Figure 3D. We did not measure inhibition by TNP-ATP at concentrations > 1 mM as our TNP-ATP was purchased as a triethylammonium salt (of indeterminate molar ratio of TNP-ATP:triethylammonium). We found that triethylammonium inhibits both Kir6.2*-GFP +SUR1 and Kir6.2*,C166S-GFP + SUR1 at millimolar concentrations. Thus, we would expect it to add to the total amount of current inhibition at high TNP-ATP concentrations. We have added a new supplement (Figure 3—figure supplement 2A,B) to demonstrate this.

We also performed additional modelling (Figure 3—figure supplement 2C,D) to illustrate that at relatively high values for L*D4 the MWC-type model predicts a nucleotide-insensitive plateau of current at higher concentrations rather than a bona fide right shift in the inhibition curve relative to the binding curve. The height of the plateau at saturating nucleotide concentrations is proportional to the unliganded open probability of the channel, which may help to explain the diversity of results from the existing literature. We have included additional discussion in the text (paragraph four subsection “Kir6.2-C166S affects the ability of bound nucleotides to close KATP.”).

Related to this, please explain the basis for selecting the prior distribution of the parameters for the modeling. Might it make sense to include information about the WT parameters in the prior distribution when fitting the mutant data?

We have now repeated our fits to the mutant data using two additional sets of priors. We used Gaussian fits to the posterior probabilities from the wild-type data as our first set. This resulted in parameter estimates that were very similar to wild-type, but the resulting curves fit the data poorly. We generated an additional set of priors using the centres of the Gaussian fits to the wild-type posterior probabilities, but with a 10-fold larger standard deviation (i.e. broader distributions centred on the same values). The resulting fits were similar to those generated from our relatively unbiased priors, with the exception of our estimates for L, which gave too much weight to unrealistic values for unliganded open probability (<1%). Thus, we believe we have chosen our priors well. We have included these new fits as Figure 4—figure supplement 4 and added additional discussion in the text (subsection “Bayesian model fitting”).

2) The kinetics work is the weakest part of the paper. There are no controls for the minimum time required to exchange the solution by perfusion, there is barely one time point to constrain the on rate at 100 uM, and the assignment of the rates are model dependent. We think that this section should be removed.

We agree with your assessment and have removed this section from the paper and edited the Materials and methods accordingly (subsection “Epifluorescence imaging and spectroscopy.”). We moved the remaining panels from the original Figure 4 to Figure 4—figure supplement 1, and renumbered other figures accordingly.
