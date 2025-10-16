# A community-led initiative for training in reproducible research

## Authors

- Susann Auer<sup>2</sup> ([ORCID: 0000-0001-6566-5060](https://orcid.org/0000-0001-6566-5060))
- Nele A Haeltermann<sup>3</sup> ([ORCID: 0000-0002-1431-7581](https://orcid.org/0000-0002-1431-7581))
- Tracey L Weissgerber<sup>4</sup> ([ORCID: 0000-0002-7490-2600](https://orcid.org/0000-0002-7490-2600))
- Jeffrey C Erlich<sup>5</sup> ([ORCID: 0000-0001-9073-7986](https://orcid.org/0000-0001-9073-7986))
- Damar Susilaradeya<sup>6</sup> ([ORCID: 0000-0002-4548-5924](https://orcid.org/0000-0002-4548-5924))
- Magdalena Julkowska<sup>7</sup>
- Małgorzata Anna Gazda<sup>8</sup> ([ORCID: 0000-0001-8369-1350](https://orcid.org/0000-0001-8369-1350))
- Benjamin Schwessinger<sup>10</sup> ([ORCID: 0000-0002-7194-2922](https://orcid.org/0000-0002-7194-2922)) †
- Nafisa M Jadavji<sup>11</sup> ([ORCID: 0000-0002-3557-7307](https://orcid.org/0000-0002-3557-7307)) †
- Angela Abitua<sup>13</sup>
- Angela Abitua
- Anzela Niraulu
- Aparna Shah
- April Clyburne-Sherinb
- Benoit Guiquel
- Bradly Alicea
- Caroline LaManna
- Diep Ganguly
- Eric Perkins
- Helena Jambor
- Ian Man Ho Li
- Jennifer Tsang
- Joanne Kamens
- Lenny Teytelman
- Mariella Paul
- Michelle Cronin
- Nicolas Schmelling
- Peter Crisp
- Rintu Kutum
- Santosh Phuyal
- Sarvenaz Sarabipour
- Sonali Roy
- Susanna M Bachle
- Tuan Tran
- Tyler Ford
- Vicky Steeves
- Vinodh Ilangovan
- Ana Baburamani
- Susanna Bachle

### Affiliations

1. Addgene Boston United States
2. Department of Plant Physiology, Institute of Botany, Faculty of Biology, Technische Universität Dresden Dresden Germany
3. Department of Molecular and Human Genetics, Baylor College of Medicine Houston United States
4. QUEST Center, Berlin Institute of Health, Charité Universitätsmedizin Berlin Berlin Germany
5. Shanghai Key Laboratory of Brain Functional Genomics, East China Normal University Shanghai China
6. Medical Technology Cluster, Indonesian Medical Education and Research Institute, Faculty of Medicine, Universitas Indonesia Jakarta Indonesia
7. Boyce Thompson Institute Ithaca United States
8. CIBO/InBIOO, Centro de Investigação em Biodiversidade e Recursos Genéticos, Campus Agrário de Vairão Porto Portugal
9. Departamento de Biologia, Faculdade de Ciências, Universidade do Porto Porto Portugal
10. Research School of Biology, Australian National University Canberra Australia
11. Department of Biomedical Science, Midwestern University Glendale United States
12. Department of Neuroscience, Carleton University Ottawa Canada
13. Reproducibility for Everyone New York United States

† Corresponding author

## Abstract

Open and reproducible research practices increase the reusability and impact of scientific research. The reproducibility of research results is influenced by many factors, most of which can be addressed by improved education and training. Here we describe how workshops developed by the Reproducibility for Everyone (R4E) initiative can be customized to provide researchers at all career stages and across most disciplines with education and training in reproducible research practices. The R4E initiative, which is led by volunteers, has reached more than 3000 researchers worldwide to date, and all workshop materials, including accompanying resources, are available under a CC-BY 4.0 license at https://www.repro4everyone.org/ .

## Why is training in reproducibility needed?

Reproducibility and replicability are central to science. Reproducibility is the ability to regenerate a result using the dataset and data analysis workflow that was used in the original study, while replicability is the ability to obtain similar results in a different experimental system (Leek and Peng, 2015; Schloss, 2018). Despite their importance, studies have shown that it can be quite challenging to reproduce and replicate peer-reviewed results (Baker and Penny, 2016; Freedman et al., 2015). In the past few years, several multi-center projects have assessed the level of reproducibility and replicability in various scientific fields, and have identified major factors that are critical for repeating and confirming scientific results (Alsheikh-Ali et al., 2011; Amaral et al., 2019; Baker et al., 2014; Button et al., 2013; Cova et al., 2021; Errington et al., 2014; Friedl, 2019; Hardwicke et al., 2018; Lazic, 2010; Marqués et al., 2020; Open Science Collaboration, 2015; Shen et al., 2012; Stevens, 2017; Strasak et al., 2007; Weissgerber et al., 2019; Weissgerber et al., 2015). In the rest of this article we will use the term reproducibility as shorthand for reproducibility and replicability, as is often done in the life sciences (Barba, 2018).

The factors that control the reproducibility of an experiment can be grouped into the four categories shown in Figure 1. The first represents technical factors, such as variability in reagents or materials used to perform research. The second category contains factors related to flaws in study design and/or statistical analysis such as the use of inappropriate controls, insufficient sample sizes to properly power the study, inappropriate statistical analyses, underpowered studies, and others. The third category contains human factors, which includes insufficient description of methods and the use of reagents or organisms that are not shared. In addition, scientific misconduct, such as hypothesizing after results have been obtained (HARKing; Kerr, 1998) or P-hacking (Fraser et al., 2018; Head et al., 2015; Miyakawa, 2020), is hard to detect and contributes to confirmation and publication bias issues. Lastly, external factors that are beyond the researchers' control can negatively impact reproducibility; these can include scientific rewards such as a high impact publication or paywalls that restrict access to crucial information. Going forward, developing solutions to minimize these confounding factors will be of vital importance to improve scientific integrity and to further accelerate the advancement of the scientific enterprise (Botvinik-Nezer et al., 2020; Fomel and Claerbout, 2009; Friedl, 2019; Gentleman and Temple Lang, 2007; Mangul et al., 2019; Mesirov, 2010; NIH, 2020; Peng, 2011).

![Figure 1.](https://cdn.elifesciences.org/articles/64719/elife-64719-fig1-v2.jpg)

**Figure 1.:** An approximation of the classification of categories that contribute to irreproducible scientific results, including technical, human, errors in study design and statistical analysis and external. Specific examples have been listed under each category.

While the problems with experimental reproducibility have been known for decades, they have only come to the fore over the past ten years (Begley and Ellis, 2012; Munafò et al., 2017; Prinz et al., 2011). Within the scientific community, systemic solutions and tools are being developed that allow scientists to efficiently share research materials, protocols, data, and computational analysis pipelines (some of these tools are covered in our training materials, see Box 1). Despite their transformative potential, these tools are underutilized, as most researchers are unaware of their existence, or do not know how to incorporate them in their daily workflows.

Integrating these tools into the standard scientific workflow has the potential to shift the scientific community towards a more transparent and reproducible future. Educational initiatives with open-source materials can significantly increase the reach of teaching materials (Lawrence et al., 2015) to accelerate the uptake of best practices and existing tools for reproducible research. Several initiatives exist that offer tutorials or seminars on some aspects of reproducibility (Box 2). While they each have their strengths, none of them individually offer a scalable solution to the existing training gap in reproducibility. Here, we present Reproducibility for Everyone, a set of workshop materials and modules that can be used to train researchers in reproducible research practices. Our trainings are scalable, from a dozen attendees in an intensive workshop to a few hundred participants in an introductory workshop that can attend at once in a virtual format or a large venue. However, the reproducibility movement worldwide is growing, and as different initiatives cover various aspects of the training process, they can together help bridge the reproducible training gap.

## Reproducibility for Everyone (R4E)

R4E was formed in 2018 to address the challenges of integrating reproducible research practices in life science laboratories across the globe. Our mission is to increase awareness of the factors that affect reproducibility, and to promote best practices for reproducible and transparent scientific research. We offer open access introductory materials and workshops to teach scientists at all career stages and across disciplines about concrete steps they can take to improve the transparency and reproducibility of their research. All workshops are offered free of charge. We developed eight modules as independent, in-depth slide sets focusing on different aspects of the day-to-day scientific workflow, allowing trainers to customize the workshop and adapt it to audiences in different disciplines (Box 1). R4E targets mainly biological and medical research practices (reagent and protocol sharing, data management) and in part computer science (bioinformatic tools) as evidenced by the range of trainings offered so far. Tools we discuss could also be useful for disciplines close to biological research like bioengineering, biophysics, (bio)chemistry, etc. Some training modules, especially Data management, Data visualization and Figure design, might be valuable for qualitative research that collects and analyzes text and other non-numerical data.

All materials, including recordings of previous R4E workshops and webinars, are available at https://www.repro4everyone.org/ (RRID:SCR_018958). The goal of R4E is to provide scientists with a clear overview of existing reproducibility-promoting tools, as well as to give scientists the opportunity to revisit all training material when needed, by providing them with full access to all training materials so they learn at their own pace. In addition, we welcome each trainee to fine-tune the material for their own field of expertise and to train their peers. For trainees who want to help run one of our workshops we offer the train-the-trainer approach: We meet with the trainee before the workshop and decide together which section of the material the trainee will present. Then we go through the material together, share speaker notes and practice with the trainee if needed to stay in time during the workshop.

We have developed materials for both introductory and intensive workshop formats that are described below:

Over the years, our community has grown and diversified substantially, consisting of scientists who taught one, or many R4E workshops. To date, we have reached more than 3000 researchers through over 30 workshops, which were predominantly held at international conferences and spanned numerous life science disciplines (e.g. ecology, biotechnology, plant sciences, neuroscience and many others). In addition, we have hosted several webinars that allowed researchers from all around the world to join, including webinars for early career scientists participating in the eLife Community Ambassadors Program. Investigators and conference organizers can request to host a workshop led by our volunteers or use our materials to learn more about responsible research practices and offer their own training.

The goal of our training is to introduce participants to a reproducible scientific workflow. Individual scientists or laboratories can make their research more reproducible by implementing as many of the steps introduced in our workshops as they are comfortable with (Figure 2). Feedback on our workshops indicate that 80% of participants learned important new aspects of reproducibly research practices and are very likely to implement at least some of the presented tools in their own research workflows in the future.

![Figure 2.](https://cdn.elifesciences.org/articles/64719/elife-64719-fig2-v2.jpg)

**Figure 2.:** From top to bottom, approaches that can be used on their own or in combination to increase the reproducibility of experiments, ordered from least reproducibility to most. The column on the right includes details of tools and resources than can be used to help scientists take each specific approach.

It is important to point out that this will likely work best as a stepwise, iterative process to avoid scientists from feeling overwhelmed with implementing too many changes at once. When writing a research paper, the largest impact on the reproducibility of your work can be made by incorporating the following changes: adding a detailed list of materials used for the research, that includes research resource identifiers (RRIDs; https://scicrunch.org/resources) and catalog numbers for all materials (kits, antibodies, seeds, cell lines, organisms, etc.) that were created or used during the study. Ideally, newly generated reagents or organisms are deposited at appropriate repositories to enable easy access for other scientists. Incorporating a detailed and specific methods section is crucial to reproduce the research. Ideally, protocols are deposited at a repository, and the DOI number of the respective protocol is incorporated in the methods section. Large data sets, including all metadata, should be deposited in public data repositories to generate findable, accessible, interoperable, and reusable (FAIR) data (Sansone et al., 2019). Finally, bioinformatic analytic pipelines and scripts can easily be shared via Github, Anaconda, or computational containers such as Singularity. At a minimum, authors should list and cite all programs used, including version numbers and parameters.

We would also like to point out that a supportive environment is critical for these efforts to be properly adopted in a research environment. Being the first one to speak up about irreproducible research practices at your lab or institute can be challenging, or in some cases even isolating. In this case, getting involved with a local ReproducibiliTea journal club or reaching out to the initiative to start a chapter of your own can help you connect with like-minded individuals. Similarly, joining the R4E community and discussing these situations with our community members can help you find solutions to convince your peers and supervisors of the importance of incorporating reproducible research practices.

## How can scientists use the R4E materials?

There are several ways for researchers to take advantage of the materials presented here to teach reproducible research practices. First, researchers can request a workshop run by the Reproducibility for Everyone team for a conference via email (hello@repro4everyone.org). Alternatively, researchers can use the slides and training materials available on our website to organize their own workshops. Reproducibility can be integrated into the research curriculum by asking trainees to organize and run a poster workshop at an institutional or departmental research day. Trainees can also discuss individual topics at journal clubs or as part of a methods course, after which they can develop plans to implement the identified solutions in their own research. Upcoming workshops and other opportunities to get involved and contribute will be shared through our Twitter account (@repro4everyone) and website (https://www.repro4everyone.org/).

## Conclusions

Widespread adoption of new tools and practices is urgently needed to make scientific publications more transparent and reproducible. This transition will require scalable and adaptable approaches to reproducibility education that allow scientists to efficiently learn new skills and share them with others in their lab, department and field.

R4E demonstrates how a common, public set of materials curated and maintained by a small group may form the basis for a global initiative to improve transparency and reproducibility in the life-sciences. Flexible materials allow instructors to adapt both the content and workshop format to meet the needs of the audience in their discipline. Continued training on reproducibility could be promoted in the laboratory by for instance changing every nth journal club to an educational meeting, discussing the latest developments in the reproducibility field.

Our workshops have reached over 3000 learners on six continents and continue to expand each year, offering a unique opportunity to train the next generation of scientists. Moving forward, R4E plans to broaden our reach by translating the existing materials into different languages and bring reproducibility training to more non-native English-speaking scientists. However, increasing training in reproducible research practices alone will not suffice to make all scientific findings reproducible. To achieve this goal, higher-level changes are needed to reduce the hypercompetitive nature of scientific research. Large structural and cultural changes are needed to transition from rewarding only breakthrough scientific findings, to promoting those that were performed using reproducible and transparent research practices.
