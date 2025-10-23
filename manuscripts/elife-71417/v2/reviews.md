# Peer review - Round 1

Editors:
- Talía Malagón, McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71417.sa1](https://doi.org/10.7554/eLife.71417.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work presents a dynamic infectious disease transmission model using geospatial data to structure transmission, using SARS-CoV-2 transmission in France as an example. The model allows for the incorporation of fine grain spatial heterogeneity and a large number of simulated individuals, providing a computationally efficient alternative to traditional agent-based models and a more realistic geographical mixing structure than traditional compartmental model. The Epidemap framework has many potential uses for supporting infectious disease planning and response activities beyond the SARS-CoV-2. The work will be of interest to infectious disease modelers, epidemiologists, and public health decision-makers working in epidemic outbreak management.

Decision letter after peer review:

Thank you for submitting your article "Emerging dynamics from high-resolution spatial numerical epidemics" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The paper does not currently meet eLife's policy regarding Availability of Data, Software, and Research Materials. The revision should include material to meet this policy.

2. The paper should be reformatted using a more traditional structure to improve readability (Introduction, Methods, Results, Discussion).

3. Include further explanations and discussion regarding how age is integrated into the model, or how the model could be extended to include host heterogeneity by age.

4. Include further description and explanation of how the distance kernel and mobility kernel were modeled.

5. There is currently very little discussion on how the results of this study compare with results from previous traditional models. There should be more discussion on how this study fits into previous literature on this topic, including the citation of key previous papers that have examined issues of spatial heterogeneity.

6. Include more high-level details regarding the model structure from the appendix in the main text to help the reader understand the structure without having to refer to previously published papers. The reviewers provide some suggestions in their reviews for which elements could be included.

7. The paper currently includes specifications regarding the computational resources needed for this platform, but should also include further discussion on computational resources required by traditional compartmental and agent-based models to so that the reader can appreciate the difference. Further discussion on how model results and computational resources compare with traditional compartmental and agent-based models.

8. Further discussion around limitations of the tool, particularly in the case of application to other infections where distance alone may not sufficiently capture transmission patterns.

Reviewer #1:

In this work, the authors present an infectious disease transmission model using geospatial data to structure transmission. Their aim was to produce a stochastic agent-based model that integrates geographic structure and infection natural history with sufficient realism without being too computationally demanding. By integrating map and daily mobility information, the work shows that interesting infection dynamics may occur at different geographical levels when geographic structure is considered in the context of transmission. Models incorporating geographical information are likely to be increasingly valuable in the future, as the COVID-19 pandemic has highlighted the need to consider regional and local needs when implementing public health measures against a pandemic pathogen.

Some of the model strengths include the use of detailed geographical information, and a minimal number of parameters needed to inform the model. A wide range of natural history of infection models can potentially be integrated to represent different agents with different transmission and immunity profiles. Perhaps one of the weaknesses of the model is the lack of age stratification, which would increase the realism of the model and provide important epidemiological information from a public health perspective. Age has turned out to be an important variable in tracking the COVID-19 pandemic impact and public health response. While the authors mention the model tracks the age of participants, the parameters and behaviors of agents do not appear to depend on age. A further discussion of how this model could be extended to include more heterogeneity in the movement patterns of agents would be useful, and whether the inclusion of further complexity would substantially increase the computational burden of simulations. There is also no data presented regarding the hospitalization component of the model, which is briefly described but not explored.

I think one of the major contributions of this work is the illustration of how high-resolution geographical data can be integrated into infectious disease models. These methods are likely to be of high interest to other infectious disease modelers, and to public health experts working in epidemic outbreak management.

– The paper does not currently meet eLife's policy regarding Availability of Data, Software, and Research Materials (https://submit.elifesciences.org/html/eLife_author_instructions.html#policies). I can appreciate that the dataset generated by the model is too large to be made available in free data repositories. However, this does not preclude increasing the reproducibility and availability of the data. In cases where the data can't be made available, it is up to the authors to explain in the manuscript the restrictions on the dataset or materials and why it is not possible to give public access. They must also provide a description of the steps others can follow to request access to the data or materials if they are interested. It is also good practice to provide access to data and materials for which the constraints do not apply. For example, what I have seen in similar cases with large or un-shareable datasets is that the authors would provide the necessary code to reproduce figures and tables in the manuscript with a smaller simulated dataset. Often also the dataset can be broken down into smaller datasets of the processed data necessary to reproduce each figure. While Figure 3 might be problematic due to the large number of observations, Figures 2 and 4 would likely be amenable to this as each panel appears to only display the results from a couple hundred data points. I suggest the authors consider this option. This should all be included in the data availability statement as well.

– Please further discuss how the model could be built on to add further demographic stratifications such as age to natural history/daily mobility patterns and interactions between agents. Would the addition of further stratifications severely affect the computational burden?

– The authors mention a parameter regarding hospitalization probability and severity of infection; however, these parameters are not included in the table of parameters in the appendix. It would seem to me there are more than 6 parameters in the model then. It is unclear why these parameters were added, as they are not explored in the results or mentioned very much in the text. Some more discussion or results regarding this component of the model would be warranted.

– There is little discussion of other models which have implemented geographical structure, and how this model compares with those. I am not very familiar with this literature, but I find it hard to believe that none have tried to implement some geographical component. Some more discussion on how this approach is innovative or different compared to what has been done in the past would be useful.

– It would be useful to include the names of the scientific papers cited in the reference list, most of these are not full references.

Reviewer #2:

This work provides a new general tool for studying the chains and patterns of transmission of infectious diseases. It addresses the limitations of mathematical models and the Agent-Based Simulation platforms in public health by using High-Performance Computing techniques, high-resolution spatial data, and complex mobile models. Based on the results of 100 stochastic simulations, the basic reproduction number, the duration of the disease and the final total epidemic size were obtained at the national level, which shows the importance of the geographical structure. Meanwhile, the influence of the distance from origin and the density of the region on the epidemic was shown at the district level. Finally, this paper also shows that the importance of super-spreading events varies according to the stage of the epidemic.

1. In the Introduction part, the authors mentioned some work on COVID-19 based on mathematical modelling. However, some existed work are not well respected. Please see some papers: Short-term predictions and prevention strategies for COVID-19: A model-based study, Applied Mathematics and Computation, 2021; Analysis of COVID-19 transmission in Shanxi Province with discrete time imported cases, MBE, 2020; An investigation of transmission control measures during the first 50 days of the COVID-19 epidemic in China, Science, 2020; Transmission dynamics of COVID-19 in Wuhan, China: effects of lockdown and medical resources, Nonlinear Dynamics, 2020.

2. For readability, please give a brief description and introduction of a distance kernel and a mobility kernel mentioned in line 52 in the text.

3. In line 55, the author mentioned that the simulation tracked the age of the individual, but this was not further described and shown in the text, as well as the description of the relevant simulation result. Given the importance of age to COVID-19, further research on age should be conducted.

4. This paper demonstrates the power and flexibility of the Epidemap platform through the application of COVID-19 in France. However, all the results obtained in the paper are obtained through numerical simulation, the authors should compare them with the real data at the national and district level of France to further prove the rationality, practical application and authenticity of this method.

Reviewer #3:

Thomine et al., have a developed a new tool for modeling infectious diseases which can consider fine grain geographic movements of tens of millions of individual agents (simulated persons), thereby enabling more realistic simulations (compared to SIR models) without the excessive computational demands required by traditional agent-based modeling approaches. Impressively, this tool, Epidemap, was able to simulate one year of daily interactions and epidemic growth trajectories for the entire population France (approximately 65 million people) in less than two hours using a standard high performance computer.

The authors present the example of an uncontrolled SARS-CoV-2 epidemic in France and identified spatio-temporal differences in disease and transmission dynamics that would not be discernable using naïve SIR modeling approaches and would be extremely computationally demand to complete using traditional ABM methods. These observations included a distinct bimodal pattern, in which each peak was comprised of different localities; a strong correlation between the timing of the epidemic peak in different regions and its distance from the point of epidemic origin; important differences in disease dynamics based on population density; and unique insights regarding secondary attack rates measured at the individual level (i.e., the reproductive number). These observations could support evidence-informed targeting of public health measures to optimize the impact of mitigation measures and support health care planning. This tool could also have great applicability to the study of other respiratory infections, particularly if additional features further enhancing the realism of the simulations, such as assigning children to schools, can be added without substantially increasing computational demands. The visual component of this tool is an especially nice feature, which could greatly support knowledge translation activities with decision-makers and planners.

The rationale for the development of this tool is clear (and important), the conclusions of this manuscript are supported by the data, and the paper is well-written. The included figures, particularly Figure 1, are very easy to follow and nicely display the key take-away messages.

The methods section could benefit from additional details to better able the reader to understand the development of this tool, specifically:

1) Please provide adequate details regarding the fundamentals of this approach in the main manuscript text. The material provided in S1 Supplementary Methods is critical to understanding this tool, particularly the summary statement regarding the three specific models. For example, the manuscript refers to the epidemiological model, but the reader must refer to a reference to learn more. Providing some high-level details regrading the model and the hospital data (including how they were used to parametrize the model) would be helpful. Similarly, it is stated that the disease progression model follows that of reference 10 – having a figure included in the manuscript would be helpful – and the daily reproduction numbers were based on a method from 18 – a brief description would be appreciated.

