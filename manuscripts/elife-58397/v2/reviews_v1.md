# Peer review - Round 1

Editors:
- Barnabas Daru, Texas A&M University-Corpus Christi United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58397.sa1](https://doi.org/10.7554/eLife.58397.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The climatic determinants shaping animal distributions are largely unknown. Network modelling of realized niche domains of 26,000 vertebrates, accounting for the climatic conditions a species experiences within its range, reveals new classification of global climate regimes.

Decision letter after peer review:

Thank you for submitting your article "Regularities in species' niches reveal the world's climate regions" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Barnabas Daru as the Guest Reviewing Editor and Reviewer #3, and the evaluation has been overseen by Christian Rutz as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Kevin Cazelles (Reviewer #1); Serban Proches (Reviewer #2).

The reviewers have seen each other's reviews as part of a post-review consultation session. Since there were no disagreements, we have decided to append their separate original reports to this decision letter. Please address the comments as completely as possible in a revised manuscript.

Since revisions are required before the work can be published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Reviewer #1:

My comments are meant to be constructive, and I hope they will be helpful as you revise your manuscript.

Overall opinion

In this manuscript, Calatayud et al. use a network-based approach to identify climatic regions based on tetrapods occurrence. With these in hand, they assess their congruence with the regions of the Köppen-Geiger climate classification (based on climate and plant distributions) and they also assess their specificity. Overall, I think that this study has a lot of merit and I truly value the work done. However, the current version of manuscript requires some work before being publishable. I have several major concerns that I develop below.

Lack of clarity

The lack of clarity is twofold. First, some sentences are just not clear and need to be rephrased. Below are three examples that all concern the description of the method:

– Subsection “Climatic transition zones” I had to read this several times to understand the meaning of it. A formal definition of D is missing (what are the species included in it).

– Subsection “Geographical signal” I think the equations are valid for 1 domain, but this is not made clear (e.g. how what makes index $i$ disappear from (2) to (1))

– The text in Appendix 1 is hard to read.

Because of this lack of clarity, I am not 100% sure about what has actually been done. It might just be a matter of being careful with the annotations and carefully detailing all the steps, so it might not be much work, but this needs to be done.

Second, some details are missing in critical parts. For example:

– "Using a hierarchical network clustering algorithm (Rosvall and Bergstrom, 2008, 2011)". This is a critical step and the procedure is published, but I think we need more details to understand what is done, i.e. the rational of the algorithm and why it is suited for this analysis. Also, I don't understand where the assessment of the domain's robustness is done in the Appendix.

– AMI is not (yet) frequently used in ecology so I would remind the reader what is it otherwise the reader may not understand the meaning of a AMI of 0.7 (e.g.).

My point being that the right level of methodological is not always provided. A few more sentences may do the jobs.

Why this is not all trivial?

Full disclaimer, I don't think the results are trivial. But at first sight, one may think so.

After my first read of the manuscript, I thought that the two following assertions of the Introduction were contradictory

– "abiotic conditions determine species ranges"

– "However, the fact that plant species are good indicators of general climatic conditions does not necessarily imply that such conditions shape the distribution of other organisms in the same manner"

If "abiotic conditions determine species ranges" and if the reference classification is based on plant distributions, given the variety of ecological links between plants and tetrapodes, then the distribution of tetrapodes communities (assuming there are properly defined) and the reference distribution (Köppen) should be very similar. And actually they are similar as it is showed in Figure 3. But after thinking more about this I convinced myself otherwise, partly thanks to the manuscript, but not only. And this is the issue: the authors should better explain why this is not all trivial in the Introduction, they should explain why one could expect significant discrepancies between the two distributions.

Impact statement

Importantly enough, I don't think that the impact statement : "Similarities in climatic niches of terrestrial vertebrates indicate the Earth's climate regions, which substantially differ from previous plant-based climate classifications." is a fair depiction of the results and it is actually contradictory with, inter alia, the results presented in Figure 3 (the caption of which reads "Tetrapoda groups and Köppen's climatic regions are largely congruent"). Unless I have miss something.

Discussion

I must say that the Discussion section includes various bold statements that the authors, for instance:

"Our results bring us closer to a definition of climatic regions that represent active factors for the organization and evolution of life."

Quite frankly, after reading the manuscript, I am not entirely sure why. I would rather discourage the authors from making such statements.

Reviewer #2:

This is a brilliant piece of work, filling in a massive gap in biogeography. I think for a first shot, including just one measure of energy and one for water is perfectly fine. The writing is good and the logic mostly consistent, with very slight lapses in the discussion.

Reviewer #3:

This study presents climate zones based on realized niches of the world's terrestrial vertebrates using network methods. In general, I found the analyses to be sound and conclusions valid, although I do have some few reservations. For example, the authors explored the effect of mean annual potential evapotranspiration and annual precipitation as proxies for energy and water inputs, and therefore determinants of tetrapod diversity. The choice of these metrics comes a bit “off-the-shelf” without unpacking the structural reasons for the potential of other variables such as elevation/altitude or latitude driving tetrapod niches, all of which are key determinants for tetrapod diversity. Other aspects that might be worth incorporating or at least discussing is how other regionalizations such as the recent update of Wallace's zoogeographic regions by Holt et al., 2013, fit into the climate niches identified in this study. How can they inform conservation in the real-world? I also provide some suggestions for improvement throughout the manuscript as detailed below.

Abstract:

Please remove the comparison to plants to avoid any controversy on whether or not plants capture the climate of a region than animal taxa or vice versa. The Abstract will read just fine without the last sentence.

Introduction:

The effect of measurement scale on patterns of biodiversity is increasingly becoming a topic of growing interest in ecology and not acknowledging it can lead to spurious conclusions (see some examples of addressing this topic):

Levin, S. A. The problem of pattern and scale in ecology. Ecology 73, 1943-1967 (1992).

Rahbek, C. & Graves, G. R. Multiscale assessment of patterns of avian species richness. Proc. Natl Acad. Sci. USA 98, 4534-4539 (2001).

Jarzyna, M. A. & Jetz, W. Taxonomic and functional diversity change is scale dependent. Nat. Commun. 9, 2565 (2018).

Daru, B.H., Farooq, H., Antonelli, A. & Faurby, S. (2020) Endemism patterns are scale dependent. Nature Communications 11: 2115

It would be important to discuss how the analysis done here can be sensitive to the measurement scale.

Figure 1: This is a nice figure and would help the reader get the message of the paper even without reading the entire manuscript! I like it. However, it appears that the coloring in panel D is switched. It should be the other way around.

Results

Animal vs plant climatic regions

I found the comparison of the Tetrapoda classes in this study to that of Köppen's plant-based regions strange. Köppen's plant-based regions were based on pioneer plant classifications and not necessarily based on the realized niches of the over 380,000 species of plants across the globe, whereas the current study uses carefully vetted updated range maps of over 26,000 vertebrates from the IUCN. I suggest the authors minimize such plant vs animal comparisons.

Figure 3: "Tetrapoda". Since this is the central figure of the paper, the authors should also indicate the names (or suggested names) of the 16 climatic regions directly on the map, perhaps in a separate blown-out figure.

Discussion:

In addition to the caveats already discussed, another caveat worthy of discussion is how sensitive are the climatic regions to the measurement scale along grain size, spatial extent or even taxonomic treatment? See similar comments above.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Regularities in species' niches reveal the world's climate regions" for further consideration by eLife.

Your article has been re-evaluated, and although we found it much improved, there are some remaining issues that need to be addressed before acceptance, as outlined below:

Reviewer #2:

I think the responses to reviewers have been very thorough.

Reviewer #3:

The work presented by Calatayud and co-authors on a zoogeographic classification of climate regimes is novel. The climatic determinants shaping animal distributions is largely unknown. Network modelling of realized niche domains of 26,000 vertebrates – accounting for the climatic conditions a species experiences within its range – reveals new classification of global climate regimes.

I enjoyed this second draft, just like I did the first time. The authors addressed some of my comments in the previous version of the manuscript. Thank you. However, a few other comments were not well addressed at least not entirely:

1) The issue of scale: The authors acknowledge incorporating how they have dealt with sensitivity of the analyses to the scale of measure in the Materials and methods. However, not only did I feel like my comments were not well understood, these were also not discussed in the Discussion. How do the findings vary across grain sizes or spatial extents?

