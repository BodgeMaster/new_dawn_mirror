#!/usr/bin/env python3

import sys, os


def htmlencode(string):
  outstring = ""
  for char in string:
    if char in ["<", ">", "'", "’", "\"", "&"]:
      replacements = {
        "<": "&lt;",
        ">": "&gt;",
        "'": "&apos;",
        "’": "&apos;",
        "\"": "&quot;",
        "&": "&amp;"
      }
      outstring = outstring + replacements[char]
    elif ord(char)>127:
      outstring = outstring + "&#" + str(ord(char)) + ";"
    else:
      outstring = outstring + char
  return outstring


if len(sys.argv)<3:
  print("Usage: " + sys.argv[0] + " <source file> <destination file>")
  sys.exit(1)

if not os.path.isfile(sys.argv[1]):
  print("Not a file: " + sys.argv[1])
  sys.exit(2)

if os.path.isfile(sys.argv[2]):
  print("File exists: " + sys.argv[2])
  print("Refusing to operate.")
  sys.exit(2)

source_file = open(sys.argv[1], "r", encoding="utf-8")
destination_file = open(sys.argv[2], "w", encoding="ascii")

element_type=""
next_source_line = source_file.readline()
while not next_source_line=="":
  if next_source_line == "\n":
    #TODO: use appropriate end action based on element type
    #TODO: deal with closing nested elements
    destination_file.write("</"+element_type+">\n")
    element_type=""
    next_source_line = source_file.readline()
    continue

  if element_type=="":
    #TODO: determine appropriate element type
    element_type="p"
    destination_file.write("<"+element_type+">\n")

  #TODO: deal with multiple spaces appropriately
  destination_file.write("  " + htmlencode(next_source_line))

  next_source_line = source_file.readline()

  if next_source_line=="" and not element_type=="":
    #TODO: deal with closing nested elements
    destination_file.write("</"+element_type+">\n")
