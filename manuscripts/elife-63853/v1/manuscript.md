# Automated annotation of birdsong with a neural network that segments spectrograms

## Authors

- Yarden Cohen<sup>1</sup> ([ORCID: 0000-0002-8149-6954](https://orcid.org/0000-0002-8149-6954)) †
- David Aaron Nicholson<sup>2</sup>
- Alexa Sanchioni<sup>3</sup>
- Emily K Mallaber<sup>3</sup>
- Viktoriya Skidanova<sup>3</sup>
- Timothy J Gardner<sup>4</sup> ([ORCID: 0000-0002-1744-3970](https://orcid.org/0000-0002-1744-3970)) †

### Affiliations

1. Department of Brain Sciences Weizmann Institute of Science Rehovot Israel
2. Department of Biology Emory University Atlanta United States
3. Department of Biology Boston University Boston United States
4. Phil and Penny Knight Campus for Accelerating Scientific Impact University of Oregon Eugene United States

† Corresponding author

## Abstract

Songbirds provide a powerful model system for studying sensory-motor learning. However, many analyses of birdsong require time-consuming, manual annotation of its elements, called syllables. Automated methods for annotation have been proposed, but these methods assume that audio can be cleanly segmented into syllables, or they require carefully tuning multiple statistical models. Here we present TweetyNet: a single neural network model that learns how to segment spectrograms of birdsong into annotated syllables. We show that TweetyNet mitigates limitations of methods that rely on segmented audio. We also show that TweetyNet performs well across multiple individuals from two species of songbirds, Bengalese finches and canaries. Lastly, we demonstrate that using TweetyNet we can accurately annotate very large datasets containing multiple days of song, and that these predicted annotations replicate key findings from behavioral studies. In addition, we provide open-source software to assist other researchers, and a large dataset of annotated canary song that can serve as a benchmark. We conclude that TweetyNet makes it possible to address a wide range of new questions about birdsong.
