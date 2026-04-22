# Supply Chain Transparency & Price Transmission Model

## Description
This project analyzes inefficiencies in the coffee supply chain and quantifies how value is lost between farmers and export markets. It uses network modeling and simulation techniques to identify bottlenecks and optimize value distribution.

## Problem
Smallholder farmers capture a limited share of export value due to:
- Weak price transmission from global markets
- High first-mile logistics costs
- Multiple intermediaries extracting value
- Lack of transparency in supply chain flows

## Solution
We developed a system-level analytical model:

- Mapped the supply chain as a directed network (graph model)
- Modeled price transmission using elasticity estimates
- Simulated risks using Monte Carlo methods
- Created cost-density metrics to identify inefficiencies

## Recommendation
- Optimize first-mile logistics to reduce cost inefficiencies
- Reduce redundant intermediaries in the supply chain
- Improve transparency of price signals reaching farmers

## Tech Stack
- Python (Pandas, NumPy, SciPy)
- Graph Modeling: NetworkX
- Simulation: Monte Carlo methods
- Visualization: Plotly
- Deployment: Streamlit
