#! /usr/bin/env python3

import os, sys, platform #Operating System Info
import shutil #File Manipulation Info

#Define Global Scope 
SOURCE = ""
DESTIN = ""

def affirmative(answer):
  if answer.lower() in ("y", "yes"):
    return True
  else:
    return False

def editConfig():
  config = open(".config", "w")
  source = input("[?] What is your source directory? ")
  destin = input("[?] What is your destination directory? ")
  print("SOURCE="+source, file=config)
  print("DESTIN="+destin, file=config)

def parseConfig():
  config = open(".config", "r")
  config = config.readlines() 
  global SOURCE 
  SOURCE = config[0].split("=")[1].strip()
  global DESTIN
  DESTIN = config[1].split("=")[1].strip()

def main():
  print("[!] You are currently working in:" + os.getcwd())
  
  #Edit Config Y/N
  answer = input("[?] Would you like to edit the configuration? (Y/N ")
  if affirmative(answer):
    editConfig()

  #Backup Y/N
  answer = input("[?] Would you like to backup this directory? (Y/N) ")

  if affirmative(answer):
    parseConfig()
    if os.path.exists(DESTIN):
      shutil.rmtree(DESTIN)
    shutil.copytree(SOURCE, DESTIN)
  else:
    print("[X] Function Terminating.")
  return

if __name__ == "__main__":
  main() 
