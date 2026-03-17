def sort_string(string):
  chars=list(string)
  chars.sort()
  new_string=""
  for char in chars:
    new_string=new_string+char
  return new_string
  

parent1_alleles=input("Parent1 Alleles? ")
parent2_alleles=input("Parent2 Alleles? ")

genotypes={}

for x in range(len(parent1_alleles)):
  allele1=parent1_alleles[x]
  for y in range(len(parent2_alleles)):
    allele2=parent2_alleles[y]
    genotype=sort_string(allele1+allele2)
    
    if genotype not in genotypes:
      genotypes[genotype]=1
    else:
      genotypes[genotype]+=1

total=0
for genotype in genotypes:
  total+=genotypes[genotype]
  

for genotype in genotypes:
  print(genotype+": "+str((genotypes[genotype]/total)*100)+"%")
  
