#!/usr/bin/env python3
"""Discord birthday wish scheduler"""
import argparse
def main():
 p=argparse.ArgumentParser(description="Discord birthday wish scheduler")
 p.add_argument("--version",action="store_true")
 args=p.parse_args()
 if args.version:print("birthday-bot v0.1.0");return
 print(f"[22:56] birthday-bot ready")
if __name__=="__main__":main()
