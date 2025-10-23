# Author response - Round 1

Authors:
- Keisuke Atsumi ([ORCID: 0000-0002-8206-4977](https://orcid.org/0000-0002-8206-4977))
- Yuusuke Nishida
- Masayuki Ushio ([ORCID: 0000-0003-4831-7181](https://orcid.org/0000-0003-4831-7181))
- Hirotaka Nishi
- Takanori Genroku
- Shogoro Fujiki ([ORCID: 0000-0002-9778-9532](https://orcid.org/0000-0002-9778-9532))

## Response text

DOI: [10.7554/eLife.93694.3.sa2](https://doi.org/10.7554/eLife.93694.3.sa2)

The following is the authors’ response to the original reviews.

Reviewer #1 (Recommendations For The Authors):

(1) The modeling process is outlined, but an explanation of why Maxent (Phillips & Dudík, 2008) was chosen for SDMs and why the specified predictor variables were used could provide additional context. This clarity would help readers understand the rationale behind the methodology.

In L.558-571 (Predictor variables subsection), we added the explanation about predictor variables as follows:

“Predictors encompass a range of environmental variables recognized to impact species distribution (Table 3): land use (Newbold et al., 2015), climate (bioclim variables (Booth et al., 2014)), vegetation (Abe, 2018), lithology (Ott, 2020) and elevational range (Udy et al., 2021). Additionally, categorical variables representing known biogeographic regions, reflecting geological history, were included. We applied Blakiston's Line —Tsugaru straits dividing the northern and main islands of Japan (i.e., Hokkaido and Honshu islands)— reflecting a significant historical migration barrier for mammals and birds (Dobson, 1994; Saitoh et al., 2015). Due to the distinct fauna (Wepfer et al., 2016; Yamasaki, 2017), we also specified oceanic islands (i.e. Ogasawara and Daito isles) which have never been connected with the Asiatic continents. Continuous environmental variables were transformed into linear, quadratic and hinge feature classes to illustrate nonlinear associations between environments and species occurrence (Phillips et al., 2017). The regularisation multiplier was set at 2.5, falling within the established optimal range of 1.5 to 4 (Elith et al., 2010; MorenoAmat et al., 2015).”

In L.614-618 (Modelling subsection), we explain why we chose MaxEnt:

“To model species distributions from presence-only data, several algorithms have been utilised, including generalised additive models, random forest, and neural networks (Norberg et al., 2019; Valavi et al., 2022). In our study, we opted for MaxEnt (Phillips and Dudík, 2008) due to its high estimation accuracy and relatively low computational burden (Valavi et al., 2022).”

(2) While the study outlines a manual reidentification process by experts for wild individuals, it might be beneficial to elaborate on the criteria or expertise level of these experts. This transparency ensures the reliability of the reidentification process. Reply

In L.519-523, we added description about experts as follows:

“These experts have professional backgrounds, serving as a technician at a prefectural research institute (fish), highly-experienced field survey conductors (plants and insects, respectively), a post-doctoral researchers (amphibians and reptiles, and mammals, respectively), and a museum curator (mollusks) specialising in the focal taxa.”

(3) The analysis of the effects of data type (Biome+Traditional data or Traditional survey data) on BI is comprehensive. However, a brief discussion on the potential implications of these effects on the study's overall conclusions could add depth to the interpretation.

We enforced our discussion about the causes and consequences of improved modelling accuracy.

In L.276-282, we argued about the causes:

“Therefore, incorporating Biome data could significantly enhance modelling accuracy in urban and suburban landscapes, which are typically underrepresented in traditional survey data. As pseudo-absences are selected based on search effort, our models utilise numerous pseudoabsences from these areas. Consequently, this might lead to better estimation of species absence in such areas, not just presence, resulting in an overall increase in model accuracy across a wider range of species.”

In L.370-387, we argued how improved modelling accuracy may help build naturepositive society as follows:

“By blending data from traditional surveys and communities, we improved the accuracy of species distribution estimates. This enhanced estimation lays the groundwork for more precise subsequent analyses. For instance, estimated distributions will be useful in selecting new protected areas or areas with OECMs (Other Effective area-based Conservation Measures: allowing a wider range of land use as long as biodiversity and ecosystem services are sustained/improved). Using estimated distributions of each species, hotspots of species or evolutionary diverse taxa can be inferred. Such sites will be good candidates for protected areas (Jones et al., 2016) or OECMs (Shiono et al., 2021). Further, estimated distributions can be used as input for spatial conservation prioritisation tools (e.g. Marxan (Ball et al., 2009)).

In our experience, stakeholders—including corporate social responsibility managers and conservation practitioners—often seek the list of species potentially inhabiting their locations. Due to the uncertainty of SDMs and their thresholding into presence/absence, on-site surveys remain essential for assessing biodiversity status. SDMs can make such surveys costeffective by screening important locations for on-site assessment (e.g., Locate phase in TNFD framework) and narrowing down the target species for surveying. Improved estimation through SDMs can mitigate risks associated with their use in society and enable more informed decisionmaking for conservation efforts.”

Following the editorial policy, we have reorganised our supplementary materials as follows:

- Formerly Supplementary File 1 - Remains unchanged.

- Formerly Supplementary File 2 - Transferred into the main text, in the subsection "Filtering suspicious occurrence record in Biome data" in the Methods section, and Table 2. Citations remain as Supplementary File 2.

-Formerly Supplementary File 3 - Remains unchanged.

-Formerly Supplementary File 4 - Transferred into "Figure 3—figure supplement 1".

-Formerly Supplementary File 5 - Transferred into Figure 4.

- Formerly Supplementary File 6 - Transferred into the main text, in the subsection "Predictor variables" in the Methods section and Table 3.

- Formerly Supplementary File 7 - Transferred into the main text, in the subsection "Pseudo-absence reflecting search effort" in the Methods section and Figure 5.

- Formerly Supplementary File 8 - Transferred into the main text, in the subsection "Model evaluation" in the Methods section and Figure 6.

- Formerly Supplementary File 9 - Renamed as Supplementary File 4.
