def file_phase_data(filename, n, m):
    real_phase_data = []
    # grab haplotype data from input file
    hapfile = open(filename)
    data = []
    # throw away first line and first two columns
    hapfile.readline()
    for i in xrange(m):
        data.append(hapfile.readline().split()[2:])
        print data
        print '\n\n===============\n\n'
    # now parse out the haplotypes!
    for i_n in xrange(n):       # for each individual
        hap_one_data = []
        hap_two_data = []
        for i_m in xrange(m):   # for each SNP
            # arbitrarily assign 0 to the SNP that individual number 0 has at this SNP position
            print data[i_m][0]
            ref_snp = data[i_m][0]
            hap_one_data.append(0 if data[i_m][i_n * 2] == ref_snp else 1)
            hap_two_data.append(0 if data[i_m][i_n * 2 + 1] == ref_snp else 1)
    return hap_one_data, hap_two_data


a, b = file_phase_data('file.txt', 25, 2)

print a
print '\n\n\n\n\n\n\n'
print b