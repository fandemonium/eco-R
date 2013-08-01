import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

#usage: for i in *.gbk; do python ~/Documents/Projects/KBase/eco-R/genbank-fan/extract_dbsource_from_gbk.py $i; done > hit_id_accession.txt 

for record in list(SeqIO.parse(sys.argv[1], 'genbank')):
#    print record
    hit_id = record.id
    org = record.annotations["source"] 
    print 'hit_id' + '\t' +  hit_id + '\t'+ org

#    print '%s\t%s\t%s\t%s' %('hit_id' +  hit_id + 'accession_number' + dbsource)
#for line in open(sys.argv[1]):
#    if "DBSOURCE" in line:
#        line = line.rstrip()
#        lexemes = line.split('')
#        id = lexemes[-1]
#        l.append(id.rstrip())
