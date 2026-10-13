#!/usr/bin/env python3
"""Find which region name a scoped MeshCore packet was sent under.

A scoped flood carries a 16-bit transport code. The firmware computes it as the first two
bytes of HMAC-SHA256(key, payload-type byte + payload), where key is the first 16 bytes of
SHA-256("#" + region name). The code depends on the packet's own bytes, so there is no table
to look up: you try candidate names and keep the ones that reproduce the code.

Usage:
  python3 tools/decode_scope.py HEX [name ...]
  python3 tools/decode_scope.py --file src/packets.json [name ...]

With no names given, a short built-in list of SoCal candidates is tried. A 16-bit code matches
a wrong name by chance about once in 65,536 tries per name, so treat a single match against a
long list as a lead and look for the same name on several packets from the same sender.

Standard library only. MIT license.
"""
import hashlib
import hmac
import json
import sys

CANDIDATES = """socal us west california ca
lax lgb sna ont san oxr sba psp bfl fat mce
la oc sd ie sb vta
santabarbara ventura losangeles orangecounty sanbernardino riverside imperial sandiego
conejovalley simivalley coachellavalley""".split()


def parse(raw_hex):
    b = bytes.fromhex(raw_hex.strip())
    route = b[0] & 0x03
    ptype = (b[0] >> 2) & 0x0F
    if route not in (0, 3):
        raise ValueError("not a transport-route packet, so it carries no scope code")
    codes = (b[1:3].hex().upper(), b[3:5].hex().upper())
    n = b[5]
    path_len = ((n >> 6) + 1) * (n & 0x3F)
    return ptype, codes, b[6 + path_len:]


def code_for(name, ptype, payload):
    key = hashlib.sha256(("#" + name).encode()).digest()[:16]
    mac = hmac.new(key, bytes([ptype]) + payload, hashlib.sha256).digest()
    code = mac[:2]
    if code == b"\x00\x00":      # the firmware moves the two reserved values to a neighbor
        code = b"\x01\x00"
    elif code == b"\xff\xff":
        code = b"\xfe\xff"
    return code.hex().upper()


def decode(raw_hex, names):
    ptype, codes, payload = parse(raw_hex)
    return codes, [n for n in names if code_for(n, ptype, payload) == codes[0]]


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[1] == "--file":
        packets = [(p["label"], p["hex"]) for p in json.load(open(argv[2], encoding="utf-8"))]
        names = argv[3:]
    else:
        packets = [("packet", argv[1])]
        names = argv[2:]
    names = names or CANDIDATES
    for label, raw in packets:
        codes, hits = decode(raw, names)
        print(f"{label}: code {codes[0]}, second code {codes[1]}, matches: {', '.join(hits) if hits else 'none of ' + str(len(names)) + ' names tried'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
