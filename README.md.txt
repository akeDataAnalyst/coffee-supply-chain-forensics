# Supply Chain Transparency & Price Transmission Model
**Subtitle:** Quantifying the "Value Leak" in the Ethiopian Coffee Frontier

## Project Description
This repository contains a **Supply Chain Forensic Engine** designed to identify structural "value leaks" in the Ethiopian coffee export corridor. In the current economic climate of 2026, smallholder farmers often capture less than 50% of the export value. This project uses Graph Theory and Monte Carlo simulations to model the "invisible" logistics costs and information asymmetries that keep farmgate prices suppressed, even when global benchmarks surge.

## The Problem: "The Invisible Leak"
In the Ethiopian coffee chain, value is extracted at every node (Collector ? Union ? Exporter). 
- **Price Asymmetry:** When the New York C-Market rises, the "transmission" to the farmgate is slow and inefficient.
- **First-Mile Friction:** Rural logistics segments (e.g., Gera to Telila) exhibit costs per kilometer up to **6x higher** than international shipping segments.
- **Structural Bottlenecks:** Centralized warehouses create single points of failure where delays lead to quality degradation and financial loss.

## The Solution: A Logistics Frontier Pipeline
I developed a 5-phase analytical approach to move from raw data to strategic intervention:

1.  **Network Mapping:** Created a Directed Acyclic Graph (DAG) of the real-world Jimma-Addis-Djibouti corridor using actual infrastructure nodes (Telila WS, Kality Mill, SGTD Doraleh).
2.  **Price Transmission Modeling:** Engineered an economic model with a 0.72 Elasticity Coefficient to simulate how price shocks move through the chain.
3.  **Monte Carlo Risk Simulation:** Conducted 1,000 iterations to quantify the impact of fuel volatility and informal leakage.
4.  **Friction Audit:** Developed a "Cost Density" metric ($/km) to pinpoint the exact locations of inefficiency.
5.  **Optimization Dashboard:** A Streamlit-based "Command Center" for simulating ROI on logistics interventions.

## Strategic Recommendation
The analysis confirms a -0.96 correlation between transport costs and farmer income. 
- **Action:** By bypassing redundant aggregation nodes and optimizing the "First-Mile" route, we can increase the farmer’s share from 47.75% to 52.59%.
- **Financial Impact:** This represents a realized income increase of $483.82 per tonne for smallholder families without requiring a change in global market prices.

## Tech Stack
- **Graph Theory:** `NetworkX` (Topology & Flow)
- **Mathematical Simulation:** `SciPy`, `NumPy` (Elasticity & Monte Carlo)
- **Data Engineering:** `Pandas` (ETL & Reconciliation)
- **Visualization:** `Plotly` (Interactive Gauges & Heatmaps)
- **Deployment:** `Streamlit` (Strategic Decision Tool)

---
**Developed by Aklilu Abera Dana | Supply Chain Data Analyst**