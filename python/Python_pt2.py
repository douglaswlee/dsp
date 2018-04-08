import sys
import os
import csv
import re

facultycsv = """name, degree, title, email
Scarlett L. Bellamy, Sc.D.,Associate Professor of Biostatistics,bellamys@mail.med.upenn.edu
Warren B. Bilker,Ph.D.,Professor of Biostatistics,warren@upenn.edu
Matthew W Bryan, PhD,Assistant Professor of Biostatistics,bryanma@upenn.edu
Jinbo Chen, Ph.D.,Associate Professor of Biostatistics,jinboche@upenn.edu
Susan S Ellenberg, Ph.D.,Professor of Biostatistics,sellenbe@upenn.edu
Jonas H. Ellenberg, Ph.D.,Professor of Biostatistics,jellenbe@mail.med.upenn.edu
Rui Feng, Ph.D,Assistant Professor of Biostatistics,ruifeng@upenn.edu
Benjamin C. French, PhD,Associate Professor of Biostatistics,bcfrench@mail.med.upenn.edu
Phyllis A. Gimotty, Ph.D,Professor of Biostatistics,pgimotty@upenn.edu
Wensheng Guo, Ph.D,Professor of Biostatistics,wguo@mail.med.upenn.edu
Yenchih Hsu, Ph.D.,Assistant Professor of Biostatistics,hsu9@mail.med.upenn.edu
Rebecca A Hubbard, PhD,Associate Professor of Biostatistics,rhubb@mail.med.upenn.edu
Wei-Ting Hwang, Ph.D.,Associate Professor of Biostatistics,whwang@mail.med.upenn.edu
Marshall M. Joffe, MD MPH Ph.D,Professor of Biostatistics,mjoffe@mail.med.upenn.edu
J. Richard Landis, B.S.Ed. M.S. Ph.D.,Professor of Biostatistics,jrlandis@mail.med.upenn.edu
Yimei Li, Ph.D.,Assistant Professor of Biostatistics,liy3@email.chop.edu
Mingyao Li, Ph.D.,Associate Professor of Biostatistics,mingyao@mail.med.upenn.edu
Hongzhe Li, Ph.D,Professor of Biostatistics,hongzhe@upenn.edu
A. Russell Localio, JD MA MPH MS PhD,Associate Professor of Biostatistics,rlocalio@upenn.edu
Nandita Mitra, Ph.D.,Associate Professor of Biostatistics,nanditam@mail.med.upenn.edu
Knashawn H. Morales, Sc.D.,Associate Professor of Biostatistics,knashawn@mail.med.upenn.edu
Kathleen Joy Propert, Sc.D.,Professor of Biostatistics,propert@mail.med.upenn.edu
Mary E. Putt, PhD ScD,Professor of Biostatistics,mputt@mail.med.upenn.edu
Sarah Jane Ratcliffe, Ph.D.,Associate Professor of Biostatistics,sratclif@upenn.edu
Michelle Elana Ross, PhD,Assistant Professor is Biostatistics,michross@upenn.edu
Jason A. Roy, Ph.D.,Associate Professor of Biostatistics,jaroy@mail.med.upenn.edu
Mary D. Sammel, Sc.D.,Professor of Biostatistics,msammel@cceb.med.upenn.edu
Pamela Ann Shaw, PhD,Assistant Professor of Biostatistics,shawp@upenn.edu
Russell Takeshi Shinohara,0,Assistant Professor of Biostatistics,rshi@mail.med.upenn.edu
Haochang Shou, Ph.D.,Assistant Professor of Biostatistics,hshou@mail.med.upenn.edu
Justine Shults, Ph.D.,Professor of Biostatistics,jshults@mail.med.upenn.edu
Alisa Jane Stephens, Ph.D.,Assistant Professor of Biostatistics,alisaste@mail.med.upenn.edu
Andrea Beth Troxel, ScD,Professor of Biostatistics,atroxel@mail.med.upenn.edu
Rui Xiao, PhD,Assistant Professor of Biostatistics,rxiao@mail.med.upenn.edu
Sharon Xiangwen Xie, Ph.D.,Associate Professor of Biostatistics,sxie@mail.med.upenn.edu
Dawei Xie, PhD,Assistant Professor of Biostatistics,dxie@upenn.edu
Wei (Peter) Yang, Ph.D.,Assistant Professor of Biostatistics,weiyang@mail.med.upenn.edu"""

with open('faculty.csv', 'w') as f:
    f.write(facultycsv)