2) How do these findings compare to traditional SIR or ABM models? Understandably, it may be too computationally demanding to run a traditional ABM for the entire population of France and would likely be out of scope for this study. For context, it would be useful to provide an estimate of the time and computational resources demanded by traditional approaches. If running these other models are possible, a comparison of the insights provided across these 3 methods would be highly valuable – particularly if there are large differences.

3) The probability of encounters is based only on distance. As the authors state, this assumption may not hold for other countries (e.g. the US where air travel is more important). This assumption may also not hold for other infections. For example, the transmission dynamics of pediatric respiratory viruses are more influenced by neighbourhood-level patterns of movement – whereas diseases of adults are more heavily influenced by larger-scale geographic patterns. Please provide the reader with more context around this limitation.

– Abstract: I'm not sure if "computational-efficient" is grammatically correct – suggested revision: computationally efficient.

– The introduction section could be strengthened by first introducing the idea of a mathematical model – and their uses – before discussing their limitations. Could you provide the reader with an explicit example of where these models have failed because they did not contain the features of an ABM (or Epidemap)? There are several examples from the COVID-19 pandemic and Ebola epidemics that readers would be familiar with and would allow them to immediately appreciate the importance of the current work.

– Introduction: You state that SIR models ignore spatial contact patterns. Though the naïve SIR model does, most SIR models are age-structured and include some sort of contact matrix (e.g. POLYMOD). Suggest rewording to "and oversimplifies contact patterns".

