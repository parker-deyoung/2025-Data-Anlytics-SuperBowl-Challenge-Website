// ── Global Chart.js defaults — dark theme ────────────────────────────────
Chart.defaults.color = '#888888';
Chart.defaults.borderColor = 'rgba(255,255,255,0.05)';
Chart.defaults.font.family = 'Inter, system-ui, sans-serif';
Chart.defaults.font.weight = '300';

const GOLD      = '#c9a84c';
const GOLD_MID  = 'rgba(201,168,76,0.5)';
const GOLD_DIM  = 'rgba(201,168,76,0.28)';
const MUTED_BAR = 'rgba(240,240,240,0.18)';

// Shared axis style helpers
const xGrid  = { color: 'rgba(255,255,255,0.04)' };
const xTick  = { color: '#666', font: { size: 11 } };
const yGrid  = { display: false };
const yTick  = { color: '#aaa', font: { size: 11 } };
const noBorder = { color: 'transparent' };
const legend = (pos = 'bottom') => ({
  position: pos,
  labels: { color: '#888', padding: 16, font: { size: 11 }, boxWidth: 12, boxHeight: 12 },
});

// ── 1. Brand Efficiency — horizontal bar (all 20 brands, avg WES) ─────────
(function () {
  const labels = [
    'Blue Square Alliance', 'Amazon Ring', 'DraftKings', 'Budweiser',
    'State Farm', 'Salesforce', 'SVEDKA Vodka', 'NFL', 'Liquid Death',
    'Instacart', 'Michelob ULTRA', "Levi's", "Lay's", 'Dove', 'OpenAI',
    'Ro', 'Google', 'Wix.com', "Dunkin'", 'Pepsi Zero Sugar',
  ];
  const values = [
    2505.5, 2166.2, 2097.3, 2039.2, 1011.3, 874.7, 854.1, 716.2,
    518.5,  492.8,  464.0,  404.2,  402.9,  375.8, 286.1, 279.8,
    238.1,  237.3,  225.9,  88.1,
  ];
  const colors = values.map(v => v >= 2000 ? GOLD : v >= 700 ? GOLD_MID : GOLD_DIM);

  new Chart(document.getElementById('chartBrandEfficiency'), {
    type: 'bar',
    data: { labels, datasets: [{ label: 'Avg WES / Tweet', data: values, backgroundColor: colors, borderRadius: 3, borderSkipped: false }] },
    options: {
      indexAxis: 'y', responsive: true, maintainAspectRatio: false,
      plugins: { legend: { display: false }, tooltip: { callbacks: { label: c => ` ${c.parsed.x.toLocaleString()} avg WES` } } },
      scales: { x: { grid: xGrid, ticks: xTick, border: noBorder }, y: { grid: yGrid, ticks: yTick, border: noBorder } },
    },
  });
}());

// ── 2. Tweet Timing — donut ───────────────────────────────────────────────
(function () {
  new Chart(document.getElementById('chartTiming'), {
    type: 'doughnut',
    data: {
      labels: ['Hour 3 — Peak', 'Hour 2', 'Hour 1', 'Hour 0'],
      datasets: [{ data: [40984, 4877, 321, 54], backgroundColor: [GOLD, GOLD_MID, GOLD_DIM, 'rgba(201,168,76,0.1)'], borderColor: '#111111', borderWidth: 2, hoverOffset: 8 }],
    },
    options: {
      responsive: true, maintainAspectRatio: false, cutout: '68%',
      plugins: {
        legend: legend(),
        tooltip: { callbacks: { label: c => ` ${c.parsed.toLocaleString()} tweets (${((c.parsed / 46257) * 100).toFixed(1)}%)` } },
      },
    },
  });
}());

// ── 3. Celebrity Flop — two-bar comparison ───────────────────────────────
(function () {
  new Chart(document.getElementById('chartCelebrity'), {
    type: 'bar',
    data: {
      labels: ['Celebrity Mentions', 'Organic Content'],
      datasets: [{ label: 'Avg Weighted Engagement Score', data: [439.9, 1702.8], backgroundColor: [MUTED_BAR, GOLD], borderRadius: 4, borderSkipped: false, maxBarThickness: 100 }],
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: { legend: { display: false }, tooltip: { callbacks: { label: c => ` Avg WES: ${c.parsed.y}` } } },
      scales: { x: { grid: { display: false }, ticks: { color: '#aaa', font: { size: 12 } }, border: noBorder }, y: { grid: xGrid, ticks: xTick, border: noBorder } },
    },
  });
}());

