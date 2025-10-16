# Peer review - Round 1

Editors:
- Elham Mahmoudi, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72602.sa0](https://doi.org/10.7554/eLife.72602.sa0)

This work analyzed more than half a million peer-reviewed articles published in two high-impact medical journals. It provides insights into the evolution of medical practice, language, and values over the past two centuries. Thus, it helps us contextualize our understanding of change in medicine and medical beliefs over time.


---

# Peer review - Round 1

Editors:
- Elham Mahmoudi, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72602.sa1](https://doi.org/10.7554/eLife.72602.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Through the Looking-Glass: Insights from Full Text Analyses of the Journal of the American Medical Association and the New England Journal of Medicine" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Elham Mahmoudi as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Paul Noble as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: William J. Turkel (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The following is a list of essential revisions to improve the article:

1. Inevitable OCR errors may affect the results. Present evidence or describe methods used to validate OCR results compared with original manuscripts.

2. Word-based approaches inevitably lose the contextual information of surrounding words. The authors addressed this in the paper to some extent. The use of more sophisticated methods like phrasal units may improve the accuracy of the results.

3. Expand the methods section of the manuscript to address some of the missing methodological issues regarding data validation. For example, explain the methods used to ensure the accuracy of the data or describe the methods used to ensure the accuracy of the various text-mining techniques.

Reviewer #1:

This work is based on a preliminary exploration of a newly developed database of about a half million unique, published works in JAMA (1883-2018) and NEJM (1812-2020). Authors used crowd-sourcing and different innovative modeling techniques to explore changes in evolution of medical language, ethical considerations, practice of medicine, disease burden, and our understanding and perspectives of medical concepts over the past 200 years. The results offer an outlook into the ways patients, the public, and the medical community have interacted with medicine over time.

Strengths:

Constructing a digitized database of all unique articles published in JAMA and NEJM over the last 200 years is one of the main strengths of this work. Using open-source, optical character recognition (OCR) software, authors digitized the PDF version of all included manuscripts to extract critical information.

In their time-series analyses, authors went beyond the typical word count over time. Instead, they measured the proportion of the occurrences of objective words over total number of published words in every given year. This method (relative vs. absolute count over time) resulted in a more realistic outcome. It can be applied to future work, examining trends in use of other medical words.

To better decipher the temporal change in the meaning of specific terms, authors used a technique known as "word embedding." This technique uses a vector representation of a target word in any given time. This means that the vector captures not only the word but also neighboring words that occur more often with the targeted word. For some words, the vector representation does not change. For others, however, the vector evolves over time. Thus, the vector provides a temporal measure of change, if any, in the meaning of a targeted word.

Furthermore, the authors used the "affinity propagation" technique, which does not require determining the word neighborhood size in advance. This unsupervised, clustering approach is used to analyze change in grouping/clustering of words over time. The main strength of this approach is that it is not based on any prior assumption or knowledge. Thus, it is less prone to selection bias. The authors used this method to create several clusters in each given time. This method has many applications in research, allowing individuals to explore historical changes in various settings.

Weaknesses:

Although the development of a text-searchable, digitized database of this magnitude is a strength, the authors did not elaborate on what type of validation they performed to ensure accuracy (i.e., sensitivity and specificity) of the digitized database against actual manuscripts. Providing more information on data validation would add value to this manuscript and facilitate construction of similar data in the future.

Despite its advantages, interpretation of findings based on the unsupervised clustering method could be challenging. Our prior knowledge and accompanying conceptual frameworks that are built upon them would enable us to better interpret results.

In this study, authors used various text-mining or natural language processing techniques to analyze their constructed database. Although the manuscript is innovative and has numerous strengths, methods of validating the results have not been discussed. The sensitivity and specificity of the findings is unknown. The method section of the manuscript can be expanded to address some of the missing methodological issues. This would increase the likelihood of reusability of both data and methods.

It has been a pleasure reading this well-written and innovative work. Although neither the data nor the methods used are new, their application in analyzing the published work of the past 200 years is novel. The constructed, digitized database would be useful if authors are able and willing to make it available to other researchers. As the authors mentioned, they only scratch the surface with their research. This database can be used to analyze the main trends in disease burden and treatment approaches, etc.

I have two main suggestions to improve the presented work. It is not clear if any data or method validations were performed. Authors used an open OCR software to digitize about a half million PDF files. What method(s) have been used to ensure the accuracy of the data? Similarly, what methods have been used to ensure the accuracy of the various text-mining approaches? Did authors use any annotation technique to compare the results with the actual data (which is the gold standard)? Did they divide the data into training and test sets to measure accuracy, sensitivity, or specificity of their findings?

This manuscript is a great contribution to literature. Strengthening the method section would increase the impact of the work.

Reviewer #2:

Applying text mining techniques to almost half-a-million articles from the Journal of the American Medical Association (1883-2018) and the New England Journal of Medicine (1812-2020), the authors highlight a few of the ways that medical language has changed over the past two centuries. They explore changes in specific disease terms, words that signal the emergence of ethics and clinical trial infrastructure, and the dramatic rise (and puzzling decline after 1950) of the word 'hospital'. Using the technique of historical word embeddings, they also show semantic change in individual words over time. The word 'patent', for example, is primarily associated with patent medicines until about 1920, and with invention and congenital heart disease thereafter. They also explore the histories of the more culturally charged words 'abortion', 'bias', 'defective' and 'race'. Finally, they use an unsupervised clustering technique called affinity propagation to study the historical evolution of word clusters in semantic space, to trace 'higher-order' medical concepts.

This paper is clearly written and concise, practically a textbook exposition of basic methods of text mining and their considerable strengths.

It is, perhaps, a bit too concise, at least from the perspective of the historian. Each of the four substantive examples ('abortion', 'bias', etc.) could easily be developed into a much longer paper in its own right. That is a bit of a weakness.

A second weakness is that working with half-a-million articles in PDF form means that inevitable OCR errors affect the results to some extent. In the congenital heart disease example, the words 'ductus' and 'arteriosis' appear with 'patent' (as expected, since "patent ductus arteriosus" is a key phrase). The words 'duetus' and 'arteriosis' also appear very frequently, however. While the latter is a possible spelling mistake, the former is clearly a frequently-occurring OCR error. Anyone who has worked with OCR versions of late-19th-century or early-20th-century sources knows that this is typically a substantial source of error. Some measure of OCR quality might help evaluate the results.

A final weakness is that word-based approaches inevitably lose the contextual information of surrounding words. This is addressed in the paper to some extent by the use of unsupervised clustering on the word embeddings. Alternate approaches would be to use longer units, either linguistically naive ones (like n-grams) or more sophisticated ones (like phrasal units).

Despite these caveats, this paper is a very welcome addition to the literature, and accessible enough to be broadly useful.

Although the authors are not in a position to share their raw dataset, if they could make a pubicly accessible interface to the results of their analysis (as Google did with its Ngram Viewer) they could greatly increase the impact of their research.
