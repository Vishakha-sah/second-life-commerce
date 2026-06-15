# Graph Report - second-life-commerce  (2026-06-14)

## Corpus Check
- 31 files · ~429,425 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 238 nodes · 279 edges · 23 communities (20 shown, 3 thin omitted)
- Extraction: 93% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `854483e3`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Backend API Endpoints|Backend API Endpoints]]
- [[_COMMUNITY_Data Schemas|Data Schemas]]
- [[_COMMUNITY_Frontend App Config|Frontend App Config]]
- [[_COMMUNITY_Frontend Node Config|Frontend Node Config]]
- [[_COMMUNITY_Core System Concepts|Core System Concepts]]
- [[_COMMUNITY_Frontend Build Scripts|Frontend Build Scripts]]
- [[_COMMUNITY_Frontend Dev Dependencies|Frontend Dev Dependencies]]
- [[_COMMUNITY_Database Management|Database Management]]
- [[_COMMUNITY_Seller Data|Seller Data]]
- [[_COMMUNITY_AI Agent Logic|AI Agent Logic]]
- [[_COMMUNITY_Product Condition Examples|Product Condition Examples]]
- [[_COMMUNITY_TypeScript Configuration|TypeScript Configuration]]
- [[_COMMUNITY_Frontend Entry Points|Frontend Entry Points]]
- [[_COMMUNITY_Amazon Kiro Tooling|Amazon Kiro Tooling]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]

## God Nodes (most connected - your core abstractions)
1. `compilerOptions` - 17 edges
2. `compilerOptions` - 16 edges
3. `🛍️ Second Life Commerce — AI Circular Economy Engine` - 7 edges
4. `Frontend Implementation Plan: Second Life Commerce` - 6 edges
5. `scripts` - 5 edges
6. `check_image_quality()` - 4 edges
7. `grade_product_image()` - 4 edges
8. `ask_gemini()` - 4 edges
9. `get_questions()` - 4 edges
10. `route_product()` - 4 edges

## Surprising Connections (you probably didn't know these)
- `Clean BIREL Rubber Boot (Red Sole)` --semantically_similar_to--> `Dirty BIREL Rubber Boot (Red Sole)`  [INFERRED] [semantically similar]
  secondlife-backend/your_new_image(1).jpg → secondlife-backend/your_new_image.jpg
- `Clean BIREL Rubber Boot (Red Sole)` --conceptually_related_to--> `Rubber Safety Boot`  [INFERRED]
  secondlife-backend/your_new_image(1).jpg → secondlife-backend/your_new_image.jpg
- `GradeResultProps` --references--> `GradeResponse`  [EXTRACTED]
  frontend/src/components/grading/GradeResult.tsx → frontend/src/services/api.ts
- `ImageAnnotatorProps` --references--> `DamageLocation`  [EXTRACTED]
  frontend/src/components/grading/ImageAnnotator.tsx → frontend/src/services/api.ts
- `QuestionnaireProps` --references--> `QuestionnaireResponse`  [EXTRACTED]
  frontend/src/components/grading/Questionnaire.tsx → frontend/src/services/api.ts

## Import Cycles
- None detected.

## Communities (23 total, 3 thin omitted)

### Community 0 - "Backend API Endpoints"
Cohesion: 0.11
Nodes (18): api_predict_return_regret(), ask_gemini(), calculate_co2_impact(), get_questions(), grade_product(), P1 Dynamic Questionnaire: Invokes real-time contextual targeted query arrays fro, P1 Routing Engine & P3 Human Accountability Queue:     Flags items automaticall, P2 Unique Wow Factor: Behavioral Return Regret Logic. (+10 more)

### Community 1 - "Data Schemas"
Cohesion: 0.20
Nodes (18): AdminQueueResponse, CO2ImpactResponse, DamageLocation, GradeResponse, ImageQuality, ListingsResponse, MarketplaceListing, Question (+10 more)

### Community 2 - "Frontend App Config"
Cohesion: 0.11
Nodes (18): compilerOptions, allowImportingTsExtensions, erasableSyntaxOnly, jsx, lib, module, moduleDetection, moduleResolution (+10 more)

### Community 3 - "Frontend Node Config"
Cohesion: 0.11
Nodes (17): compilerOptions, allowImportingTsExtensions, erasableSyntaxOnly, lib, module, moduleDetection, moduleResolution, noEmit (+9 more)

