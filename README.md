# Trip Planner — Buildathon Prototype

A working, click-through prototype of the trip planning app — built as static HTML/CSS/vanilla JS, no build step, no backend required to demo.

## What's real vs. mocked

This is a **prototype for user testing**, not a finished product. Being upfront about what's genuinely functional vs. simulated:

**Fully working, real logic:**
- **Navigation** — one drawer, one back button, both living in the shell only (not duplicated per page), so they can't get out of sync with whatever screen is showing
- **Solo vs. Group trips genuinely differ** — Brainstorming, To-Do, Wallet, and Budget all branch real UI/logic based on trip type, not just a label
- **Resume-trip flow** — leaving a trip (Home, Bucketlist, etc.) doesn't end it; Home shows a real "Resume trip" card with your trip's name and picks up exactly where you left off
- **Bucketlist** — collision-free card placement (phyllotaxis spacing algorithm), photo upload, notepad per destination, push-to-trip flow, country selected from a real static list of world countries (not geocoded — see note below)
- **Brainstorming + The Plan + AI Chat** — all three share one instance (not three separate copies), so the shortlist is genuinely shared across them: an AI suggestion, a shared link, and a manual add all land in the same list
- **Budget** — real debt-simplification algorithm for "who owes whom," three-way expense splits, **live currency rates** fetched from the Frankfurter API (free, no key) covering 30+ currencies
- **Home personalization** — "Popular in ___" reads your real Bucketlist data: matches one of 4 hand-curated countries (Japan, Indonesia, Portugal, Sri Lanka) when possible, otherwise honestly shows your own saved places instead of fabricating recommendations for countries we haven't researched. Cards reuse whatever photo you uploaded to that place in Bucketlist — same image, not fetched separately.
- **Click-to-edit from Home** — tapping a "From your Bucketlist" card jumps straight to that exact card in Bucketlist, already open for editing. Only your own entries are clickable; the curated cards aren't, since you never created those.
- **Following/Saved** — itinerary-only sharing (destinations and days), deliberately never includes who else was on the trip

**Intentionally simulated (flagged in-app or here):**
- AI Chat's day-restructuring and "suggest a place" replies are simple keyword triggers, not a real LLM call
- FAQ/SOS has real, researched content for 9 countries (Indonesia, Thailand, Singapore, Malaysia, Vietnam, UAE, Switzerland, Japan, Georgia) — local essential apps are verified via current search, not guessed. Safety notes are general, reasonable travel knowledge, honestly marked unverified (not sourced from a real local reporting network yet). A few embassy emergency numbers are directly verified from official Indian government sources (Thailand, UAE); others honestly link to India's official MEA emergency contacts list rather than showing an unverified number. Everywhere else in the world still has no content yet — this is a deliberately bounded, high-value set, not full global coverage
- Wallet document "uploads" and everything else only live in memory — nothing survives a page reload
- Following's shared itineraries are seed data standing in for real followed users
- No real backend or accounts yet — this is a single-user simulation; group features (polls, opt-ins, shortlist) are demoed as if you're the only real participant

**A deliberate reversal worth knowing about**: an earlier version of Bucketlist tried live geocoding (first Nominatim, then Wikipedia's REST API) to auto-detect a place's country from free text. Both failed real browser CORS testing — not occasionally, consistently. Rather than ship something that silently fails for some users, this was replaced with a static dropdown of world countries: no network call, can't fail, works offline. One extra tap, in exchange for actually working.

## Structure

```
index.html          — app shell: drawer, back button, tab bar, iframe-based navigation
pages/
  home.html          — landing, create-trip flow, resume-trip card, Bucketlist personalization
  trip.html          — Brainstorming + AI Chat + The Plan (one shared instance, three internal views)
  todo.html          — To-Do (solo/group aware)
  wallet.html        — Wallet (solo/group aware)
  budget.html        — Budget (solo/group aware, live FX rates)
  faq.html           — FAQ, Helplines, SOS
  bucketlist.html    — Someday/Bucketlist vision board
  following.html     — Following feed + Saved itineraries (one shared instance, two internal views)
  profile.html       — Profile (sign-in stub, pending real accounts)
```

Each page is a fully self-contained HTML file (own `<style>` and `<script>`) — this avoids ID/function-name collisions that would happen if everything were merged into one script scope. The shell (`index.html`) ties them together with a tab bar and iframes. Pages that need to talk to each other (Bucketlist → Home for personalization, Home → Bucketlist for click-to-edit) do it via `postMessage` through the shell, which is the single source of truth for navigation state.

## Running locally

No build step for the real app. Any static file server works:

```bash
cd tripapp
python3 -m http.server 8000
# open http://localhost:8000
```

(Opening `index.html` directly via `file://` mostly works too, but some browsers restrict iframe/fetch behavior on `file://` — a local server is more reliable, and required for Budget's live FX rates to load.)

### Building the single-file preview

`build_preview.py` bundles every page into one self-contained `preview.html` (useful for sharing a quick link without a server). Rebuild it after any changes to `pages/*.html` or `index.html`:

```bash
python3 build_preview.py
```

## Deploying — two easy options, no build step needed

**Option A — GitHub Pages**
1. Push this repo to GitHub (see below)
2. Repo Settings → Pages → Source: deploy from branch `main`, folder `/ (root)`
3. Your app is live at `https://<username>.github.io/<repo-name>/`

**Option B — Netlify drop**
1. Go to [app.netlify.com/drop](https://app.netlify.com/drop)
2. Drag the whole `tripapp` folder in
3. Live instantly, no account required for a quick test link

## Pushing to your own GitHub

This folder is already a git repo with commit history. From inside it:

```bash
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git branch -M main
git push -u origin main
```

(Create the empty repo on GitHub first — github.com → New repository — without initializing a README, so there's no merge conflict.)

## Known limitations worth telling testers about

- Exchange rates need internet — Budget will show a smaller offline fallback currency set without a connection
- Everything resets on reload — there's no persistence layer yet (Firebase sign-in is the planned next step)
- This is a single-user simulation — group features (polls, opt-ins, shortlist) are demoed as if you're the only real participant, with seed data standing in for the rest of the group
- The logo and "TripApp" name in the top bar are explicitly placeholder — a real name/mark decision is still pending
