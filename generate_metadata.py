#!/usr/bin/env python3

print("Model directory path (ex. misc/octocat)")
path = input(" :: ")

pathBlocks = path.split("/")

for block in pathBlocks:
    if not block:
        pathBlocks.remove(block)
if pathBlocks[0] == "models":
    pathBlocks = pathBlocks[1:]

print(pathBlocks)