For instance, the authors stated that "Extracting the climatic values that a species range covers from a high-resolution climatic raster (such as 0.08°) may reduce commission errors at the species range's borders, but otherwise increases this error. Extracting the climatic values that a species range covers from a high-resolution climatic raster (such as 0.08°) may reduce commission errors at the species range's borders, but otherwise increases this error."

While this assumption may be true to some extent, however, the authors did not test this empirically.

Another example of the need to test for scale effects is how the authors stated that: "To alleviate the effects of these potential errors, we first extracted the climatic values from the high-resolution rasters (0.08°). Then, we computed the average climatic values among selected raster pixels located within cells of 0.5 degrees. In this way, we reduced the effects of commission errors both at the borders of and inside species ranges. We also conducted a bootstrap significance test that takes the uncertainty of species ranges into account (see below)."

In terms of grain size for instance, it is well known that significant climate variation can exist even within a 0.5 degree cell (equivalent to ~50 km) that spans mountain peaks and valleys, and where temperatures can vary over 20°C. In a case where the average of 0.08 degree cells are taken within a 0.5 degree cell, is it unlikely that the average represents the climatic conditions of the grid cell. I imagine this will also be quite different at a grid resolution of 1.0 degree, 2.0 degrees, and/or 5 degrees etc. It is not clear how this was addressed in the Materials and methods and discussed in the Discussion.

In terms of the spatial extent, will the findings still hold up if this was analyzed at a regional continental scale or local country level (and varying along the grain sizes mentioned above)? Adding a test and a discussion along these lines would be important.

2) Climatic transition zones

The authors analyzed an important issue about climate transition zones which can represent places where different climate regimes admix and potentially provide source for novel species interactions, and potentially high diversity. However, the authors miss a great opportunity to return to this aspect later in the Discussion. I was hoping for some real discussion about this where you discussed regions of milder climates. Do the transition zones correspond to these regions of milder climates, and/or what do they mean?
