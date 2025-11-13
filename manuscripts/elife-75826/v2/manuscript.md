# Adaptation of Drosophila larva foraging in response to changes in food resources

## Authors

- Marina E Wosniack<sup>1</sup> ([ORCID: 0000-0003-2175-9713](https://orcid.org/0000-0003-2175-9713))
- Dylan Festa<sup>2</sup> ([ORCID: 0000-0003-3803-1542](https://orcid.org/0000-0003-3803-1542))
- Nan Hu<sup>3</sup>
- Julijana Gjorgjieva<sup>1</sup> ([ORCID: 0000-0001-7118-4079](https://orcid.org/0000-0001-7118-4079)) †
- Jimena Berni<sup>3</sup> ([ORCID: 0000-0002-5068-1372](https://orcid.org/0000-0002-5068-1372)) †

### Affiliations

1. Computation in Neural Circuits Group, Max Planck Institute for Brain Research Frankfurt Germany ([ROR:02h1nk258](https://ror.org/02h1nk258))
2. School of Life Sciences, Technical University of Munich Munich Germany ([ROR:02kkvpp62](https://ror.org/02kkvpp62))
3. Department of Zoology, University of Cambridge Cambridge United Kingdom ([ROR:013meh722](https://ror.org/013meh722))
4. Brighton and Sussex Medical School,, University of Sussex Brighton United Kingdom ([ROR:00ayhx656](https://ror.org/00ayhx656))

† Corresponding author

## Abstract

All animals face the challenge of finding nutritious resources in a changing environment. To maximize lifetime fitness, the exploratory behavior has to be flexible, but which behavioral elements adapt and what triggers those changes remain elusive. Using experiments and modeling, we characterized extensively how Drosophila larvae foraging adapts to different food quality and distribution and how the foraging genetic background influences this adaptation. Our work shows that different food properties modulated specific motor programs. Food quality controls the traveled distance by modulating crawling speed and frequency of pauses and turns. Food distribution, and in particular the food–no food interface, controls turning behavior, stimulating turns toward the food when reaching the patch border and increasing the proportion of time spent within patches of food. Finally, the polymorphism in the foraging gene (rover–sitter) of the larvae adjusts the magnitude of the behavioral response to different food conditions. This study defines several levels of control of foraging and provides the basis for the systematic identification of the neuronal circuits and mechanisms controlling each behavioral response.

## Introduction

Most moving organisms need to explore their surroundings to increase their chances of finding nutritious resources. This is a challenging task in natural environments, where food quality varies both in time (e.g., seasonal effects) and space (e.g., patchy distribution). Therefore, the exploratory behavior of animals has to be flexible and adapt to environmental challenges. From the perspective of evolutionary ecology, foraging strategies have evolved to maximize lifetime fitness under distinct constraints (Stephens and Krebs, 1987) including the concentration of food inside patches (Charnov, 1976). Accordingly, several hypotheses and models have been developed to predict the optimal foraging strategy that an animal will adopt (Stephens and Charnov, 1982; Viswanathan et al., 2011). These models postulate that animals will use different strategies depending on the distribution of the resources. In environments where resources are abundant, animals will search and exploit them performing short movements in random directions, in patterns well approximated by Brownian random walks. When resources are sparse, and foragers have incomplete knowledge about their location, a more diffusive strategy is needed, with an alternation between short- and long-range movements, which can be modeled as a Lévy random walk. Analysis of animal movements in the wild has demonstrated that environmental context can induce the switch between Lévy to Brownian movement patterns (Humphries et al., 2010), but the effective mechanisms behind the implementation of such behavior (e.g., cognitive capacity, memory) often remain elusive (Budaev et al., 2019). Understanding the motor mechanisms that regulate the execution of different movement strategies and the transitions between them could provide insight into how the nervous system can drive the search for resources in complex and ever-changing environments. Drosophila larva is an excellent model to study this question, because the movement of single animals can be tracked for long periods of time in a controlled environment.

Larvae of the fruit-fly are constantly foraging and feeding to fulfill their nutritional needs for the following non-feeding pupal stage. They explore the substrate by executing sequences of crawls, pauses, and turns (Berni, 2015; Berni et al., 2012) and can efficiently explore an environment even without brain input (Sims et al., 2019). Larvae approach (or avoid) sources of odor by triggering oriented turns during chemotaxis (Gomez-Marin et al., 2011) and can also navigate through gradients of light intensity (Kane et al., 2013; Humberg and Sprecher, 2018), temperature (Luo et al., 2010; Lahiri et al., 2011), and mechanosensory cues (Jovanic et al., 2019). Their natural habitat is decaying vegetable matter distributed in patches (Ringo, 2018), and due to food decay and intraspecific competition larvae are constantly deciding what patch to visit and how long to stay before exploring for new higher quality food patches. This constant exploration comes at a high energetic cost since crawling behavior is very demanding (Berrigan and Lighton, 1993; Berrigan and Pepin, 1995).

The foraging behavior of Drosophila both in the larval and adult stages is influenced by the foraging (for) gene (Sokolowski, 2001; Sokolowski et al., 1997). Larvae with the rover allele crawl significantly longer paths on a yeast paste than larvae with the sitter allele, and a proportion of 70% rovers and 30% sitters is observed in natural populations (Sokolowski, 2001). Due to the higher dispersal of rover larvae, their pupae are usually found in the ground while those from sitter are usually found on the fruit (Sokolowski et al., 1986). However, it is not known if the behavioral differences between rover and sitter larvae can be observed in food substrates of different compositions, nor how rovers and sitters behave in a patchy environment of regions with and without food (even though it has been hypothesized that rover larvae are more likely than sitter to leave a patch of food to search for a new one, Sokolowski, 2001).

Previous studies on larval foraging focused on the behavior in homogeneous substrates, where larvae engage in a highly exploratory movement pattern if no food is available (Berni et al., 2012; Godoy-Herrera et al., 1984; Sims et al., 2019). However, the natural habitat of larvae is very patchy and it is not clear how they select feeding vs. exploring when the environment has food patches separated by areas without food. Previous studies have shown that larvae are more willing to leave a patch if the protein concentration is low but tend to stay in the patch if its nutritional content is adequate (Ringo, 2018). Nevertheless, these studies lack an individualized tracking of the path executed by larvae during patchy exploration.

Here, we investigate the mechanisms of foraging that adapt to changes in food distribution. To address this challenge, we investigate how (1) the quality of the food and (2) its distribution, homogenous vs. constrained in small patches, influence larval foraging. We test the effect of the rover and sitter genetic dimorphism in the different food distributions and disentangle the role of olfaction in remaining in food patches using anosmic animals. By combining a detailed analysis of individual larval trajectories from behavioral experiments and computational modeling, we characterize the elements of the navigation routine and show how they adapt to a changing environment. Our results show a modular adaptation to different food characteristics. Food quality modulates crawling speed, turning frequency, and fraction of pauses controlling the distance traveled and therefore the area explored. The patchy distribution of food triggers oriented turns toward the food at the patch interface, increasing the time larvae exploit the food inside the patch. The foraging polymorphism of rovers and sitters adjusts the degree of the behavioral response to different food conditions. The detailed description of the larval behavior and the model presented here provide the basis for the systematic identification of the neuronal circuits and mechanisms controlling each behavioral response modulated by different food resources.

## Results

### Food quality controls the distance traveled modulating the speed and the frequency of pauses

To study the effect of different food substrates in foraging larvae, we devised a behavioral assay where larvae explore different substrates with minimal external stimuli (Figure 1A). The three different substrates (agar, sucrose, yeast) had the same agar density but distinct nutritional quality (with yeast being the richest due to its high content of protein) (Materials and methods). Wildtype larvae from different polymorphisms – rovers and sitters – were separately recorded because of previously reported differences in foraging behavior (Sokolowski et al., 1997). We recorded the free exploratory behavior of groups of 10 third-instar larvae in large arenas (240 × 240 mm2) for 50 min and then tracked each individual trajectory (Risse et al., 2013; Sims et al., 2019). Three independent replicates were analyzed. To identify salient turning points in the trajectory and to obtain the distribution of turning angles of each larva, we used the Ramer–Douglas–Peucker algorithm (Materials and methods). Larvae explored the three different substrates (Figure 1B and Figure 1—figure supplement 1A) by executing sequences of crawls, turns (marked as circles in the trajectories), and pauses. Interestingly, we observed that a preferential orientation – clockwise (CW) or counter-clockwise (CCW) – is present in many trajectories, and the paths described often have circular shapes (Figure 1B).

![Figure 1.](https://cdn.elifesciences.org/articles/75826/elife-75826-fig1-v2.jpg)

**Figure 1.:** (A) Experimental setup: 10 larvae of the same phenotype (rover or sitter) were placed on the top of an agar-coated arena and recorded for 50 min, experiments were repeated three times with independent samples. Three types of substrates were used: agar-only (blue), sucrose (green), and yeast (orange). (B) Sample trajectories of rover larvae in the different substrates (top: agar, bottom left: sucrose, bottom right: yeast) with turning points identified by the RDP algorithm. Corresponding turning angle distributions are shown as an inset. (C) Average crawling speeds of rovers (N = 30, 30, 29) and sitters (N = 29, 30, 30) in the different substrates: agar (A, blue), sucrose (S, green), and yeast (Y, orange). The speed was calculated during bouts of crawls. Horizontal line indicates median, the box is drawn between the 25th and 75th percentiles, whiskers extend above and below the box to the most extreme data points within 1.5 times the interquartile range, points (gray for rovers, white for sitters) indicate all data points. (D) Average number of turns per minute registered in each trajectory. (E) Fraction of time in which larvae did not move (pauses). (F) Total distance traveled in 50 min. (G) Handedness score. The horizontal dashed line corresponds to a score of 0.5, that is, an equal number of counter-clockwise (CCW) and clockwise (CW) turns. Mann–Whitney–Wilcoxon test with Bonferroni correction was performed since the data were not normally distributed. ns: 0.05 < p < 1, *0.01 < p < 0.05, **0.001 < p < 0.01, ****p < 0.0001. The number of larvae tested is detailed in Table 1. Statistical power and Cohen’s size effect of non-significant comparisons are included in Table 4.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/75826/elife-75826-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Sample trajectories of sitter larvae in different substrates with the respective turning angle distributions in the inset. Top (blue): agar, bottom left (green): sucrose, bottom right (orange): yeast. (B) Crawling speeds in the agar (A, blue), sucrose (S, green), and yeast substrate (Y, orange). Darker colors are used to label rover’s data, lighter colors label sitter’s data. Horizontal line indicates median, the box is drawn between the 25th and 75th percentiles, whiskers extend above and below the box to the most extreme data points within a distance equal to 1.5 times the interquartile range and points indicate all data points. (C) Average number of turns executed by the larvae per minute. (D) Fraction of time in which larvae did not move (pauses). (E) Crawled distance in the first 5 min of the recording. (F) Crawled distance for the entire recording (50 min). (G) Handedness score. Mann–Whitney–Wilcoxon paired test (samples not normally distributed). The number of larvae tested is detailed in Table 1. ns: 0.05 < p < 1, *0.01 < p < 0.05, **0.001 < p < 0.01, ***0.0001 < p < 0.001.

We found that the presence of food in the substrate had a strong effect on the larval crawling speed. Rover (sitter) larvae crawl on average at a speed of 0.84, 0.68, and 0.37 mm/s (0.96, 0.68, and 0.31 mm/s) in the agar, sucrose, and yeast, respectively (Figure 1C). In addition to changing speed, larvae suppressed turning in the food substrates, with rover (sitter) larvae executing an average of 2.65, 2.44, and 2.00 (2.79, 2.13, and 1.71) turns per minute in the agar, sucrose, and yeast, respectively (Figure 1D). Larvae also paused more often in the yeast substrate (Figure 1E and Video 1). Most pausing larvae were completely still, except for internal movements in their gut, suggesting they were digesting (Video 1). As a consequence, the total distance traveled showed a clear dependence with food quality, with yeast, the most nutritious food, generating the shorter path and consequently often a smaller explored area (Figure 1B, F and S1A).

![Video 1.](https://cdn.elifesciences.org/articles/75826/elife-75826-video1.mp4.jpg)

**Video 1.:** A sitter larva was allowed to feed on a fine layer of yeast supplemented with 0.1% Bromophenol blue sodium salt (B5525, Sigma). During pauses the larvae are immobile and only the movement of their gut content can be seen.

We next quantified the individual orientation preference of each larva based on its turning angle distributions. We defined the handedness score H of a larva as the number of CCW turns divided by the total number of turns in the trajectory, that is, CCW and CW combined. Larvae with H > 0.5 (H < 0.5) have a bias to turn CCW (CW). Surprisingly, in both rover and sitter populations we found larvae with a very strong handedness, meaning that larvae have individual biases when turning in homogeneous environments that do not provide orientation cues in the form of sensory stimuli (Figure 1G).

Finally, we contrasted the differences in exploratory behavior of rovers and sitters in the different homogeneous substrates (Figure 1—figure supplement 1B–G). In particular, we were interested in evaluating if sitter larvae crawled significantly less than rovers in the first 5 min of the recording in the food substrates, as previously observed in experiments using yeast substrates (Sokolowski, 1980). We did not find significant differences between the crawled distances of rovers and sitters in the substrates that we tested. Thus, when the resources are distributed homogenously, the genetic foraging dimorphism could not be detected.

In summary, we have provided a detailed characterization of larval foraging behavior in homogenous substrates with different types of food. We found that larval crawling speed and probabilities to turn and to pause are behavioral elements that are adapted according to the quality of food.

### A phenomenological model of crawling describes larval exploratory behavior in patchy substrates

In ecological conditions, the fruit on which Drosophila eggs are laid and on which the larvae forage decays over time. To maximize their survival chances, and reduce competition, larvae therefore move toward food patches that are more nutritious and less crowded (Del Pino et al., 2015). Here, we designed a phenomenological model to simulate larval exploratory trajectories in different substrates based on our collected data (Figure 1 and Methods). The model predicted the fraction of time larvae spent inside patches of food, as a measure of food exploitation, if larvae only used the information about the substrate while foraging. Each type of larva (rover, sitter) had a distribution of crawling speeds $v$ and probabilities to crawl Pcrawl, to turn Pturn, and to pause Ppause in a given time step for each type of homogeneous substrate: agar, sucrose, and yeast (Figure 2A). To capture the variability in the turning behavior, each simulated larva had its own set of parameters for the turning angle distribution based on a single recorded larva. The simulated trajectories preserved the CW or CCW orientation inherited from the turning angle distributions characterized in the experiments (Figure 2B).

![Figure 2.](https://cdn.elifesciences.org/articles/75826/elife-75826-fig2-v2.jpg)

**Figure 2.:** (A) Simulated larva crawls at time steps tk and tk+2, turns at tk+1, and makes a pause at tk+3. Crawling speed and turning angle are sampled from normal and von Mises probability distributions, respectively. At each time step, there is a constant probability to turn Pturn or to pause Ppause. (B) Sample model trajectories and turning angle distributions of sitter larvae simulated in different homogeneous substrates: agar (left), sucrose (middle), and yeast (right). (C) Simulations with patchy environments: food (sucrose or yeast) is distributed inside two circular regions, with agar in the remaining substrate. Crawling speeds, turning and pause probabilities are sampled from different distributions when the simulated larva is inside (green) or outside (blue) the patch. (D) Sample model trajectories and turning angle distributions of sitter larvae in simulated patchy substrates: sucrose (left) and yeast (right) patches. (E) Average fraction of time each simulated larva (rover (r), sitter (s), N = 30) spent inside patches (sucrose and yeast) in the simulations. Horizontal line indicates median, the box is drawn between the 25th and 75th percentiles, whiskers extend above and below the box to the most extreme data points that are within a distance to the box equal to 1.5 times the interquartile range and points indicate all data points. Mann–Whitney–Wilcoxon paired test two-sided. ns: 0.05 < p < 1, ****p < 0.0001.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/75826/elife-75826-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Each simulated rover (left) and sitter (right) larva (bars with different color shades, N = 30) has a fixed turning angle distribution with parameters corresponding to one rover/sitter from the agar experiments. N = 30 simulation runs of each larva were performed in the same homogenous environment with sucrose. Horizontal line indicates median, the box is drawn between the 25th and 75th percentiles, whiskers extend above and below the box to the most extreme data points that are within a distance to the box equal to 1.5 times the interquartile range and points indicate all data points. (B) Same as (A) but for yeast patches. (C) Average fraction of time spent inside patches of rovers and sitters in agar patches, where the same parameters are used for inside and outside the patches. (D) Same as (A) for agar patches. Mann–Whitney–Wilcoxon paired test (samples not normally distributed). ns: 0.05 < p < 1, *0.01 < p < 0.05, **0.001 < p < 0.01, ***0.0001 < p < 0.001.

Using our model based on crawling behavior in homogeneous substrates, we next tested how changes in the food distribution influence the exploratory trajectories of rovers and sitters. We modeled heterogeneous environments with two circular patches of food substrate with agar substrate in the rest of the arena (Figure 2C, see Materials and methods). The two patches had a fixed radius (25 mm) that corresponds to the surface area of a grape (Xie et al., 2018). We simulated larval exploration of rovers and sitters in patches of two food substrates – sucrose and yeast (Figure 2D). The initial position was picked at random in each simulation, but always inside one of the two food patches to match the experiments.

We next quantified the fraction of simulation time that rovers and sitters spent inside patches. For each larva, this was averaged over 30 simulation runs (Figure 2E and Figure 2—figure supplement 1A, B). Inside sucrose patches, the percentage of time spent inside patches was small for both rovers and sitters (9.2% and 9.8%, respectively). These values were only slightly larger than those in a simulated environment with patches made of agar (7.47% for rovers and 6.99% for sitters – Figure 2—figure supplement 1A, C, D) – that is, the same speed and probabilities to turn and pause inside and outside patches. This result is unsurprising since in our homogeneous substrate experiments with rover and sitter larvae both had similar behavior in the agar and sucrose arenas. In simulations with yeast patches, the percentage of time spent inside patches was higher for both rovers (22.6%) and sitters (26.9%). This increase can be linked to the slower speeds and more frequent pauses in the homogeneous yeast substrate executed by the larvae. In spite of non-significant differences in the crawling of rovers and sitters in the homogeneous yeast substrate (Figure 1—figure supplement 1B–G), in our model simulated sitter larvae remained longer inside the yeast patches due to their lower (though not significantly different average crawling speed in the homogeneous yeast substrate experiments).

Thus far, our model predicts that, in patchy environments, larvae spend a relatively small proportion of time inside patches (approximately 1% for sucrose and 3% for yeast) while exploring takes up most of their time with a significant energy cost. However, our model does not integrate other possible mechanisms that a larva might employ to remain inside a food patch besides decreasing its crawling speed and increasing the fraction of pause events. We therefore compared the model predictions on foraging efficiency in patchy environments with behavioral experiments.

### Increased proportion of time in patches relies on turns toward the patch center at the food–no food interface

We next recorded the larval behavior in arenas with patchy substrates. We used the same size and distribution of food patches as in our simulations (Figure 3A). Food was distributed inside, with agar outside patches (Figure 3A and Materials and methods). We tested sucrose and yeast at the same concentration as in the homogenous substrate. We also performed experiments using apple juice as a nutrient, motivated by the fact that it is ecologically relevant and that, unlike sucrose, the fructose contained in apple juice is volatile, which makes it detectable by smell and not only by taste. Groups of five larvae of the same type (rovers or sitters) were placed inside each patch (total of two) at the beginning of the recordings (total of ten larvae of the same type per replicate, repeated in three independent experiments).

![Figure 3.](https://cdn.elifesciences.org/articles/75826/elife-75826-fig3-v2.jpg)

**Figure 3.:** (A) Experimental setup: Five larvae of the same phenotype were placed on top of each food patch (two patches, total: 10 larvae per experiment). Three types of food patches were tested: sucrose (green), yeast (orange), and apple juice solution (magenta). Agar was uniformly spread in the arena outside the food patches. (B) Sample trajectories of sitter larvae in the three patch substrates with inward (outward) turns marked in black (white) circles. Distribution of turning directions is shown on the bottom of each trajectory. (C) Larval crawling speeds of rovers and sitters measured inside (colored bars) and outside (blue bars) food patches: sucrose (S, green), yeast (Y, orange), and apple juice (AJ, magenta). Horizontal line indicates median, the box is drawn between the 25th and 75th percentiles, whiskers extend above and below the box to the most extreme data points that are within a distance to the box equal to 1.5 times the interquartile range and points indicate all data points. (D) Average number of turns executed per minute. (E) Fraction of time in which larvae did not move (pauses). (F) Handedness score. (G) Total distance crawled by rover (r; darker colors) and sitter (s; lighter colors) larvae in the first 5 min of the recording. (H) Fraction of time spent inside patches of rovers (r) and sitters (s). (I) Left: Identification of turning angle as inwards ($\theta_{2}<\theta_{1}$, black) or outwards ($\theta_{2}>\theta_{1}$, white). Right: Circular regions with fixed distances relative to the patch center. The yellow line represents the patch border. (J) Relative fraction of inward turns calculated as a function of the distance from the patch center. The distance bin that includes the patch radius is highlighted in yellow. Left: Sucrose, middle: apple juice, right: yeast patches. Top: Rovers, bottom: sitters. Mann–Whitney–Wilcoxon test two-sided was performed since the data are not normally distributed. ns: 0.05 < p < 1, *0.01 < p < 0.05, **0.001 < p < 0.01, ***0.0001 < p < 0.001, ****p < 0.0001. The total number of larvae tested is detailed in Table 1. Statistical power and Cohen’s size effect of non-significant comparisons are included in Table 4.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/75826/elife-75826-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Sample trajectories of rover larvae in patchy substrates where certain individuals visited both the two patches (sucrose, green), while others remained in the same patch for the entire duration of the experiment (yeast, orange and apple juice, magenta). Inward (outward) turns are marked in black (gray) circles. The distribution of turning directions is shown on the bottom of each trajectory. (B) Left: Crawling speed inside patches: sucrose (S, green), yeast (Y, orange), and apple juice (AJ, magenta). Data from rover (sitter) larvae shown in darker (lighter) colors. Right: Crawling speed outside patches. Horizontal line indicates median, the box is drawn between the 25th and 75th percentiles, whiskers extend above and below the box to the most extreme data points that are within a distance to the box equal to 1.5 times the interquartile range and points indicate all data points. (C) Average number of turns per minute inside (left) and outside (right) patches. (D) Fraction of pauses inside (left) and outside (right) patches. (E) Crawling speed outside patches compared to agar-only. (F) Percentage of rover (R), sitter (S) larvae that switched handedness from left to right (or right to left) once they crossed the border of the patches. Mann–Whitney–Wilcoxon paired test (samples not normally distributed). ns: 0.05 < p < 1, **0.001 < p < 0.01, , ****p < 0.0001. The number of larvae tested is detailed in Table 1.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/75826/elife-75826-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) Sample trajectories of sitter larvae in agar–agar patches or agar–gel patches. Note that the larvae do not change their behavior at the patch boundary. Distribution of turning directions is shown on the bottom of each trajectory. (B) Relative fraction of inward turns calculated as a function of the distance from the patch center. The distance bin that includes the patch radius is highlighted in yellow.

We tracked the trajectories with the same methods used in the homogeneous environment (Figure 3B and Figure 3—figure supplement 1A). Then, we performed the analysis separately for the two different regions: inside and outside the patches, and quantified features of the larval exploratory behavior. Inside yeast and apple juice patches, larvae crawled significantly slower than outside them (Figure 3C). In yeast patches, both rovers and sitters executed fewer turns inside than outside (Figure 3D). All larvae made significantly more pauses inside the food patches than outside (Figure 3E). We also observed that the handedness score of the larvae is less broad than in the homogeneous substrates (Figure 3F), which may be caused by reorientations that are triggered to prevent the larva from exiting the food patch. As expected from the phenotype, sitter larvae crawled a shorter distance in the first 5 min of the recording in the yeast but also the sucrose substrates (Figure 3G). In general, sitter larvae had slower crawling speeds and executed fewer turns in the patchy environments than rovers (Figure 3—figure supplement 1A–C). We also noticed that sitters paused more inside patches than rovers (Figure 3—figure supplement 1D). Outside yeast and apple juice patches, the crawling speed increased but did not return to levels similar to the agar-only condition, suggesting that the behavior of larvae that exit the patch is influenced by the recent food experience or that larvae might still be sensing the food (Figure 3—figure supplement 1E). In line with this, in yeast the number of turns outside the patch was higher than inside the patch.

Our model predicted that fraction of time spent inside patches should vary according to the substrate: larvae should remain longer inside yeast patches than inside sucrose patches (Figure 2E). In particular, simulated sitter larvae stayed longer than simulated rovers inside yeast patches. In the experiments, the same trend was observed: for both rovers and sitters the fraction of time spent inside patches was higher in the yeast compared to both sucrose and apple juice patches (Figure 3H). Sitter larvae stayed significantly longer inside yeast patches than rovers (Figure 3H). Nevertheless, the percentage of time the larvae spent inside patches in the experiments was very different from our model predictions. Rover (sitter) larvae remained on average 72.6% (72.3%) of the experiment inside sucrose, 85.7% (90.0%) inside yeast, and 75.6% (81.3%) inside apple juice patches. Those values were much higher in the experiments than what we predicted with our simulations, and suggest that larvae might employ other mechanisms in addition to slower crawling and more frequent pauses to remain inside the food.

To gain more insight into the strategies used by larvae to increase the time spent inside the food patches, we studied the distribution of turns in the food–no food interface. First, we labeled each turn as inwards or outwards depending on whether they were oriented toward or away from the patch center (Tao et al., 2020; Figure 3I, left). We observed that inward turns occur more often than outward turns at the border of the patch for the three substrates (Figure 3B, inward turns are shown in black). To control for possible mechanosensory effects due to the border edges, we prepared new arenas with patches that contained no nutrients, either using the same agar that composed the rest of the arena, or using ultrasound gel (Methods). Larvae in the agar–agar or the agar–gel border did not show any changes in their preference to turn toward the patch center, confirming that the behavioral change observed in response to food is specific (Figure 3—figure supplement 2).

We then studied the fraction of turns toward the patch center as a function of the distance to the patch center (Figure 3I, right). For the three types of substrates, the bias to turn inwards was clearly manifested when the larvae experienced the patch border (patch radius: 25 mm, distance bin: 20–30 mm) (Figure 3J). The bias persisted when the larva exited the patch (distance bins: 30–40, 40–50, 50–60 mm). We did not consider further distance bins in our analysis because most larvae did not reach those locations in our experiments.

Therefore, our model predictions do not seem to be well supported by experiments with patchy substrates. In particular, we conclude that when larvae reach the food–no food interface their turning behavior changes. This is accomplished by turning toward the patch center while maintaining the handedness (Figure 3J and Figure 3—figure supplement 1F) and represents an important mechanism to remain inside the food.

### Anosmic larvae also select turns toward the patch center when reaching the food–no food border, but not on the yeast

It is well known that Drosophila larvae can efficiently navigate toward or away an odor source using chemotaxis (Louis et al., 2008; Gomez-Marin et al., 2011; Schulze et al., 2015). Chemosensory information from gustatory and olfactory receptors is combined to allow larvae to locate food sources in the environment (Vosshall and Stocker, 2007). We next wondered how much of the tendency to turn toward the patch center once outside the patch could be attributed to processing olfactory cues.

Thus, we repeated the patchy experiments with mutant anosmic larvae, where Orco, the obligatory co-receptor for all olfactory neurons, apart the CO2 sensing ones, is mutated (Vosshall and Stocker, 2007) and tested if they show the same distant-dependent bias when exploring the patchy substrate.

Anosmic larvae extensively explored the patchy substrate (Figure 4A). In general, they exhibited a small difference in crawling speeds when comparing their behavior inside vs. outside of food patches (Figure 4B). Curiously, this difference in speeds was non-significant inside vs. outside yeast patches. We also found that the fraction of pauses of anosmic larvae in yeast patches was smaller than that of rovers and sitters (Figures 3G and 4D). This suggests that yeast patches are not attractive to anosmic larvae, in agreement with the lower fraction of time spent inside yeast patches relative to sucrose and apple juice patches (Figure 4F).

![Figure 4.](https://cdn.elifesciences.org/articles/75826/elife-75826-fig4-v2.jpg)

**Figure 4.:** (A) Sample trajectories of anosmic larvae in the three patch substrates with inward (outward) turns marked in red (gray) circles. Distribution of turning directions is shown on the bottom of each trajectory. (B) Crawling speeds of anosmic larvae measured inside (colorful bars) and outside (blue bars) food patches: sucrose (S, green), yeast (Y, orange), and apple juice (AJ, magenta). Horizontal line indicates median, the box is drawn between the 25th and 75th percentiles, whiskers extend above and below the box to the most extreme data points that are within a distance to the box equal to 1.5 times the interquartile range and points indicate all data points. (C) Average number of turns per minute inside and outside patches. (D) Fraction of pauses inside and outside patches. (E) Handedness score of anosmic larvae inside and outside patches. (F) Fraction of time spent inside patches for different types of food. (G) Relative fraction of inward turns calculated as a function of the distance from the patch center, top: sucrose, middle: yeast, bottom: apple juice. The distance bin that includes the patch radius is highlighted in yellow. Mann–Whitney–Wilcoxon test two-sided was performed since the data are not normally distributed. ns: 0.05 < p < 1, **0.001 < p < 0.01, ***0.0001 < p < 0.001, ****p < 0.00001. The number of larvae tested is detailed in Table 1. Statistical power and Cohen’s size effect of non-significant comparisons are included in Table 4.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/75826/elife-75826-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Average turns toward the center (± standard error of the mean, SEM) as a function of the distance away from the patch center. A two-way analysis of variance (ANOVA) for repeated measures was done. A significant effect of food (F(2, 76) = 5.168; p = 0.008) and distance (F(4.439, 282.3) = 5.741; p = 0.0001) was found, but non-significant interaction effect (p = 0.5). Tukey’s multiple comparisons test was performed. *p = 0.02; **p = 0.001. (B) Comparison of the fraction of turns toward center in the first half of the experiment vs. the second half. Each dot represents the inward turn ratio for either a rover or a sitter larva, at distance from patch center in the 20–30, 30–40, or 40–50 mm interval, respectively. A Mann–Whitney U-test on each distribution pair did not detect significant differences (p > 0.05), except for the 20–30 yeast condition (p = 0.042).

Next, we investigated if anosmic larvae can bias their turns at the patch border interface without navigating odorant cues. Turns in the trajectory were labeled as inwards or outwards (as in Figure 3I) and the fraction of turns toward the patch center was analyzed as a function of the distance away from the patch center.

In sucrose and apple juice substrates, anosmic larvae consistently increased the fraction of inward turns near the patch border (20–30 mm; Figure 4G). This was not the case in the yeast patches, where no bias was detected at the patch border.

In sum, we found that anosmic larvae, apart from on yeast, trigger turns toward the patch center at the food–no food interface, suggesting that olfaction is not the only mechanism responsible for the turning bias that increases the fraction of time larvae spend inside patches.

Taste very likely influences the probability that larvae remain in the patches. To control for the diffusion of nutrients (sucrose and apple juice) at the edge of a patch, we evaluated the maximum distance at which an increased fraction of turns toward the center was significantly different when compared to the yeast non-responsive anosmic control. At a distance greater than 0.5 cm from the edge, anosmic larvae on sucrose, apple juice, and yeast were indistinguishable, suggesting that diffusion has a limited impact on behavior (Figure 4—figure supplement 1A).

Finally, to control for possible effects of diffusion over time, we compared the fraction of turns toward the center in the first and second half of the experiment. For most distance and nutrients, the two distributions were not significantly different (Figure 4—figure supplement 1B).

### To remain inside of the food patch larvae combine turning bias with other strategies

To understand the impact of the turning bias on the percentage of time that larvae spend inside patches, we included a distance-dependent probability of turning toward the patch center in our model (Figure 5A). After drawing a turning angle from the probability distribution, the turn was implemented toward the patch center with probability $P_{bias}$ that depends on the distance between the current position and the center of the closest patch (Figure 5B). For each simulated substrate, larva type, and relative distance, $P_{bias}$ corresponds to the fraction of turns toward the patch center quantified in our experiments (Figures 3J and 4G).

![Figure 5.](https://cdn.elifesciences.org/articles/75826/elife-75826-fig5-v2.jpg)

**Figure 5.:** (A) Schematic showing inward turn (clockwise, CW) being selected by the simulated larva. By selecting inward turns, the trajectory approaches the patch center. (B) Spatial-dependent probability of turning toward the patch center. Each region is a concentric circle with a fixed probability of drawing inward turns (see Figure 3I, right). The yellow line shows the patch border. (C) Sample simulated trajectories for a sitter larva with biased inward turns: sucrose patch (green), yeast patch (orange), and apple juice patch (magenta). (D) Fraction of time spent inside patches of rovers (r; darker colors) and sitters (s; lighter colors) in the different substrates: sucrose (S, green), yeast (Y, orange), and apple juice (AJ, magenta). Each point is 30 simulation runs of one larva (total: 30 larvae simulated per substrate). Horizontal line indicates median, the box is drawn between the 25th and 75th percentiles, whiskers extend above and below the box to the most extreme data points that are within a distance to the box equal to 1.5 times the interquartile range and points indicate all data points. (E) Sample trajectories of sitter larvae in environments with varying number of randomly located patches, with a fixed total area of yeast substrate being distributed (Np = 1, 2, 8, 32 from left to right). (F) Average fraction of time spent inside patches of distinct substrates (S: sucrose, green; Y: yeast, orange, and A: apple juice, magenta) for rovers (left) and sitters (right) as a function of the number of patches. Each point is the average of 30 larvae (30 simulation runs each). Bars show the standard deviation. (G) Same as (F) but for the average fraction of visited patches. Mann–Whitney–Wilcoxon paired test was performed since the data are not normally distributed. ns: 0.05 < p < 1, ***0.0001 < p < 0.001.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/75826/elife-75826-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Each rover/sitter larva (bars, N = 15 for sucrose, N = 30 for yeast and apple juice) has a fixed turning angle distribution with parameters corresponding to one rover/sitter from the agar experiments. Simulation runs were performed in the same environment with sucrose (green), yeast (orange), and apple juice (purple) patches. (B) Each anosmic larva (bars, N = 30 for sucrose, yeast and apple juice) has a fixed turning angle distribution with parameters corresponding to one anosmic larva from the agar experiments. N = 30 simulation runs were performed in the same environment with sucrose (green), yeast (orange), and apple juice (purple) patches. Horizontal line indicates median, the box is drawn between the 25th and 75th percentiles, whiskers extend above and below the box to the most extreme data points that are within a distance to the box equal to 1.5 times the interquartile range and points indicate all data points. (C) Average fraction of time spent inside patches comparing rovers (r) an sitters (s) with anosmic larvae in sucrose (S, green), yeast (Y, orange), and apple juice (AJ, magenta) patches. Mann–Whitney–Wilcoxon test two-sided. ns: 0.05 < p < 1, , **** p < 0.0001.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/75826/elife-75826-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) Sample trajectories of sitter larvae in sucrose (top) and apple juice (bottom) patchy arenas with varying number of patches (Np = 1, 2, 8, 32 from left to right). (B) Average fraction of time spent inside patches of distinct substrates (S: sucrose, green; Y: yeast, orange, and A: apple juice, magenta) for anosmic larvae as a function of the number of patches. Each point is the average of 30 larvae (30 simulation runs each). Bars show the standard deviation. (C) Same as (B) but for the average fraction of visited patches. (D) Average fraction of time spent inside patches of distinct substrates (from left to right: sucrose, yeast, apple juice) for rovers (solid line, filled circles) and sitters (dashed line, open circles) as a function of the number of patches. Each point is the average of 30 larvae (30 simulation runs each). Bars show the standard deviation. (E) Same as (D) but for the average fraction of visited patches.

We observed that the simulated trajectories with this distance-dependent turning bias resemble the experimental ones much more (Figure 5C), with larvae often returning to a patch when leaving its border. Indeed, larvae spent three times longer inside a patch in the new simulations compared to the model without biased orientations (Figure 5D and Figure 5—figure supplement 1A): now rover (sitter) larvae remain on average 31.1% (28.9%) of the simulation inside sucrose patches and 63.8 (68.4%) of the simulation inside the yeast patches. Simulated anosmic larvae also showed a gain in the ratio of time inside patches (Figure 5—figure supplement 1B, C). Therefore, biased orientations at the patch border are an important mechanism employed by larvae to return to a food source when they detect a change in the substrate quality. This can be achieved without olfactory orientation cues, since anosmic animals can also perform biased turns (Figure 4G). However, the ratio of time that simulated larvae remain inside patches was still smaller than that measured in the experiments (Figures 3H and 4F). We reason that other mechanisms, such as working or short-term memory (Louis et al., 2008; Schleyer et al., 2015), or other sensory modalities at the vicinity of the border of the patch (see discussion) can contribute to increasing the time inside the food.

### Our model reveals the interplay between food quality and patches fragmentation

We next used our model to investigate how a further fragmentation of the food patches affects the ability of larvae to stay in patches where they can feed. To test we fixed the total area of food S and varied the number of patches choosing the center coordinates for each patch randomly (Figure 5E). We tested seven levels of fragmentation from 1 to 64 patches and to compensate for different patch radii, we adjusted the distance-dependent probability to turn inwards of each larva (Figures 3J and 4G, see Materials and methods). We modeled the three types of food tested thus far, for rover, sitter, and anosmic larvae. In total, this would represent 1575 hr of experiment, highlighting the advantage of the model.

First, we quantified the average fraction of the time spent inside patches relative to the whole simulation for the different food substrates as a function of the number of patches (Figure 5F and Figure 5—figure supplement 2A, B). As expected, both rovers and sitters spent less time inside a patch as the number of patches increases (and thus the patches radius decreases) (Figure 5F). Larvae spent longer inside patches in more nutritious environments, for example yeast, irrespective of the number of available patches. Interestingly, despite the small differences we previously quantified, our results showed that sitter larvae consistently spent more time inside yeast patches than rovers for each number of patches (Figure 5—figure supplement 2D). This was not observed in the sucrose or apple juice patches. Anosmic animals also spent less time inside patches when the number of patches increases, but the dependence on the quality of food was much less pronounced (Figure 5—figure supplement 2B).

Next, we investigated the effect of different food substrates on the number of patches larvae explore to understand how fractioning environment would affect exploitation, which is key for survival. We quantified the fraction of new patches a larva visits during the simulation (discounting the source patch, since all the simulations start with the larva inside one patch) (Figure 5G). Rovers and sitters explored more patches in the less nutritious substrate (sucrose), with a slightly higher fraction of visited patches for rovers in the sucrose and yeast patches (Figure 5G; Figure 5—figure supplement 1E). Anosmic larvae showed a weaker effect of the substrate on the fraction of patches visited (Figure 5—figure supplement 1C).

Our model predicts a trade-off between the quality of the food and the fraction of patches visited: when exploring a substrate with low-quality (high-quality) food, the larvae are more (less) likely to leave and more (fewer) patches are visited.

### Larvae experience a trade-off between food consumption and exploration

To confirm that larvae adapt their behavior as modeled in response to different quality and fragmentation of food, we compared the behavior of larvae in two and eight patches. We conducted new experiments in arenas with eight patches of sucrose and yeast with rover and sitter larvae. Three sets of random positions of patches were used for each replicate (Figure 6B). Each larva (total of eight) was placed inside a different patch and left to crawl for 50 min. The data were compared to the experiments with two patches (Figure 3).

![Figure 6.](https://cdn.elifesciences.org/articles/75826/elife-75826-fig6-v2.jpg)

**Figure 6.:** (A) Sample simulated trajectories for sitter and rover larvae exploring in eight patches: sucrose patch (green) and yeast patch (orange). (B) Sample experimental trajectories of rover and sitter larvae in an arena with eight patches of food. Three random distributions (exp1; exp2; exp3) were used for each type of food: sucrose patches (green) and yeast patches (orange). (C) Fraction of time spent inside patches of rovers (darker colors) and sitters (lighter colors) on sucrose (green) and yeast (orange). Horizontal line indicates median, the box is drawn between the 25th and 75th percentiles, whiskers extend above and below the box to the most extreme data points that are within a distance to the box equal to 1.5 times the interquartile range and points indicate all data points. (D) Average fraction of time spent inside patches of distinct substrates (sucrose, green; yeast, orange) for rovers and sitters as a function of the number of patches. Data represent mean ± standard deviation. (E) Same as (D) but for the average fraction of visited patches. analysis of variance (ANOVA) test was performed for (C) and (D) (normally distributed) and Mann–Whitney–Wilcoxon paired for (E) (non-normally distributed). ns: 0.05 < p < 1, *0.01 < p < 0.05, **0.001 < p < 0.01, ****0.00001 < p < 0.0001. The number of larvae tested is detailed in Table 1. Statistical power and Cohen’s size effect of non-significant comparisons are included in Table 4.

A first comparison of the trajectories of simulated and experimental larvae exploring in an environment with eight patches shows great similarity (Figure 6A, B). As predicted by the model, both rovers and sitter spent half of the time inside patches when the area of food was divided in eight compared to two patches (Figures 5F and 6C, D). Furthermore, the larvae stayed longer on the yeast patches compared to the sucrose ones (Figure 6C, D), supporting the prediction of the model that larvae will spend less time in less nutritious patches irrespective of the number of available patches.

We then analyzed the effect of food quality on the proportion of patches visited by the larvae. There were no significant differences comparing the larvae in yeast and sucrose apart for rover in yeast for two patches. In this case, the model had predicted a difference between yeast and sucrose that is not present experimentally, probably because the larvae spend more time on the patches than what the model predicted via other mechanisms. However, it is clear that larvae spent more time looking for new patches (outside patches, Figure 6C, D) when the quality of food was lower (in sucrose) compared to higher quality (yeast), but they did not reach more patches in our experimental timeline. It is possible that having left a source of poor food, the larvae were more interested in exploring in search of food of better quality.

Finally, we were particularly interested in testing the prediction that larvae would reach a steady state in the proportion of patches visited as the food would become more fragmented. This was supported by the experiments with two and eight patches despite our suspicion that.

Overall, the experiments show how larvae tune the elements of the navigation routine to generate a foraging behavior that adapts to the quality and spatial distribution of food resources.

## Discussion

Foraging behavior is a complex process influenced by many internal factors (locomotion style, sensory perception, cognitive capacity, age) and external variables (spatiotemporal distribution of resources, presence of predators, social interactions with co-specifics). Here, we focused on the detailed characterization of foraging in a single model organism, the fruit fly Drosophila larva, using extensive experiments and modeling. This allowed us to study the role of both internal and external factors on foraging: (1) genetics (rovers, sitters, and later orco null anosmic animals), (2) food quality (agar, yeast, sucrose, and apple juice), and (3) food spatial distribution (homogeneous and heterogeneous environments).

We systematically investigated larval exploratory behavior first in experimental arenas with homogeneously distributed food. Larval crawling speed, turning frequency and fraction of pausing events adapted according to the quality of the food substrate (Figure 1C–E). The quality of the food had a strong impact on the distance traveled by the larvae. In yeast, larvae moved less and their speed and turn frequency were decreased. They also made more pauses, with the majority remaining stationary, except for internal gut movements (Video 1), which suggested that they were digesting the yeast. The pauses were rarely observed in sucrose, which is metabolized more quickly than yeast, even when mixed with agar (Figure 1E).

We observed that larval trajectories often had a circular shape, revealing an individual preference for a given turning direction in the absence of direction cues, which we quantified as the larval handedness (Figure 1B, F). The population variability in the handedness has been quantified in adult flies (Buchanan et al., 2015), but to our knowledge not until now at the larval stage. In adult walking flies, individual preferences of turning left or right in maze tests have been shown to persist across days (Buchanan et al., 2015) and recently have been linked to anatomical differences in the synaptic distribution of bottleneck neurons downstream of the central complex (Skutt-Kakaria et al., 2019). It is therefore possible that, as found in adults, larval individual differences in neuronal connections could define handedness. It would be interesting to understand the evolutionary advantage of handedness, if there is one, and to relate it to the ‘hard-wired’ circuitry controlling Lévy search behavior (Sims et al., 2019).

It is expected that animals change their foraging behavior depending on the quality and spatial distribution of food, with more localized exploitation of resources where they are abundant and a more exploratory behavior when resources become scarce (Humphries et al., 2010). We tested this in a phenomenological model of larval foraging behavior in patchy substrates (Humphries et al., 2010; Figure 2). We reasoned that crawling speed, turning frequency and fraction of pauses are the behavioral elements that adapt when the larva crosses the food–no food interface at the patch boundary. To quantify the food exploitation, we measured the fraction of the time each larva spent inside the patches. We found that decreasing the speed and turning frequency and increasing the fraction of pauses is not sufficient to explain why larvae remain inside the food for longer periods.

In experiments with patchy substrates, we found that larvae spend a longer time inside food patches than predicted with our model (Figure 3H). The lack of agreement between the experiments and our model was not surprising, since the latter does not include additional mechanisms that could guide the larva back to the patch when it leaves it, such as chemotaxis (Louis et al., 2008; Gomez-Marin et al., 2011). Since in chemotaxis larvae redirect their turns toward a source of odor, we classified each turn in their recorded trajectory as toward or away from the patch center. We observed that the fraction of inward turns is very high around the patch border (Figure 3J). To test whether larvae could redirect their turns toward the food when exiting it using olfactory cues, we repeated the experiments with anosmic mutants. Surprisingly, in sucrose and apple juice substrate anosmic larvae bias their turns toward the patch center when in the neighborhood of the patch border (Figure 4G). Therefore, this reorientation at the border does not seem to rely solely on olfaction. When exiting the food patch, larvae sense the lack of taste and it is possible that the turn bias changes as a result of temporal integration of the recent sensory-motor experience allowing them to return to the patch, as observed when navigating in an olfactory or light intensity gradient. Also, the patches of sucrose and apple juice were in direct contact with the surrounding agar arena. This has the advantage of generating a smooth transition in the substrate (Figure 3—figure supplement 1E, F), but it also allows diffusion at the interface which the larvae can sense as they crawl away from the food (Lebrun and Junter, 1993). In anosmic larvae, the fraction of turns toward the center for sucrose and apple juice patches was only higher compared to the one for the yeast patch (where there was no food effect) within the first half centimeter outside the patch, suggesting that the impact of diffusion could be significant only in that region (Figure 4—figure supplement 1).

An experiment using the gustatory sweet sensor Gr43a mutant on sucrose, which is not volatile and does not produce smell, could help discerning the contribution of taste at the border of the patch (Fujishiro et al., 1984; Marella et al., 2006; Miyamoto et al., 2013; Wang et al., 2004; Mishra et al., 2013). For yeast, the lack of smell completely changed the response of the larvae, which did not show differences inside and outside the patch for most foraging parameters (Figure 4B, C, E, G). In this instance, taste was not sufficient to retain larvae inside the yeast patch (compare Figure 3H with Figure 4F) even though several gustatory receptors have been shown to be activated by yeast metabolites (Wisotsky et al., 2011; Ganguly et al., 2017; Croset et al., 2016).

Another sensory modality that could have influenced the larval behavior at the food–no food interface, is mechanosensation. We excluded the possible role of the border of the patches performing experiments in patches without food (Figure 3—figure supplement 2). However, when larvae are crawling, they leave a print of their denticle attachment on the agar, that could inform them about their previous location and help returning to the food. Overall, the differences in behavior of larvae exposed to different foods, revealed the complexity of the sensory-motor processing involved in foraging.

One of the strengths of our phenomenological model is that it incorporates a modular organization of foraging that could reflect how the crawl and turn modules are controlled. First, we modeled a stochastic search where no information regarding food is available outside of the current location, because food is absent or because the larvae cannot sense it. This corresponds to an autonomous search behavior implemented by circuits located in the ventral nerve cord without input from the brain (Berni et al., 2012; Sims et al., 2019). Second, we incorporated a goal-directed navigation that allows larvae to return to the food. Our phenomenological model includes a distance-dependent probability to turn inwards that mimics the effect of chemotaxis (when present), as much as any other possible mechanism that contributes to the turning probability. As a consequence, we observed that simulated larvae, even when the resources are fractioned in eight patches, could stay inside the food patch for longer periods, in line with experimental observations (Figures 5 and 6). The model could be improved by setting the turning properties outside the patch to match as closely as possible experimental observations. To this end, we could consider studies of larvae crawling in different attractive gradients, where the changes in turning probability and angle, including weathervaning, have been investigated in relation to precise spatiotemporal information of odorants (Louis et al., 2008; Gomez-Marin et al., 2011; Davies et al., 2015). It would also be helpful to have information about other attractive gradients, like taste, to know if a common set of mechanisms is used regardless of the sensory modality. Using this information, our model could be used to investigate how crawling speed and turning properties are controlled via descending pathways from the brain (Tastekin et al., 2018; Jovanic et al., 2019). Finally, in the presence of nutrients, our model adjusts movements to stay on the food patch. The concerted decrease in turning rate and crawling speed and increase in the number of pauses, suggests that a neuromodulatory depression of movement (Marder, 2012; Lin et al., 2019) could be relevant in this phase. It would be interesting to investigate more generally how neuromodulators influence the decision to remain or explore new food resources in relation to the resources available and the larval motivational state.

Overall, we found both in our experiments and modeling that larvae spend less time exploiting patches of less nutritious food (e.g., sucrose). What could be the effect of this when several patches are available in the substrate? Our model results predict that larvae would spend more time exploring and more patches would be visited when food quality is lower (Figure 5G). In natural environments, this would enhance the chances that larvae will eventually find a better food source in the surroundings. Our experiments show a slightly different picture, where larvae indeed explore for a longer period when on less nutritious food but the number of patches they find is not increased compared to when they are on a more nutritious food (Figure 6C, D). It is possible that having left a poor food source, the larvae are more likely to continue looking for a more nutritious one, in the short term, instead of visiting and exploiting a new poor patch. Therefore, the internal state of the animal is probably playing an important role in the decision of choosing a new patch of food to exploit (Ringo, 2018; Branch and Shen, 2017).

The differences we found in the foraging behavior of rovers and sitters are not as drastic as previously reported, where the length of the path of rovers was roughly twice that of sitters when crawling in a yeast paste for 5 min (Sokolowski, 2001). In the homogeneous agar, sucrose, and yeast substrates, we did not observe significant differences in the path length of rovers and sitters (Figure 1—figure supplement 1). This was expected for the no-food condition (agar substrate; Kaun et al., 2007; Yang et al., 2000), but not in the presence of yeast (Sokolowski, 2001). This could be attributed to differences in the food preparation protocol: we applied a thin layer of yeast on top of the agar surface instead of thick yeast suspension as in Sokolowski, 1980 to allow recording from underneath the food (Risse et al., 2013). Also, our experiments were conducted in the dark, which might influence behavior (Sokolowski, 1980).

Interestingly, when the food is constrained inside patches, as done in the classical work studying the foraging polymorphism, we observed significantly shorter crawling paths of sitters in sucrose and yeast patches (Figure 3G). Sitters’ crawling speed was also slower and they perfomed fewer turns per minute and more pauses (Figure 3—figure supplement 1). It is possible that the presence of a patch border plays a significant role for the foraging polymorphism phenotypic expression.

In summary, we have identified a set of behavioral elements – the crawling speed, frequency and biasing of turns, and fraction of pauses – that adapt when larvae explore environments with a patchy distribution of food sources. This adaptation leads to an efficient substrate exploration, as larvae either increase the time inside nutritious food patches or continue exploring the substrate depending on the local quality of food.

## Materials and methods

### Animals

Rover and sitter flies were a gift of Marla Sokolowski (University of Toronto) and Orco[2] from Bloomington stock center (stock 23130). Flies were allowed to lay eggs for 1 day in standard corn meal food, which consists of 420 g of cornmeal; 450 g of dextrose; 90 g of yeast; 42 g of agar; 140 ml of 10% Nipagin in 95% EtOH; 22 ml of propionic acid, and 6.4 l of water. Larvae that were 72 hr old were collected for the experiment.

### Larva tracking

We recorded movies of larval exploratory behavior in arenas with minimal external stimuli – the recordings were made in the dark with a constant temperature of 25°C. Each trial lasted 50 min and the larvae were simultaneously tracked in a 240 × 240 mm2 arena with a 2-mm thick layer of 0.4% agar-based coating (see the protocol of substrate preparation below).

At each trial, 10 young third-instar larvae (72–80 hr since egg laying) of approximately the same size were washed to remove traces of food and allowed to crawl freely for 5 min on a clean 0.4% agar coated plate before being transferred to the arena (Table 1). We used a Frustrated Total Internal Reflection (FTIR)-based imaging method to record the larval exploratory behavior (Risse et al., 2013). Movies (duration 50 min) were recorded with a Basler acA2040-180km CMOS camera at 2048 × 2048 px2 resolution, using Pylon and StreamPix software, mounted with a 16-mm KOWA IJM3sHC.SW VIS-NIR Lens and 825-nm high-performance longpass filter (Schneider, IF-093). We recorded the movies at 2 frames per second to obtain forward movement displacements and actual pause turns that are recorded accurately rather than to include ‘flickering’ movements associated with peristaltic movements.

**Table 1.**
 Number of larvae per recording.


<table>
  <thead>
    <tr>
      <th>Substrate</th>
      <th>Number of trials</th>
      <th>Average number of larvae per trial</th>
      <th>Total larvae</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Agar homogeneous</td>
      <td>3 rovers3 sitters</td>
      <td>10 rovers10 sitters</td>
      <td>30 rovers29 sitters</td>
    </tr>
    <tr>
      <td>Sucrose homogeneous</td>
      <td>3 rovers3 sitters</td>
      <td>10 rovers10 sitters</td>
      <td>30 rovers30 sitters</td>
    </tr>
    <tr>
      <td>Yeast homogeneous</td>
      <td>3 rovers3 sitters</td>
      <td>10 rovers10 sitters</td>
      <td>29 rovers30 sitters</td>
    </tr>
    <tr>
      <td>Agar 2 patches</td>
      <td>3 sitters</td>
      <td>9 sitters</td>
      <td>28 sitters</td>
    </tr>
    <tr>
      <td>Gel 2 patches</td>
      <td>3 sitters</td>
      <td>11 sitters</td>
      <td>33 sitters</td>
    </tr>
    <tr>
      <td>Sucrose 2 patches</td>
      <td>2 rovers2 sitters3 anosmic</td>
      <td>8 rovers8 sitters10 anosmic</td>
      <td>15 rovers15 sitters28 anosmic</td>
    </tr>
    <tr>
      <td>Sucrose 8 patches</td>
      <td>3 rovers3 sitters</td>
      <td>8 rovers8 sitters</td>
      <td>24 rovers19 sitters</td>
    </tr>
    <tr>
      <td>Yeast 2 patches</td>
      <td>3 rovers3 sitters3 anosmic</td>
      <td>10 rovers10 sitters10 anosmic</td>
      <td>30 rovers27 sitters21 anosmic</td>
    </tr>
    <tr>
      <td>Yeast 8 patches</td>
      <td>3 rovers3 sitters</td>
      <td>8 rovers8 sitters</td>
      <td>25 rovers21 sitters</td>
    </tr>
    <tr>
      <td>Apple juice 2 patches</td>
      <td>3 rovers3 sitters3 anosmic</td>
      <td>10 rovers10 sitters10 anosmic</td>
      <td>30 rovers30 sitters29 anosmic</td>
    </tr>
  </tbody>
</table>

### Substrate preparation

The following food substrates were prepared for our experiments, and stored refrigerated for up to 1 day:

In the case of agar and sucrose homogeneous substrates, the solution was homogeneously spread on top of the acrylic arena and we waited for it to reach room temperature before transferring the larvae to the arena. Yeast homogeneous arenas were obtained by spreading 5 ml of 20% yeast in water with a soft metallic disk. For sucrose or apple juice patchy arenas, first, the agar solution was homogeneously spread in the acrylic arena. When the solution cooled down, two holes in the agar were made at fixed positions (Figure 3A) using circular-shaped Petri dishes with a 25-mm radius. We carefully removed the agar inside the holes and transferred the food solutions to the holes with the same thickness as the agar around them. Control two agar patches were filled with 04% agar alone. For each one of the two yeast patches, 100 µl of yeast solution was placed on a 25-mm-radius metal disc and printed on the agar. For gel 2 patches control we stamped a drop of 150–200 mg of ultrasound gel for TENS machine (Boots ingredients: purified water, glycerin, propylen glycol, hydroxyethylcellulose, sodium citrate, citric acid, domiphen bromide). The viscosity of the gel is not identical to the one of yeast, but it informs us about the transition from viscous and smooth (gel-yeast) to agar. For eight patches, we chose three distributions randomly generated in the modeling experiment (Figure 6A, lower panel). Using a 12.5-mm-radius disc we printed the patches with 25 µl of yeast solution. For sucrose 8 holes were made using a cylinder and then filled with food solution. One larva was placed in each patch, meaning that each larva was exposed to a different distribution of the resources. The experiments were repeated three times.

### Descriptive statistics of larval trajectory

The data (x,y coordinates of individual larvae) were extracted from the behavioral movies using the FIM track free software (Risse et al., 2017). We used a Kalman filter to the (x,y) coordinates of each larva (code will be available at github after the paper is accepted). The position of each larva in video frame j is represented as the vector:

$$
R→(t_{j})=(x(t_{j}),y(t_{j})),j=1,2,…,N
$$

where $xt_{j}$ and $yt_{j}$ are the centroid coordinates, $t_{j}=jΔt(j=1,…,N)$ , $Δt=0.5$ s, and $N=6000$ is the number of frames continuously recorded during the experiment. We defined the following quantities that were used in our analysis.

Velocity:

$$
V→(t_{j})=\frac{R→(t_{j})−R→(t_{j−1})}{Δt}
$$

Heading:

$$
H→(t_{j})=\frac{V→(t_{j})}{s(t_{j})}
$$

Scalar speed:

$$
s(t_{j})=‖V→(t_{j})‖
$$

Instantaneous turn rate:

$$
|\frac{Δ\theta}{Δt}|(t_{j})=\frac{cos^{−1}(H→(t_{j−1})⋅H→^{T}(t_{j}))}{Δt},(0\leqΔ\theta\leq\pi)
$$

Next, the Ramer–Douglas–Peucker algorithm (https://pypi.org/project/rdp/) was used to simplify the larval trajectories and therefore identify the locations where larvae executed turns. After visual inspection of the simplified trajectories, we fixed the distance dimension $\epsilon$, that represents the maximum distance between the original points and the simplified curve. $\epsilon=2.5$ mm to the analysis with agar, sucrose, and apple juice and $\epsilon=1.25$ mm to the yeast analysis.

With turning points identified in the trajectory, the turning angles were obtained in the range $[−\pi,\pi]$ using the atan2 function in python. As a convention, clockwise turns were in the range $-\pi,0$ and counter-clockwise turns in the range $0,\pi$ . The handedness index of each larva was obtained as:

$$
H=\frac{N_{CCW}}{N_{CCW}+N_{CW}}
$$

where $N_{CCW}$ is the number of counter-clockwise turns in the trajectory and $N_{CW}$ the number of clockwise turns. Thus, if $H>0.5$ ($H<0.5$) the larva has a bias to execute more counter-clockwise (clockwise) turns.

From the turning points identified by the RDP algorithm, we built a vector that registers 1 in the time points where turns were registered and 0 otherwise. The length of this vector is the number of frames in the recording. Next, we applied a rolling window of 120 frames (1 min) to this vector and summed the elements within the window. Then, we averaged the number of turns registered within each 1-min window to obtain the average number of turns per minute.

### Patch radius and center coordinates

We used imageJ to determine the center and radius of each patch in the experiments. A frame of the recording was adjusted for contrast and brightness until the borders of the patch became visible. Circular regions of interest were drawn for each patch and the center coordinates and radius were obtained.

### Classification of turns as toward the patch center

Let $S→t_{k}$ be the trajectory simplified by the RDP algorithm, where each point is a turning point of the original trajectory. To classify the $k$ th turn in the trajectory as inwards or outwards, we define the following vectors:

$$
V→_{1}=S→(t_{k})−S→(t_{k−1})
$$



$$
V→_{2}=S→t_{k+1}-S→t_{k}
$$



$$
U→=P→-S→t_{k}
$$

where $S→t_{k-1}$ and $S→t_{k+1}$ are the previous and the following turning locations and $P→$ is the center of the patch that is closest to $S→t_{k}$ . The following angles are then computed (Figure 3I, left):

$$
\theta_{1}=cos^{−1}(\frac{V→_{1}⋅U→}{‖V→_{1}‖‖U→‖})
$$



$$
\theta_{2}=cos^{−1}(\frac{V→_{2}⋅U→}{‖V→_{2}‖‖U→‖})
$$

and the turn at $S→t_{k}$ is classified as inwards (outwards) if $\theta_{2}<\theta_{1}$ ($\theta_{2}>\theta_{1}$) (Tao et al., 2020).

### Model

#### Homogeneous substrate

The simulated crawling substrate has rigid boundaries and the same dimensions as the behavioral arenas used in the experiments (240 × 240 mm2). At each time step $t_{k}$ the simulated larva can be at one of three different states (Figure 2A):

The parameter values and distributions were obtained from our experimental data of larval crawling in homogeneous substrates and are unique for each type of larva and substrate (Table 2). Crawl, turn or pause events were registered with a constant probability per time step (Pcrawl = 1 − (Pturn + Ppause)) and the simulation duration was the same as our behavioral recordings (50 min). To capture the variability in the turning behavior, each larva was simulated with its own set of parameters for the turning angle distribution according to one recorded larva (with an average of 30 sitter and 30 rover larvae recorded at each type of substrate). The RDP algorithm was then used to identify salient turning points in the simulated trajectory (Figure 2B).

**Table 2.**
 Parameters of model in homogeneous and patchy substrates obtained in homogeneous substrate experiments.


<table>
  <thead>
    <tr>
      <th>Substrate</th>
      <th>Larva</th>
      <th>Mean v (mm/s)</th>
      <th>Std v (mm/s)</th>
      <th>Pturn/s</th>
      <th>Ppause/s</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Agar</td>
      <td>Rover</td>
      <td>0.84</td>
      <td>0.13</td>
      <td>0.044</td>
      <td>0.0083</td>
    </tr>
    <tr>
      <td>Agar</td>
      <td>Sitter</td>
      <td>0.96</td>
      <td>0.13</td>
      <td>0.046</td>
      <td>0.0063</td>
    </tr>
    <tr>
      <td>Sucrose</td>
      <td>Rover</td>
      <td>0.68</td>
      <td>0.092</td>
      <td>0.041</td>
      <td>0.012</td>
    </tr>
    <tr>
      <td>Sucrose</td>
      <td>Sitter</td>
      <td>0.68</td>
      <td>0.085</td>
      <td>0.035</td>
      <td>0.021</td>
    </tr>
    <tr>
      <td>Yeast</td>
      <td>Rover</td>
      <td>0.37</td>
      <td>0.13</td>
      <td>0.033</td>
      <td>0.25</td>
    </tr>
    <tr>
      <td>Yeast</td>
      <td>Sitter</td>
      <td>0.31</td>
      <td>0.11</td>
      <td>0.028</td>
      <td>0.25</td>
    </tr>
  </tbody>
</table>

#### Patchy substrate

##### Without biased turns toward the food

We modeled patchy environments initially with two circular patches (radius 25 mm) of food substrate (sucrose or yeast) with agar substrate in the rest of the arena (Figure 2C). Crawling speed and probabilities to turn or pause were drawn based on the current position of the simulated larva. The parameters were sampled from the corresponding food experiment when the larva was inside a patch, and sampled from the agar experiment when the larva was outside the patch. The turning angle distribution of each simulated larva corresponded to one from the recordings in the agar substrate. The same turning angle probability distribution was used whether the larva is inside or outside the patch. The initial position was picked at random in each simulation, but always inside one of the two food patches to match the experiments.

##### With biased turns toward the food

Except for the choice of turning angles, the model was the same as the one described above. The biased choice of turns toward the food followed the implementation in Tao et al., 2020. After drawing a turning angle from the von Mises probability distribution, the turn direction was chosen such that the larva points toward the patch center with probability $P_{bias}$ that depends on the distance between the current position relative to the center of the closest patch (Figure 5B). When the simulated larva was further than 60 mm away from the closest patch center, no bias was applied in the turning direction since the data were very sparse in this region (most larvae never crawled such long distances away from the patch of food in the experiments). Each turn was defined by a set of three points ${p_{1},p_{2},p_{3}}$ where $p_{1}$ is where the turn initiates, $p_{2}$ is the end location of a left turn, and $p_{3}$ the end location of a right turn. Three movement vectors that characterize the turn options (to the left or to the right) were defined as:

$$
v_{1}→=p_{2}−p_{1}
$$



$$
v_{2}→=p_{3}−p_{1}
$$



$$
u→=-p_{1}
$$

We next calculated the angle $\theta$ the larval trajectory makes with the inward vector $u→$ when turning to the left ($p_{2}$) or to the right ($p_{3}$). The inward turn is the turn that results in the smallest $\theta$ (as shown in Figure 5A).

##### With more patches

We fixed the total surface area of food to be distributed in $N$ patches as $S=2\piR^{2}$ , where $R=25mm$ is the radius of the patches from the previous simulations and experiments. Then, the radius of each $N$ th patch is given by $R`=\sqrt{S/N\pi}$. The simulated larvae started within a random food patch, and were tracked for 50 min. The simulation parameters were kept the same as in the two patches model, except that the distances in the distance-dependent probability to turn inwards were adjusted for smaller patch radius, by multiplying the distance values by $R`/R$.

### Model parameters (Tables 2–4)

**Table 3.**
 Parameters of corrected model in patchy substrates obtained in patchy substrate experiments.


<table>
  <thead>
    <tr>
      <th>Patchy substrate</th>
      <th>Larva</th>
      <th>Mean v inside (outside) (mm/s)</th>
      <th>Std v inside (outside) (mm/s)</th>
      <th>Pturn/s inside (outside)</th>
      <th>Ppause/s inside (outside)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Agar + sucrose</td>
      <td>Rover</td>
      <td>0.60 (0.65)</td>
      <td>0.27 (0.25)</td>
      <td>0.037 (0.044)</td>
      <td>0.039 (0.0014)</td>
    </tr>
    <tr>
      <td>Agar + sucrose</td>
      <td>Sitter</td>
      <td>0.52 (0.57)</td>
      <td>0.28 (0.26)</td>
      <td>0.030 (0.030)</td>
      <td>0.088 (0.040)</td>
    </tr>
    <tr>
      <td>Agar + yeast</td>
      <td>Rover</td>
      <td>0.37 (0.44)</td>
      <td>0.19 (0.20)</td>
      <td>0.039 (0.068)</td>
      <td>0.17 (0.023)</td>
    </tr>
    <tr>
      <td>Agar + yeast</td>
      <td>Sitter</td>
      <td>0.26 (0.36)</td>
      <td>0.14 (0.17)</td>
      <td>0.025 (0.048)</td>
      <td>0.32 (0.053)</td>
    </tr>
    <tr>
      <td>Agar + apple juice</td>
      <td>Rover</td>
      <td>0.44 (0.53)</td>
      <td>0.24 (0.26)</td>
      <td>0.026 (0.017)</td>
      <td>0.096 (0.076)</td>
    </tr>
    <tr>
      <td>Agar + apple juice</td>
      <td>Sitter</td>
      <td>0.39 (0.48)</td>
      <td>0.21 (0.22)</td>
      <td>0.021 (0.031)</td>
      <td>0.13 (0.065)</td>
    </tr>
  </tbody>
</table>

**Table 4.**
 Statistical power and Cohen’s effect size of non-significant comparisons.


<table>
  <thead>
    <tr>
      <th>Figure 1</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3">D – Avg. number of turns per min</td>
      <td>Power (1 − β)</td>
      <td>Cohen’s size effect (d)</td>
    </tr>
    <tr>
      <td>Rover</td>
      <td>Agar</td>
      <td>Sucrose</td>
      <td>0.24</td>
      <td>0.34</td>
    </tr>
    <tr>
      <td>Rover</td>
      <td>Sucrose</td>
      <td>Yeast</td>
      <td>0.48</td>
      <td>0.52</td>
    </tr>
    <tr>
      <td>Sitter</td>
      <td>Sucrose</td>
      <td>Yeast</td>
      <td>0.47</td>
      <td>0.51</td>
    </tr>
    <tr>
      <td colspan="3">G – Handedness</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Rover</td>
      <td>Agar</td>
      <td>Sucrose</td>
      <td>0.13</td>
      <td>−0.22</td>
    </tr>
    <tr>
      <td>Rover</td>
      <td>Agar</td>
      <td>Yeast</td>
      <td>0.05</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>Rover</td>
      <td>Sucrose</td>
      <td>Yeast</td>
      <td>0.19</td>
      <td>0.31</td>
    </tr>
    <tr>
      <td>Sitter</td>
      <td>Agar</td>
      <td>Sucrose</td>
      <td>0.14</td>
      <td>0.25</td>
    </tr>
    <tr>
      <td>Sitter</td>
      <td>Agar</td>
      <td>Yeast</td>
      <td>0.08</td>
      <td>0.16</td>
    </tr>
    <tr>
      <td>Sitter</td>
      <td>Sucrose</td>
      <td>Yeast</td>
      <td>0.08</td>
      <td>−0.15</td>
    </tr>
    <tr>
      <td>Figure 3</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">C – Crawling speed</td>
      <td>Power (1 − β)</td>
      <td>Cohen’s size effect (d)</td>
    </tr>
    <tr>
      <td>Sucrose</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Rover</td>
      <td>In</td>
      <td>Out</td>
      <td>0.14</td>
      <td>−0.34</td>
    </tr>
    <tr>
      <td>Sitter</td>
      <td>In</td>
      <td>Out</td>
      <td>0.20</td>
      <td>−0.44</td>
    </tr>
    <tr>
      <td colspan="3">D – Avg. number of turns per min</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sucrose</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Rover</td>
      <td>In</td>
      <td>Out</td>
      <td>0.29</td>
      <td>−0.56</td>
    </tr>
    <tr>
      <td>Sitter</td>
      <td>In</td>
      <td>Out</td>
      <td>0.05</td>
      <td>−0.02</td>
    </tr>
    <tr>
      <td colspan="3">F – Handedness</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Rover</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sucrose</td>
      <td>In</td>
      <td>Out</td>
      <td>0.11</td>
      <td>−0.30</td>
    </tr>
    <tr>
      <td>Yeast</td>
      <td>In</td>
      <td>Out</td>
      <td>0.10</td>
      <td>−0.24</td>
    </tr>
    <tr>
      <td>Apple juice</td>
      <td>In</td>
      <td>Out</td>
      <td>0.15</td>
      <td>0.31</td>
    </tr>
    <tr>
      <td>Sitter</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sucrose</td>
      <td>In</td>
      <td>Out</td>
      <td>0.06</td>
      <td>−0.15</td>
    </tr>
    <tr>
      <td>Yeast</td>
      <td>In</td>
      <td>Out</td>
      <td>0.06</td>
      <td>−0.14</td>
    </tr>
    <tr>
      <td>Apple juice</td>
      <td>In</td>
      <td>Out</td>
      <td>0.16</td>
      <td>−0.39</td>
    </tr>
    <tr>
      <td colspan="3">G – Crawl dist. 5 min</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Apple juice</td>
      <td>Rover</td>
      <td>Sitter</td>
      <td>0.20</td>
      <td>0.34</td>
    </tr>
    <tr>
      <td colspan="3">H – Fraction of time spent inside patch</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sucrose</td>
      <td>Rover</td>
      <td>Sitter</td>
      <td>0.08</td>
      <td>0.20</td>
    </tr>
    <tr>
      <td>Apple juice</td>
      <td>Rover</td>
      <td>Sitter</td>
      <td>0.32</td>
      <td>−0.40</td>
    </tr>
    <tr>
      <td>Figure S3</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Apple juiceCrawling speed</td>
      <td>Power (1 − β)</td>
      <td>Cohen’s size effect (d)</td>
    </tr>
    <tr>
      <td>In</td>
      <td>Rover</td>
      <td>Sitter</td>
      <td>0.61</td>
      <td>0.60</td>
    </tr>
    <tr>
      <td>Out</td>
      <td>Rover</td>
      <td>Sitter</td>
      <td>0.32</td>
      <td>0.40</td>
    </tr>
    <tr>
      <td colspan="3">Avg. number of turns per min</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>In</td>
      <td>Rover</td>
      <td>Sitter</td>
      <td>0.53</td>
      <td>0.55</td>
    </tr>
    <tr>
      <td>Out</td>
      <td>Rover</td>
      <td>Sitter</td>
      <td>0.09</td>
      <td>0.18</td>
    </tr>
    <tr>
      <td colspan="3">Fraction of pauses</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>In</td>
      <td>Rover</td>
      <td>Sitter</td>
      <td>0.32</td>
      <td>−0.40</td>
    </tr>
    <tr>
      <td>Out</td>
      <td>Rover</td>
      <td>Sitter</td>
      <td>0.07</td>
      <td>0.10</td>
    </tr>
    <tr>
      <td>Figure 4</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">AnosmicB – Crawling speed</td>
      <td>Power (1 − β)</td>
      <td>Cohen’s size effect (d)</td>
    </tr>
    <tr>
      <td>Sucrose</td>
      <td>In</td>
      <td>Out</td>
      <td>0.51</td>
      <td>−0.56</td>
    </tr>
    <tr>
      <td>Yeast</td>
      <td>In</td>
      <td>Out</td>
      <td>0.23</td>
      <td>−0.39</td>
    </tr>
    <tr>
      <td colspan="3">C – Avg. number of turns per min</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sucrose</td>
      <td>In</td>
      <td>Out</td>
      <td>0.10</td>
      <td>−0.19</td>
    </tr>
    <tr>
      <td>Yeast</td>
      <td>In</td>
      <td>Out</td>
      <td>0.32</td>
      <td>−0.50</td>
    </tr>
    <tr>
      <td colspan="3">E – Handedness</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sucrose</td>
      <td>In</td>
      <td>Out</td>
      <td>0.10</td>
      <td>0.24</td>
    </tr>
    <tr>
      <td>Yeast</td>
      <td>In</td>
      <td>Out</td>
      <td>0.07</td>
      <td>−0.16</td>
    </tr>
    <tr>
      <td>Apple juice</td>
      <td>In</td>
      <td>Out</td>
      <td>0.45</td>
      <td>0.58</td>
    </tr>
    <tr>
      <td colspan="3">F – Fraction of time spent inside patch</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Sucrose</td>
      <td>Yeast</td>
      <td>0.26</td>
      <td>0.40</td>
    </tr>
    <tr>
      <td></td>
      <td>Sucrose</td>
      <td>Apple juice</td>
      <td>0.44</td>
      <td>−0.50</td>
    </tr>
    <tr>
      <td>Figure 6</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">C – Fraction of time spent inside patch – eight patches</td>
      <td>Power (1 − β)</td>
      <td>Cohen’s size effect (d)</td>
    </tr>
    <tr>
      <td>Sucrose</td>
      <td>Rover</td>
      <td>Sitter</td>
      <td>0.14</td>
      <td>−0.31</td>
    </tr>
    <tr>
      <td>Yeast</td>
      <td>Rover</td>
      <td>Sitter</td>
      <td>0.31</td>
      <td>0.45</td>
    </tr>
    <tr>
      <td colspan="3">E – Fraction of visited patches</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Rover</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sucrose</td>
      <td>2 patches</td>
      <td>8 patches</td>
      <td>0.05</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Sitter</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sucrose</td>
      <td>2 patches</td>
      <td>8 patches</td>
      <td>0.07</td>
      <td>0.15</td>
    </tr>
    <tr>
      <td>Yeast</td>
      <td>2 patches</td>
      <td>8 patches</td>
      <td>0.56</td>
      <td>−0.62</td>
    </tr>
  </tbody>
</table>
