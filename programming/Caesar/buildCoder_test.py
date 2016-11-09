from caesar import *
#from buildCoderReady import *
data = Caesar()

print "+++ START TEST 1 {",
print data.build_coder(7) == {'A': 'H', 'C': 'J', 'B': 'I', 'E': 'L', 'D': 'K', 'G': 'N', 'F': 'M', 'I': 'P', 'H': 'O', 'K': 'R', 'J': 'Q', 'M': 'T', 'L': 'S', 'O': 'V', 'N': 'U', 'Q': 'X', 'P': 'W', 'S': 'Z', 'R': 'Y', 'U': 'B', 'T': 'A', 'W': 'D', 'V': 'C', 'Y': 'F', 'X': 'E', 'Z': 'G', 'a': 'h', 'c': 'j', 'b': 'i', 'e': 'l', 'd': 'k', 'g': 'n', 'f': 'm', 'i': 'p', 'h': 'o', 'k': 'r', 'j': 'q', 'm': 't', 'l': 's', 'o': 'v', 'n': 'u', 'q': 'x', 'p': 'w', 's': 'z', 'r': 'y', 'u': 'b', 't': 'a', 'w': 'd', 'v': 'c', 'y': 'f', 'x': 'e', 'z': 'g'},
print "} END TEST 1 +++\n"

print "+++ START TEST 2 {",
print data.build_coder(1) == {'A': 'B', 'C': 'D', 'B': 'C', 'E': 'F', 'D': 'E', 'G': 'H', 'F': 'G', 'I': 'J', 'H': 'I', 'K': 'L', 'J': 'K', 'M': 'N', 'L': 'M', 'O': 'P', 'N': 'O', 'Q': 'R', 'P': 'Q', 'S': 'T', 'R': 'S', 'U': 'V', 'T': 'U', 'W': 'X', 'V': 'W', 'Y': 'Z', 'X': 'Y', 'Z': 'A', 'a': 'b', 'c': 'd', 'b': 'c', 'e': 'f', 'd': 'e', 'g': 'h', 'f': 'g', 'i': 'j', 'h': 'i', 'k': 'l', 'j': 'k', 'm': 'n', 'l': 'm', 'o': 'p', 'n': 'o', 'q': 'r', 'p': 'q', 's': 't', 'r': 's', 'u': 'v', 't': 'u', 'w': 'x', 'v': 'w', 'y': 'z', 'x': 'y', 'z': 'a'},
print "} END TEST 2 ++++\n"

print "+++ START TEST 3 {",
print data.build_coder(8) == {'A': 'I', 'C': 'K', 'B': 'J', 'E': 'M', 'D': 'L', 'G': 'O', 'F': 'N', 'I': 'Q', 'H': 'P', 'K': 'S', 'J': 'R', 'M': 'U', 'L': 'T', 'O': 'W', 'N': 'V', 'Q': 'Y', 'P': 'X', 'S': 'A', 'R': 'Z', 'U': 'C', 'T': 'B', 'W': 'E', 'V': 'D', 'Y': 'G', 'X': 'F', 'Z': 'H', 'a': 'i', 'c': 'k', 'b': 'j', 'e': 'm', 'd': 'l', 'g': 'o', 'f': 'n', 'i': 'q', 'h': 'p', 'k': 's', 'j': 'r', 'm': 'u', 'l': 't', 'o': 'w', 'n': 'v', 'q': 'y', 'p': 'x', 's': 'a', 'r': 'z', 'u': 'c', 't': 'b', 'w': 'e', 'v': 'd', 'y': 'g', 'x': 'f', 'z': 'h'},
print "} END TEST 3 +++\n"

print "+++ START TEST 4 {",
print data.build_coder(13) == {'A': 'N', 'C': 'P', 'B': 'O', 'E': 'R', 'D': 'Q', 'G': 'T', 'F': 'S', 'I': 'V', 'H': 'U', 'K': 'X', 'J': 'W', 'M': 'Z', 'L': 'Y', 'O': 'B', 'N': 'A', 'Q': 'D', 'P': 'C', 'S': 'F', 'R': 'E', 'U': 'H', 'T': 'G', 'W': 'J', 'V': 'I', 'Y': 'L', 'X': 'K', 'Z': 'M', 'a': 'n', 'c': 'p', 'b': 'o', 'e': 'r', 'd': 'q', 'g': 't', 'f': 's', 'i': 'v', 'h': 'u', 'k': 'x', 'j': 'w', 'm': 'z', 'l': 'y', 'o': 'b', 'n': 'a', 'q': 'd', 'p': 'c', 's': 'f', 'r': 'e', 'u': 'h', 't': 'g', 'w': 'j', 'v': 'i', 'y': 'l', 'x': 'k', 'z': 'm'},
print "} END TEST 4 +++\n"

print "+++ START TEST 5 {",
print data.build_coder(0) == {'A': 'A', 'C': 'C', 'B': 'B', 'E': 'E', 'D': 'D', 'G': 'G', 'F': 'F', 'I': 'I', 'H': 'H', 'K': 'K', 'J': 'J', 'M': 'M', 'L': 'L', 'O': 'O', 'N': 'N', 'Q': 'Q', 'P': 'P', 'S': 'S', 'R': 'R', 'U': 'U', 'T': 'T', 'W': 'W', 'V': 'V', 'Y': 'Y', 'X': 'X', 'Z': 'Z', 'a': 'a', 'c': 'c', 'b': 'b', 'e': 'e', 'd': 'd', 'g': 'g', 'f': 'f', 'i': 'i', 'h': 'h', 'k': 'k', 'j': 'j', 'm': 'm', 'l': 'l', 'o': 'o', 'n': 'n', 'q': 'q', 'p': 'p', 's': 's', 'r': 'r', 'u': 'u', 't': 't', 'w': 'w', 'v': 'v', 'y': 'y', 'x': 'x', 'z': 'z'},
print "} END TEST 5 +++\n"

print "This test is not valide for PRD! +++ START TEST 6 {",
print data.build_coder(-2) == {'A': 'Y', 'C': 'A', 'B': 'Z', 'E': 'C', 'D': 'B', 'G': 'E', 'F': 'D', 'I': 'G', 'H': 'F', 'K': 'I', 'J': 'H', 'M': 'K', 'L': 'J', 'O': 'M', 'N': 'L', 'Q': 'O', 'P': 'N', 'S': 'Q', 'R': 'P', 'U': 'S', 'T': 'R', 'W': 'U', 'V': 'T', 'Y': 'W', 'X': 'V', 'Z': 'X', 'a': 'y', 'c': 'a', 'b': 'z', 'e': 'c', 'd': 'b', 'g': 'e', 'f': 'd', 'i': 'g', 'h': 'f', 'k': 'i', 'j': 'h', 'm': 'k', 'l': 'j', 'o': 'm', 'n': 'l', 'q': 'o', 'p': 'n', 's': 'q', 'r': 'p', 'u': 's', 't': 'r', 'w': 'u', 'v': 't', 'y': 'w', 'x': 'v', 'z': 'x'},
print "} END TEST 6 +++\n"

print data.build_coder(0)
