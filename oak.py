#!/usr/bin/env python3

import csv
import json
import os
import re
import sys

from rich.console import Console
from rich.table import Table

def main():
  print(sys.argv)

  root = sys.argv[1]

  sets = {}
  sets_path = os.path.join(root, 'sets', 'en.json')
  for s in json.load(open(sets_path)):
    sets[s['id']] = s

  # sets = json.load(open(sys.argv[1]))
  #
  # table = Table(title="Pokémon Sets")
  # table.add_column("ID")
  # table.add_column("Name")
  # for s in sets:
  #   table.add_row(s['id'], s['name'])
  #
  # console = Console()
  # console.print(table)


  set_id = sys.argv[2]
  s = sets[set_id]

  print(set_id)

  cards = {}
  cards_path = os.path.join(root, 'cards', 'en', f'{set_id}.json')
  print(cards_path)
  for c in json.load(open(cards_path)):
    card_number = int(re.search(f'{set_id}\-(\d+)', c['id']).group(1))
    cards[card_number] = c

  with open(f'{set_id}.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Set', 'ID', 'Number', 'Type', 'Rarity', 'Name', 'Quantity'])
    for card_number in sorted(list(cards.keys())):
      card = cards[card_number]
      if card['supertype'] == 'Pokémon':
        card_type = card['types'][0]
      elif 'subtypes' in card:
        card_type = card['subtypes'][0]
      else:
        card_type = None

      #print(cards[i])
      csvwriter.writerow([s['name'], card['id'], card_number, card_type, card['rarity'], card['name'], None])






if __name__ == '__main__':
  main()