### Community 4 - "Core System Concepts"
Cohesion: 0.15
Nodes (15): AI Agent Logic, CO2 Impact Display, Damage Annotation Overlay, FastAPI Backend, Google Gemini Flash API, Green Points System, JSON Database, Member A (Lead) (+7 more)

### Community 5 - "Frontend Build Scripts"
Cohesion: 0.12
Nodes (15): dependencies, axios, lucide-react, react, react-dom, @tailwindcss/vite, name, private (+7 more)

### Community 6 - "Frontend Dev Dependencies"
Cohesion: 0.12
Nodes (16): devDependencies, autoprefixer, eslint, @eslint/js, eslint-plugin-react-hooks, eslint-plugin-react-refresh, globals, postcss (+8 more)

### Community 7 - "Database Management"
Cohesion: 0.29
Nodes (6): initialize_db(), Bootstraps the JSON files if they don't exist yet., Safely reads data from a specified JSON file., Safely writes structured data back to the JSON file., read_json(), write_json()

### Community 8 - "Seller Data"
Cohesion: 0.29
Nodes (6): user_rahul, green_points, listings_count, user_sakshi, green_points, listings_count

### Community 9 - "AI Agent Logic"
Cohesion: 0.73
Nodes (5): ask_gemini_with_image(), check_image_quality(), full_image_analysis(), grade_product_image(), safe_parse_json()

### Community 10 - "Product Condition Examples"
Cohesion: 0.83
Nodes (4): BIREL Brand, Rubber Safety Boot, Clean BIREL Rubber Boot (Red Sole), Dirty BIREL Rubber Boot (Red Sole)

### Community 18 - "Community 18"
Cohesion: 0.08
Nodes (24): GradeResultProps, ImageAnnotatorProps, QuestionnaireProps, CO2Impact(), CO2ImpactProps, DecisionCardProps, api, CO2ImpactResponse (+16 more)

### Community 19 - "Community 19"
Cohesion: 0.12
Nodes (15): 🎨 Design System & Aesthetic Constraints (The "Anti-Slop" Mandate), Frontend Implementation Plan: Second Life Commerce, 🏗️ Phase 1: Scaffold & Base Components, 📸 Phase 2: Upload & AI Grading Flow, 📋 Phase 3: Routing & Sustainability, 🤔 Phase 4: Wow-Factor Features, Tailwind Theme Extensions (`tailwind.config.js`), Task 1: Initialize Project & Tailwind (+7 more)

### Community 20 - "Community 20"
Cohesion: 0.18
Nodes (10): 📜 Development Conventions, ⚙️ Feature Priority (Hackathon Roadmap), P1: Must-Have (Day 1), P2: Wow Factor (Day 2), P3: If Time Allows, 🚀 Project Overview, 📂 Project Structure, 🛍️ Second Life Commerce — AI Circular Economy Engine (+2 more)

### Community 21 - "Community 21"
Cohesion: 0.50
Nodes (3): Expanding the ESLint configuration, React Compiler, React + TypeScript + Vite

## Knowledge Gaps
- **99 isolated node(s):** `GradeResponse`, `UserAnswers`, `RegretRequest`, `RedeemRequest`, `green_points` (+94 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `devDependencies` connect `Frontend Dev Dependencies` to `Frontend Build Scripts`?**
  _High betweenness centrality (0.012) - this node is a cross-community bridge._
- **What connects `Bootstraps the JSON files if they don't exist yet.`, `Safely reads data from a specified JSON file.`, `Safely writes structured data back to the JSON file.` to the rest of the system?**
  _107 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Backend API Endpoints` be split into smaller, more focused modules?**
  _Cohesion score 0.11428571428571428 - nodes in this community are weakly interconnected._
- **Should `Frontend App Config` be split into smaller, more focused modules?**
  _Cohesion score 0.10526315789473684 - nodes in this community are weakly interconnected._
- **Should `Frontend Node Config` be split into smaller, more focused modules?**
  _Cohesion score 0.1111111111111111 - nodes in this community are weakly interconnected._
- **Should `Frontend Build Scripts` be split into smaller, more focused modules?**
  _Cohesion score 0.125 - nodes in this community are weakly interconnected._
- **Should `Frontend Dev Dependencies` be split into smaller, more focused modules?**
  _Cohesion score 0.125 - nodes in this community are weakly interconnected._