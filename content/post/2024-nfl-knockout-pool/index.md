---
title: "Using Statistical Modeling to Win a NFL Knockout Pool"
subtitle: "How simulated annealing optimization can give you an edge in your office pool"
author: "Nicholas F. Brazeau"
date: 2024-11-13
categories: ["Statistics", "Sports", "Fun"]
tags: ["NFL", "optimization", "simulation", "R"]
draft: false
---

## Introduction

Admittedly, I am a terrible sports fan. However, I do enjoy competition and the opportunity to participate in a little "smack talk" with family and friends.

Every year, family, friends, and folks from my childhood community come together to play a game of **NFL Pool Knockout**. The rules are deceptively simple:

- Each participant picks **one NFL team each week**
- If your team **wins**, you advance to the next week
- If your team **loses or ties**, you're eliminated
- Each team can only be selected **once during the season**
- Last person standing wins

Sounds simple, right? The strategy, however, is surprisingly complex.

---

## The Complexity Problem

At first glance, you might think: "Just pick the best team each week!" But there's a catch—once you use a team, you can't use them again. This creates a classic **resource allocation problem** under uncertainty.

Consider the mathematical scale:
- 18 weeks in an NFL season
- 32 teams available
- Number of possible strategies: **18! ≈ 6.4 × 10¹⁵**

That's 6.4 quadrillion possible ways to order your picks. You can't evaluate them all.

### The Strategic Dilemma

Should you:
- **Burn your best teams early** to guarantee survival through the early weeks?
- **Save elite teams for late** when fewer opponents remain?
- **Balance risk across the season** with a mix of safe and risky picks?

The answer depends on:
1. **Team strength** — Who's actually good?
2. **Schedule strength** — Who do they play each week?
3. **Bye weeks** — When are teams not playing?
4. **Opponent strategy** — What are others likely to pick?
5. **Variance** — How unpredictable are the outcomes?

This is where statistics comes in.

---

## The Statistical Approach

I built an R package called [`nflKOSA`](https://github.com/nickbrazeau/nflKOSA) (NFL Knockout Simulated Annealing) to solve this optimization problem. The package focuses on the core challenge: **given win probabilities for each matchup, find the optimal sequence of team selections**.


### Simulated Annealing Optimization

Once we have win probabilities for every matchup, we need to find the optimal sequence of team selections across 18 weeks. This is a **combinatorial optimization problem** that's too large for brute force.

**Simulated Annealing** is a probabilistic optimization algorithm inspired by metallurgy (the process of slowly cooling metal to minimize defects). Here's how it works:

1. Start with a random strategy (sequence of team picks)
2. Calculate the "energy" (expected number of weeks survived)
3. Propose a small change (swap two team selections)
4. If the new strategy is better, accept it
5. If the new strategy is worse, sometimes accept it anyway (with probability based on "temperature")
6. Slowly reduce the "temperature" to converge on an optimum

The key insight: **accepting worse solutions early prevents getting stuck in local optima.** By occasionally accepting suboptimal moves, the algorithm can escape local peaks and find the global maximum.

### Evaluating Strategies

Each strategy is evaluated by calculating the **expected weeks survived**. For a given sequence of team picks, this is:

```
Expected Weeks = Σ P(survive to week w)
               = Σ Π(win probability for weeks 1 through w)
```

The simulated annealing algorithm maximizes this objective by:
1. Starting with a random team selection sequence
2. Using the `cost()` function to evaluate the strategy (negative expected weeks)
3. Using the `proposal()` function to generate alternative strategies
4. Accepting improvements and occasionally accepting worse solutions
5. Cooling the temperature parameter to converge on the optimum

The optimization returns:
- **Optimal team sequence** — Which team to pick each week
- **Expected survival** — Based on the product of win probabilities
- **Final cost** — Negative expected weeks survived



*Post drafted with assistance from Claude.AI*
