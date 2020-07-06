# IRcoeffCalc
## Inbred and Relationship Coefficients Calculator

### Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Coefficients](#coefficients)
* [Instruction](#instruction)

## General info
This is a project that was created as my BA thesis. Using data in specified format, you can calculate coefficient of inbreeding and coefficient of relationship for analyzed population.

## Coefficients

Both coefficients relate to similar issues, have similar meanings and are calculated in a similar way. The most key difference between them is that the coefficient of inbreeding is calculated only for one individual from the population, and the coefficient of relationship is calculated between two individuals. 

The purpose of calculating the inbreeding coefficient is to find out how much of the individual's genes are identical by origin at a given locus. This is important, for example, from an animal breeder's point of view. Individuals are associated with each other in order to achieve undesirable characteristics by the breeder, however, too high a coefficient of inbreeding in an individual usually results in deterioration of his physical and mental condition, susceptibility of the disease and increased mortality. Breeders need to calculate inbreeding rates and control gene flow in their breeding population to avoid negative effects of mating. The situation is very similar in the case of the relationship of kinship, because the mating of related individuals leads to inbred individuals.

**Coefficient of inbreeding** is the probability that both gametes at the same locus carry genes identical by origin. The more closely the two individuals are related, the greater the chance that their offspring will be inbred.
This factor is in the range 0 to 1:
- 0 - the individual certainly did not receive identical genes from their parents,
- 1 - the connecting gametes are certainly identical in terms of a given gene.

**Coefficient of relationship** is the probability that a given gene from an allele pair of one individual is identical in origin to one of the genes of the same allele pair of the other individual.
This factor is also in the range 0 to 1:
- 0 - individuals certainly do not have identical genes,
- 1 - individuals definitely have identical genes on each loci.