# No pandas for all these solutions
# REGEX
# Function to read in a csv file, return dict (keys = degrees, values = frequencies)
# Use regular expressions so, for example 'PhD' and 'Ph.D.' are the same
def count_degrees(csv_file_name):
    with open(csv_file_name) as f:
        faculty = [lines.strip().split(',') for lines in f]
    deg_idx = faculty[0].index(' degree')
    deg_lists = [x[deg_idx].strip().split(' ') for x in faculty[1:]]
    all_degs = [re.sub('[.]', '', x) for strings in deg_lists for x in strings]
    return {i: all_degs.count(i) for i in all_degs}

# DICT, READFILE
# Function to read in a csv file, return dict (keys = titles, values = frequencies)
# Need to take care of an unintentional typo
def count_titles(csv_file_name):
    valid_titles = ['Assistant Professor of Biostatistics',
        'Associate Professor of Biostatistics',
        'Professor of Biostatistics']
    
    with open(csv_file_name) as f:
        faculty = [lines.strip().split(',') for lines in f]
    title_idx = faculty[0].index(' title')
    all_titles = [x[title_idx] for x in faculty[1:]]
    
    invalid = [(i,x) for i,x in enumerate(all_titles) if x not in valid_titles]
    for i in invalid:
        if 'Assistant' in i[1]:
            all_titles[i[0]] = 'Assistant Professor of Biostatistics'
        elif 'Associate' in i[1]:
            all_titles[i[0]] = 'Associate Professor of Biostatistics'
        else:
            all_titles[i[0]] = 'Professor of Biostatistics'
    
    return {i: all_titles.count(i) for i in all_titles}

# REGEX
# Function to read in a csv file, return list of emails
def emails(csv_file_name):
    # regex solution
    l_new = []
    # pattern = re.compile(r'[a-zA-Z0-9.%_-]+@[a-zA-Z0-9.%_-]+\.[a-zA-Z]')
    pattern = re.compile(r'[a-zA-Z0-9.%_-]+@[a-zA-Z0-9.%_-]+')
    
    with open(csv_file_name) as f:
        faculty = [lines.strip().split(',') for lines in f]
    for row in faculty:
        for item in row:
            if re.match(pattern, item):
                l_new.append(item)
    return l_new
    
    # no regex solution
    #email_idx = faculty[0].index(' email')
    #return [x[email_idx] for x in faculty[1:]]

# REGEX
# Function that given a list of emails, return unique email domains
def unique_domains(emails):
    #all_domains = [re.search(r'([a-zA-Z0-9.%_-]+)@([a-zA-Z0-9.%_-]+\.[a-zA-Z]+)',
    #                         x).group(2) for x in emails]
    all_domains = [re.search(r'([a-zA-Z0-9.%_-]+)@([a-zA-Z0-9.%_-]+)',
                             x).group(2) for x in emails]
    return list(set(all_domains))

# WRITE TO CSV
# Function that given a list of emials, writes to a file called emails.csv
def write_to_csv(list_of_emails):
    with open('emails.csv', 'w') as f:
        f.write('list_of_emails\n')
        for lines in list_of_emails:
            f.write(lines)
            f.write('\n')

# DICT
# Function which reads in a csv file and returns a dict (keys=last name, value=row)
# If multiple entries for each last name, should be reflected in dict
def get_dict():
    d = {}
    
    with open('faculty.csv') as f:
        faculty = [lines.strip().split(',') for lines in f]
    
    name_idx = faculty[0].index('name')
    last_names = [x[name_idx].split(' ')[-1] for x in faculty[1:]]
    
    for i in range(len(last_names)):
        faculty[i+1][name_idx] = last_names[i]
    fac_info = [tuple(x) for x in faculty[1:]]
    
    for i in fac_info:
        if i[name_idx] not in d: 
            d[i[name_idx]] = [list(i[1:])]
        else: 
            d[i[name_idx]].append(list(i[1:]))
    return d

# DICT
# Function which reads in a csv file and returns a dict
# Keys = tuple of name, Value = rows
# Should be a unique row per tuple
def get_dict2():
    
    d = {}
    
    with open('faculty.csv') as f:
        faculty = [lines.strip().split(',') for lines in f]
    name_idx = faculty[0].index('name')
    
    names = [tuple(x[name_idx].split(' ')) for x in faculty[1:]]
    
    for i in range(len(names)):
        faculty[i+1][name_idx] = names[i]
    
    for i in faculty[1:]:
        d[i[name_idx]] = i[1:]
    return d