– Regarding the following statement: "A third limit resides in the way geographic structure is implemented into the simulation (but see (7))." Please clarify what is meant without the reader referring to a reference.

– Such a model is likely only relevant to the study of respiratory viruses, this should be stated as a limitation – or, if modifications can be made to enable the study of other infectious diseases (e.g. STIs), this should be highlighted as a strength of Epidemap.

– The readability of the manuscript would also benefit from a more traditional structure, i.e., sub-headers in the abstract and main text for background, methods, results, and discussion. Similarly, the funding statement is provided as reference. This, along with a conflict of interest statement, should be explicitly provided in-text.

– In the supplement, you refer to the spread of COVID-19. Recommended revision: SARS-CoV-2.

– To enhance the clarity of Figure 2, it would be helpful to line-up the x-axes of (a) and (b).

Specific aspects of the methodology that are not clear from the manuscript or supplemental:

– The justification for some modeling choices has not been provided and it is not clear what impact, if any, this would have had on the results. Namely, what was the rationale for initializing the model with 15 infected individuals in Paris and aligning the axis for Figure 2 based a value of 700 ICU beds. Assumedly, the choice for Paris is due to this being the most likely place for importation, but this is not clear. The choices for the other two values appears arbitrary.

– It is not clear how the interaction model accounts for household and school/workplace encounters. For example, are these included in the random movement or separately? Does the risk of transmission differ in these contexts? These dynamics would be quite different than a random encounter at, for example, the grocery store. Similarly, can transmission occur within hospitals?

– The age of contacts is recorded, but it is not clear how/if this information is incorporated into the simulation; e.g. differences in disease severity profiles on the basis of age.

– How were the point estimates and 95% CI calculated?
