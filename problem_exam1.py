from collections import  deque

eggs = deque([int(x) for x in input().split(", ")])
papers = [int(x) for x in input().split(", ")]
box = 0
while len(eggs) and len(papers):
    piece_papier = papers.pop()
    piece_egg = eggs.popleft()
    if piece_egg == 13 or piece_egg == -13:
        papers.append(piece_papier)
        first = papers.pop(0)
        last = papers.pop(-1)

        papers.insert(0, last)
        papers.append(first)
        continue
    if piece_egg <= 0:
        papers.append(piece_papier)
        continue
    if piece_egg + piece_papier <= 50:
        box += 1
        continue
if box:
    print(f"Great! You filled {box} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if  len(eggs):
    print(f"Eggs left: {(', '.join(map(str, eggs)))}")
if len(papers):
    print(f"Pieces of paper left: {(', '.join(map(str, papers)))}")