// ── 4. Yell Index — ALL 20 brands, horizontal grouped bars ───────────────
(function () {
  const labels = [
    'Amazon Ring', 'Wix.com', 'Michelob ULTRA', 'Ro', 'Dunkin\'',
    'Dove', 'OpenAI', 'Salesforce', 'Lay\'s', 'NFL',
    'Pepsi Zero Sugar', 'Instacart', 'Liquid Death', 'Blue Square',
    'Budweiser', 'DraftKings', 'Google', 'Levi\'s', 'SVEDKA Vodka', 'State Farm',
  ];
  const allCaps = [179.5, 4.7, 2.3, 3.4, 0.7, 0.4, 0.3, 0.3, 0.2, 0.2, 0.3, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
  const normal  = [ 10.4, 11.1, 1.2, 5.2, 1.0, 9.4, 8.4, 0.8, 1.5, 3.0, 23.7, 1.8, 5.6, 1.5, 1.2, 16.4, 1.9, 4.2, 0.6, 1.1];

  new Chart(document.getElementById('chartYell'), {
    type: 'bar',
    data: {
      labels,
      datasets: [
        { label: 'ALL-CAPS Avg Likes', data: allCaps, backgroundColor: GOLD,     borderRadius: 2, borderSkipped: false },
        { label: 'Normal-Case Avg Likes', data: normal, backgroundColor: GOLD_DIM, borderRadius: 2, borderSkipped: false },
      ],
    },
    options: {
      indexAxis: 'y', responsive: true, maintainAspectRatio: false,
      plugins: { legend: legend(), tooltip: { callbacks: { label: c => ` ${c.dataset.label}: ${c.parsed.x} avg likes` } } },
      scales: { x: { grid: xGrid, ticks: xTick, border: noBorder }, y: { grid: yGrid, ticks: { color: '#aaa', font: { size: 10 } }, border: noBorder } },
    },
  });
}());

// ── 5. Audience Archetype Scatter — 20 brands, 4 quadrants ───────────────
(function () {
  // {x: visual_content_rate_pct, y: flesch_kincaid_grade, label}
  // Quadrant thresholds: x ≥ 25 = high visual, y ≥ 10 = high reading
  const pts = [
    { x: 18.1, y: 7.6,  label: 'Amazon Ring' },
    { x: 16.2, y: 9.0,  label: 'Blue Square' },
    { x: 16.0, y: 10.6, label: 'Budweiser' },
    { x: 13.9, y: 8.2,  label: 'Dove' },
    { x: 50.6, y: 10.1, label: 'DraftKings' },
    { x: 23.1, y: 8.9,  label: "Dunkin'" },
    { x: 12.7, y: 7.4,  label: 'Google' },
    { x: 16.2, y: 9.0,  label: 'Instacart' },
    { x: 15.5, y: 8.5,  label: "Lay's" },
    { x: 26.4, y: 9.2,  label: "Levi's" },
    { x: 15.4, y: 8.1,  label: 'Liquid Death' },
    { x: 6.8,  y: 9.9,  label: 'Michelob ULTRA' },
    { x: 22.2, y: 7.7,  label: 'NFL' },
    { x: 13.4, y: 8.8,  label: 'OpenAI' },
    { x: 7.2,  y: 5.8,  label: 'Pepsi Zero Sugar' },
    { x: 26.5, y: 9.4,  label: 'Ro' },
    { x: 22.3, y: 8.7,  label: 'SVEDKA Vodka' },
    { x: 13.5, y: 8.3,  label: 'Salesforce' },
    { x: 12.2, y: 7.0,  label: 'State Farm' },
    { x: 50.0, y: 6.9,  label: 'Wix.com' },
  ];

  const VIS_THRESHOLD   = 25;  // % visual content
  const READ_THRESHOLD  = 10;  // grade level

  // Classify into 4 named archetypes
  const archetypes = {
    Analyst: { color: GOLD,          points: [] },  // high reading, low visual
    Scholar:  { color: GOLD_MID,     points: [] },  // high reading, high visual
    Reactor:  { color: MUTED_BAR,    points: [] },  // low reading,  low visual
    Browser:  { color: 'rgba(201,168,76,0.4)', points: [] },  // low reading, high visual
  };

  pts.forEach(p => {
    const highVis  = p.x >= VIS_THRESHOLD;
    const highRead = p.y >= READ_THRESHOLD;
    if (!highVis && highRead)  archetypes.Analyst.points.push(p);
    else if (highVis && highRead) archetypes.Scholar.points.push(p);
    else if (!highVis && !highRead) archetypes.Reactor.points.push(p);
    else                          archetypes.Browser.points.push(p);
  });

  const datasets = Object.entries(archetypes).map(([name, a]) => ({
    label: name,
    data: a.points.map(p => ({ x: p.x, y: p.y, label: p.label })),
    backgroundColor: a.color,
    pointRadius: 6,
    pointHoverRadius: 8,
  }));

  // Draw quadrant shading via beforeDraw plugin
  const quadrantPlugin = {
    id: 'quadrant',
    beforeDraw(chart) {
      const { ctx, chartArea: ca, scales } = chart;
      if (!ca) return;
      const vx = scales.x.getPixelForValue(VIS_THRESHOLD);
      const vy = scales.y.getPixelForValue(READ_THRESHOLD);
      ctx.save();
      const shade = 'rgba(201,168,76,0.04)';
      // top-left (Analyst): high reading, low visual
      ctx.fillStyle = shade;
      ctx.fillRect(ca.left, ca.top, vx - ca.left, vy - ca.top);
      ctx.restore();
    },
  };

  new Chart(document.getElementById('chartArchetype'), {
    type: 'scatter',
    plugins: [quadrantPlugin],
    data: { datasets },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: {
        legend: legend('bottom'),
        tooltip: {
          callbacks: {
            label: c => ` ${c.raw.label} — Visual: ${c.raw.x}%, Grade: ${c.raw.y}`,
          },
        },
      },
      scales: {
        x: {
          title: { display: true, text: 'Visual Content Rate (%)', color: '#666', font: { size: 11 } },
          min: 0, max: 60,
          grid: xGrid, ticks: xTick, border: noBorder,
        },
        y: {
          title: { display: true, text: 'Flesch-Kincaid Grade Level', color: '#666', font: { size: 11 } },
          min: 4, max: 12,
          grid: { color: 'rgba(255,255,255,0.04)' }, ticks: { color: '#666', font: { size: 11 } }, border: noBorder,
        },
      },
    },
  });
}());

