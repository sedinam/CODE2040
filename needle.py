
"""This code is to try and identify a needle in a haystack given an array that represents the haystack 
It returns the index of the needle value
Stage 2 """

def main():
  needle = "BXMmm"
  haystack = ["uyhC4","puF8F","bxqXJ","BXMmm","zB3VY","8la4i","wlIXP","TXwXA","8AJ8I","xaJfW","lSNGM","LpRTz","zaxSi","lMl0I","ydJhS","bRSwZ","iam8A","LxtpR","8DHZE","8MAdi"]
  for i in range(len(haystack)):
      if haystack[i] == needle:
        print i
        return i
main()

