# Rapid transporter regulation prevents substrate flow traffic jams in boron transport

## Authors

- Naoyuki Sotta<sup>1</sup> ([ORCID: 0000-0001-5558-5155](https://orcid.org/0000-0001-5558-5155))
- Susan Duncan<sup>2</sup> ([ORCID: 0000-0001-9581-1145](https://orcid.org/0000-0001-9581-1145))
- Mayuki Tanaka<sup>1</sup>
- Takafumi Sato<sup>1</sup>
- Athanasius FM Marée<sup>2</sup> ([ORCID: 0000-0003-2689-2484](https://orcid.org/0000-0003-2689-2484)) †
- Toru Fujiwara<sup>1</sup> ([ORCID: 0000-0002-5363-6040](https://orcid.org/0000-0002-5363-6040)) †
- Verônica A Grieneisen<sup>2</sup> ([ORCID: 0000-0001-6780-8301](https://orcid.org/0000-0001-6780-8301)) †

### Affiliations

1. Graduate School of Agricultural and Life Sciences The University of Tokyo Tokyo Japan
2. Department of Computational and Systems Biology John Innes Centre Norwich United Kingdom

† Corresponding author

## Abstract

Nutrient uptake by roots often involves substrate-dependent regulated nutrient transporters. For robust uptake, the system requires a regulatory circuit within cells and a collective, coordinated behaviour across the tissue. A paradigm for such systems is boron uptake, known for its directional transport and homeostasis, as boron is essential for plant growth but toxic at high concentrations. In Arabidopsis thaliana, boron uptake occurs via diffusion facilitators (NIPs) and exporters (BORs), each presenting distinct polarity. Intriguingly, although boron soil concentrations are homogenous and stable, both transporters manifest strikingly swift boron-dependent regulation. Through mathematical modelling, we demonstrate that slower regulation of these transporters leads to physiologically detrimental oscillatory behaviour. Cells become periodically exposed to potentially cytotoxic boron levels, and nutrient throughput to the xylem becomes hampered. We conclude that, while maintaining homeostasis, swift transporter regulation within a polarised tissue context is critical to prevent intrinsic traffic-jam like behaviour of nutrient flow.

## Introduction

Robust growth and functioning of all living organisms, including plants, requires a well-balanced uptake of nutrients from the environment. However, nutrients are not always readily available in the environment at the organisms’ optimal levels. This issue is exacerbated for sessile plants which take up essential minerals, required for their growth and functioning, from the soil in which the nutrient concentrations are mainly determined by elemental contents of igneous rocks. Most soils are either deficient or in excess of essential elements (Roy et al., 2006). Plants have therefore evolved to take up these essential minerals from the soil in a regulated manner over a wide range of concentrations through their roots, conveying the nutrients to the rest of the plant body via the vascular network. For a well-balanced uptake of nutrients from soils by roots, nutrient transport processes need to be regulated in a nutrient-dependent manner, which constitutes one of the essential processes for plant growth and crop production.

For roots to transport soil-derived nutrients into its central vascular tissues, which will ultimately transport it to other regions of the plant, a flow of nutrients has to be established which crosses several cell files, from the cells in contact with the medium (typically epidermal or lateral root cap cells) to the xylem. Boron is one of such essential nutrients for plants, critical for cell wall composition (O'Neill et al., 2004). Borate is cross-linking a pectic polysaccharide, Rhamnogalacturonan II, which makes it indispensable for tissue growth (Kobayashi et al., 1996). Only available in the soil, boron is transported to the xylem through an intricate system of polarly localised membrane transporters that bring boron from the apoplast into the cytosol, and then back again into the apoplast (Miwa and Fujiwara, 2010). The boron transport mainly takes place in the form of boric acid and borate. At neutral pH, boron is mostly present in the form of boric acid (Woods, 1996).

Two families of transporters, BORs and NIPs, are involved in boron transport through the root. BOR proteins export boron from within the cell to the cell wall, while NIP proteins enhance bidirectional permeability. Both BORs and NIPs present polar localisation, often complementary. In the root, BOR1 (At2g47160) and BOR2 (At3g62270) locate on the inwards-facing membranes of the cell (Takano et al., 2010; Miwa et al., 2013), while NIP5;1 (At4g10380) locates on the outwards-facing membranes (Takano et al., 2010). Being polarised in such a manner, their combined action and localisation allows for a highly efficient boron uptake and transport to the xylem, even when boron is only available at very low concentrations in the medium. This transport system ensures that within the root tissue much higher boron concentrations can be reached than what is available in the medium, allowing for significant xylem loading which then provides sufficient boron for the growing shoot. Indeed, both nip5;1 and bor1, bor2 mutants present severe growth defects under low boron concentrations (Noguchi et al., 1997; Takano et al., 2006-06; Miwa et al., 2013). Such a coordinated and directed polar transport is reminiscent of the intricate polar auxin transport networks within the plant, although their axes of polarity are often perpendicular to one another (Robert and Friml, 2009).

Likewise, the boron transport system faces constraints: While boron is required for cell wall strength and stability, too high intracellular boron concentrations elicit DNA damage, growth retardation and eventually cell death (Sakamoto et al., 2011-09). Unsurprisingly, therefore, is has been found that the protein levels of the boron transporters are regulated by boron itself, with both NIP5;1 and BOR1, 2 protein levels dropping at higher boron concentrations (Takano et al., 2005; Takano et al., 2006-06; Takano et al., 2010; Miwa et al., 2013). Such boron-dependent regulation is considered essential to allow for boron homoeostasis, preventing boron toxicity when boron availability is high, but allowing for efficient uptake when availability is low. Protein down-regulation takes place through two distinct mechanisms. In the case of NIP5;1 boron reduces protein levels via mRNA degradation (Tanaka et al., 2011; Tanaka et al., 2016), while in the case of BOR1, 2 the mechanism involves increased protein degradation (Takano et al., 2005; Miwa et al., 2013). Surprisingly, however, in both cases the down-regulation of boron transporters by boron occurs on a short time scale: when a plant is transferred from low to high levels of boron, swift downregulation of BORs (via protein degradation), and NIPs (via transcript degradation) is observed (Takano et al., 2005; Tanaka et al., 2011; Tanaka et al., 2016). The BOR1 degradation occurs through endocytosis, apparent 30 min after the transfer from low to high boron media. After two hours BOR1 has already mostly disappeared, suggesting that the half life of BOR1 is well below one hour (Takano et al., 2005). The half life of NIP5;1 mRNA after the transfer from low to high boron media is 10–15 min (Tanaka et al., 2011). Such rapid time scales seem at odds with the expected natural variations of boron a plant would experience, as there is no evidence supporting considerable fluctuations in soil boron concentrations, neither spatially nor temporally. This is due to boron being available to plants as boric acid, which is highly water-soluble (solubility: 0.92 mol/L at 25°C). Consequently, boron is very mobile in the soil (Nable et al., 1997), rendering patchy heterogeneous boron levels throughout the soil neither stable nor probable. The main process that presumably would allow a plant growing at a fixed location to experience rising boron levels is through drought, a phenomenon which fails to account for the necessity of transporter down-regulation occurring on the order of minutes. Also watering of plants is not expected to quickly change the boron levels. Keren and Bingham, 1985, analysing the effects of solution-to-soil ratio on the boron concentration in soil water, propose that soil adsorption plays a role in buffering the fluctuations in boron concentration in soil water as a consequence of fluctuations in the water-soil ratio. Mathematical modelling was used to predict the boron concentrations in the soil solution from the water-to-soil ratio (Keren, 1981), revealing that boron concentration in the soil is robust against fluctuations in the water-to-soil ratio if soil adsorption is considered. From these in-depth studies, the picture consolidates that rapid fluctuations in boron concentration are indeed unlikely, or rare events even if they could occur under very specific and unlikely conditions. Given that there is no apparent necessity for swift regulation, it is thus surprising to find cost-ineffective down-regulation mechanisms through degradation of mRNA and protein underpinning this system, instead of more cost-effective down-regulation processes via transcriptional repression.

In short, down-regulation of boron transporters can be readily understood as a natural adaptive mechanism for plants to optimise growth and function at different geographical locations with varying natural boron concentrations. Nevertheless, it remains intriguing as to why plants have evolved such a swiftness in the regulation of these transporters. Puzzled by this behaviour, we questioned if other dynamical constraints are operating on polarised root tissue that could explain the need for these rapid timescales. To address this, we explored possible implications of dynamical transporter regulation in a parsimonious model that captures the nutrient flux across a small cross-section of a generic root tissue, with an explicit focus on the swiftness of the temporal regulation.

### A simple model for boron uptake to probe implications of boron transporter regulation swiftness

In Arabidopsis thaliana, boron is shuttled from the soil across the epidermis, cortex and endodermis into the stele, to finally be taken up into the xylem, mediated by the action of secondary active boron exporters (BORs) and the enhancement of permeability through NIPs. Previously, we analysed boron patterning by using a two-dimensional cross-sectional model of the entire Arabidopsis root meristem, considering all spatial nuances of transporter localisation, polarity and intensity, whilst neglecting transporter dynamics and regulation (Shimotohno et al., 2015-04). Instead, transporter levels and activity were static, fixed to the observed steady state transporter expression under constant boron medium condition of 0.3 μM. While neglecting regulation of transporter expression or activity, a characteristic boron pattern emerged on the level of the root, presenting highest concentrations at the stem cell niche. This boron profile gradually decreased longitudinally up to the start of the differentiated tissues. The computationally simulated characteristic boron distribution, which we confirmed experimentally through LA-ICP-MS, strongly indicates that the mature root tissue is involved mainly in transporting boron from the soil into the xylem, while the distal meristematic tissues have a differential boron transport function, namely, to locally provide higher boron levels for fuelling local growth (i.e., cell wall material) at those regions. In that study, however, we did not address the dynamics of the transporter regulation nor how nutrient homeostasis is achieved. Here, we investigate the dynamics of the transporters and their mutual feedback with the generated boron distribution. We do so by spatially focussing on the differentiated tissue region involved in xylem-uptake.

At the elongation and differentiation zone of the root, transporters possess a striking polar expression; BORs are located at the inside-facing membranes of the cells, while NIPs are concentrated to the outside facets (see Figure 1A,B). Although protein levels can present strong variation between cell files, the transcription of the transporters takes place throughout the entire root tissue, even for NIP5;1 (Figure 1—figure supplement 1). We therefore use the simplifying assumption that all cell files are intrinsically the same in respect to the potential of expressing the transporters, and variations arise solely as a consequence of the nutrient distributions.

![Figure 1.](https://cdn.elifesciences.org/articles/27038/elife-27038-fig1-v2.jpg)

**Figure 1.:** (A) Confocal microscope images of BOR1-GFP and GFP-NIP5;1 localisation in A. thaliana roots, revealing polar localisation of both transporters, facing inwards and outwards, respectively. Cell file identities are shown in the top-left with numbers representing, in increasing order, cell files from the outermost to the innermost cells, such as ep, epidermis; co, cortex; en, endodermis; va, vasculature. (B) Detailed view along a transversal section of the tissue at the proximal meristem. lrc, lateral root cap. (C) Schematic diagram of the NIP-BOR boron transport model, consisting of a transversal root cross-section composed of $n$ cells between the medium and the xylem. For a simplified A. thaliana model, we consider $n=4$. Depicted is a generic root model consisting of $n$ cell files, not showing all cells and cell walls in between $W_{2}$ and $W_{n−2}$ for illustration purposes. The model includes intracellular and apoplastic compartments, as well as membrane-based properties such as transporter activity and background permeability rates. $lw$: cell wall width; $lc$: cell width; $h⁢c$: cell height. For a full description of the parameters, see Table 1.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/27038/elife-27038-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Promoter activity of NIP5;1 was observed with transgenic plants expressing proNIP5;1-GUS. (A) From the root tip to differentiation zone. White bar, 100 μm. (B) Cross-section of elongation zone. Approximate root position from which the section was obtained is indicated by black line in (A). Bar, 50 μm.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/27038/elife-27038-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** Seedlings were germinated and grown on MGRL plates with various boron concentrations for seven days. GFP-NIP5;1 and BOR1-GFP in epidermis were observed with confocal microscope. Cell walls were visualised with PI staining. Scale bar is 20 μm.

Our analysis focuses on the transversal nutrient flow through the root that results from boron entering and leaving the different cell files transversally. Effectively, in our simple model, we only consider a single row of cells and, for simplicity, only four cell files over which boron is transported from the soil into the xylem (Figure 1C). To capture the dynamics of boron transport and transporter activities in root tissue, the model’s variables are the boron concentration in cells (C) and cell walls (W), and transporter activities of NIPs (N) and BORs (B) for each individual cell (n). The mutual dependency between these variables is described using ordinary differential equations (ODEs). For each cell file of the model, the transporters are produced at an equal rate, have the same transport potential, and are regulated in the same way. The modelled cells loosely map to the outermost epidermis (cell 1), the cortex (cell 2), the endodermis (cell 3), and finally to the pericycle/vasculature (cell 4). The last cell of the row is endowed with an upward convective flow, which captures the shootwards convective flow of the xylem. For reasons of simplicity, we consider these four cells to have equal dimensions, and make the same assumption for all intermediate cell walls (Figure 1C).

Given that transporter regulation can be observed in response to varying the boron conditions in the medium (Takano et al., 2005, Takano et al., 2006-06Takano et al., 2006-06, 2010; Miwa et al., 2013), (Figure 1—figure supplement 2), boron sensing underpinning those responses could either involve measurements of the intracellular concentration or involve measurements of the intercellular concentration (i.e., the levels within the apoplast). In the case of NIP5;1, we recently revealed that NIP5;1 mRNA degradation is triggered by boron-dependent ribosome stalling during the translation process (Tanaka et al., 2016). The boron-dependent degradation was also observed in an in vitro system without cell wall fraction, which suggests that the sensing mechanism depends on the cytoplasmic boron concentration. For the BORs the precise subcellular location of the boron sensing has not yet been determined, but it is reasonable to assume that the regulation is also responding to cytosolic boron levels, given that the purpose of the nutrient homeostasis is to keep the nutrient levels within the cell within bounds, and to this end directly sensing the cytoplasmic boron concentration is beneficial. In short, given the current knowledge, cytosolic boron sensing is the most parsimonious assumption.

Hence, our model assumes that all the boron transporters of a cell are regulated by the cytosolic boron concentration within that respective cell. Note that we loosely use the term ‘boron’ in our model to refer to both boric acid as well as borate. They can be found in a dynamic chemical equilibrium, $B(OH)_{3}+H_{2}O⟺B(OH)_{4}^{−}+H^{+}$, with a $pK$ value of 9.24 (Woods, 1996). Given that this process does not involve any enzyme kinetics, this distinction is not explicitly considered in our model. Moreover, we solely focus on the import of soluble boron (both boric acid and borate), not considering any boron that is bound to the cell wall.

The temporal dynamics of the soluble boron concentration within the cytosol ($C_{i}$) and in the cell walls ($W_{i}$, being the cell wall adjacent to the inward facing facet of cell $i$) is determined by their inflow and outflow from and to neighbouring compartments:

$$
C_{i}˙={(p+N_{i})⁢(W_{i-1}-C_{i})-B_{i}⁢C_{i}+p⁢(W_{i}-C_{i})}⁢\frac{1}{l⁢c},
$$



$$
W_{i}˙={p(C_{i}−W_{i})+(p+N_{i+1})(C_{i+1}−W_{i})+B_{i}C_{i}}\frac{1}{lw}.
$$

Here, $N_{i}$ and $B_{i}$ represent boron permeabilities due to, respectively, the bi-directional transport by NIPs and the directional transport by BORs within cell $i$. Transporter-independent boron permeability through the plasma-membrane is also taken into account, described by parameter $p$. To capture the tissue context, boundary conditions are set at both extremities of the transversal cell series. The outer cell wall of the first cell (cell 1) is in contact with medium. Given the rapid diffusion rate of boric acid in water, we assume that the boron concentration in the outermost cell wall ($W_{0}$) is the same as in the medium, constant over time. The xylem transport that occurs from roots to upper tissue is represented by a removal term, with rate $a$, attributed to the innermost cell ($i=n$) of the cell row:

$$
C_{n}˙=(p+N_{n})⁢(W_{n-1}-C_{n})⁢\frac{1}{l⁢c}-a⁢C_{n}⁢\frac{1}{h⁢c}.
$$

Assuming that transport activities are proportional to protein concentration, it follows that the dynamical regulation of NIP and BOR permeability ($N_{i}$ and $B_{i}$) are in direct proportion to the dynamics of their proteins (we will later show that our main insights do not depend on the assumption that the BOR transporter does not saturate under the range of concentrations here treated). It was therefore not necessary to introduce explicit variables for protein concentrations. Instead we directly use permeability, representing the protein concentrations and their regulation. The protein concentration, and thus the effective permeability, is determined by production and degradation rates.

As mentioned, accumulation of NIP5;1 mRNA is regulated through boron-dependent mRNA degradation. This suggest that the production of NIP5;1 protein is boron dependent. On the other hand, degradation of NIP5;1 protein is not found to be boron dependent (Takano et al., 2010; Tanaka et al., 2016). Thus, the levels of $N_{i}$ vary due to a production term that is dependent on cytosolic boron concentration and a constant degradation term:

$$
N_{i}˙=\alpha_{N}⁢\frac{k_{N}^{n_{N}}}{k_{N}^{n_{N}}+C_{i}^{n_{N}}}-ξ_{N}⁢N_{i},
$$

where $\alpha_{N}$ is the production rate, $ξ_{N}$ is degradation rate, and $n_{N}$ is the Hill coefficient capturing the boron-dependent inhibitory regulation.

Accordingly, given that BOR protein levels are regulated through boron-dependent degradation (Takano et al., 2005), but there is no evidence of boron dependent production, $B_{i}$ varies over time due to constant production and boron-dependent degradation terms:

$$
B_{i}˙=\alpha_{B}-ξ_{B}⁢(1+d_{B}⁢\frac{C_{i}^{n_{B}}}{k_{B}^{n_{B}}+C_{i}^{n_{B}}})⁢B_{i},
$$

where $\alpha_{B}$ is the production rate, $ξ_{B}$ the basal degradation rate, $d_{B}$ the maximum boron-independent degradation rate, and $n_{B}$ the Hill coefficient capturing the boron-dependent inhibitory regulation.

We wish to use this model to understand the significance, if any, of the swift transporter regulation. To assess the effects of regulation swiftness on transport, we therefore introduce a time-scaling factor $ϵ$, which multiplies both the entire $N_{i}˙$ and $B_{i}˙$ terms (Equations 6 and 7). To align ourselves with the current experimental evidence that indicates swift regulation of NIP5;1 on the mRNA level and of BORs on the protein level, we modulate the production rate and degradation rate for NIP5;1 and BOR1, respectively. However, changing production rates of NIPs through a factor $ϵ$ without changing the degradation rate would result in changes of the overall protein concentration which might influence the system’s behaviour, not due to the swiftness of the regulation but due to the changes in equilibrium protein concentration. This also holds for the BOR regulation. Thus, to avoid such possible undesired effects, the time-scaling factor multiplies the entire right-hand side of the dynamics:

$$
N_{i}˙=ϵ_{N}⁢(\alpha_{N}⁢\frac{k_{N}^{n_{N}}}{k_{N}^{n_{N}}+C_{i}^{n_{N}}}-ξ_{N}⁢N_{i}),
$$



$$
B_{i}˙=ϵ_{B}⁢{\alpha_{B}-ξ_{B}⁢(1+d_{B}⁢\frac{C_{i}^{n_{B}}}{k_{B}^{n_{B}}+C_{i}^{n_{B}}})⁢B_{i}}.
$$

We define $ϵ=1$ as representing the swiftness of regulation in the wild type scenario, while reducing $ϵ$ allows us to simulate behaviours that would occur with less rapid regulatory dynamics, and increasing $ϵ$ allows us to consider even higher swiftness of regulation than experimentally observed. Note that the regulation of the transporter activity by cytosolic boron concentrations occurs through a sigmoidal relationship, in which $k_{B}$ and $k_{N}$ are the boron concentrations at the half maximum of the Hill function, defining the sensitivity of the response to the boron concentration. We set $k_{B}≃30k_{N}$, consistent with our observations that the sensitivity of BOR expression is much less than that of NIP5:1 (Figure 1–Figure supplement 2), but will also show that our results do not require large differences between these two parameters.

We have assessed what is the biologically acceptable range for each parameter, based on the available literature (see Material and methods for details). Default parameter values were chosen to lie within these valid ranges, and are given in Table 1.

### From steady state flows to oscillatory dynamics

When regulation swiftness lies within the experimentally observed regime ($ϵ_{B}=ϵ_{N}=ϵ=1$), a constant flow of boron that is transported across the root ensues (Figure 2). Boron concentrations within the cells ($C_{n}$) remain constant over time. This steady state behaviour, however, is disrupted when the transporter regulation swiftness is decreased ten-fold ($ϵ=0.1$). Oscillations in the boron concentration arise in all cells, but most strikingly in the endodermis (cell 3) and cortex (cell 2) (Figure 2A), as well as in the cell walls (Figure 2B). Decreasing the transporters’ regulation swiftness even further ($ϵ=0.01, 0.001$) consistently enhances the amplitude of such oscillations, and enlarges their periods (Figure 2A,B). We conclude that even when environmental boron levels ($C_{0}$) and xylem activity ($a$) remain constant, simply deviating from the rapid experimentally observed transporter’s regulation swiftness is sufficient to push the boron transport system into an oscillatory dynamics.

![Figure 2.](https://cdn.elifesciences.org/articles/27038/elife-27038-fig2-v2.jpg)

**Figure 2.:** Time development in the four-cell NIP-BOR model of the boron concentration in the cells (A) and cell walls (B), and of the transporter activity of BOR (C) and NIP (D). The simulations are started using the default parameter setting (Table 1). At the time points 48, 72 and 96 hr, the parameters determining the transporter regulation dynamics ($ϵ_{N}$ and $ϵ_{B}$) were each time reduced to one tenth of their previous value. $C_{1}$ to $C_{4}$ are the boron concentrations in the outermost cell 1 up to the innnermost cell 4. $W_{i}$ represents boron concentration in cell wall fraction between cell $i$ and cell $i+1$ and $N_{i}$ are transporter activity of BOR and NIP in cell $i$, respectively.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/27038/elife-27038-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Robustness of behaviour regarding choice of $k_{B}$ parameter.(A, B) In the standard four-cell model, cellular boron concentrations still present traffic-jam-like behaviour at reduced transporters’ regulation dynamics swiftness ($ϵ$) when $k_{B}$ is reduced to (A) $k_{B}=400$ μM; or (B) $k_{B}=250$ μM. (C) At very low values, here $k_{B}=100$ μM, the concentrations remain stable even at reduced transporters’ regulation dynamics swiftness ($ϵ$), due to the trivial result that such low values obstruct boron uptake by the system. (D) Equilibrium relative throughput values, as a function of $k_{B}$, with unity representing the throughput for $k_{B}=600$ μM. Flow stabilisation at reduced transporters’ regulation dynamics swiftness for low $k_{B}$ values is basically due to a 5-fold reduction in throughput, comparable to real traffic jams not occurring during off-peak hours. Note that for all panels $k_{N}=20$ μM, its standard value.

The reason the cells undergo such dramatic concentration variations at lower regulation swiftness can be intuitively linked to the accompanying changes in transporter levels which also ensue (Figure 2C,D). They are initially triggered by minute fluctuations in the concentrations, but then cause increasingly larger changes in cytosolic and apoplastic concentrations. It is not immediately clear, however, how it depends on either the NIP or BOR transporter regulation, why regulation swiftness exacerbates oscillation amplitudes and how their interdependencies either produce stable flows or unstable oscillations that propagate throughout the tissue. What we can already conclude though, is that within a polarised tissue rapid transport dynamics are necessary to ensure flux homeostasis and avoid instabilities in concentration levels. But to fully understand the process we will first observe how in the model the steady flow regime behaves in terms of transporter expression levels when we assume that the regulatory dynamics are as swift as experimentally observed.

### Parsimonious model, under wild type dynamical settings, generates stable transporter expression

Given that our question is focused on the possible advantages of swift transporter regulation within a polarised tissue context, our model purposely ignored details of tissue-specific regulation, using the simplifying assumption that all cells are endowed with the same potential of expressing transporters. This assumption may initially seem at odds with the actual distinct GFP levels of the GFP-tagged proteins (Figure 1B), which qualitatively indicates stronger BOR1 expression in the epidermis and endodermal files and pronounced NIP5;1 expression in the outermost cell file (lateral root cap or epidermis) only. It was therefore interesting to observe that our parsimonious model could already account for general features of the the observed transporters’ expression patterns (Figure 2C,D) solely as a consequence of the relative positioning of the cells within the cell row: in the model, NIP only becomes highly expressed in the outermost cell, the epidermis ($N_{1}$, representing NIP5;1 in cell 1, is by far the highest variable in the steady flow case). These relative levels are in qualitative agreement with the experimental findings regarding NIP5;1. Moreover, in contrast to this strong expression in the epidermis, in the model NIPs are present at much lower amounts in all the other inner cell files (cell 2, cell 3 and cell 4), again qualitatively similar to the experimental observations. These model results can be understood as follows. Although all in silico cells share the same intrinsic properties, as a consequence of NIPs acting as permeability facilitators rather than directional transporters, it is impossible for the cell file in contact with the medium (cell 1, the outermost cell file, that is, epidermal cell) to reach higher concentrations than the level in the medium. Only the next cell inwards, cell 2, is capable of reaching higher levels, due to the directed polar action of the BORs. The inevitable low boron levels in the epidermis give rise to the observed lack of NIP downregulation within the first cell file, and hence to its preferential expression.

The expression patterns of the active exporters, BORs, are quite different from NIP5;1, but again there are similarities between the model results (B values) and confocal images, with BORs distinctly expressed in the epidermis (cell 1) at the highest levels, in the cortex (cell 2) at high levels, whilst in the endodermis it is relatively weaker (cell 3) (Figure 1B). The model’s qualitative correspondence between the transporter expression patterns and those experimentally observed suggests that concentration-dependent regulation is at least sufficient for such expression patterns to arise. Corroborating this, GUS expression under the NIP5;1 promoter is indeed present in the inner root tissues, albeit the NIP5;1 protein levels in those cells are very low, supporting the notion that these files are likely responsive and capable of expressing NIP5;1, but inhibited to do so by the boron levels that arise due to the cells’ positioning within the tissue (Figure 1—figure supplement 1). However, these results, while suggesting sufficiency of our parsimonious assumptions in relation to observed transporter levels, do not offer evidence that tissue-specific regulation is not occurring. At most, the qualitative matches justify, at first instance, that the model is kept simple, without the need of introducing ad hoc tissue-specific dependencies, when exploring the effects transporter regulation dynamics. Furthermore, these results indicate that under our experimentally observed parameter values, the system presents steady nutrient throughput and constant cellular concentrations and transporter levels over time.

### The spatial nature of the unstable flows: traffic-jam-like behaviour

We next investigated more carefully the spatial-temporal characteristics of the oscillatory behaviour that arises when transporter swiftness is decreased (Figure 3A). Kymographs make it visually clear that oscillations in the individual cells are in fact spatially coupled, manifested as a boron wave that propagates backwards over the tissue, that is, the pulse moves in the direction contrary to the nutrient flow itself. The initiation of the instability, as seen by the first peak in concentration, occurs close to the xylem (i.e., the last cell, here, cell 4), followed by a strong rise in endodermal concentrations (in cell 3) around 90 min later. Due to boron’s inhibitory influence on the transporters, this intracellular rise leads to a decrease in both NIPs and BORs within that cell. This transporter downregulation causes a drop in boron throughput across that cell, leading to an accumulation of boron in the adjacent, outward facing, cell wall. Background permeability rates along the plasma membrane allow this apoplastic rise in concentrations to trigger an increase boron concentrations in the next outermost neighbouring cell, in this case, the cortex cell (cell 2). Cortex concentration levels thus rise, again triggering a shutdown of transporters, causing the same process to ensue in a spatially coupled manner in the outermost cell, the epidermis. In the epidermis, however, boron levels can never rise above the soil concentration levels, as discussed previously, such that the backward travelling wave loses its amplitude and terminates. The overall process is observed to be cyclical, with levels rising again close to the xylem, until a next wave is triggered in the innermost cells (Video 2). Moreover, we found that such traffic-jam-like behaviour is robust when smaller differences between $k_{B}$ and $k_{N}$ are considered (Figure 2—figure supplement 1A–C), as long as $k_{B}$ is sufficiently large as not to too strongly interrupt boron throughput through the tissue altogether (Figure 2—figure supplement 1D). Obviously, if $k_{B}$ is too low, and traffic-jam-like behaviour are prevented, the plant would also not be able to take up boron, thus, this would be a parameter setting that is biologically irrelevant. Therefore, although our interpretation of the experimental results (Figure 1—figure supplement 2) suggest larger differences between $k_{B}$ and $k_{N}$, given that these are indirect estimates that rely on underlying assumptions, this robustness analysis shows that, within a biologically reasonable window, our results hold even when $k_{B}$ were to be smaller.

![Figure 3.](https://cdn.elifesciences.org/articles/27038/elife-27038-fig3-v2.jpg)

**Figure 3.:** (A–G) Kymographs of boron concentration in NIP-BOR models consisting of four (A) up to ten (G) cells. Boron concentrations in cells and cell walls are represented through a heat map colouring with development over time displayed vertically. Boron concentrations exceeding 3000 μM are displayed using the same red colour. Regions of high concentration can be observed to displace to the left, contrary to the direction of boron flow due to the transporter activity. Default parameters were used (Table 1), with exception of the transporter regulation swiftness, $ϵ_{N}$ and $ϵ_{B}$, which were both set to 0.01. Above each kymograph a schematic diagram of the tissue structure is shown, corresponding to that of Figure 1C.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/27038/elife-27038-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Boron concentrations in the cells and cell walls of a 100-cell NIP-BOR ring model, represented through a heat map colouring and time development shown vertically. The default parameters were used (Table 1), with exception of the transporter regulation swiftness, $ϵ_{N}$ and $ϵ_{B}$, which were both set to 0.01.

We next wondered if this traffic-jam-like effect dissipates over larger tissues. Our four-cell model is a simplified representation of A. thaliana, which has less cell files between the epidermis and the xylem than most other roots of experimental plant models. However, if one distinguishes the pericycle from the vasculature, a five-cell model would be more appropriate. We show that the variables of the five-cell model present similar dynamics as our default model when BOR transporter regulation is lowered to 400 μM (Figure 4—figure supplement 2A–D). Lowering $k_{B}$ slightly stabilises the dynamics (as shown in Figure 2—figure supplement 1), which counteracts increasing destabilisation of the constant flow regime when the number of cell files in the tissue increases. Conversely, given that this renders smaller tissues (such as our default four-cell model), more robust against traffic-jam-like behaviour, our default setting should be regarded as a worse-case scenario for such dynamics to occur, rather than being a special case. To further appreciate tissue-size dependencies, and explore the generality of these effects for other plants which might have highly deviating cell file numbers, we gradually increased the in silico tissue from 4 to 10 cell files. Figure 3B–G shows that the phenomenon is conserved irrespective of the number of cells between the medium and the convective xylem flux. Larger transversal tissue segments are able to generate higher wave amplitudes, but in all cases the peak in boron propagates contrary to the nutrient flow with approximately the same speed. The same phenomenon was still observed even when the model contained 100 cell files (Figure 3—figure supplement 1), suggesting that large tissues do not prevent these effects from occurring, but rather increase its likelihood.

In short, when transporter regulation swiftness is sufficiently slow, due to the downregulation of transporters under the control of increased boron concentrations, a traffic jam-like behaviour emerges: a high boron concentration peak appears, correlating with locally lower transport rates, triggering a low-transport high-boron wave that back-propagates from cell to cell in the direction contrary to the transport polarisation direction within the tissue. This occurs independently of the size of the plant tissue under consideration.

We next studied the importance of the relative dynamics of BOR and NIP regulation to trigger these phenomena, that is, which of the processes have to be sufficiently slow.

### Traffic jam-like behaviour depends on swift regulation of both transporters

Under what conditions and parameter values for transporter regulation rates does the traffic jam phenomenon manifest itself? In our previous simulations, we simultaneously decreased the swiftness of both the NIP and the BOR regulation. Oscillations in boron concentration then arose due to a change in stability of both the flow and steady state of boron concentrations. We next probed the system’s stability while varying the regulation swiftness of the NIPs and BORs independently. This was done by analysing the equilibrium of the simplified, A. thaliana inspired, four-cell model. We linearised the ODEs around the equilibrium using a Taylor expansion, and then evaluated the stability of the equilibrium in terms of the largest eigenvalue, for 40,000 different parameter combinations. The phase-portrait that emerges (Figure 4A) shows a large region in which the system becomes unstable and oscillations arise (indicated in red), as well as a region in which sufficient regulation swiftness ensures that the system is stable and oscillations do not develop (indicated in blue). For the stable (blue) parameter settings, any perturbation dampens out (Figure 4B), whereas for parameter settings within the red region, oscillations dominate. The frequency of the oscillations is determined by a relative lack of swift regulation for both transporters, as shown by the colour map in Figure 4. This phase diagram is qualitatively unaffected for the five-cell model at $k_{B}=$400 μM (Figure 4—figure supplement 2F). Furthermore, we also checked if saturation in the activity of the BOR transporter might obstruct or stabilise the system against the appearance of the oscillations. (The NIPs, being a channel, should be less prone to undergo concentration-dependent saturation effects in permeability.) Contrary to this, we found that such a saturation in permeability of the BOR transporter does not change the likelihood or transporter-response dependency to present traffic-jam-like behaviour, but rather, when they arise due to slow dynamics, the oscillations present much higher amplitudes in concentration variations, with peak boron levels becoming more than twice as high due to the transport saturation (Figure 4—figure supplement 3).

![Figure 4.](https://cdn.elifesciences.org/articles/27038/elife-27038-fig4-v2.jpg)

**Figure 4.:** (A) Diagram showing combinations of transporter regulation swiftness ($ϵ_{N}$–$ϵ_{B}$ plane) for the four-cell NIP-BOR model for which stable flows (blue) or oscillations, that is, ‘traffic jams’, (red) ensue. (B) Oscillatory periods of the boron concentration variation. The white curved line represents the boundary between the stable and the unstable region, equivalent to the boundary between the blue and red area in (A). Four insets plot $C_{2}$ [μM] over time [hour] for the indicated parameter values (white dots), illustrating the behaviour of the model at those points within the $ϵ_{N}$–$ϵ_{B}$ plane.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/27038/elife-27038-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Numerically calculated oscillation period for the four-cell NIP-BOR model, shown on the $ϵ_{N}$–$ϵ_{B}$ plane. This figure should be compared to the analytic diagram inferred from the imaginary part of the largest eigenvalue, shown in Figure 4B. Except for $ϵ_{N}$ and $ϵ_{B}$, which are varied, default parameters are as given in Table 1.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/27038/elife-27038-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A–D) Time development in the five-cell NIP-BOR model of the boron concentrations in the cells (A) and cell walls (B), and of the transporter activity of BOR (C) and NIP (D). Default parameter setting (Table 1) was used, except for $k_{B}$, which was set to a lower value of 400 μM. At the time points 48, 72 and 96 hr, the parameters determining the transporter regulation dynamics ($ϵ_{N}$ and $ϵ_{B}$) were each time reduced to one tenth of their previous value. $C_{1}$ to $C_{5}$ represent boron concentration in cell 1 (‘epidermis’); cell 2 (‘cortex’); cell 3 (‘endodermis’); cell 4 (‘pericycle’); and cell 5 (‘vasculature’), respectively. $W_{i}$ represents the boron concentration in the cell wall fraction between cell $i$ and cell $i+1$ and $N_{i}$ are the transporter activity of BOR and NIP in cell $i$, respectively. (E) Diagram showing combinations of transporter regulation swiftness ($ϵ_{N}$–$ϵ_{B}$ plane) for the 5 cell NIP-BOR model for which stable flows (blue) or oscillations, that is, ‘traffic jams’, (red) ensue. (F) Oscillatory periods of the boron concentration variation. The white curved line represents the boundary between the stable and the unstable region, equivalent to the boundary between the blue and red area in (E). Four insets plot $C_{2}$ [μM] over time [hour] for the indicated parameter value combinations (white dots), illustrating the behaviour of the model at those points within the $ϵ_{N}$–$ϵ_{B}$ plane.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/27038/elife-27038-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (A–D) Time development of (A) cellular and (B) cell wall boron concentrations as well as (C) BOR and (D) NIP levels in the 5 cell NIP-BOR model in which we additionally consider the saturation of BOR transporter permeability. We altered the BOR-mediated flux ($J$) as a function of BOR protein levels at the membrane ($B$) and the intracellular boron concentration ($C$), from the standard linear regime, $J_{i}=B_{i}⁢C_{i}$, into a Michaelis-Menten saturating form given by $J_{i}=B_{i}⁢\frac{C_{i}}{1+C_{i}/c_{B}}$, in which $c_{B}$ is the Michaelis constant, the boron concentration at which the flux becomes half as large due to saturation, as well as the concentration at which the flux reaches its half-maximum value. The simulations use the default parameter setting (Table 1), but introduce the above saturation in BOR transport with the Michaelis constant set to $c_{B}=1000$ μM. The time dynamics of the system’s variables (A–D) show that oscillatory behaviour remains dependent on the transporters’ regulation dynamics swiftness ($ϵ_{N}$ and $ϵ_{B}$) in a very comparable fashion, but that the amplitude of the oscillations in these variables becomes much larger than when saturation in BOR permeability is not considered. For further details regarding this figure, see Figure 2.

From this combined analysis it becomes apparent that the parameter values we derived to capture wild type dynamics of transporter regulation (i.e., point 1,1) fall into the stable regime. Hence, the wild type system is robust against perturbations and does not present traffic jam-like behaviour. However, independent small reductions from these values in either NIP or BOR regulation rate can cause the tissue to experience oscillations. Not only does the analysis reveal that both transporters are required to present a rapid response, and that this is independent of the BOR-dependent fluxes becoming saturated, but their combined swiftness is synergistic: if one transporter is extremely fast, the other can be bit slower than what is otherwise needed. However, for any parameter setting, a certain speed in responsiveness needs to present to prevent oscillations.

### Physiological implications of flow instabilities for the root system

Traffic jams are commonly experienced by vehicle drivers in urban areas. In terms of human transport, traffic jams are an undesirable outcome as they reduce the throughput through the highway and increase the time to reach the destination. Traffic jams displace backwards in space (contrary to the flow) while giving rise to increased car densities at the specific location of the traffic jam (Kesting and Treiber, 2013). All those properties can also observed in our plant tissue model, namely diminished throughput of boron from the soil to the xylem and backwards propagating pulses of locally increased boron concentrations within cells. Moreover, again analogous to real-life traffic jams, traffic-jam-like behaviour in plant nutrient uptake has undesirable implications in the biological context as well. High intracellular boron is detrimental to plant health as it causes DNA damage and ultimately causes cell death (Sakamoto et al., 2011-09). Plants are therefore likely to have evolved mechanisms to avoid high intracellular boron levels to limit boron-induced damage. Lower throughput across the root implies reduced xylem loading and hence a reduction in the boron absorption efficiency, critical for plant growth at low boron conditions.

To better quantify the magnitude of these effects, we performed a simulation screen to evaluate the expected physiological impact of the transporter swiftness in the form of increased boron levels within the cells due to the instabilities, as well reduction in throughput (see Materials and methods for details). We observe increasing maximum levels in boron concentration for slower regulation swiftness (Figure 5A), as well as higher fold-changes in boron concentration (Figure 5B). This suggests that sufficiently rapid transport regulation is important to reduce the risk of DNA damage when either considering absolute concentrations or the increase over the basal equilibrium boron concentrations. Moreover, under the conditions in which traffic jams and large-amplitude variations occur, we measured a considerable reduction in total throughput through the tissue (Figure 5C). In our default model we assume the BOR transporter-driven flux to be linear with the cellular boron concentration. If we instead consider Michaelis-Menten saturated BOR transport (using a biologically reasonable Michaelis constant — the boron concentration at which the flux becomes half as large due to saturation, as well as the concentration at which the flux reaches its half-maximum value — of $c_{B}=$1000 μM) the system’s capacity of uptake and throughput only marginally decreases. In stark contrast, the detrimental effects of the instabilities that arise due to slowing down the regulatory dynamics are amplified when BOR saturation is considered (see details of saturation implementation in the caption of Figure 4—figure supplement 3). The impact of the traffic jams becomes much more severe, with peak levels during the concentration fluctuations more than twice as high as the default scenario (compare Figure 2 to Figure 4—figure supplement 3). This is a direct consequence of the cell not being able to effectively efflux boron when intracellular levels spike. Taken all into consideration, we infer that selective pressures operating on the root’s capacity to absorb boron optimally and robustly could result in the system evolving to a regime of rapid regulation of transporters.

![Figure 5.](https://cdn.elifesciences.org/articles/27038/elife-27038-fig5-v2.jpg)

**Figure 5.:** In the BOR-NIP model with 4 cells, physiological output for the simulation period between 24 and 48 hr was displayed on the $ϵ_{N}$–$ϵ_{B}$ plane. (A) Maximum boron concentration in any cell. (B) Maximum amplitude variation in boron concentration for any cell (highest boron concentration/lowest boron concentration). (C) Average throughput, measured as the output from the last cell, which represents the xylem, between 24 and 48 hr of simulation.

### Traffic jam-like behaviour is independent of bottlenecks in the tissue context

Our model thus far consisted of a segment of polarised tissue, of a variable number of cell files, linking the soil to the xylem via a polar flow of nutrients. Consequently, both soil and xylem, although presenting stable characteristics over time, do constitute abrupt boundary conditions: the first sets a constant medium concentration, and the second presents a constant convective flow away from the transversal section. We thus questioned if these boundary conditions are responsible for triggering the traffic jam-like regime that arises under lower rates of transport gene regulation. During the last decades a similar discussion has been taking place regarding what triggers the analogous traffic jams in discrete macroscopic systems such as road networks (Kesting and Treiber, 2013). Although traffic jams are readily triggered by bottlenecks (such as road obstructions, roundabouts, etc.), theoretical models of traffic jam behaviour predicted that the collective systems parameters alone could be sufficient to render the free flow state unstable. It depends on the car density exceeding a critical value as well as how speed relates to the local car density. To prove this theoretical insight, Sugiyama et al., 2008 developed an experiment in which cars were confined to move on a homogeneous circular road. Above a critical car density they observed a transition from a free flow to a traffic jam state, due to the collective effect of the vehicles. They concluded that, although no bottleneck was present, the intrinsic parameters of the system rendered it unstable, such that the smallest of naturally occurring fluctuations was enhanced to disrupt the free flow. This experiment illustrates the non-intuitive notion of traffic jams being generated spontaneously under certain critical parameter regimes.

Inspired by this strategy, and for us to be able to rule out that the origin of the nutrient-flow instabilities within the plant tissue is provided by the soil boron concentration or the xylem flow, we constructed an in silico polarised tissue composed of 6 cells, wrapped up into a ring, that is, the first cell is connected to the last. The ring structure avoids boundary conditions (i.e., bottlenecks) and offers a scenario in which uninterrupted flows (either stable or unstable) can be studied. We allow the dynamics of the polarised tissue to evolve from an initial situation in which concentrations are homogeneous over the whole ring-tissue. When transporter regulation is as swift as in wild type (Figure 6A), a steady flow with no oscillation in the concentrations is observed. When transporter regulation swiftness is decreased to sufficiently low values as to cause unstable flows (as derived from the analysis shown in Figure 4), oscillations arise. After an initial period in which the flows seem constant, random numerical fluctuations in the simulation bring forth a rise of boron concentration in a random cell, which, due to the mechanism of inhibition by boron of the boron transporters, results in local interruption of flows and the back propagation of the boron concentration pulse (Figure 6C,D, Video 1). The frequency of these oscillations is decreased, and the wave broadened, as the regulation speed is decreased (Figure 6C,D). These simulations demonstrate that the unstable flow regime — which we now can conclusively eliminate as being triggered by boundary conditions — continuously self-propagates.

![Figure 6.](https://cdn.elifesciences.org/articles/27038/elife-27038-fig6-v2.jpg)

**Figure 6.:** Kymographs of the boron concentration in the cells and cell walls of the six-cell NIP-BOR ring model, represented by heat map colours and time development shown progressing vertically. The default parameters were used (Table 1), with $ϵ_{N}$ and $ϵ_{B}$ varied as specified for each kymograph.

![Video 1.](https://cdn.elifesciences.org/articles/27038/elife-27038-video1.mp4.jpg)

**Video 1.:** Time is indicated above the simulation, and dynamics show an initially constant flow, with low boron concentrations in all cells. Due to the intrinsic instability of the system, minute numerical noise generates boron peaks in the cells, a pattern which propagates counterclockwise (i.e., against the flow) through the tissue. Cytosolic boron concentrations, as well as those in the cell walls between cells, are depicted through the colour bar shown in the movie. Transporter levels (of both BORs and NIPs) are characterised through the colour changes along the radial membranes, again depicted through the colour bars shown in the movie.

### Mechanisms underlying rapid regulation

Our model analysis highlights the requirement for rapid regulation of both BOR1 and NIP5;1 transporters to stabilise boron flux through root cells and minimise risks associated with transient high levels of boron in cells, both considered to be important constraints for the plant. Current experimental evidence shows rapid downregulation of the BOR1 protein (Takano et al., 2005; Takano et al., 2010), and NIP5;1 transcript (Tanaka et al., 2011; Tanaka et al., 2016), although the fine details regarding the molecular mechanisms remain to be elucidated. The modelling however predicts permanently fast regulation, not only when boron levels drop, but also when they remain constant. This is however difficult to prove with techniques that we have used previously.

To experimentally explore the regulatory swiftness of the bidirectional transporter NIP5;1 at the transcript level, we used single molecule RNA FISH (smFISH). In this method ~40 complementary fluorescently labeled oligonucleotide probes are used to visualise RNA at the cellular level (Raj and Tyagi, 2010; Duncan et al., 2017). Initially, we combined probe sets to detect mRNA for both NIP5;1 and the housekeeping gene PP2A (specifically A3 scaffolding subunit of PP2A, At1g13320) and compared abundance and cellular distribution (Figure 7A) (Czechowski et al., 2005; Duncan et al., 2016). Consistent with published smFISH experiments, PP2A mRNA appeared evenly diffused throughout all cells (Figure 7B) (Duncan et al., 2016). In contrast, we observed many nuclear accumulations of NIP5;1 RNA that were accompanied by few cytoplasmic mRNA copies (125 nuclear accumulations in 149 cells) (Figure 7B). Large nuclear smFISH RNA signals have been reported for highly transcribed genes. They are typically accompanied by many copies of cytoplasmic mRNA and considered to represent bursts of transcription, where multiple Pol II associate with a locus (Battich et al., 2015; Duncan et al., 2016).

![Figure 7.](https://cdn.elifesciences.org/articles/27038/elife-27038-fig7-v2.jpg)

**Figure 7.:** (A) Schematic of probes used to detect NIP5;1 intron 1 (red), NIP5;1 exonic (green) and PP2A exonic (red) RNA. (B) Representative images of cells showing NIP5;1 (green) and PP2A (red) exonic RNA distributions. (C) Representative images showing co localisation of exons (green) and intron 1 (red) regions from NIP5;1 nascent transcripts. DNA labelled with DAPI (blue). Scale bar: 10 μm in (B) and 1 μm in (C).

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/27038/elife-27038-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** Mature mRNA and pre-mRNA abundance was separately quantified by qRT-PCR, with probes specific to mature mRNA (probe 1 and 5 for NIP5;1; 1 and 3 for PP2A) or pre-mRNA (probe 2 and 3). (A) Probe design for mature- and pre-mRNA specific qRT-PCR. Arrowheads indicate positions and directions of each probe. Probe 4 and 5 were used for normalising concentrations of standard DNA fragments. For details, see Materials and methods and Table 3. (B) Ratio of abundance of mature mRNA/pre-mRNA abundance for NIP5;1 and PP2A. Asterisk indicates significant difference at p<0.05 using Welch’s t-test.

Arabidopsis genes that contain introns must undergo pre-mRNA splicing before mature transcripts are translated (Morello and Breviario, 2008-06). Co-transcriptional splicing is common for plant genes and this ensures that introns are removed from the pre-mRNA and rapidly degraded close to the site of transcription (Reddy et al., 2013-10). This system allows intronic smFISH RNA labelling to be used as an effective method to identify loci actively engaged in transcription (Levesque and Raj, 2013; Duncan et al., 2016; Rosa et al., 2016). We used this approach to further investigate NIP5;1 transcription and found 72% of cells with at least one NIP5;1 intron signal. As expected, this was lower than the 84% previously reported for the more highly expressed gene PP2A (Duncan et al., 2016). When we combined NIP5;1 exonic and intronic RNA smFISH probe sets we observed 92.5% of nuclear accumulations co-localised with intron signals ($n=111$) (Figure 7C). This is consistent with the nuclear accumulations representing sites of ongoing RNA production and degradation, rather than separate nuclear storage compartments.

The suggested rapid degradation of NIP5;1 mRNA after transcription was further supported by an independent approach, in which we performed qRT-PCR using probes specific to pre- or mature mRNA to measure mature mRNA/pre-mRNA ratio in root cells. The average mature mRNA/pre-mRNA ratio of NIP5;1 was less than 25% of that of PP2A (Figure 7—figure supplement 1). In accordance with our interpretation of the smFISH results, this again indicates a high degradation rate of NIP5;1 mRNA.

In light of our model predictions, these observations combined point to a highly dynamic sensing system where RNA is turned over at or near the site of transcription, to limit NIP5;1 levels when boron is above a threshold level. We recently demonstrated that NIP5;1 transcript degradation occurs through ribosome stalling, triggering degradation in the cytoplasm (Tanaka et al., 2016). We also identified an upstream sequence that promotes mRNA degradation, but does not trigger ribosome stalling. The data presented in Figure 7 provides evidence of mRNA degradation occurring close to the site of transcription. Together these results suggest that mRNA degradation could occur through two coordinated B-dependent processes; one where cytoplasmic degradation is triggered by ribosome stalling and another localised in the nucleus where RNA is turned over at the site of transcription. Relief of this repression could then ensure rapid boron uptake when required. Our model suggests that such a dynamic mRNA production/decay process could support the necessary swift boron-mediated transporter regulation critical for the evolution of controlled, stable boric acid flows through polarised tissue.

These results also support the notion of a constant turnover (both producing and breakdown the RNA) occurring for regulating NIP5;1 transcript levels. We propose that this ‘wasteful’ process can now be understood in light of constraints of stable flows through polarised tissue. Interestingly, the regulation of the transporters is of a different nature, one predominantly on the level of protein degradation (BOR1), the other occurring on the level of transcript accumulation (NIP5;1).

### Conclusion

We conclude that the experimentally observed swiftness of boron transporters’ boron-mediated downregulation can be understood as a necessary mechanism to maintain optimal constant xylem loading rates over time, while also avoiding DNA damage due to oscillations within cells. One could argue that without a substrate-mediated downregulation of the transporters there would not be the need to avoid traffic jam-like behaviour through swift regulatory dynamics in the first place. However, were the system not to present the regulation, the plant would be unable to shield itself from toxic soil boron levels (Figure 8A) and be much less efficient in growing at low soil boron levels (Figure 8B). Thus, some kind of inhibitory regulation necessarily has to be present, to ensure plant plasticity under different environmental conditions. As a consequence, the speed of the transporter downregulation needs to be sufficiently high. We showed that this is an intrinsic requirement, simply because boron transporters are polarly located: The requirement itself does not depend on external boron fluctuations in the medium, number of cell files composing the root tissue, possible saturable activity of the transporter itself nor the magnitude, location or strength of the xylem flow.

![Figure 8.](https://cdn.elifesciences.org/articles/27038/elife-27038-fig8-v2.jpg)

**Figure 8.:** (A) Maximum boron concentration; and (B) throughput, for the four-cell NIP-BOR model, plotted for varying boron concentrations in the medium. The default parameters are used (Table 1). When transporter regulation is not considered, NIP and BOR activity were fixed to their unregulated equilibrium value in the wild type model, namely $\frac{\alpha_{N}}{ξ_{N}}$ and $\frac{\alpha_{B}}{ξ_{B}}$.

Our study has been based on the well-characterised system of directed boron transport, owing to the richness in quantitative experimental measurements regarding BOR and NIP regulation. However, the implications of our derived insights apply to any system in which the dynamics of polar transport of a given substance relies on an inhibitory feedback between the concentration of that substance and its local transport rate. For example, the phosphate and iron transport systems present both polar transporters as well as substrate-dependent regulation, serving as candidates for such phenomena and dynamical constraint avoidance. In the case of the phosphate transport system, transporters localised to the outer side of the epidermis are responsible for uptake (LePT1 and LePT2, Liu et al., 1998), and they have recently been found to carry a domain possibly involved in phosphate sensing which leads to rapid degradation of phosphate transporter in a phosphate-dependent manner (Gu et al., 2016). Similar regulation is also reported for the iron (Fe) transport system, where polar accumulation of IRT1, a major Fe transporter for Fe uptake into roots, is regulated in an Fe-dependent manner (Barberon et al., 2014). Even other transport systems which do not shuttle nutrients might display this sort of instability, such as polar auxin transport, for which stable flows might also require fast response dynamics regarding the activity of auxin importers and efflux facilitators (Robert and Friml, 2009). Indeed, for any polarised tissue in which adaptive regulation of transport levels is necessary we can expect to find intrinsic temporal constraints operating to ensure that steady state flows are maintained and large fluctuations avoided.

In molecular terms, we discovered that although both transporters are predicted to work synergistically and are both required to be effectively similar in regard to rapid regulation, their regulations are biologically encoded in unique ways. We here experimentally focused on the regulatory swiftness of the bidirectional transporter NIP5;1, and found strong evidence that it constitutes a system in which production is maintained high but degradation is rapidly controlled transcriptionally, allowing for the necessarily rapid boron-dependent response. It will be interesting to speculate what underlying reason, if any, has caused the directed exporter, BOR1, which is similarly known and required to be swiftly regulated, to be controlled on a biologically distinct level.

For this work, the analogy with motorway traffic jams was helpful to build an understanding of principles of polarised transport dynamics, albeit both systems obviously deviate in important aspects. Boron concentrations are continuous and can reach arbitrarily high levels, as opposed to (incompressible) cars. Yet, the discrete nature of cells and their regulated polar transporters, combined with the boron-dependent inhibition of the transporters themselves, resembles cars slowing down in response to busy regions along the motorway. Moreover, in both systems highly sensitive responses can prevent jamming (Sugiyama et al., 2008). We therefore propose that the notion of traffic jams can be universally instructive and helpful for biologists considering physiology and regulated growth through polarised transport in plants, as well as for future efforts to enhance plant growth under diverse environmental conditions.

## materials and methods

### Observation of protein localisation of boron transporters

For plant culture, MGRL medium was used (Fujiwara et al., 1992) supplemented with 1% sucrose and solidified with 1.5% gellan gum. For Figure 1, A. thaliana transgenic lines carrying BOR1-GFP (Kasai et al., 2011) and GFP-NIP5;1 #8 (Tanaka et al., 2011) were germinated and pre-incubated for 5 days on normal MGRL medium plate, and then grown for 2 days on MGRL plates with 0.3 μM boric acid. For Figure 1—figure supplement 2, plants were grown for seven days on MGRL medium with the indicated boric acid concentrations. Images were captured with a confocal microscope (FV1000, Olympus, Japan). GFP fluorescence was observed with 473 nm excitation and 510 nm emission. Cell wall was stained with 10 μg/mL propidium iodide aqueous solution for 3 min, and observed with 559 nm excitation and 619 nm emission.

NIP5;1 promoter activity was observed using a transgenic A. thaliana strain carrying NIP5;1 promoter-GUS (strain −2,180$Δ$UTR312 #8 in Tanaka et al., 2011). Seedlings were germinated and cultured on MGRL medium plate. Four-day-old seedlings were stained with GUS staining solution: 100 mM Na$_{2}$HPO$_{4}$ (pH 7.0), 0.1% Triton X-100, 2 mM K$_{4}$Fe(CN)$_{6}$, 2 mM K$_{3}$Fe(CN)$_{6}$, 0.5 mg/mL X-Gluc (5-bromo-4-chloro-3-indolyl $\beta$-D-glucuronide cyclohexylammonium Salt, Glycosynth, UK) in a decompressed desiccator for 20 min at room temperature. After rinsed with phosphate buffer (pH 7.0), stained seedlings were mounted in 45°C molten 5% agar (gelling temperature 30–31°C, Nacalai, Japan) aqueous solution and solidified at 4°C for 3 hr. The samples were trimmed into blocks and sliced with a vibrating microtome with thickness of 100 μm. The sliced sections were observed with microscope.

### Model parameter choices

Although we have constructed our model as parsimonious as possible to qualitatively explore what kind of behaviours could emerge from a polarised tissue with transporter regulation, our model requires a few important parameters to be set. We have sought to explore the possible dynamics of our system while staying well within the expected limits of what is experimentally considered plausible in terms of the boron transport system. Below we give a brief description of the data our parameter choices were based on, and, when possible, how reasonable ranges could be established.

The plasmamembrane boron permeability rate ($p$) is set to a maximum rate of 8·10-2 s$^{-1}$ and a minimum rate of 4.4·10-3 s$^{-1}$, based on the estimation of boric acid membrane permeability by Raven, 1980 and on more recent experimental measurements performed on internodal cells of the charophyte alga Chara corallina (Stangoulis et al., 2001). Note that the plasmamembrane’s permeability rate for boric acid is relatively high compared to other nutrient elements, due to boric acid existing in a non-charged form under physiological pH.

The degradation rates $ξ_{B}$, $ξ_{N}$ represent the effective decay rate of the actual transporter activity, not just of the transporter protein. This includes processes such as its removal from the membrane, its inactivation due to usage, etc. As it amalgamates a range of inactivation/degradation processes, we set it higher than typical protein degradation rates, but lower than typical membrane residence times, using a half life of 9 s. The valid ranges for the production rate of the transporter activities, $\alpha_{B}$ and $\alpha_{N}$, were derived from the degradation rates $ξ_{B}$, $ξ_{N}$, combined with qualitative conditions for the transporter equilibrium levels. It is as yet not possible to obtain these values directly through experiments, as several intermediate steps are involved. Instead we impose that the transporter activity steady state level does not exceed the plasmamembrane’s permeability by a thousand fold:

$$
p<B^{*},N^{*}<1000⁢p.
$$

Combining these conditions we could then extract the valid ranges for $\alpha_{B}$ and $\alpha_{N}$. As explained in the main text, we take $k_{B}≃30k_{N}$, based on our observations of the sensitivity of BOR and NIP5;1 expression under different boron concentrations (Figure 1—figure supplement 2), further corroborated by earlier data on NIP5;1, as displayed in Figure 1B in Tanaka et al., 2011. We also ran simulations to show robustness of the observed behaviours for smaller variations between $k_{B}$ and $k_{N}$ by assuming lower values of $k_{B}$ (Figure 2—figure supplement 1, Figure 4—figure supplement 2). The parameter $d_{B}$ determines the maximum fold increase in BOR degradation at very high intracellular boron concentrations. It was set to a 50-fold increase, based on rough assessments of experiments in which plants were transferred to high boron conditions, with the caveat that assessment of the temporal change in functional, membrane-located BOR as a function of the intracellular boron concentration is very challenging. Typical cell sizes (height, $h⁢c$; width, $l⁢c$) and cell wall width ($l⁢w$) were estimated from confocal microscope images of A. thaliana roots. The xylem loading rate $a$ was calculated as follows: Hosy et al., 2003 reported that in mature Arabidopsis the rate of transpiration is 0.1 g water/g FW tissue/hour at 70% humidity under daytime conditions. Given an Arabidopsis FW at 18 days of around 0.2 g/plant, transpiration is 20 mg/hour/plant, or roughly 5·106 μm3/s. Considering a stem xylem cross-sectional surface area being roughly 107 μm2, the convective velocity $a$ should therefore be around 5·106 μm3/s / 107 μm2 = 0.5 μm/s.

### Numerical analysis

Numerical and analytical calculations were computed using Wolfram Mathematica 10.2. To calculate time development of the model, ODEs were solved numerically using the NDSolve[] function, setting the initial conditions for each variable to zero. The parameters used in the models are shown in Table 1. The solutions of the ODEs were visualised as a line plot or kymograph, using the Plot[] or ListDensityPlot[] functions.

**Table 1.**
 Model Parameters.


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th rowspan="2">Parameter</th>
      <th rowspan="2">Unit</th>
      <th rowspan="2">Description</th>
      <th colspan="2">Acceptable range</th>
      <th rowspan="2">Default</th>
    </tr>
    <tr>
      <th>Max.</th>
      <th>Min.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">BOR</td>
      <td>ϵB</td>
      <td>-</td>
      <td>Time constant for transporter regulation</td>
      <td>-</td>
      <td>-</td>
      <td>1</td>
    </tr>
    <tr>
      <td>αB</td>
      <td>μm s-2</td>
      <td>Production rate of transporter activity</td>
      <td>4.9×102</td>
      <td>3.7×10-9</td>
      <td>2.0×10-1</td>
    </tr>
    <tr>
      <td>ξB</td>
      <td>s-1</td>
      <td>Basal degradation rate</td>
      <td></td>
      <td>1.6×10-6</td>
      <td>7.6×10-2</td>
    </tr>
    <tr>
      <td>kB</td>
      <td>μM</td>
      <td>Boron concentration for half-maximum in Hill’s function</td>
      <td>1000</td>
      <td>1</td>
      <td>600</td>
    </tr>
    <tr>
      <td>dB</td>
      <td>-</td>
      <td>Amplitude of increased degradation rate by boron</td>
      <td>100</td>
      <td>0</td>
      <td>50</td>
    </tr>
    <tr>
      <td>nB</td>
      <td>-</td>
      <td>Hill’s coefficient</td>
      <td>-</td>
      <td>-</td>
      <td>2</td>
    </tr>
    <tr>
      <td>cB</td>
      <td>μM</td>
      <td>Boron concentration at which the flux reaches its half-maximum value</td>
      <td>∞</td>
      <td>500</td>
      <td>1000</td>
    </tr>
    <tr>
      <td rowspan="5">NIP</td>
      <td>ϵN</td>
      <td>-</td>
      <td>Time constant for transporter regulation</td>
      <td>-</td>
      <td>-</td>
      <td>1</td>
    </tr>
    <tr>
      <td>αN</td>
      <td>μm s-2</td>
      <td>Production rate of transporter activity</td>
      <td>4.9×102</td>
      <td>3.7×10-9</td>
      <td>2.0×10-1</td>
    </tr>
    <tr>
      <td>ξN</td>
      <td>s-1</td>
      <td>Basal degradation rate</td>
      <td></td>
      <td>1.6×10-6</td>
      <td>7.6×10-2</td>
    </tr>
    <tr>
      <td>kN</td>
      <td>μM</td>
      <td>Boron concentration for half-maximum in Hill’s function</td>
      <td>1000</td>
      <td>1</td>
      <td>20</td>
    </tr>
    <tr>
      <td>nN</td>
      <td>-</td>
      <td>Hill’s coefficient</td>
      <td>-</td>
      <td>-</td>
      <td>2</td>
    </tr>
    <tr>
      <td rowspan="3">Cell size</td>
      <td>l⁢c</td>
      <td>μm</td>
      <td>Cell width</td>
      <td>20</td>
      <td>5</td>
      <td>10</td>
    </tr>
    <tr>
      <td>l⁢w</td>
      <td>μm</td>
      <td>Cell wall width</td>
      <td>2</td>
      <td>0.2</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>h⁢c</td>
      <td>μm</td>
      <td>Cell height</td>
      <td>150</td>
      <td>5</td>
      <td>20</td>
    </tr>
    <tr>
      <td rowspan="3">Other</td>
      <td>p</td>
      <td>μm s-1</td>
      <td>Membrane background permeability of boron</td>
      <td>8×10-2</td>
      <td>2.3×10-3</td>
      <td>3×10-2</td>
    </tr>
    <tr>
      <td>a</td>
      <td>μm s-1</td>
      <td>Xylem loading rate (in the last cell)</td>
      <td>500</td>
      <td>0</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>c0</td>
      <td>μm</td>
      <td>Boron concentration in medium</td>
      <td>5000</td>
      <td>0</td>
      <td>300</td>
    </tr>
  </tbody>
</table>

To evaluate the physiological impact (maximum concentration and amplitude of cytosolic boron, and throughput towards shoots) of transporter regulation swiftness, numerical simulations were repeated for combinations of $ϵ_{B}$ and $ϵ_{N}$, which were independently varied between 0.01 and 2, at intervals of 0.01. For each simulation, minimum and maximum boron concentration for each cell and average throughput through the cell row between 24 to 48 h simulation time were recorded using the ‘EventLocator’ method of the NDSolve[] function.

For the ring model, the boundary conditions in the original model were removed by connecting the last cell in the tissue-segment to the first one. This was done by using a tissue composed of six cells and then introducing a cell wall between cell 6 and cell 1. The boron concentration in the novel cell wall is referred to as $W_{6-1}$. This generates a six-cell ring model. Because within a ring-model the total amount of boron is conserved, introducing an additional ODE for this cell wall component effectively means an overdetermination of variables, causing numerical issues. Hence the value of the new variable was instead defined as follows:

$$
W_{6-1}=(B_{t⁢o⁢t⁢a⁢l}-l⁢c⁢h⁢c⁢\sumi=16C_{i}-l⁢w⁢h⁢c⁢\sumi=15W_{i})⁢\frac{1}{l⁢w⁢h⁢c},
$$

where $B_{t⁢o⁢t⁢a⁢l}$ is the total amount of boron in the whole system, which is constant over time as there is no input into nor outflow from the system. The initial boron concentration of all cells and cell walls in the simulation were set to 300 μM, and $B_{t⁢o⁢t⁢a⁢l}$ was determined accordingly.

The local stability analysis was performed as follows: First, all possible equilibria for the set of ODEs were found using the NSolve[] function. Next, analytical descriptions of the Jacobian matrix of the ODEs around the equilibria were derived using the D[] function. Finally, the stability of the system for varying values of $ϵ_{B}$ and $ϵ_{N}$ was determined according to the signs of the eigenvalues of the Jacobian matrix. (Please note that changing $ϵ_{B}$ and/or $ϵ_{N}$ does not change the number of equilibria or their value, only their stability can change.) The system is stable when the real parts of all the eigenvalues are negative, and unstable in any other case. The imaginary part of the largest eigenvalues was then used to estimate the oscillatory period in the unstable region, based on the following conversion:

$$
O⁢s⁢c⁢i⁢l⁢l⁢a⁢t⁢o⁢r⁢y⁢p⁢e⁢r⁢i⁢o⁢d=\frac{2⁢\pi}{\lambda_{i⁢m}}.
$$

To compare the predicted oscillatory period close to the unstable equilibrium with the actual oscillatory period of the system, the oscillatory period was also calculated numerically (Figure 4—figure supplement 1). For certain parameters individual variables can present rather complicated patterns, for example temporarily maximum values, followed by a slight decrease and then further rise before decreasing again. We therefore used the following algorithm to determine the oscillatory period: The ODEs were numerically solved using the NDSolve[] function. The ‘EventLocator’ method was then used to collect all extrema for three variables, $C_{2}$, $C_{3}$ and $N_{2}$, for the period between 24 and 72 hr. Using the first set of extrema as a reference point, the second and potentially later sets of extrema were then compared against the first set. The first case for which all differences were within ±0.1% for all three variables was then labeled as being identical to the reference point, and the corresponding time interval reported as the oscillatory period.

### smFISH probe design

The probes were designed using the online program Stellaris™ Probe Designer version 2.0 and ordered from LGC Biosearch Technologies (Petaluma, CA). For probe sequences see Table 2.

**Table 2.**
 Probes used in the smFISH experiments.


<table>
  <thead>
    <tr>
      <th>NIP5;1 exon probes</th>
      <th>NIP5;1 intron 1 probes</th>
      <th>PP2A mRNA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>acgaaaatggagctaggact</td>
      <td>gtagtcgattttcttacggt</td>
      <td>ccgagcgatctatcaatcag</td>
    </tr>
    <tr>
      <td>cggtttcaccaaacacaagt</td>
      <td>attactagcacaaaccactt</td>
      <td>gacatcctcaccaaaactca</td>
    </tr>
    <tr>
      <td>gtgttttaaacttcgccagt</td>
      <td>cggatggtgacgaatgagta</td>
      <td>tcgggtataaaggctcatca</td>
    </tr>
    <tr>
      <td>tggaggagccatcaccatta</td>
      <td>atgcaatatgcggttatgga</td>
      <td>tagctcgtcgataagcacag</td>
    </tr>
    <tr>
      <td>cattgaatccactctcatcc</td>
      <td>tctattgttaggtttactga</td>
      <td>ccaagagcacgagcaatgat</td>
    </tr>
    <tr>
      <td>gttggtttccgatgatcaaa</td>
      <td>ggttcctagccagaaatttt</td>
      <td>atcaactcttttcttgtcct</td>
    </tr>
    <tr>
      <td>cggcaagcatttgcatcgag</td>
      <td>tgtaatttttaggcttacgt</td>
      <td>catcgtcattgttctcacta</td>
    </tr>
    <tr>
      <td>atgttgaccccaagttgatc</td>
      <td>ctttgtaaggttataacgct</td>
      <td>atagccaaaagcacctcatc</td>
    </tr>
    <tr>
      <td>gagggaaaatcggtgaagca</td>
      <td>aacgagccattggatttctt</td>
      <td>atacagaataaaacccccca</td>
    </tr>
    <tr>
      <td>ttgcgagtgagggagacatc</td>
      <td>cgtggattccaatgttttct</td>
      <td>caagtttcctcaacagtgga</td>
    </tr>
    <tr>
      <td>tgaatgttcccacgaactcg</td>
      <td>ttcccaattcattattttcc</td>
      <td>tcatctgagcaccaattcta</td>
    </tr>
    <tr>
      <td>gctgtcgcggtgaatatcaa</td>
      <td>tgtctcgatctcattttttt</td>
      <td>tagccagaggagtgaaatgc</td>
    </tr>
    <tr>
      <td>catcgtatttctggttcacg</td>
      <td>ccctatagtacatctatatt</td>
      <td>cattcaccagctgaaagtcg</td>
    </tr>
    <tr>
      <td>gttaccgattagggtttctg</td>
      <td>attacgatcgatttgtgagt</td>
      <td>ggaaaatcccacatgctgat</td>
    </tr>
    <tr>
      <td>tatgatcatcactgcgagtc</td>
      <td>ttctctgtatttcagagctt</td>
      <td>atattgatcttagctccgtc</td>
    </tr>
    <tr>
      <td>cctgagatatgacctgttga</td>
      <td>agtattatcttttggtcact</td>
      <td>attggcatgtcatcttgaca</td>
    </tr>
    <tr>
      <td>cagtgatgggtttaggtgag</td>
      <td>ccctatgatctttttcaata</td>
      <td>aaattagttgctgcagctct</td>
    </tr>
    <tr>
      <td>cttagagcagcgaatgctat</td>
      <td>ctcctccaagtgtgacgtaa</td>
      <td>gctgattcaattgtagcagc</td>
    </tr>
    <tr>
      <td>tatgtaagcagggacgtgtg</td>
      <td>ctagttcatgtcgtgttaaa</td>
      <td>ccgaatcttgatcatcttgc</td>
    </tr>
    <tr>
      <td>gcgcaaatggaagctgagac</td>
      <td>atttaattctcggttgcgac</td>
      <td>caaccctcaacagccaataa</td>
    </tr>
    <tr>
      <td>gaacactcctttaagtgcga</td>
      <td>ttcactctctttctatttgc</td>
      <td>ctccaacaatttcccaagag</td>
    </tr>
    <tr>
      <td>caccaccggacataaaagga</td>
      <td>ctcttagtttttcttagact</td>
      <td>caaccatataacgcacacgc</td>
    </tr>
    <tr>
      <td>tccaaggctaacagatggaa</td>
      <td>taagttgagatcgagtgggc</td>
      <td>agtagacgagcatatgcagg</td>
    </tr>
    <tr>
      <td>tgaactcaagagcaaaggct</td>
      <td>gagtcggtgtccattgaata</td>
      <td>gaacttctgcctcattatca</td>
    </tr>
    <tr>
      <td>cggcagttacaacaaagagg</td>
      <td>actattagctcattgtcaca</td>
      <td>cacagggaagaatgtgctgg</td>
    </tr>
    <tr>
      <td>aacggcacgagtgtcggtag</td>
      <td>atttacgcaacttgcgtgtt</td>
      <td>tgacgtgctgagaagagtct</td>
    </tr>
    <tr>
      <td>aacggctatacctgccaatt</td>
      <td>agcgtgaccgttttattttt</td>
      <td>cccattataactgatgccaa</td>
    </tr>
    <tr>
      <td>aatattgagcatgaccgtgg</td>
      <td>actttgtattcgtcattgca</td>
      <td>tggttcacttggtcaagttt</td>
    </tr>
    <tr>
      <td>atagatccaccagtcgatgg</td>
      <td>gacctaaccaaaccatacgt</td>
      <td>tctacaatggctggcagtaa</td>
    </tr>
    <tr>
      <td>tcctagagttctcacaggat</td>
      <td>gcttccgtcatggacagaaa</td>
      <td>cgattatagccagacgtact</td>
    </tr>
    <tr>
      <td>atagtttcctgatgcaacgg</td>
      <td>ctaaaagaatcccatccggt</td>
      <td>gactggccaacaagggaata</td>
    </tr>
    <tr>
      <td>ccagatacacccatagtgac</td>
      <td>aaaggacaagagccgtggat</td>
      <td>catcaaagaagcctacacct</td>
    </tr>
    <tr>
      <td>cagatatggcaccaagtgta</td>
      <td>tccacgttaacgagcatcaa</td>
      <td>ttgcatgcaaagagcaccaa</td>
    </tr>
    <tr>
      <td>ttaacacctgtgtagaccgc</td>
      <td>gcgtgtgatctgtctatatc</td>
      <td>acggattgagtgaaccttgt</td>
    </tr>
    <tr>
      <td>gtcagtcacgctatcgttaa</td>
      <td>tacagtcaacggttagtatt</td>
      <td>cttcagattgtttgcagcag</td>
    </tr>
    <tr>
      <td>aaagctcctaaccggacgag</td>
      <td>gtcattagtagttactagtt</td>
      <td>ggaccaaactcttcagcaag</td>
    </tr>
    <tr>
      <td>gtctctcactcacttaacga</td>
      <td>agtattatttctgctgtcca</td>
      <td>ggaactatatgctgcattgc</td>
    </tr>
    <tr>
      <td>tccaaagctttttcatatca</td>
      <td>ctagagggttctgagtcgaa</td>
      <td>gtgggttgttaatcatctct</td>
    </tr>
    <tr>
      <td>gccttttattcttcacacaa</td>
      <td>gagatgtttcttgtctaaca</td>
      <td>tgcacgaagaatcgtcatcc</td>
    </tr>
    <tr>
      <td>tgcgtggacttatagtcaca</td>
      <td>gtactagatgaatagaggct</td>
      <td>ttactggagcgagaagcgat</td>
    </tr>
    <tr>
      <td>aggtttatatagaccgatgc</td>
      <td></td>
      <td>gaacatgtgatctcggatcc</td>
    </tr>
    <tr>
      <td>aatgacgagacaagttcgca</td>
      <td></td>
      <td>ctctgtctttagatgcagtt</td>
    </tr>
    <tr>
      <td>agaaacccaaaccacacata</td>
      <td></td>
      <td>catcattttggccacgttaa</td>
    </tr>
    <tr>
      <td>ataaaaacagcctcgtctcc</td>
      <td></td>
      <td>cgtatcatgttctccacaac</td>
    </tr>
    <tr>
      <td>acacatgccatagattttat</td>
      <td></td>
      <td>atcaacatctgggtcttcac</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>ttggagagcttgatttgcga</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>acacaattcgttgctgtctt</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>cgcccaacgaacaaatcaca</td>
    </tr>
  </tbody>
</table>

### Observation of NIP5;1 RNA

Col-0 seeds were stratified for 2 d at 4°C and then germinated and grown under 16/8 hr light conditions at 20°C on MGRL plates (30μM boric acid). smFISH was carried out on seedlings as described by Duncan et al., 2017. Briefly, 5d old seedlings were fixed for 30 min in 4% paraformaldehyde. Root squash samples were prepared on slides. Tissue permeabilisation was achieved by immersing the samples in 70% ethanol for a minimum of one hour. Two washes were carried out with wash buffer (10% formamide and 2x SSC). 100 mL of hybridisation solution (0.3 M Sodium chloride and 30 mM tri-Sodium citrate dihydrate, referred to as ’2x SSC’, 10% dextran sulfate and 10% formamide) containing probes (final concentration 25 nM) was then left to hybridise at 37°C in the dark overnight. Each sample was washed twice with wash buffer following hybridisation buffer removal with the second wash left to incubate for 30 min at 37°C. Each slide was then incubated with 100mL 4’ 6-diamidino-2-phenylindole dihydrochloride (DAPI, Sigma, St. Luis, MO) (100 ng/mL) at 37°C for 30 min. The DAPI solution was removed before 100 μL 2x SSC was added and then removed. Samples were then incubated for 2 min at room temperature with 100 μL GLOX buffer (0.4% glucose in 10 mM Tris, 2x SSC) before being mounted in 100 μLof GLOX buffer containing 1 μL of glucose oxidase (#G0543, Sigma) and 1 μL catalase (Sigma) under 22 mm x 22 mm No. 1 coverslips (Slaughter, Uppminster, UK) and sealed by nail varnish. A Zeiss Elyra PS1 inverted microscope was used for imaging. A x100 oil-immersion objective (1.46 NA) and cooled EM-CCD Andor iXon 897 camera (512$\times$512 QE>90%) were used to obtain all images. (Quasar®570 probes: excitation by 561 nm laser, signals detected between 570–640 nm. Quasar®670 probes: excitation by 642 nm laser, signals detected between 655–710 nm. DAPI: excitation by 405 nm laser, signals detected between 420–480 nm.) For all experiments a series of optical sections were set up with z-steps of 0.2 μm. All smFISH images were de convolved with Huygens Professional version 16.05 (Scientific Volume Imaging, the Netherlands, http://svi.nl) using the QMLE algorithm with Good signal to noise settings and 50 iterations. Maximum Z projections in Figure 7 were performed using Fiji (an implementation of ImageJ, a public domain program by W. Rasband available from http://rsb.info.nih.gov/ij/).

### Determination of mature mRNA/pre-mRNA abundance ratio

Col-0 seedlings were germinated and grown on MGRL plates containing 30 μM boric acid for eight days. Total RNA was extracted from whole roots of about 25 seedlings with four replicates, using NucleoSpin RNA Plant (MACHEREY-NAGEL). To reduce contamination of genome DNA, 500 ng of prepared RNA was subjected to DNase treatment with RQ1 RNase-Free DNase (Promega), following the manufacture’s protocol. Reverse transcription was performed with Super Script III reverse transcriptase (Thermo Fisher Scientific) with random primers. To compare the abundance of cDNAs with different sequences, absolute quantification by realtime PCR was conducted, using PCR-synthesised DNA fragments with known concentration as standard templates. To detect mature or pre-mRNA specifically, exon-exon or intron-exon probes were designed (Figure 7—figure supplement 1 and Table 3). Realtime PCR was performed with Thermal Cycler Dice® Real Time System and SYBR Premix Ex Taq II (Tli RNaseH Plus) (Takara), following the supplied standard shuttle 2-step PCR protocol. As standard DNA templates, DNA fragments corresponding to cDNA of mature- or pre-mRNA of NIP5;1 and PP2A were amplified by PCR with Prime Star GXL (Takara), using Col-0 cDNA or genome DNA as a template. The primers used are shown in Table 3. The PCR products were subjected to electrophoresis and the target fragment was purified from the gel slices with QIAquick Gel Extraction Kit (Qiagen). The concentration of the purified DNA was estimated by NanoDrop 1000 (Thermo Fisher Scientific). Tenth dilution series of 1 pg/μL~1 ag/μL template DNA were applied for standard curve. The copy number of each standard DNA solution was normalized by realtime PCR $C_{t}$ values of the exon-exon proves which amplify both mature- and pre-mRNA sequences (Figure 7—figure supplement 1 and Table 3). As a negative control, in parallel, after the total RNA extraction, the same samples were processed with the same procedure except reverse transcription, confirming that realtime PCR signals from contaminated genome DNA does not affect the final results.

**Table 3.**
 Primers used in qRT-PCR experiments.


<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Sequence</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>NIP5;1_qRT-PCR-1</td>
      <td>caccgattttccctctcctgat</td>
      <td rowspan="10">Probes for realtime PCR</td>
    </tr>
    <tr>
      <td>NIP5;1_qRT-PCR-2</td>
      <td>ctctttcttactctctagcctc</td>
    </tr>
    <tr>
      <td>NIP5;1_qRT-PCR-3</td>
      <td>gaatgttcccacgaactcgg</td>
    </tr>
    <tr>
      <td>NIP5;1_qRT-PCR-4</td>
      <td>acattcatcttgatattcacc</td>
    </tr>
    <tr>
      <td>NIP5;1_qRT-PCR-5</td>
      <td>gcatgcagcgttaccgatta</td>
    </tr>
    <tr>
      <td>PP2A_qRT-PCR-1</td>
      <td>ccatgtttgaggatcttacgc</td>
    </tr>
    <tr>
      <td>PP2A_qRT-PCR-2</td>
      <td>tgtctacatctcagcttcagtgtc</td>
    </tr>
    <tr>
      <td>PP2A_qRT-PCR-3</td>
      <td>gctccaacaatttcccaaga</td>
    </tr>
    <tr>
      <td>PP2A_qRT-PCR-4</td>
      <td>caagattcggttagattattg</td>
    </tr>
    <tr>
      <td>PP2A_qRT-PCR-5</td>
      <td>gcgagaaattgacaatcacag</td>
    </tr>
    <tr>
      <td>NIP5;1_mRNA_F</td>
      <td>atttaggtgacactatagtaagctcaaagactaaccaaac</td>
      <td rowspan="4">For amplification of the standard DNA fragments</td>
    </tr>
    <tr>
      <td>NIP5;1_mRNA_R</td>
      <td>ttacacatgccatagattttat</td>
    </tr>
    <tr>
      <td>PP2A_mRNA_F</td>
      <td>atttaggtgacactatagcggtctcatttctcgttcttc</td>
    </tr>
    <tr>
      <td>PP2A_mRNA_R</td>
      <td>cacttgataagtaaattatttg</td>
    </tr>
  </tbody>
</table>

![Video 2.](https://cdn.elifesciences.org/articles/27038/elife-27038-video2.mp4.jpg)

**Video 2.:** Simulation output revealing the details of boron flows over the membranes, due to transporter dynamics and background membrane permeability rates.
