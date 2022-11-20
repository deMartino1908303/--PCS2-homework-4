from data_reader import fasta_reader
from Bio.Seq import Seq

DNA = Seq("".join(fasta_reader("rosalind_revp.txt")))


opp_DNA = str((DNA).complement())
DNA = str(DNA)

for start_counter in range(len(DNA)):
    for end_counter in range(start_counter, len(DNA)):
        palind_check = opp_DNA[start_counter:end_counter + 1]
        template = DNA[start_counter:end_counter + 1]
        if len(palind_check) >=4 and len(palind_check) <= 12:
            if template[::-1] == palind_check:
                with open("zzzzresult.txt", "a") as done:
                    done.write(str(start_counter+1))
                    done.write(" ")
                    done.write(str(len(template)))
                    done.write("\n")
