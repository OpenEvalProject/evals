# Peer review - Round 1

Editors:
- Hugo J Bellen, Baylor College of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58630.sa1](https://doi.org/10.7554/eLife.58630.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

We believe that the monitoring assay that the authors here developed will be useful in many fly labs and anticipate that this work will impact the research of very different types of fly research.

Decision letter after peer review:

Thank you for submitting your article "The Drosophila Individual Activity Monitoring and Detection System (DIAMonDS)" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and K VijayRaghavan as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jonathan Andrews (Reviewer #1); Michael B O'Connor (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

We encourage you to carefully read the critiques and address all the issues that are listed below.

Reviewer #1:

The paper entitled ‘The Drosophila Individual Activity Monitoring and Detection System (DIAMonDS)’ highlights a new detection/tracking system which utilizes a flatbed CCD scanner to track and identify multiple life cycle events (pupariation, eclosion, and death) using a newly developed algorithm. In support of this novel monitoring system, the authors provide multiple examples of the tracking system in action, including analysis of larval and adult movement and the detection of pupariation and eclosion at a high temporal resolution. The authors also provide several examples of more complex experiments which can be accomplished in a high-throughput manner using DIAMonDS, including lifespan and stress resistance assays. As described, this system would provide a researcher with an automated tool for measuring the timing of multiple major developmental milestones in Drosophila development – essentially allowing for more accurate and less labor intensive observation.

While DIAMonDS is certainly valuable in its current incarnation, the authors do note a number of worrying limitations which I believe should be resolved prior to publication, and there are several areas of the manuscript where I believe more detail is warranted.

1) As DIAMonDS detects changes between the static and active phases in the Drosophila lifecycle through changes in motion, it is essential that the authors demonstrate (or provide an explanation of) how they discriminate between less motile stages of development (or death) and normal cessation of motion while alive, such as in grooming or sleep behavior in the adult.

2) Similar to critique #1, this type of motion detection may not be as effective in animals with some form of locomotor defect. An additional experiment demonstrating that DIAMonDS can reliably detect and classify larvae or adults with reduced locomotion is prudent to demonstrate that it can work, even if the flies are impaired in some way.

3) It is currently unclear how the DIAMonDS system handles events that occur "off-camera", as can be observed in frame 77-79 of Video 1. This may be a potential sources of error during tracking – for example, if a larvae crawls into an area where it is not observed and pupates, or if an animal dies out of view.

4) It is unclear how (or if) the system would discriminate between pupation and a dead larvae. A failure to account for this could easily result in a false-positive for pupation.

5) Paragraph four subsection “Pupariation and eclosion timing detection by DIAMonDS”: I was unable to locate a description of the semi-automatic (TH) methods presented here in the Materials and methods section.

6) The inability of the methods described in the manuscript to handle Oregon-R or Canton-S strains significantly limits the usefulness of the system. A set of optimal conditions for common laboratory strains should be included with the manuscript.

7) As admitted by the authors, the size of the wells may adversely affect fly health. It would be worthwhile to see a comparison between the smaller chambers and a larger chamber, so as to allow for future users of the system to make more informed decisions about how to implement it.

Reviewer #2:

The manuscript by Seong et al. describes the development of a sophisticated activity monitoring system that is able to determine with, great accuracy, the timing of major life stage transitions during Drosophila development. Specifically, the system relies on time lapse imaging and A.I. based learning to pinpoint three transitions: (1) larval to pupal, (2) pupal to adult, (3) adult to death. The basic principle is to establish the location of a larva, pupa or adult at each time point within either a 96 or 384 well plate and then determine if it has changed at the next time point. Since larva and adults are motile and pupa and dead flies are not then it is conceptually easy to distinguish the stage transition through location changes by monitoring location changes. The authors demonstrate that the system works, at least for the W1118 genetic background, and is able to replicate known developmental characteristics such as the fact the females typically eclose a few hours before males and that the timing of the larval to pupal transition is diet (sugar) sensitive. They also demonstrate that it can be used to establish Kaplan-Meier lifespan curves which are capable of distinguishing environmental effects on adult lifespan such as the presence of DDT or paraquat in the food. Overall this system appears to have great potential for quantitatively measuring a number of developmental parameters that are presently very tedious to determine manually and are therefore not amenable to high throughput procedures that are needed for genetic and drug screening.

I do not feel competent to comment on the software development and AI procedures used to train the system other than to say that they appear to work quite reliably as long as the optics are not disturbed. Herein lies the biggest disappointment.

1) The authors conclude their Results section by saying that they cannot reliably measure lifespan in common strains such as Oregon-R and Canton-S because of accidental death effects due to such issues as water condensation in the wells and also due to blockage of the optical light path by the spread of food particles and feces on the well lid that obscures detection of the fly's position during imaging. The authors say that additional refinements of the system will be needed to overcome these challenges for adult lifespan analysis. I wonder, however, if the authors have tried something as simple as replacing the lid of the microtiter dish at some frequency during the lifespan measurements. I recognize that the entire chamber will need to be immersed in a CO2 chamber or cooled to knock the flies out and that this may influence the lifespan kinetics, but have the authors attempted anything like this as a work around to the degenerating light path and water accumulation issues during aging studies?

Despite this drawback, I think the system still has significant utility for assaying environmental and genetic effects on larval to pupa and pupal to adult transitions and this makes it is worth communicating to the Drosophila research community.
