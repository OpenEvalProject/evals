# Author response - Round 1

Authors:
- Shereen R Kadir ([ORCID: 0000-0002-3960-988X](https://orcid.org/0000-0002-3960-988X))
- Andrew Lilja ([ORCID: 0000-0001-8311-3702](https://orcid.org/0000-0001-8311-3702))
- Nick Gunn
- Campbell Strong
- Rowan T Hughes ([ORCID: 0000-0001-5618-381X](https://orcid.org/0000-0001-5618-381X))
- Benjamin J Bailey
- James Rae
- Robert G Parton ([ORCID: 0000-0002-7494-5248](https://orcid.org/0000-0002-7494-5248))
- John McGhee ([ORCID: 0000-0002-9264-7535](https://orcid.org/0000-0002-9264-7535))

## Response text

DOI: [10.7554/eLife.64047.sa2](https://doi.org/10.7554/eLife.64047.sa2)

Reviewer #1:

[…]

Overall, the authors have accomplished an impressive amount of work and created what is no doubt a stunning experience. This is also evident in the quality of the images and figure design in the manuscript itself. The supplementary tables and figures are highly detailed and very useful to any who would seek to understand and recreate some of the technical aspects of this work. Although the authors discuss and lament the lack of a database beyond the PDB to share and annotate integrative modeling efforts like theirs, they do not follow-up by offering to share the models created in this study as a way to remedy such a problem. Nevertheless, I would recommend that this study be published in eLife as I believe it represents an impressive effort towards the advanced visualization of environments relevant to the readership. I would however ask that the authors address the points made above and summarized here for clarity here:

1. Please provide a clearer definition or discussion of your intended user.

We more clearly define the primary user group as tertiary and university biology students. Secondary users have also been identified (public, experimental scientists), but are not the core target group.

2. For this user, what are the specific learning/communication objectives?

We more clearly define that the key objective of Nanoscape in this group is to support the learning of advanced biological concepts such as scale, density and interactions which may be misleading or oversimplified in other learning material. New Section in paper: Nanoscape Evaluation and broader applications

3. Draw more direct connections between these objectives and the specific design decisions that drove your project implementation.

Design decisions were paramount for both computational performance and aesthetic comfort. To avoid being visually overwhelmed, we had to reduce the number of proteins and small molecules (eg. water) in the environment. This also allowed a better appreciation of the 'vistas' of organic landscape and how several components interact with one another. In another example, the complexity of the ECM had to be simplified due to uncertainties about how the components co-ordinate their interactions with surface receptors. Proteins were stylised as polygonal meshes to highlight protein domains (some later animated), instead of atomic representation. In most cases, the appearance of the mesh of each component (protein/cell/blood vessel, etc.) was modified (made low-poly) to ensure real-time performance.

4. Although carrying out an assessment study may be beyond the scope of this manuscript, please discuss how this could be carried out and, in doing so, provide a more explicit statement of learning goals and outcomes.

We suggest that evaluation of the application for measures of usability (attention, cognitive demand etc) and educational value (as a didactic aid) is vital and is planned for phase 2 of this project. We would like to understand if Nanoscape, with its increased level of authenticity can help deepen the understanding of advanced topics such as protein density and molecular scale. Assessors can vary these parameters in application and evaluate the effect each has on basic and advanced cellular topics through exams. We would also like to test the effect of immersion and interactivity of this application against a more linear version of the content (like a pre-recorded video).

5. I would also want to know (and have the authors describe) whether they intend to share their models and the experience itself (since they say it can be set up on a user desktop – as opposed to their previous project which appears to require a more involved set-up for VR).

We will be making this publicly accessible (likely via the Steam store).

6. Finally, I find the suggestion in the conclusion that such environments may become useful for scientists to 'reflect upon their own data' is very interesting. However, such a statement requires some level of discussion addressing how visual design choices may need to change to accommodate the goals of this new kind of audience. Is there a difference in what molecular actors (or representational choices) could be left out or included, and what specific aspects of this interactive and immersive environment do the authors find most promising for use by the scientific community?

Have touched on the value to scientists – we believe that this application probably won’t offer a platform for rigorous data interrogation, but perhaps more holistic reflection of how systems integrate by seeing several modalities of data presented in the one cohesive format. Users may also gain an appreciation of the piece simply as an aesthetic piece of art or entertainment.

Reviewer #2:

[…]

I have but one concern that is relatively very minor. It would be helpful if the authors provided some additional context as to who their users are? The users are mentioned several times throughout the manuscript as a consideration in design decisions made, but no clear characterization of the anticipated user group is ever offered.

Please see reviewer 1, comments 1-2.

Reviewer #3:

This article discusses the use of computer visualization techniques to create an explorable 3D virtual environment, called Nanoscape, depicting a breast cancer cell within the context of a tumor.

1. Although the title suggests that the article will describe the Nanoscape application in detail, we were disappointed that only a cursory description of this project was given. While we understand that Nanoscape has yet to be released (and so user feedback should not be expected), we hoped to better understand what the purpose of the overall project is. Who is the target audience, how would the application be implemented, and what do the authors hope to achieve? An explanation of the novel features of Nanoscape (in comparison to other similar efforts) is particularly important given that many of the software techniques that have been used for this project have been previously released and/or described by others (e.g.Molecular Maya for protein modeling, CellPack for creating crowded environments) and do not represent new methods.

Please see reviewer 1, comments 1-2.

2. We were concerned that the article appears to be written primarily for 3D biomedical illustrators, rather than for research biologists. The article itself questioned whether 3D visualizations could support experimentalists (see lines 115-117). Given the readership of eLife, we felt that a much stronger consideration for the role of 3D visualization in the research sphere, and/or a more in-depth discussion of how these types of applications (and Nanoscape in particular) can impact public engagement and outreach is warranted.

Please see reviewer 1, comment 6.

3. In many sections of the article, the authors discussed general challenges faced when creating molecular environments, but did not discuss how they met these challenges in creating the Nanoscape models and how they made the decisions that they ultimately made. For example, the authors discussed the issue of conformational flexibility of proteins (paragraph starting on line 227) and the limitation posed when only one conformation of a protein has been structurally solved. How did the authors solve this problem in the case of Nanoscape? Likewise, when discussing the dynamics of lipids within a membrane, the authors point out that depicting the movement and heterogeneity of membranes is challenging, but did not describe how this challenge was met in the context of Nanoscape.

In many cases, proteins existed only in one conformational state, so molecular animations were not possible for those. This application did not intend to offer rigorous molecular dynamics simulations, as this was outside the scope of the work. Where several protein states existed, we were able to animate those proteins with a reasonable level of confidence. Another option that we did not explore was to simply use artistic licence and artistically manipulate conformational changes to suggest flexibility of the proteins, but this was not completed for the current version of the application. We also note that due to performance reasons, we elected to simulate the cell membrane as an animated texture instead of individual lipids.

4. In line 202, mMaya is described as a software that "qualitatively replicate(s) molecular dynamics," and this software is described throughout the article as the main tool that was used to create dynamic animations of different proteins. A direct comparison of the process and computed trajectories produced by mMaya and those produced by established molecular dynamics simulation packages and/or coarse-grained modeling would ideally be provided to better support this description of mMaya, especially considering that mMaya is likely to be a software that is unfamiliar to many readers, and that there are (as far as we know) no other publications that describe the use of mMaya in the scientific literature.

Have included a detailed description of mMaya from its publishers in the supplementary figures.
