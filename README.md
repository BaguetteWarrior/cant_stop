# Can't Stop – Algorithm Competition

## Overview

This project was developed as part of an academic programming competition. The objective was to design an algorithm capable of playing **Can't Stop**, a strategic dice-based board game, and compete against algorithms developed by other students.

The goal was to build an agent that could make intelligent decisions, maximize its chances of winning, and outperform competing implementations.

## The Game

Can't Stop is a push-your-luck board game based on rolling four dice and combining them into pairs. Each combination determines which numbered paths a player can advance on.

Players must decide:
- Which dice combination to play.
- Whether to continue rolling or stop and secure their progress.
- How to balance risk-taking against the possibility of losing temporary progress.

The first player to complete three paths wins the game.

## Algorithm & Strategy

My algorithm uses probability calculations and strategic decision-making to optimize its moves.

### 1. Probability Analysis

The algorithm calculates the probabilities of obtaining different dice combinations by enumerating all possible outcomes of four six-sided dice.

It uses these probabilities to estimate how likely each numbered path is to be selected in future rolls.

### 2. Path Prioritization

The algorithm evaluates the progress made on each active path relative to its total length.

It prioritizes paths based on their relative progression, allowing it to focus on the most promising opportunities rather than choosing moves randomly.

### 3. Risk Management

One of the main challenges in Can't Stop is deciding when to stop and secure progress or continue rolling.

The algorithm evaluates the expected value of continuing by considering:
- The probability of advancing on each active path.
- The number of times each path has already been selected during the current turn.
- The potential loss of temporary progress if no valid advancement is possible.

It then compares the expected value of continuing against the value of stopping to make its decision.

### 4. Move Selection

When choosing a dice combination, the algorithm prioritizes combinations containing the numbered paths it considers most valuable.

This combines path prioritization with probability-based risk management to make decisions throughout the game.

## Tournament System

The project also includes a tournament framework to evaluate algorithms against one another.

The tournament system:
- Runs multiple games between competing algorithms.
- Tests each algorithm against every other participant.
- Tracks wins and scores.
- Displays the results dynamically using Matplotlib.

This makes it possible to compare different strategies over hundreds of games rather than relying on individual matches.

## Technologies & Concepts

- **Language:** Python
- **Libraries:** Matplotlib
- **Probability:** Enumeration of possible dice outcomes and probability calculations.
- **Algorithms:** Heuristic decision-making and expected-value evaluation.
- **Game Theory:** Risk management and strategic optimization.
- **Simulation:** Automated matches and tournament evaluation.

## Project Context

Developed as part of a student programming competition in which independently implemented algorithms competed against each other in Can't Stop.

The project provided practical experience in algorithm design, probabilistic reasoning, strategic decision-making, and competitive programming.
