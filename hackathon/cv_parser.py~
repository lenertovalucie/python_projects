#! /usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Script to parse PDF resumes, create a csv file containing info
#hackyourstart - Python hacketon(19.-20.11.2016)
"""

import re
import string
import os
import logging
import argparse
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine


logging.basicConfig(level=logging.ERROR)


def make_printable(text):
    result = ""
    for letter in text:
        if letter in string.printable:
            result += letter
    return result


def pdf_to_str(file):
    fp = open(file, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize('')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    text = ""
    for page in doc.get_pages():
        interpreter.process_page(page)
        layout = device.get_result()
        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                text += lt_obj.get_text()

    return make_printable(text).strip()


def find_email(text):
    pattern = "[^\s@]+@[^@\s]+\.[^@\s]+"

    emails = ";".join(re.findall(pattern, text))

    return emails


def find_phone_number(text):
    pattern = "[\d\-\(\) \+]{9,}"

    result = (re.findall(pattern, text))
    final = []

    for number in result:
        number = number.strip()
        if not "  " in number:
            number = number.replace(" ", "")
            number = number.replace("-", "")
            if len(number) >= 9:
                final.append(number)

    return ";".join(final)


def find_name(text):
    pattern = r"\W*([A-Z][A-Za-z]*\.? (?:[A-Z][A-Za-z]*\.? ?){0,3}[A-Z][A-Za-z]*)\s?"
    name = re.findall(pattern, text)
    if name:
        return (name[0])
    else:
        return "N/A"


def find_year(line):
    pattern = r"([(19)(20)]\d{3})"
    year = re.findall(pattern, line)
    if year:
        return year
    return False


def find_jobs_and_education(text):
    lines = text.splitlines()
    resultList = []

    for i, line in enumerate(lines):
        if find_year(line):
            resultTuple = find_year(line), i
            resultList.append(resultTuple)
    sortedResultList = sorted(resultList)
    lineWithLatestYear = sortedResultList[-1][1]

    if lineWithLatestYear < len(lines) - 1:
        yearPlusOneLine = lines[lineWithLatestYear] + ";" + lines[lineWithLatestYear + 1]
    else:
        yearPlusOneLine = lines[lineWithLatestYear] + ";"

    return yearPlusOneLine

def other_section_detected(line):
    keywordsEducation = ["Education", "University", "Qualification", "Training", "Courses"]
    keywordsWork = ["Experience", "Positions", "Work", "Job", "Professional", "Profession"]
    keywordsOther = ["Publications", "Skills", "Reference"]

    for k in keywordsEducation:
        if k.lower() in line.lower():
            return "Education"

    for k in keywordsWork:
        if k.lower() in line.lower():
            return "Work"

    for k in keywordsOther:
        if k.lower() in line.lower():
            return "Other"

    return False


def separate_section(text):
    lines = text.splitlines()
    sections = {}
    currentSectionName = "ContactInformation"
    currentSectionContent = ""

    for line in lines:
        if (other_section_detected(line)):
            if currentSectionName in sections:
                sections[currentSectionName] += currentSectionContent
            else:
                sections[currentSectionName] = currentSectionContent
            currentSectionContent = ""
            currentSectionName = other_section_detected(line)
            currentSectionContent += line + "\n"
        else:
            currentSectionContent += line + "\n"

    return sections


def create_resume_output(list_of_dict, file_name):
    header = []
    for row in list_of_dict:
        for k in row:
            if k not in header:
                header.append(k)
    data = []
    for row in list_of_dict:
        row_list= [row.get(x, "N/A") for x in header]
        row_list = [(i if i else "N/A") for i in row_list]
        data.append(row_list)

    return write_csv(data,header,file_name)


def write_csv(data, header, file_name):
    header = [str(s).replace("'","").replace(",","") for s in header]
    header = ['"{}"'.format(s) for s in header]
    clean_data = []
    for row in data:
        clean_data.append([str(s).replace("'","").replace(",","") for s in row])

    result = ",".join(header) + "\n"
    for row in clean_data:
        result += (",".join(['"{}"'.format(s) for s in row]))
        result += "\n"

    if not file_name:
        print (result)
    else:
        with open(file_name, "w") as f:
            f.write(result)


def main():
    parser = argparse.ArgumentParser(description='Script to parse PDF resumes, create a csv file containing info')
    parser.add_argument('path_to_cvs', help='Path to cvs')
    parser.add_argument('--output_file_name','-o',default = None, help='Name of output file')

    args = parser.parse_args()
    input, output = args.path_to_cvs, args.output_file_name

    dir_list =(os.listdir(input))

    final_list = []

    for file in dir_list:
        cvs_dict = dict()
        pdf_text = pdf_to_str(input + file)
        sectionsDictionary = separate_section(pdf_text)
        cvs_dict["name"] =  find_name(sectionsDictionary['ContactInformation'])
        cvs_dict["email"] =  find_email(sectionsDictionary['ContactInformation'])
        cvs_dict["phone_number"] =  find_phone_number(sectionsDictionary['ContactInformation'])
        cvs_dict["last_education"] = find_jobs_and_education(sectionsDictionary['Education'])
        cvs_dict["last_profession"] = find_jobs_and_education(sectionsDictionary['Work'])

        final_list.append(cvs_dict)

    create_resume_output(final_list, output)


if __name__ == "__main__":
    main()
