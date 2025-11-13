# Compound-V formations in shorebird flocks

## Authors

- Aaron J Corcoran<sup>1</sup> ([ORCID: 0000-0003-1457-3689](https://orcid.org/0000-0003-1457-3689))
- Tyson L Hedrick<sup>1</sup> ([ORCID: 0000-0002-6573-9602](https://orcid.org/0000-0002-6573-9602)) †

### Affiliations

1. University of North Carolina at Chapel Hill Chapel Hill United States

† Corresponding author

## Abstract

Animal groups have emergent properties that result from simple interactions among individuals. However, we know little about why animals adopt different interaction rules because of sparse sampling among species. Here, we identify an interaction rule that holds across single and mixed-species flocks of four migratory shorebird species spanning a seven-fold range of body masses. The rule, aligning with a one-wingspan lateral distance to nearest neighbors in the same horizontal plane, scales linearly with wingspan but is independent of nearest neighbor distance and neighbor species. This rule propagates outward to create a global flock structure that we term the compound-V formation. We propose that this formation represents an intermediary between the cluster flocks of starlings and the simple-V formations of geese and other large migratory birds. We explore multiple hypotheses regarding the benefit of this flock structure and how it differs from structures observed in other flocking species.

## Introduction

The collective movements of animals—from schooling fish to swarming insects and flocking birds—have long excited intrigue among observers of nature. Collective motion arises as an emergent property of interactions between individuals (reviewed by Herbert-Read, 2016 and by Vicsek and Zafeiris, 2012). Thus, much attention has been placed on identifying local interaction rules (Ballerini et al., 2008a; Herbert-Read et al., 2011; Katz et al., 2011; Lukeman et al., 2010) and how those rules affect group structure and movement (Buhl et al., 2006; Hemelrijk and Hildenbrandt, 2012). However, comparative data across species are still limited, preventing us from testing hypotheses regarding the evolution and diversity of collective movement patterns.

Hundreds of bird species fly in groups, but most quantitative research has focused on starlings (Attanasi et al., 2014; Ballerini et al., 2008b; Cavagna et al., 2010), homing pigeons (Nagy et al., 2013; Nagy et al., 2010; Pettit et al., 2015; Pettit et al., 2013; Usherwood et al., 2011) and birds that fly in V-formations (Badgerow and Hainsworth, 1981; Cutts and Speakman, 1994; Hummel, 1983; Lissaman and Shollenberger, 1970; Maeng et al., 2013; Portugal et al., 2014; Weimerskirch et al., 2001). These data indicate that smaller birds fly in relatively dense cluster flocks that facilitate group cohesion and information transfer (Attanasi et al., 2014; Ballerini et al., 2008a), whereas larger migratory birds fly in highly structured V formations (also known as line or echelon formations) that provide aerodynamic and energetic benefits (Lissaman and Shollenberger, 1970; Portugal et al., 2014; Weimerskirch et al., 2001). However, descriptive accounts of flock structure over a greater range of species (Heppner, 1974; Piersma et al., 1990) cover a range of flock types, spanning the extremes of V-formation and large cluster flocks. The species whose flocking behavior have been studied quantitatively differ in many ways that could be important for flocking, including body size, ecology, the frequency of aggregation and its behavioral context. Therefore, on the basis of the available data, it is difficult to conclude what factors cause birds to adopt a specific group formation, or even what factors affect interaction rules, positioning and behavior within flocks.

We aimed to address these questions by collecting three-dimensional (3D) trajectories of the birds in flocks of four shorebird species that have similar ecologies (all forage in large groups in coastal habitats and migrate long distances) but that cover a seven-fold range of body mass and two-fold range of wingspan. Our study species include dunlin (Calidris alpina Linnaeus 1758; 56 g, 0.34 m wingspan), short-billed dowitcher (Limnodromus griseus Gmelin 1789; 110 g, 0.52 m wingspan), American avocet (Recurvirostra americana Gmelin 1789; 312 g, 0.72 m wingspan), and marbled godwit (Limosa fedoa, Linnaeus, 1758; 370 g, 0.78 m). Molecular dating indicates that these species diverged from their nearest common ancestor approximately 50 million years ago (Mya) (Baker et al., 2007), providing time for evolutionary diversification of flocking behavior. By comparing the group structure of birds across a range of body sizes and by comparing our data with those in the literature, we aimed to determine the extent to which flock structure varies across species with different body sizes and ecologies. We employ three approaches: (1) identification of local interaction rules by quantifying the relative positions of birds and their nearest neighbors; (2) quantification of the degree of spatial structure within flocks; and (3) measurement of individual speeds and wingbeat frequencies to examine how local and global position within the flock affect flights behavior.

On the basis of existing flock data, we hypothesized that flocks of larger shorebird species would be more structured than those of smaller species (recapitulating the trend of larger birds flying in highly structured V formations) and that larger species would also exhibit aerodynamic formations more frequently. Because a previous study showed that flying in a cluster flock is energetically costly in pigeons (Usherwood et al., 2011), we hypothesized that birds flying in the middle and rear of flocks and birds flying closer to their nearest neighbor would have reduced flight performance (lower speed relative to their wingbeat frequency). Surprisingly, we found that all four species studied here flew in a flock structure that we term the compound-V formation. We propose that this structure might be an adaptation for aerodynamic flocking in migratory species, and that ecology is an underappreciated driver of the evolution of avian flocking behavior.

## Results

We reconstructed the 3D trajectories from 18 bird flocks that ranged in size from 189 to 1039 individuals, which were recorded for 2.4–13.2 s at 29.97 frames per second (Figure 1, Table 1). This resulted in 1,598,169 3D position measurements that were used to examine flock structure. Sixteen of the 18 flocks were comprised entirely of a single species. The remaining two flocks were mixed-species flocks of marbled godwits and short-billed dowitchers. Computer vision techniques allowed the species of individuals in mixed-species flocks to be identified on the basis of differences in body size (see 'Materials and methods').

![Figure 1.](https://cdn.elifesciences.org/articles/45071/elife-45071-fig1-v1.jpg)

**Figure 1.:** (a) Multi-camera videography was used to reconstruct 3D trajectories of shorebirds flying near high-tide roosts in Humboldt Bay, California. (b) Overhead and (c) profile views of an example flock. Symbol sizes reflect actual scales for birds with outstretched wings. Flock position data are available in Figure 1—source data 1.

**Table 1.**
 Flock parameters.Table 1—source data 1.Flock parameter data.


<table>
  <thead>
    <tr>
      <th>Flock</th>
      <th>Species</th>
      <th>N birds</th>
      <th>N frames</th>
      <th>†, ‡Nearest neighbor distance (m).</th>
      <th>§Nearest neighbor power</th>
      <th>†Ground speed (m·s−1)</th>
      <th>†Airspeed (m·s−1)</th>
      <th>Wind speed (m·s−1)</th>
      <th>¶Wind direction (deg.)</th>
      <th>†Z-speed (m·s−1)</th>
      <th>†Turnrate (° s−1)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0417–2</td>
      <td>Godwit</td>
      <td>286</td>
      <td>147</td>
      <td>1.30 (0.79–2.15) 1.67</td>
      <td>0.361</td>
      <td>5.23 (3.59–8.23)</td>
      <td>9.36 (8.04–10.54)</td>
      <td>5.73</td>
      <td>4.3</td>
      <td>1.11 (0.16–1.91)</td>
      <td>40.5 (18.4–80.9)</td>
    </tr>
    <tr>
      <td>0417–2</td>
      <td>Dowitcher</td>
      <td>309</td>
      <td>147</td>
      <td>1.16 (0.72–1.89) 2.23</td>
      <td>0.385</td>
      <td>5.15 (3.39–8.42)</td>
      <td>9.25 (7.94–10.47)</td>
      <td>5.73</td>
      <td>4.63</td>
      <td>1.26 (0.30–2.00)</td>
      <td>43.0 (19.4–81.9)</td>
    </tr>
    <tr>
      <td>0417–3</td>
      <td>Godwit</td>
      <td>474</td>
      <td>278</td>
      <td>1.81 (1.01–2.94) 2.32</td>
      <td>0.428</td>
      <td>3.32 (1.71–6.55)</td>
      <td>7.87 (6.42–9.39)</td>
      <td>5.73</td>
      <td>5.3</td>
      <td>−0.18 (−1.27 – 0.76)</td>
      <td>26.8 (8.0–80.6)</td>
    </tr>
    <tr>
      <td>0417–4</td>
      <td>Godwit</td>
      <td>803</td>
      <td>397</td>
      <td>1.71 (1.02–2.58) 2.19</td>
      <td>0.391</td>
      <td>6.30 (3.04–9.44)</td>
      <td>8.82 (7.68–9.93)</td>
      <td>5.73</td>
      <td>47.2</td>
      <td>0.22 (−0.73 – 1.03)</td>
      <td>14.3 (4.66–40.8)</td>
    </tr>
    <tr>
      <td>0417–4</td>
      <td>Dowitcher</td>
      <td>74</td>
      <td>397</td>
      <td>1.57 (0.94–2.37) 3.01</td>
      <td>0.382</td>
      <td>6.51 (3.00–9.56)</td>
      <td>8.65 (7.49–9.65)</td>
      <td>5.73</td>
      <td>48.1</td>
      <td>0.39 (−0.53 – 1.21)</td>
      <td>19.8 (6.6–49.2)</td>
    </tr>
    <tr>
      <td>0420–1</td>
      <td>Godwit</td>
      <td>639</td>
      <td>177</td>
      <td>1.19 (0.59–1.94) 1.52</td>
      <td>0.408</td>
      <td>7.05 (5.12–9.91)</td>
      <td>10.54 (7.91–12.98)</td>
      <td>4.06</td>
      <td>9.2</td>
      <td>−0.26 (−1.83 – 1.03)</td>
      <td>22.6 (7.39–75.9)</td>
    </tr>
    <tr>
      <td>0420–2</td>
      <td>Godwit</td>
      <td>309</td>
      <td>147</td>
      <td>1.54 (0.83–2.38) 1.97</td>
      <td>0.43</td>
      <td>8.95 (7.09–11.59)</td>
      <td>10.50 (8.76–12.11)</td>
      <td>4.06</td>
      <td>59.7</td>
      <td>−0.06 (−0.95 – 0.68)</td>
      <td>11.9 (3.77–37.7)</td>
    </tr>
    <tr>
      <td>0427–2</td>
      <td>Dowitcher</td>
      <td>354</td>
      <td>397</td>
      <td>1.07 (0.61–2.00) 2.06</td>
      <td>0.424</td>
      <td>6.22 (3.06–9.76)</td>
      <td>9.03 (5.53–12.77)</td>
      <td>3.50</td>
      <td>23.5</td>
      <td>0.56 (−0.89 – 1.79)</td>
      <td>20.2 (6.68–60.1)</td>
    </tr>
    <tr>
      <td>0427–3</td>
      <td>Dowitcher</td>
      <td>391</td>
      <td>217</td>
      <td>1.15 (0.61–2.06) 2.21</td>
      <td>0.463</td>
      <td>10.9 (8.64–13.3)</td>
      <td>10.98 (7.99–13.98)</td>
      <td>3.50</td>
      <td>73.3</td>
      <td>0.32 (−2.10 – 2.15</td>
      <td>24.8 (8.30–70.9)</td>
    </tr>
    <tr>
      <td>0427–5</td>
      <td>Dowitcher</td>
      <td>511</td>
      <td>170</td>
      <td>1.23 (0.70–1.98) 2.37</td>
      <td>0.421</td>
      <td>5.31 (4.23–6.49)</td>
      <td>7.14 (4.85–9.18)</td>
      <td>4.60</td>
      <td>26.9</td>
      <td>0.73 (−0.24 – 1.52)</td>
      <td>20.8 (7.62–57.4)</td>
    </tr>
    <tr>
      <td>1230–1</td>
      <td>Dunlin</td>
      <td>351</td>
      <td>198</td>
      <td>1.08 (0.58–1.78) 3.18</td>
      <td>0.465</td>
      <td>6.98 (6.03–7.85)</td>
      <td>7.65 (6.67–8.34)</td>
      <td>1.20</td>
      <td>44.1</td>
      <td>−0.23 (−0.52 – 0.09)</td>
      <td>27.3 (11.9–46.6)</td>
    </tr>
    <tr>
      <td>1230–2</td>
      <td>Dunlin</td>
      <td>592</td>
      <td>75</td>
      <td>0.80 (0.47–1.23) 2.35</td>
      <td>0.387</td>
      <td>6.61 (6.00–7.30)</td>
      <td>7.60 (5.84–8.48)</td>
      <td>1.10</td>
      <td>22.6</td>
      <td>−0.12 (−0.56 – 0.32)</td>
      <td>11.4 (3.7–26.8)</td>
    </tr>
    <tr>
      <td>1230–3</td>
      <td>Dunlin</td>
      <td>477</td>
      <td>125</td>
      <td>0.86 (0.49 1.37 2.53</td>
      <td>0.392</td>
      <td>6.71 (5.85–7.73)</td>
      <td>7.54 (5.52–8.36)</td>
      <td>1.08</td>
      <td>35.5</td>
      <td>0.11 (−0.49 – 0.84)</td>
      <td>19.6 (5.27–42.9)</td>
    </tr>
    <tr>
      <td>1230–4</td>
      <td>Dunlin</td>
      <td>189</td>
      <td>73</td>
      <td>0.89 (0.50–1.50) 2.62</td>
      <td>0.502</td>
      <td>8.28 (7.44–9.70)</td>
      <td>7.47 (5.27–8.53)</td>
      <td>1.08</td>
      <td>36.5</td>
      <td>−0.03 (−0.57 – 0.45</td>
      <td>24.6 (7.5–52.9)</td>
    </tr>
    <tr>
      <td>0101–1</td>
      <td>Dunlin</td>
      <td>1039</td>
      <td>228</td>
      <td>1.03 (0.59–1.64) 3.03</td>
      <td>0.41</td>
      <td>8.39 (7.41–9.98)</td>
      <td>7.46 (5.74–8.64)</td>
      <td>1.63</td>
      <td>118.4</td>
      <td>−0.23 (−0.73 – 0.27)</td>
      <td>17.7 (4.9–42.1)</td>
    </tr>
    <tr>
      <td>0101–3</td>
      <td>Dunlin</td>
      <td>961</td>
      <td>188</td>
      <td>0.92 (0.52–1.50) 2.71</td>
      <td>0.416</td>
      <td>8.61 (7.70–9.42)</td>
      <td>7.74 (6.25–8.76)</td>
      <td>1.63</td>
      <td>117.6</td>
      <td>−0.02 (–0.33 – 0.36)</td>
      <td>13.0 (3.6–32.2)</td>
    </tr>
    <tr>
      <td>0101–4</td>
      <td>Dunlin</td>
      <td>269</td>
      <td>340</td>
      <td>1.00 (0.35–2.12) 2.94</td>
      <td>0.45</td>
      <td>6.56 (4.96–8.12)</td>
      <td>7.63 (5.12–8.72)</td>
      <td>1.63</td>
      <td>39.3</td>
      <td>−0.14 (−0.70 – 0.30)</td>
      <td>18.3 (4.4–46.9)</td>
    </tr>
    <tr>
      <td>1220–1</td>
      <td>Avocet</td>
      <td>323</td>
      <td>90</td>
      <td>1.09 (0.70–1.69) 1.51</td>
      <td>0.429</td>
      <td>6.02 (4.55–7.57)</td>
      <td>8.18 (6.21–9.31)</td>
      <td>2.39</td>
      <td>1.4</td>
      <td>0.33 (−0.98 – 0.90)</td>
      <td>25.2 (10.4–48.8)</td>
    </tr>
    <tr>
      <td>1220–2</td>
      <td>Avocet</td>
      <td>321</td>
      <td>245</td>
      <td>1.19 (0.72–1.90) 1.65</td>
      <td>0.432</td>
      <td>6.96 (5.26–9.22)</td>
      <td>8.00 (6.88–8.96)</td>
      <td>2.39</td>
      <td>8.2</td>
      <td>0.10 (−1.49 – 0.74)</td>
      <td>30.2 (12.7–54.5)</td>
    </tr>
    <tr>
      <td>1220–3</td>
      <td>Avocet</td>
      <td>281</td>
      <td>280</td>
      <td>1.30 (0.78–2.10) 1.81</td>
      <td>0.472</td>
      <td>7.50 (5.32–8.93)</td>
      <td>7.93 (6.28–8.88)</td>
      <td>2.39</td>
      <td>22.3</td>
      <td>0.33 (−0.62 – 0.83</td>
      <td>23.9 (6.18–49.1)</td>
    </tr>
  </tbody>
</table>

_†Values are medians and (in brackets) 10th-90th percentiles of values extracted at one-wingbeat intervals from all individuals of each flock.‡Values in italics are in wingspan units instead of metric units.§Exponent of power law fit to distance of 10 nearest neighbors.¶Wind direction is relative to the overall flight direction where 0° is a pure headwind and 180° a pure tailwind. Note that data are presented separately in consecutive rows for each species in mixed-species flocks (0417–2 and 0417–4). Data used for generating this table are available in Table 1—source data 1._

### Nearest-neighbor alignment

We examined flock structure by quantifying the position of each bird with respect to its nearest neighbor. We used modal values to characterize typical neighbor positions because position distributions were skewed as a result of values being cropped at zero. In all flocks, nearest neighbors flying within the same horizontal plane [an elevation slice of ±1 wingspan, a mean of 56% of nearest neighbors across all flocks (range 35–76%)] exhibited a distinctly peaked distribution, where modal neighbor position was offset both in front-back and lateral distance (Figure 2a,b). By contrast, nearest neighbor birds flying outside the horizontal elevation slice of ±1 wingspan were distributed randomly with a peak directly above or below the focal bird (Figure 2c,d). This indicates that shorebirds adopt alignment rules for neighbors flying within their same elevation slice. On average, birds flew at approximately the same height as their nearest leading neighbor (−0.01 ± 0.02 m, mean ± s.d. for the median trailing height across all 18 flocks).

![Figure 2.](https://cdn.elifesciences.org/articles/45071/elife-45071-fig2-v1.jpg)

**Figure 2.:** (a, b) Histograms of nearest-neighbor alignment for birds flying within ±1 wingspan of elevation (godwit flock 0420–1) show a distinctive peak at a trailing distance and lateral distance of approximately one wingspan; focal birds are shown in light gray and nearest neighbors in black. Inset bird silhouettes show profile views of the birds’ relative flight elevations. (c, d) Histograms of nearest-neighbor alignment for birds flying outside ±1 wingspan of elevation for the same flock show a largely random distribution with a modal location of nearly straight above or below the focal bird. Data used for generating this figure are available in Figure 2—source data 1.

Both nearest-neighbor lateral distance and front-back distance differed among flocks and species (Figure 3a). Species wingspan strongly predicted modal lateral neighbor position (linear regression, slope = 0.85, R2 = 0.93, F = 228.29, p<0.0001). Wingspan also predicted front-back distance (slope = 0.70, R2 = 0.86, F = 99.57, p<0.0001), although less strongly than lateral distance. After scaling alignment positions to wingspan (i.e., dividing neighbor distances by species wingspan), a distinctive pattern emerges (Figure 3b). Specifically, the flocks adopted a modal lateral distance of approximately one wingspan (mean 1.04, range 0.88–1.24 wingspans). This non-dimensionalized lateral distance had a weak inverse relationship to species wingspan (linear regression, slope = −0.37, R2 = 0.37, F = 9.38, p=0.007) and was not related to flock density (i.e. nearest neighbor distance, non-dimensionalized by wingspan; linear regression, R2 = 0.07, F = 1.15; p=0.30). Non-dimensionalized trailing distance was inversely proportional to species wingspan (linear regression, slope = −0.40, R2 = 0.33, F = 7.93, p=0.012) and increased with non-dimensional flock density (linear regression, slope = 0.13, R2 = 0.58, F = 22.39; p=0.0002). In summary, across all four species, shorebirds adhere to a non-dimensional spacing rule of aligning to neighbors with a lateral offset of approximately one wingspan while allowing trailing distance to vary with flock density.

![Figure 3.](https://cdn.elifesciences.org/articles/45071/elife-45071-fig3-v1.jpg)

**Figure 3.:** (a) Summary of modal neighbor position for nearest neighbors within ± 1 wingspan in single-species flocks of all four species, depicted in absolute metric distance and (b) the same data plotted in distances relative to the wingspan of each species. Open symbols indicate modal neighbor positions for individual flocks. Closed symbols and silhouettes show the average position for each species. Data used for generating this figure are available in Figure 3—source data 1.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/45071/elife-45071-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** The silhouettes show the position of the focal bird at the origin and the lateral and horizontal position modes. The dashed line box shows the ‘aerodynamic neighbor’ region for comparison with shorebird flocks Figure 3—figure supplement 2. Note that the lateral and horizontal modal positions are calculated separately, and the result is not necessarily congruent with the most populated 2D grid cell. Data used for generating this figure are available in Figure 3—source data 1.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/45071/elife-45071-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** The dashed line box shows the ‘aerodynamic neighbor’ region for comparison with shorebird flocks, 29.3% of all nearest neighbors fall within this region. Data used for generating this figure are available in Figure 3—source data 1.

Data from mixed-species flocks of godwits and dowitchers further support the non-dimensional nature of the lateral spacing rule within individual flocks. Both dowitchers and godwits adjusted their lateral spacing depending on the species of their neighbor (Figure 4). Godwits following conspecifics had a modal lateral spacing of 0.76 m, or 0.97 godwit wingspans. When following the smaller dowitchers, godwits reduced the modal lateral distance to 0.60 m or 0.92 wingspans when calculated using the average wingspan of dowitchers and godwits (Mann-Whitney U = 525,684; n1 = 1034; n2 = 81; p=0.0004). Dowitchers following conspecifics flew with a modal lateral distance of 0.51 m, or 0.98 dowitcher wingspans. When following the larger godwits, dowitchers increased the modal lateral distance to 0.58 m or 0.89 average wingspans (Mann-Whitney U test; U = 66,341; n1 = 743; n2 = 149; p<0.0003).

![Figure 4.](https://cdn.elifesciences.org/articles/45071/elife-45071-fig4-v1.jpg)

**Figure 4.:** Data from mixed species flocks show that birds adjust their lateral spacing depending on the species (and size) of their nearest leading neighbor. (a) Godwits following conspecifics adopt a larger lateral distance than (b) godwits following the smaller dowitchers. (c) Dowitchers following conspecifics use a shorter lateral distance than (d) dowitchers following the larger godwits. These results support the hypothesis that shorebirds adopt a lateral spacing rule that is dependent on the size of their leading neighbor. Dashed lines are provided to facilitate comparison of modal lateral positions between (a) and (b) and between (c) and (d). Data used to generate this figure are available in Figure 4—source data 1.

### Comparison of simple- and compound-V formations

While recording the larger cluster flocks, we also recorded four godwit simple-V formations of between 16 and 44 individuals, which were recorded for between 42 and 211 frames (Figure 5). Here we compare the positioning of godwits in simple and compound-V formations. In both cases, nearest neighbors were most commonly in the same horizontal plane (mean of 61% in godwit cluster flocks, 97.9% in godwit simple-V formations), defined as extending one wingspan above and below the focal bird, with the follower positioned over a narrow lateral range and wider range of trailing distances (Figures 3b and 5b). The modal lateral position in the simple-V formations was slightly less (mean of 0.8 wingspans) than that in the compound-V formations, where the mean modal lateral position among godwit flocks was 0.96 wingspans (Generalized Linear Model with terms for flock and simple versus compound-V formation; p<0.0001; Figure 5, Figure 5—source data 1). The modal trailing distance in simple-V formations was 0.50 wingspans; in compound-V formations of godwits, the mean modal trailing distance was 0.86 wingspans.

![Figure 5.](https://cdn.elifesciences.org/articles/45071/elife-45071-fig5-v1.jpg)

**Figure 5.:** Incidental to our cluster flock recordings, we also recorded several instances of godwits flying in a simple-V, echelon or line formation, and the largest of these examples is shown here. (a) Overhead view of the flock; average flight direction is along the positive Y axis; blue circles show bird positions and black lines are 2D velocity vectors. All birds are within a ± 1 wingspan horizontal slice. (b) The relative location of nearest neighbors; the modal location (red circle) was at a displacement of 0.8 wingspans lateral and 0.5 wingspans trailing distance. Trailing position was more varied than lateral position. Wind speed was low (<2 m s−1) according to weather station data and the wind speed estimated from the ground speed and flight direction of the birds. The data used to generate this figure are available in Figure 3—source data 1.

### Extended flock structure

We next examined how individual neighbor alignment rules relate to flock structure. We measured the angular distribution of neighbors at distances of two, four, six, and eight wingspans and at the maximum distance at which half of the flock remains in the flock’s core (range 5.8–24.3 wingspans). This last measure was used as a proxy for whole flock structure while avoiding edge effects (see 'Materials and methods'). For this analysis, we included all neighbors flying within a ±15 degree elevation slice relative to each focal bird. This was used instead of the ±1 wingspan slice used in other analyses (e.g., Figure 2, Figure 3) because this metric corresponds to a decreasing proportion of the volume at further distances. At a distance of two wingspans, flocks were consistently asymmetrical, with trailing birds more frequently flying to the left of their leading neighbors in 12 of 18 flocks and to the right of their nearest leading neighbors in the remaining six flocks. This asymmetry persisted at all distances within the flock (Figure 6a), including the overall flock shape (Figure 6b). The direction of asymmetry was independent of relative camera viewing direction and flock turning direction but was positively correlated with relative wind direction (see statistical results in Table 2).

![Figure 6.](https://cdn.elifesciences.org/articles/45071/elife-45071-fig6-v1.jpg)

**Figure 6.:** (a) Polar plot showing mean neighbor angle for right-aligned and left-aligned flocks over a range of distances. Shaded regions show 95% confidence intervals. (b) Overhead and profile views of an example right-aligned flock (avocet flock 1220–2). Note the many echelon formations aligned from back left to front right and the overall shape of the flock. The inset shows scale in wingspans. The data used to generate this figure are available in Figure 6—source data 1.

**Table 2.**
 Flock orientation.Table 2—source data 1.Flock orientation data.


<table>
  <thead>
    <tr>
      <th>Variable</th>
      <th>Test</th>
      <th>N</th>
      <th>R2</th>
      <th>t/F</th>
      <th>P</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Wind direction</td>
      <td>Circular correlation</td>
      <td>18</td>
      <td>0.29</td>
      <td>2.29</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>Turn direction</td>
      <td>Linear regression</td>
      <td>18</td>
      <td>0.00</td>
      <td>0.04</td>
      <td>0.83</td>
    </tr>
    <tr>
      <td>Camera direction</td>
      <td>Circular correlation</td>
      <td>18</td>
      <td>0.02</td>
      <td>0.61</td>
      <td>0.54</td>
    </tr>
  </tbody>
</table>

_Tests of the relationship between flock left-right orientation (Figure 6) and environmental factors. The data usedto generate this table are available in Table 2—source data 1._

### Flock biomechanics

We quantified several biomechanically relevant parameters from individual birds in flocks, including ground speed, estimated air speed, ascent or descent speed, wingbeat frequency and flapping phase. We created linear mixed effects (LME) statistical models to predict wingbeat frequency and airspeed from local and global flock positions and other flight parameters (Table 3). While speeds were measured for all individuals, flapping frequency and phase were only available from six cluster flocks in which birds were sufficiently close to the cameras to allow wingbeat measurements and for the simple-V formations. We examine only data for which wingbeat and estimated air speed data were available (N = 3306 individuals). We were also unable to measure flapping parameters from Dunlin, the smallest species recorded here.

**Table 3.**
 Flock biomechanics.Table 3—source data 1.Flock biomechanical data.


<table>
  <thead>
    <tr>
      <th>Wingbeat frequency predictors</th>
      <th>Estimate</th>
      <th>S.E.</th>
      <th>T</th>
      <th>d.f.</th>
      <th>P</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Intercept (dowitchers)</td>
      <td>8.82</td>
      <td>0.132</td>
      <td>66.5</td>
      <td>2817</td>
      <td>&lt;0.00001</td>
    </tr>
    <tr>
      <td>Godwit</td>
      <td>−2.19</td>
      <td>0.035</td>
      <td>−63.5</td>
      <td>2817</td>
      <td>&lt;0.00001</td>
    </tr>
    <tr>
      <td>Avocet</td>
      <td>−1.91</td>
      <td>0.040</td>
      <td>−47.5</td>
      <td>2817</td>
      <td>&lt;0.00001</td>
    </tr>
    <tr>
      <td>Airspeed (m s−1)</td>
      <td>−0.05</td>
      <td>0.013</td>
      <td>−4.3</td>
      <td>2817</td>
      <td>0.00002</td>
    </tr>
    <tr>
      <td>Flock position</td>
      <td>0.13</td>
      <td>0.032</td>
      <td>4.0</td>
      <td>2817</td>
      <td>0.00006</td>
    </tr>
    <tr>
      <td>Nearest neighbor distance (wingspans)</td>
      <td>−0.03</td>
      <td>0.010</td>
      <td>−3.2</td>
      <td>2817</td>
      <td>0.00153</td>
    </tr>
    <tr>
      <td>Nearest neighbor species</td>
      <td>−0.45</td>
      <td>0.038</td>
      <td>11.9</td>
      <td>2817</td>
      <td>&lt;0.00001</td>
    </tr>
    <tr>
      <td>Z-speed (m s−1)</td>
      <td>0.29</td>
      <td>0.019</td>
      <td>15.1</td>
      <td>2817</td>
      <td>&lt;0.00001</td>
    </tr>
    <tr>
      <td>Airspeed predictors</td>
      <td>Estimate</td>
      <td>S.E.</td>
      <td>T</td>
      <td>d.f.</td>
      <td>P</td>
    </tr>
    <tr>
      <td>Intercept (dowitchers)</td>
      <td>10.69</td>
      <td>0.225</td>
      <td>47.5</td>
      <td>2832</td>
      <td>&lt;0.00001</td>
    </tr>
    <tr>
      <td>Godwit</td>
      <td>−0.25</td>
      <td>0.067</td>
      <td>−3.7</td>
      <td>2832</td>
      <td>0.00022</td>
    </tr>
    <tr>
      <td>Avocet</td>
      <td>−1.51</td>
      <td>0.067</td>
      <td>−22.6</td>
      <td>2832</td>
      <td>&lt;0.00001</td>
    </tr>
    <tr>
      <td>n.n. distance (wingspans)</td>
      <td>−0.08</td>
      <td>0.015</td>
      <td>−5.2</td>
      <td>2832</td>
      <td>&lt;0.00001</td>
    </tr>
    <tr>
      <td>Edge distance (wingspans)</td>
      <td>−0.03</td>
      <td>0.003</td>
      <td>−10.3</td>
      <td>2832</td>
      <td>&lt;0.00001</td>
    </tr>
    <tr>
      <td>Wingbeat frequency (H z)</td>
      <td>−0.12</td>
      <td>0.025</td>
      <td>−5.0</td>
      <td>2832</td>
      <td>&lt;0.00001</td>
    </tr>
    <tr>
      <td>Flock position</td>
      <td>−0.24</td>
      <td>0.045</td>
      <td>−5.4</td>
      <td>2832</td>
      <td>&lt;0.00001</td>
    </tr>
    <tr>
      <td>Aerodynamic neighbor</td>
      <td>0.23</td>
      <td>0.040</td>
      <td>5.7</td>
      <td>2832</td>
      <td>&lt;0.00001</td>
    </tr>
  </tbody>
</table>

_Results from linear mixed-effects models relating wingbeat frequency and airspeed to other measured variables. Nearest neighbor only defined when this bird is leading the focal bird. Godwit and avocet are dummy variables coding species differences relative to dowitchers. Nearest neighbor species is coded −1 for a smaller neighbor, 0 for same the species, and 1 for a larger neighbor. Flock position is continuously scaled from 0.0 (front) to 1.0 (back). Aerodynamic neighbor was coded 1 for birds flying within 0.7–1.5 wingspans lateral distance and within two wingspans distance from their nearest leading neighbor, 0 otherwise. Models were selected using Bayesian information criteria. The data used to generate this table are available in Table 3—source data 1. d.f., degrees of freedom._

We observed several individual and flock effects on flight speed and wingbeat frequency (see Table 3 for full statistical results). As expected, different species flew with different characteristic flapping frequencies (LME, p<0.00001 for all species) and speeds (LME, p<0.00001 for dowitcher and avocet, p=0.00022 for godwit), and climbing flight was associated with an increase in flapping frequency (LME, p<0.00001). Birds flying near the front of the flock along the direction of travel (birds were given a continuous index with 0 being the frontmost and 1 the rearward-most position) flew faster (LME, p<0.00001) and with a lower flapping frequency than those near the rear (LME, p<0.00006). Birds flying near the edge of the flock also flew faster than those in the middle (LME, p<0.00001). Higher flapping frequencies were correlated with slower flight (LME, p<0.00001). Birds flying within a plausible range of locations for aerodynamic interaction (0.7–1.5 wingspans lateral distance and within two wingspans overall distance of their leading neighbor, coded as ‘Aerodynamic neighbor’ in Table 3) flew faster than expected after controling for the other effects described above (LME, p<0.00001, Figure 7). However, positioning in this aerodynamic interaction region had no effect on flapping frequency, as it was not in our best model of wingbeat frequency based on Bayesian information criteria (BIC; Table 3). Adding the aerodynamic neighbor to the best model makes the term non-significant (LME, p=0.30) and increases the BIC of the model by 6.8.

![Figure 7.](https://cdn.elifesciences.org/articles/45071/elife-45071-fig7-v1.jpg)

**Figure 7.:** Here we show the effect of neighbor position on flight speed. (a) Flight speed residuals after accounting for species, flapping frequency, distance from flock edge, nearest neighbor distance in terms of wingspans and overall position along the length of the flock. (b) Flight speed residuals after accounting for just species and flapping frequency. White spaces in the heat map are bins with fewer than 20 samples, out of 2848 possible in (a) and 3306 possible in (b). Both analyses reveal a broadly similar pattern, where the positive effect of neighbor position on flight speed is strongest at a one wingspan lateral displacement and a trailing distance of 0 to 0.5 wingspans. This pattern cannot be generated by trailing birds passing leaders because the roles reverse after passing occurs, leaving no net speed difference. The data used to generate this figure are available in Figure 7—source data 1.

We examined the compound-V-flock data for evidence of flapping synchronization by examining the temporal and spatial phase offset between pairs of nearest neighbors for which synchronous wingbeat frequency data were available for at least 20 frames (see 'Materials and methods'). We found no evidence for temporal (Rayleigh test; N = 117; Z = 1.98; p=0.14) or spatial wingbeat synchronization (Rayleigh test; N = 117; Z = 1.28; p=0.27) in the compound-V-formation shorebird flocks. We performed the same tests on the simple-V formation of godwits and again found no support for phasing relationships (Rayleigh test; temporal phasing N = 39; Z = 0.09; p=0.90; spatial phasing; N = 39; Z = 0.46, p=0.63).

## Discussion

Here, we report on the first cross-species quantitative analysis of bird flocking behavior. On the basis of previous studies, we predicted that larger species would adopt more structured flocks and would exhibit more frequent aerodynamic positioning. Neither of these hypotheses were supported by our data. Instead, we document a flock structure that we term the compound-V formation, in which birds in cluster flocks align to nearest neighbors within their same elevation slice (±1 wingspan) with a one-wingspan lateral offset while allowing front-back distance to fluctuate with flock density (Figures 2, 3 and 4). This flock type is similar to the shorebird ‘cluster’ and ‘bunch’ formations described by Piersma et al. (1990) and the ‘front cluster’ of Heppner (1974). Here, this structure was observed in single- and mixed-species flocks of four shorebird species covering a seven-fold range in body mass. The simple alignment rule produces a flock structure that can be observed at all spatial scales within the flock, including overall flock shape (Figure 6). This is in contrast to flocks of other species, such as starlings, in which structure is only observed within each neighbor’s six nearest neighbors, equivalent to 1.2–2.7 wingspans (Ballerini et al., 2008a). Our data also show that shorebird global flock alignment is responsive to estimated local wind conditions (Table 2), and future work exploring this interaction may allow identification of the mechanism that governs the overall alignment. Wind conditions did not have discernible effects on local alignment, possibly because of the uncertainty in the measurement of the wind vector itself.

Mixed-species assemblages typically represent around 10% of migratory shorebird flocks (Piersma et al., 1990), possibly because species that have different preferred flight speeds would have to compromise their flight speed in order to remain together as a group. Our data include ~10% mixed-species flocks (2 of 18) and support the hypothesis that differences in preferred flight speed influence whether different species flock together. We documented two mixed-species flocks of godwit and dowitcher; these flocks had an airspeed of 9.02 ± 0.34 m s−1 (mean ± s.d., n = 2). The single-species godwit and dowitcher flocks had airspeeds of 9.64 ± 1.53 (n = 3) and 8.99 ± 1.92 m s−1 (n = 3), respectively. Dunlin, which were present at the same time as godwits and dowitchers but did not fly in mixed flocks with these species, had an airspeed of 7.58 ± 0.11 m s−1 (n = 7). Similarly, Avocets not observed to mix with other species at our field site, and they flew with airspeeds of 8.04 ± 0.13 m s−1 (n = 3). Thus, the similarity in preferred flight speeds among godwits and dowitchers might be important for these species to form mixed-species flocks. Dunlin and avocets also flew at similar airspeeds, but were not observed in mixed-species flocks, perhaps because of their large difference in body size, wingbeat frequency, and/or maneuverability.

The flock data presented here also include other interesting results that lack clear explanations. Flight speed varied with position from front to rear and from center to margin (Table 2), implying that the flocks were not necessarily in equilibrium. This might cause larger flocks to separate into several smaller flocks over time, consistent with the observation that the arrival group size of migratory species is typically smaller than the departure group size (Piersma et al., 1990).

Because birds in simple and compound-V formations adopt similar neighbor alignment rules, functional hypotheses for simple-V formations might also apply to compound-V formations. These include collision avoidance and information transfer (Dill et al., 1997). Collision avoidance is a plausible hypothesis to explain the formation of simple-V formations because they theoretically permit birds to keep all neighbors out of their direct path of travel. This is not the case for compound-V formations, where many birds are flying in front of and behind one another (Figure 1b; Figure 6b). The problem of collision avoidance is exacerbated in compound-V formation because birds tend to fly in the same horizontal plane. A better strategy for collision avoidance is to fly in a three-dimensional shape, such as that adopted by flocks of chimney swifts (Evangelista et al., 2017). In these flocks, the most common neighbor position is further lateral than in the shorebird flocks and with a shorter trailing distance, more completely moving those individuals out of the path of other flock members (Figure 3—figure supplement 1). Finally, even in the simple-V formation recorded here (Figure 5), birds flew with approximately 20% of wingspan overlap and so did not have an entirely clear forward path. Thus, collision avoidance appears to be an unlikely explanation for the structuring of both the compound-V and simple-V formations recorded here.

Simple and compound-V formations might also be structured to maximize the observability of neighbors, facilitating information transfer by helping birds to detect and respond to changes in neighbor speed or direction, and improving flock cohesiveness by allowing information to propagate through the flock more quickly. Dill et al. (1997) proposed that birds in V formation should maximize the measurement of neighbor movements by aligning at a 35.3 degree angle (relative to the direction of travel), or alternatively should maximize the measurement of neighbor speed by aligning at a 63.4 degree angle. The shorebird flocks examined here had modal neighbor-position alignment angles ranging from 33.7 to 51.8 with an average of 41.2 degrees. Neither this mean angle nor the nearly 20-degree range in alignment angle is consistent with Dill’s hypotheses or others calling for a single optimal alignment angle. Our finding that lateral spacing is uncorrelated with flock density, whereas trailing spacing increases with decreasing density, shows that the shorebird flocks are more organized in lateral distance than in trailing distance or alignment angle. Thus, hypotheses calling for organization based on alignment angle, whether to maximize information transfer or to keep lead birds in the visual fovea of trailing neighbors in a V formation (Badgerow and Hainsworth, 1981), are not well supported by our results.

Theoretical (Badgerow and Hainsworth, 1981; Hummel, 1983; Lissaman and Shollenberger, 1970; Maeng et al., 2013) and empirical research (Portugal et al., 2014; Weimerskirch et al., 2001) has provided support for the hypothesis that birds flying in simple-V formations gain aerodynamic and energetic benefits, and we propose that such benefits might also explain why birds adopt the compound-V formation. In both cases, birds fly with a lateral offset of approximately one wingspan while allowing trailing distance to vary (Figures 3 and 5), facilitating aerodynamic interaction. When compared to simple-V formations, compound-V formations allow greater flock densities, which should allow more rapid information transfer (Attanasi et al., 2014), larger flock sizes, and improved predator defense (Powell, 1974). Analyses of the airspeeds and wingbeat frequencies of flocking shorebirds provide some support for the aerodynamic alignment hypothesis. Birds flying in positions where beneficial aerodynamic interactions are predicted to occur flew faster than expected after controling for other factors (aerodynamic neighbor term in Table 3, linear mixed effects model for airspeed, p<0.0001). Over the entire dataset, 29.7% of nearest neighbor positions were in the ‘aerodynamic neighbor’ location (Figure 3—figure supplement 2), compared with only 3.4% of nearest neighbor in flocking chimney swifts (Figure 3—figure supplement 1). This faster flight should produce a reduced cost of transport, assuming there are no unmeasured compensating factors such as a simultaneous increase in stroke amplitude. Nevertheless, this speculative interpretation of the compound-V formation raises many new questions, such as how birds in the flock can maintain different speeds without separating and why an aerodynamic benefit would manifest as an increase in speed instead of, for example, a reduction in flapping frequency and airspeed as suggested by theoretical models (Hummel, 1983). Furthermore, despite the similarities in modal position among compound-V and simple-V flocks (Figures 3 and 5), it is not clear whether a single set of adjustment rules or responses to changes in neighbor position can produce both flock types. These questions, and a definitive explanation for why birds adopt a compound-V formation, cannot be answered with the current dataset. Progress in these areas will depend on new theoretical modeling and data collection from on-bird loggers measuring physiological, flock positioning and biomechanical data from a variety of species over a range of behavioral contexts. Further videographic flock surveys may also improve understanding of the variety of flock types, especially when collected with careful attention to behavioral context and with full measurement of local environmental conditions.

## Materials and methods

### Field recording

We recorded multi-camera video of freely behaving, wild birds in Humboldt County, California between 17 April and 27 April 2017 and between 20 December 2017 and 1 January 2018. Recordings were made at the Arcata Marsh Wildlife Sanctuary (40°51'25.35"N, 124° 5'39.37"W) and above agricultural fields in the Arcata bottoms (40°53'51.98"N, 124° 6'55.85"W). No birds were captured or handled, and we made efforts to avoid influencing bird behavior. Video was captured at 29.97 frames per second and 1920 × 1080 pixel resolution using three Canon 6D cameras with 35 mm or 50 mm lenses. Cameras were set along a 10 m transect and staggered in elevation. We set cameras up to overlook locations where birds aggregated during high tide or when foraging in agricultural fields. Flocking events included birds moving with the tide, or flushing in response to predators (e.g., peregrine falcons) or for unknown reasons. Cameras recorded continuously for up to 3 hr per day. For analysis, we selected flocks that included at least 100 individuals and that had an orientation and size that allowed visual discrimination of individuals within the flock.

### Bird detection

We used the MATLAB R2017a (Natick, MA, USA) computer vision toolbox to generate code for detecting birds in video recordings. A foreground detector first separated moving objects from the stationary background. A gaussian filter was then applied to the image with a diameter matched to bird size under the recording conditions. Two-dimensional peak detection found local peaks in the smoothed image that were taken as potential bird positions.

Under some conditions, overlapping wings of adjacent birds prevented accurate detection of many individuals. To overcome this problem, we developed a frame-averaging algorithm that helped to obscure the wings and to emphasize the bodies. Here, optic flow determines the overall movement of the flock for each frame. Using the optic flow measurements and two-dimensional interpolation, the algorithm subtracts movement between frames. A rolling 5-frame window is then applied to the entire video. This procedure highlights pixels that are moving in the same direction as the flock, such as the birds’ bodies, while filtering pixels that are moving in other directions, such as the wings.

### Three-dimensional calibration

Camera calibration followed established methodology (Hedrick, 2008; Jackson et al., 2016; Theriault et al., 2014), with the exception that the distance between cameras, instead of an object placed in view of the cameras, was used to scale the scene. This approach allowed us to record in locations where it was infeasible to place calibration objects in front of the cameras (e.g., over water). The in-camera horizontal alignment feature was used to align cameras to the horizon. The pitch of the camera was measured with a digital inclinometer with 0.1-degree precision. This allowed alignment of the scene to gravity in post processing, with the vertical (Z axis) origin placed at the level of the cameras. This permitted direct measurement of the elevation of the birds relative to one another.

Background objects that were visible in the scene were used as calibration points. We developed a preliminary calibration using stationary objects such as trees, poles, and sitting birds. We then added flying birds, ensuring that points covered a wide range of distances and elevations relative to the cameras. Calibrations had low direct linear transformation (DLT) residuals (<0.5–1 pixel), indicating high-quality calibrations.

### Camera synchronization

Cameras were synchronized by broadcasting audio tones over Walkie Talkies (Motorola Talkabout MH230) to each camera. Audio tones were broadcast approximately once every five minutes during recording. A time offset was determined for each pair of cameras using cross-correlation of the audio tracks. This offset allowed camera synchronization within ±one half of a frame, or 16.6 ms.

In recordings where birds were relatively close to the camera (<50 m) and moving at relatively high pixel speeds, we used sub-frame interpolation to achieve increased synchronization accuracy of one tenth of a frame, or ±1.7 ms. To determine the subframe offset, we interpolated tracks of moving birds used as background points in the calibration at 0.1 frame intervals from −1 to +1 frame (−1.0,–0.9, etc). We then calculated the DLT residual for a calibration with each combination of subframe-interpolated points for the three cameras. The set of offsets generating the lowest DLT residuals was used for the final calibration and applied to birds tracked in the study.

### Three-dimensional assignment

To reconstruct the three-dimensional positions of birds in a flock, 2D detections of individuals must be correctly assigned between cameras. We modified established software for this task (Evangelista et al., 2017; Wu et al., 2009). Briefly, the software first finds all combinations of 2D points having DLT residuals of <3 pixels. The software iteratively generates 3D points, starting with points that have the lowest DLT residuals and only allowing a 2D detection to be reused a single time. This helps with the problem of occlusion while limiting the number of ‘ghost’ birds (bird positions created from incorrectly matching detections among cameras). This process is repeated twice. The first iteration allows the user to determine a bounding region in the 3D space in which the flock is contained. In the second iteration, three-dimensional positions outside this bounding region are filtered before they can be considered as potential 3D points.

### Track generation

After 3D points have been generated, they are linked between frames to generate individual flight tracks. Here, a Kalman filter predicts the position of each bird in the subsequent frame for the 2D information from each camera and for the reconstructed 3D positions. In the first frame, the Kalman filter is seeded using optic flow measurements. For each frame step, a cost matrix is created from weighted sums of the 2D and 3D errors between predicted track positions and each reconstructed 3D point. The Hungarian algorithm is used to find a global optimum that minimizes the error in track assignment. A track that is not given an assignment is continued with a gap of up to four frames (0.13 s), after which it ends and any re-detection of the bird in question will start a new track.

### Wingbeat frequency analysis

We measured wingbeat frequencies in a subset of recordings in which birds were both large enough and close enough to cameras to discern wingbeat oscillations. This excluded flocks of our smallest species, dunlin, and some flocks that were relatively distant from cameras. To measure wingbeat frequency, we used blob analysis to find a bounding box for each bird in each frame. We excluded blobs for which the bounding box included two or more birds as determined using the track-assignment algorithm described above. We averaged four components of the bounding box to measure wingbeat phase: height, inverse of the width, detrended X-coordinate of top-left corner, and inverse of detrended Y-coordinate of the top-left corner. This allowed quantification of wingbeat phase independent of bird orientation with respect to the cameras. Wingbeat phase was averaged across cameras and bandpass filtered before a 128-point Fast Fourier Transform (FFT) was applied to measure wingbeat frequency. The frame rate of the cameras (29.97 frames per second) and the FFT window determined a wingbeat frequency bin size of 0.12 wingbeats s−1. Our method is similar to that used in a recent study of two corvid species (Ling et al., 2018).

### Species identification in mixed-species flocks

We recorded two mixed-species flocks of godwits and dowitchers. The size difference between species allowed species identification using the detected pixel area and distance of each bird (Figure 8). Here, blob analysis quantifies the pixel area for each bird in each tracked frame. Area data were excluded when two tracked birds were within a single blob bounding box. A low-pass filter was applied to the sequence of pixel area data across frames for each tracked bird to remove wingbeat effects. An object’s pixel area scales with the inverse of the square root of distance. Therefore, for each frame, the square root of the filtered pixel area was multiplied by bird’s distance to provide a distance-scaled area. This value was averaged across frames and across cameras for each bird track. In mixed-species flocks, a histogram of the scaled area had two distinct peaks with only a small amount of overlap (Figure 8a). Fitting two normal distributions to these data revealed an expected error rate in species identification of 3.3%. The scaled area where the two normal distributions intersect was used as the threshold for species identification.

![Figure 8.](https://cdn.elifesciences.org/articles/45071/elife-45071-fig8-v1.jpg)

**Figure 8.:** (a) Histogram of scaled pixel area of birds within a mixed-species flock. The two peaks are modeled as normal distributions. The area value where the two distributions intersect (indicated by the arrow) is used as the threshold for species identification. (b) Example section of a mixed-species flock with species identifications labeled by color.

### Neighbor alignment metrics

We quantified the relative position of each bird and its nearest neighbor in the flock (Figure 2). This was done separately for neighbors within ±1 wingspan in flight elevation—the potential positions at which aerodynamic interactions and collisions are plausible—and for neighbors beyond ±1 wingspan. For each flock, we calculated the modal lateral distance and modal front-back distance by taking the peak of a probability density function generated with a kernel density estimator and a smoothing bandwidth of 0.25 wingspans. We used modal values because distance calculations are truncated at zero, producing skewed distributions.

In a subsequent analysis (Figure 6), we quantified the angular distribution of neighbors at distances of two, four, six, and eight wingspans, and at a maximum radius depending on the size of the flock. Two-wingspan bins centered at the reference distance were used for selecting data points (e.g. birds within 1–3 wingspans were included in the two-wingspan bin). Our aim was to examine the extent of internal structure within the flock. Because edge effects could create the appearance of internal structure, we excluded birds whose edge distance was less than the wingspan of the bin being analyzed. For example, for the two-wingspan analysis, all birds within three wingspans of the horizontal edge of the flock were excluded. The maximum radius was taken as the median horizontal edge distance of all birds in the flock (Figure 9). This ensured that our analysis always included at least half of the flock.

![Figure 9.](https://cdn.elifesciences.org/articles/45071/elife-45071-fig9-v1.jpg)

**Figure 9.:** An overhead view of an example flock of avocets (flock 1220–2). Because flocks were always spread out in the horizontal direction, a compact hull is fitted to the XY-coordinates to create a boundary. The minimum horizontal distance of each bird to the hull is the bird’s edge distance. The median edge distance is taken as the flock’s maximum radius for computing alignment metrics (Figure 6). Here, birds within the maximum edge distance (6.5 wingspans or 4.55 m) are labeled edge, and birds beyond the maximum edge distance are labeled core.

### Wingbeat phase analysis

We conducted an analysis to test for temporal and spatial wingbeat phase synchronization, following previously established methods (Portugal et al., 2014). We selected pairs of nearest neighbors in flocks where simultaneous wingbeat frequency data were available for both individuals for at least 20 frames (0.66 s). Cross correlation was used to determine the temporal phase offset between the birds. This value was divided by 2πd, where d is wingbeat duration, to attain a value between 0 and 2π. The spatial phase offset equals the temporal phase offset minus 2πλ, where λ is wingbeat wavelength. We tested for temporal and spatial synchrony by applying Rayleigh’s test for homogeneity of circular data to the temporal and spatial phase delays.

### Estimating wind speed and direction

We estimated local wind speed and direction for each flock using observed variation of ground speeds from birds flying in different directions. Ground speeds and flight directions were calculated for each bird at one-wingbeat time intervals. Median ground speed was calculated for each 10-degree bin having at least 500 data points. A circle was then fit to these median values, with the center of the circle representing a vector of wind direction and magnitude. Ground speeds and wind direction and magnitude were then used to calculate airspeeds. This approach is similar in principle to that used to estimate local wind speed from the drift in the ground reference frame position of circling vultures (Weinzierl et al., 2016), and shares the important assumption that airspeed is independent of wind direction. However, birds are theoretically expected and empirically known to vary airspeed with wind speed when flying in order to reach a destination efficiently (Hedrick et al., 2018; Shamoun-Baranes et al., 2007). Whether this is the case for shorebird flocks (making shorter flocks around the stopover point) is unknown, so we did not attempt to model this possible effect.

We compared our wind estimates to data from nearby weather stations. Our estimated wind direction and speed was typically within ±45 degrees and ±2 m s−1 of weather station data (weather station KCAARCAT25). To avoid disturbing the birds, we did not attempt to release helium balloons to measure local wind conditions at altitude. Note that because our analysis here is based almost entirely on the positions and speeds of birds relative to their neighbors, our results are largely insensitive to the wind speed and direction. However, precise determination of bird airspeed and wind direction is required to model the expected position of the wake of the bird, and the absence of this information means that it is not possible to determine when or even if trailing birds interact with the wake of a leading neighbor, or to predict what flapping phase offset would be appropriate for aerodynamically beneficial interaction.

### Statistical analysis

Analyses were conducted using the statistical toolbox in MATLAB r2017b (The Mathworks, Natick, MA, USA). We tested uniformity of circular distributions using Rao’s test (Fisher, 1995). Because multiple peaks were sometimes present, modal values were calculated using a circular kernel density estimator as an indicator of the predominant alignment direction. For the biomechanical analysis, we used linear mixed-effects models to predict individual wingbeat frequency and airspeed from seven fixed effects—nearest neighbor distance, nearest-neighbor lateral distance, edge distance, airspeed, vertical speed, nearest neighbor species, front-back flock position and hypothesized aerodynamic positioning. Bayesian information criterion (BIC) was used for model selection. All P-values were computed assuming two-tailed distributions.