// ── 6. Counter-Intuitive Visual Effect — 20 brands, horizontal grouped ────
(function () {
  // Sorted by text-only RT descending for clear storytelling
  const labels = [
    'Blue Square', 'Amazon Ring', 'Salesforce', 'State Farm', 'NFL',
    'DraftKings', 'SVEDKA Vodka', 'Instacart', 'Michelob ULTRA',
    'Budweiser', 'Dove', 'Liquid Death', "Levi's", "Lay's",
    "Dunkin'", 'Google', 'Wix.com', 'OpenAI', 'Ro', 'Pepsi Zero Sugar',
  ];
  const textRT   = [14492.53, 13111.35, 4743.75, 5583.19, 4167.58, 4560.41, 4365.21, 2827.45, 2463.20, 7912.93, 2091.48, 2804.36, 1985.19, 2090.54, 1257.41, 1286.06, 1606.91, 1531.79, 898.93, 359.45];
  const visualRT = [ 2388.77,   488.90, 2005.39, 1262.32, 1520.37, 16253.93, 3939.08, 571.68, 339.78, 22170.25, 524.38, 1409.76, 2111.01, 1590.84, 700.88, 522.81, 746.03, 735.80, 2776.88, 1118.41];

  new Chart(document.getElementById('chartVisualEffect'), {
    type: 'bar',
    data: {
      labels,
      datasets: [
        { label: 'Text-Only Avg Retweets', data: textRT,   backgroundColor: GOLD,     borderRadius: 2, borderSkipped: false },
        { label: 'Visual Avg Retweets',    data: visualRT, backgroundColor: GOLD_DIM, borderRadius: 2, borderSkipped: false },
      ],
    },
    options: {
      indexAxis: 'y', responsive: true, maintainAspectRatio: false,
      plugins: {
        legend: legend(),
        tooltip: { callbacks: { label: c => ` ${c.dataset.label}: ${c.parsed.x.toLocaleString()} avg RT` } },
      },
      scales: {
        x: { grid: xGrid, ticks: { ...xTick, callback: v => v >= 1000 ? `${(v/1000).toFixed(0)}k` : v }, border: noBorder },
        y: { grid: yGrid, ticks: { color: '#aaa', font: { size: 10 } }, border: noBorder },
      },
    },
  });
}());

// ── Funnel bar animation on scroll ───────────────────────────────────────
(function () {
  const bar = document.querySelector('.funnel__bar--clean');
  if (!bar) return;
  const obs = new IntersectionObserver(entries => {
    if (entries[0].isIntersecting) {
      bar.style.width = '70.97%';
      obs.disconnect();
    }
  }, { threshold: 0.3 });
  obs.observe(bar.closest('.funnel__row') || bar);
}());
