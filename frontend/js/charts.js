// ── Global Chart.js defaults — dark theme ────────────────────────────────
Chart.defaults.color = '#888888';
Chart.defaults.borderColor = 'rgba(255,255,255,0.05)';
Chart.defaults.font.family = "'Inter', system-ui, sans-serif";
Chart.defaults.font.weight = '300';

const GOLD = '#c9a84c';
const GOLD_MID = 'rgba(201,168,76,0.5)';
const GOLD_DIM = 'rgba(201,168,76,0.28)';
const MUTED_BAR = 'rgba(240,240,240,0.18)';

// ── 1. Brand Efficiency — horizontal bar (all 20 brands) ─────────────────
(function () {
  const labels = [
    'Blue Square Alliance', 'Amazon Ring', 'DraftKings', 'Budweiser',
    'State Farm', 'Salesforce', 'SVEDKA Vodka', 'NFL', 'Liquid Death',
    'Instacart', 'Michelob ULTRA', "Levi's", "Lay's", 'Dove', 'OpenAI',
    'Ro', 'Google', 'Wix.com', "Dunkin'", 'Pepsi Zero Sugar',
  ];
  const values = [
    2505.5, 2166.2, 2097.3, 2039.2, 1011.3, 874.7, 854.1, 716.2,
    518.5, 492.8, 464.0, 404.2, 402.9, 375.8, 286.1, 279.8,
    238.1, 237.3, 225.9, 88.1,
  ];

  // Color bars by tier: top 4 = gold, next 4 = mid, rest = dim
  const colors = values.map((v) => {
    if (v >= 2000) return GOLD;
    if (v >= 700) return GOLD_MID;
    return GOLD_DIM;
  });

  new Chart(document.getElementById('chartBrandEfficiency'), {
    type: 'bar',
    data: {
      labels,
      datasets: [{
        label: 'Avg WES / Tweet',
        data: values,
        backgroundColor: colors,
        borderRadius: 3,
        borderSkipped: false,
      }],
    },
    options: {
      indexAxis: 'y',
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: (ctx) => ` ${ctx.parsed.x.toLocaleString()} avg WES`,
          },
        },
      },
      scales: {
        x: {
          grid: { color: 'rgba(255,255,255,0.04)' },
          ticks: { color: '#666', font: { size: 11 } },
          border: { color: 'transparent' },
        },
        y: {
          grid: { display: false },
          ticks: { color: '#aaa', font: { size: 11 } },
          border: { color: 'transparent' },
        },
      },
    },
  });
}());

// ── 2. Tweet Timing — donut ───────────────────────────────────────────────
(function () {
  new Chart(document.getElementById('chartTiming'), {
    type: 'doughnut',
    data: {
      labels: ['Hour 3 — Peak', 'Hour 2', 'Hour 1', 'Hour 0'],
      datasets: [{
        data: [40984, 4877, 321, 54],
        backgroundColor: [GOLD, GOLD_MID, GOLD_DIM, 'rgba(201,168,76,0.1)'],
        borderColor: '#111111',
        borderWidth: 2,
        hoverOffset: 8,
      }],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      cutout: '68%',
      plugins: {
        legend: {
          position: 'bottom',
          labels: {
            color: '#888',
            padding: 16,
            font: { size: 11 },
            boxWidth: 12,
            boxHeight: 12,
          },
        },
        tooltip: {
          callbacks: {
            label: (ctx) => {
              const pct = ((ctx.parsed / 46257) * 100).toFixed(1);
              return ` ${ctx.parsed.toLocaleString()} tweets (${pct}%)`;
            },
          },
        },
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
      datasets: [{
        label: 'Avg Weighted Engagement Score',
        data: [439.9, 1702.8],
        backgroundColor: [MUTED_BAR, GOLD],
        borderRadius: 4,
        borderSkipped: false,
        maxBarThickness: 100,
      }],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: (ctx) => ` Avg WES: ${ctx.parsed.y}`,
          },
        },
      },
      scales: {
        x: {
          grid: { display: false },
          ticks: { color: '#aaa', font: { size: 12 } },
          border: { color: 'transparent' },
        },
        y: {
          grid: { color: 'rgba(255,255,255,0.04)' },
          ticks: { color: '#666', font: { size: 11 } },
          border: { color: 'transparent' },
        },
      },
    },
  });
}());

// ── 4. Yell Index — grouped bars ─────────────────────────────────────────
// Shows ALL-CAPS vs normal-case avg likes; Amazon Ring is the sole outlier.
(function () {
  const brands = ['Amazon Ring', 'Dove', 'Pepsi Zero Sugar', 'NFL', 'Liquid Death', 'Salesforce'];
  const allCaps = [179.5, 0.4, 0.3, 0.2, 0.1, 0.3];
  const normal = [10.4, 9.4, 23.7, 3.0, 5.6, 0.8];

  new Chart(document.getElementById('chartYell'), {
    type: 'bar',
    data: {
      labels: brands,
      datasets: [
        {
          label: 'ALL-CAPS Avg Likes',
          data: allCaps,
          backgroundColor: GOLD,
          borderRadius: 3,
          borderSkipped: false,
        },
        {
          label: 'Normal-Case Avg Likes',
          data: normal,
          backgroundColor: GOLD_DIM,
          borderRadius: 3,
          borderSkipped: false,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'bottom',
          labels: {
            color: '#888',
            padding: 16,
            font: { size: 11 },
            boxWidth: 12,
            boxHeight: 12,
          },
        },
        tooltip: {
          callbacks: {
            label: (ctx) => ` ${ctx.dataset.label}: ${ctx.parsed.y} avg likes`,
          },
        },
      },
      scales: {
        x: {
          grid: { display: false },
          ticks: { color: '#aaa', font: { size: 11 } },
          border: { color: 'transparent' },
        },
        y: {
          grid: { color: 'rgba(255,255,255,0.04)' },
          ticks: { color: '#666', font: { size: 11 } },
          border: { color: 'transparent' },
        },
      },
    },
  });
}());
