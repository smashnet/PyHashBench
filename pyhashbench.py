'''
A tiny tool that finds SHA256 hashes starting with a certain amount of zeros for random challenges. I wanted to mess around with my new Pi 3 and see how it behaves under full load ;) Also I feel like writing something ;)

Author: Nicolas Inden
eMail: nico@smashnet.de
XMPP: nico@jabber.pgrp.de
GPG-Key-ID: B2F8AA17
GPG-Key: http://files.smashnet.de/B2F8AA17.asc
GPG-Fingerprint: A757 5741 FD1E 63E8 357D 48E2 3C68 AE70 B2F8 AA17
Date: 17.03.2016
License: MIT License
'''

import hashlib
import random
import time
import string
import multiprocessing
import argparse

current_time_millis = lambda: int(round(time.time() * 1000))

def findHashes((zeroes, count, challenge)):
  zeroes, count, challenge = (zeroes, count, challenge)
  current = 0
  counter = 0
  checkstring = ''.rjust(zeroes,'0')

  random.seed()
  while(current < count):
    current += 1
    
    head = str(random.randint(0,99999999)) + challenge
    res = hashlib.sha256(head).hexdigest()

    if res.startswith(checkstring):
      counter += 1
      print "sha256({0})\t-> {1}".format(head, res)

  return (counter, count)


if __name__ == '__main__':
  cores = multiprocessing.cpu_count()
  print "Found {0} cores!".format(cores)

  aparse = argparse.ArgumentParser(description='Benchmark your CPU calculating SHA256 hashes.')
  aparse.add_argument('--threads', type=int, default=cores, help='Number of threads to be used')
  aparse.add_argument('--zeroes', type=int, default=4, help='Number of heading zeroes a hash must have')
  aparse.add_argument('--hashes', type=int, default=1000000, help='Number of hash tries')
  args = aparse.parse_args()

  print "Using {0} threads!".format(args.threads)
  print "Generating challenge ..."

  challenge = []

  for i in range (0,10):
	  challenge.append(random.choice(string.letters))

  challenge = ''.join(challenge)
  print "\t -> {0}".format(challenge)

  timebefore = current_time_millis()

  p = multiprocessing.Pool(args.threads)
  res = p.map(findHashes, [(args.zeroes, args.hashes/args.threads, challenge) for i in range(0,args.threads)])
  
  timeafter = current_time_millis()
  duration = timeafter - timebefore

  totalFound = 0
  totalTested = 0
  for found,tested in res:
    totalFound += found
    totalTested += tested

  print "Found {0} hashes. Tested {1} hashes using {2} cores.".format(totalFound, totalTested, args.threads)
  print "This took {0:0.3f} seconds.\nBye bye!".format(duration/1000.0)
