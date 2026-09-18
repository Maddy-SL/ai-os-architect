# UI/UX & Frontend Standards

Follow these directives when generating frontend code, components, dashboards, and views.

---

## 1. Show Controls, Not Paragraphs
- Never fill dashboard cards with descriptive paragraphs or tutorial text.
- Fill cards with real interactive UI primitives:
  - Segmented tabs
  - Micro status badges & metric pills
  - Toggle switches
  - Avatar stacks
  - Search / filter inputs
  - Action buttons with clear verbs

---

## 2. Palette & Design Tokens
- **Neutral Foundation**: Use Zinc or Slate foundation (`bg-slate-50` light / `bg-slate-950` dark).
- **Contrast**: Never use pure `#000000` text on `#FFFFFF`. Use `text-slate-900` or `text-slate-100`.
- **Single Primary Accent**: Exactly ONE primary accent color per view (`indigo-600`, `violet-600`, or `emerald-600` with <80% saturation).
- **Semantic Status**: Use standard functional colors for state (`emerald` for success/active, `amber` for warning/pending, `rose` for error/blocked).

---

## 3. Borders & Elevation
- **Hairline Borders**: `border border-slate-200/80 dark:border-slate-800`.
- **Subtle Elevation**: `shadow-sm` on cards and interactive elements. Avoid heavy drop-shadows.
- **Consistent Radius**: `rounded-lg` or `rounded-md` across all cards, buttons, and inputs.

---

## 4. Data Realism
- Use realistic technical names, entity names, and currency figures.
- Never use placeholder strings like "Lorem ipsum", "John Doe", "Company ABC", or "Item 1".
