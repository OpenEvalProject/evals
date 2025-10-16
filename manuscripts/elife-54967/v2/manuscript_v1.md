# A community-maintained standard library of population genetic models

## Authors

- Jeffrey R Adrion<sup>1</sup>
- Christopher B Cole<sup>2</sup> ([ORCID: 0000-0002-6733-633X](https://orcid.org/0000-0002-6733-633X))
- Noah Dukler<sup>3</sup> ([ORCID: 0000-0002-8739-8052](https://orcid.org/0000-0002-8739-8052))
- Jared G Galloway<sup>4</sup>
- Ariella L Gladstein<sup>5</sup>
- Graham Gower<sup>6</sup> ([ORCID: 0000-0002-6197-3872](https://orcid.org/0000-0002-6197-3872))
- Christopher C Kyriazis<sup>7</sup>
- Aaron P Ragsdale<sup>8</sup> ([ORCID: 0000-0003-0715-3432](https://orcid.org/0000-0003-0715-3432))
- Georgia Tsambos<sup>9</sup> ([ORCID: 0000-0001-7001-2275](https://orcid.org/0000-0001-7001-2275))
- Franz Baumdicker<sup>10</sup>
- Jedidiah Carlson<sup>11</sup>
- Reed A Cartwright<sup>12</sup>
- Arun Durvasula<sup>13</sup> ([ORCID: 0000-0003-0631-3238](https://orcid.org/0000-0003-0631-3238))
- Ilan Gronau<sup>14</sup>
- Bernard Y Kim<sup>15</sup>
- Patrick McKenzie<sup>16</sup>
- Philipp W Messer<sup>17</sup> ([ORCID: 0000-0001-8453-9377](https://orcid.org/0000-0001-8453-9377))
- Ekaterina Noskova<sup>18</sup> ([ORCID: 0000-0003-1168-0497](https://orcid.org/0000-0003-1168-0497))
- Diego Ortega Del Vecchyo<sup>19</sup>
- Fernando Racimo<sup>6</sup> ([ORCID: 0000-0002-5025-2607](https://orcid.org/0000-0002-5025-2607))
- Travis J Struck<sup>20</sup>
- Simon Gravel<sup>8</sup>
- Ryan N Gutenkunst<sup>20</sup> ([ORCID: 0000-0002-8659-0579](https://orcid.org/0000-0002-8659-0579))
- Kirk E Lohmueller<sup>7</sup> ([ORCID: 0000-0002-3874-369X](https://orcid.org/0000-0002-3874-369X))
- Peter L Ralph<sup>21</sup>
- Daniel R Schrider<sup>5</sup> ([ORCID: 0000-0001-5249-4151](https://orcid.org/0000-0001-5249-4151))
- Adam Siepel<sup>3</sup>
- Jerome Kelleher<sup>22</sup> †
- Andrew D Kern<sup>21</sup> ([ORCID: 0000-0003-4381-4680](https://orcid.org/0000-0003-4381-4680)) †

### Affiliations

1. Department of Biology University of Oregon Eugene United States
2. Weatherall Institute of Molecular Medicine University of Oxford Oxford United Kingdom
3. Simons Center for Quantitative Biology Cold Spring Harbor Laboratory Cold Spring Harbor United States
4. Department of Biology and Institute of Ecology and Evolution University of Oregon Eugene United States
5. Department of Genetics University of North Carolina at Chapel Hill Chapel Hill United States
6. Lundbeck GeoGenetics Centre, Globe Institute University of Copenhagen Copenhagen Denmark
7. Department of Ecology and Evolutionary Biology University of California, Los Angeles Los Angeles United States
8. Human Genetics McGill University Montreal Canada
9. Melbourne Integrative Genomics, School of Mathematics and Statistics University of Melbourne Melbourne Australia
10. Department of Mathematical Stochastics University of Freiburg Freiburg Germany
11. Department of Genome Sciences University of Washington Seattle United States
12. The Biodesign Institute and The School of Life Sciences Arizona State University Tempe United States
13. Department of Human Genetics University of California, Los Angeles Los Angeles United States
14. IDC Herzliya Herzliya Israel
15. Department of Biology Stanford University Stanford United States
16. Department of Ecology, Evolution, and Environmental Biology Columbia University New York United States
17. Department of Biological Statistics and Computational Biology Cornell University Ithaca United States
18. Computer Technologies Laboratory ITMO University Saint Petersburg Russian Federation
19. International Laboratory for Human Genome Research National Autonomous University of Mexico Juriquilla Mexico
20. Molecular and Cellular Biology University of Arizona Tucson United States
21. Institute of Ecology and Evolution University of Oregon Eugene United States
22. Big Data Institute, Li Ka Shing Centre for Health Information and Discovery University of Oxford Oxford United Kingdom

† Corresponding author

## Abstract

The explosion in population genomic data demands ever more complex modes of analysis, and increasingly these analyses depend on sophisticated simulations. Re-cent advances in population genetic simulation have made it possible to simulate large and complex models, but specifying such models for a particular simulation engine remains a difficult and error-prone task. Computational genetics researchers currently re-implement simulation models independently, leading to inconsistency and duplication of effort. This situation presents a major barrier to empirical researchers seeking to use simulations for power analyses of upcoming studies or sanity checks on existing genomic data. Population genetics, as a field, also lacks standard benchmarks by which new tools for inference might be measured. Here we describe a new resource, stdpopsim, that attempts to rectify this situation. Stdpopsim is a community-driven open source project, which provides easy access to a growing catalog of published simulation models from a range of organisms and supports multiple simulation engine backends. This resource is available as a well-documented python library with a simple command-line interface. We share some examples demonstrating how stdpopsim can be used to systematically compare demographic inference methods, and we encourage a broader community of developers to contribute to this growing resource.
