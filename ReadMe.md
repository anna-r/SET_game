# SET Game

Command line program that automatically plays the card game set

## Background

### SET

The object of the game is to identify a "set" of three cards from 12 cards laid out on the table. Each card has four features which can vary as follows:

 * Symbols: Each card has ovals (Ov), squiggles(Sq), or diamonds (Di) on it
 * Colors: The symbols are red (R), green (G), or purple (P)
 * Number: Each card has one, two, or three symbols on it.
 * Shading: The symbols on are either solid (So), striped (St) or no fill (Nf)

A "set" consists of three cards in which each of the card’s features, looked at one-by-one are the same on each card, or are different on each card. All of the features must separately satisfy this rule. In other words: shape must be either the same on the 3 cards, or different on each of the 3; color must either be the same on the 3 cards, or different on the each, etc.

The dealer shuffles the cards and lays out 12 cards (cards in play). If a set is found, the three cards are removed and another three are pulled from the deck.
If no set is found, three more cards are drawn from the deck and placed on the table for a total of 15 cards.
Play continues until there are no more cards in the deck and no more sets among the cards in play.

## Getting Started

Each time the program runs a new game of SET is played by the program

### Prerequisites

Requires Python 3 or newer

### Running

```
python3 Set.py
```

### Example Output

```
['1_So_R_Ov', '2_So_R_Ov', '3_So_R_Ov', '1_St_R_Ov', '2_St_R_Ov', '3_St_R_Ov', '1_Nf_R_Ov', '2_Nf_R_Ov', '3_Nf_R_Ov', '1_So_R_Di', '2_So_R_Di', '3_So_R_Di', '1_St_R_Di', '2_St_R_Di', '3_St_R_Di', '1_Nf_R_Di', '2_Nf_R_Di', '3_Nf_R_Di', '1_So_R_Sg', '2_So_R_Sg', '3_So_R_Sg', '1_St_R_Sg', '2_St_R_Sg', '3_St_R_Sg', '1_Nf_R_Sg', '2_Nf_R_Sg', '3_Nf_R_Sg', '1_So_G_Ov', '2_So_G_Ov', '3_So_G_Ov', '1_St_G_Ov', '2_St_G_Ov', '3_St_G_Ov', '1_Nf_G_Ov', '2_Nf_G_Ov', '3_Nf_G_Ov', '1_So_G_Di', '2_So_G_Di', '3_So_G_Di', '1_St_G_Di', '2_St_G_Di', '3_St_G_Di', '1_Nf_G_Di', '2_Nf_G_Di', '3_Nf_G_Di', '1_So_G_Sg', '2_So_G_Sg', '3_So_G_Sg', '1_St_G_Sg', '2_St_G_Sg', '3_St_G_Sg', '1_Nf_G_Sg', '2_Nf_G_Sg', '3_Nf_G_Sg', '1_So_P_Ov', '2_So_P_Ov', '3_So_P_Ov', '1_St_P_Ov', '2_St_P_Ov', '3_St_P_Ov', '1_Nf_P_Ov', '2_Nf_P_Ov', '3_Nf_P_Ov', '1_So_P_Di', '2_So_P_Di', '3_So_P_Di', '1_St_P_Di', '2_St_P_Di', '3_St_P_Di', '1_Nf_P_Di', '2_Nf_P_Di', '3_Nf_P_Di', '1_So_P_Sg', '2_So_P_Sg', '3_So_P_Sg', '1_St_P_Sg', '2_St_P_Sg', '3_St_P_Sg', '1_Nf_P_Sg', '2_Nf_P_Sg', '3_Nf_P_Sg']
There are 81 cards in the deck
Current Cards in Play:
['1_Nf_P_Sg', '3_St_P_Sg', '3_Nf_R_Ov', '2_Nf_P_Ov', '1_So_R_Sg', '3_St_G_Di', '2_St_G_Di', '1_So_G_Di', '1_St_G_Ov', '2_Nf_G_Di', '2_So_P_Di', '2_So_G_Sg']
There are 69 cards remaining in the deck
SET found: ['1_Nf_P_Sg', '3_Nf_R_Ov', '2_Nf_G_Di']
Set count: 1
```

The first line is all the cards in the deck; each card follows the convention introduced in the background and is given by (Number)_(Shading)_(Color)_(Symbol).

The computer will use its algorithm to find a set from the twelve or fifteen cards in play, and if a set exists, it'll be displayed, otherwise not set found.
