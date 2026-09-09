/**
 * TimeVault Scoring Preview Engine
 * Dynamically computes weighted criteria analysis in the client wizard
 * without requiring full-page roundtrips.
 */

document.addEventListener('DOMContentLoaded', () => {
  const scoreInputs = document.querySelectorAll('.matrix-score-input');
  const weightBadges = document.querySelectorAll('.factor-weight-val');

  function recalculateLiveScores() {
    // Gather all factors and their weights
    const factorWeights = {};
    document.querySelectorAll('[data-factor-id]').forEach(el => {
      const fid = el.getAttribute('data-factor-id');
      const wt = parseInt(el.getAttribute('data-factor-weight') || '5', 10);
      factorWeights[fid] = wt;
    });

    let totalWeight = 0;
    Object.values(factorWeights).forEach(w => totalWeight += w);
    const maxScore = totalWeight * 10;

    // Gather option sums
    const optionSums = {};
    const optionCounts = {};

    scoreInputs.forEach(input => {
      const fid = input.getAttribute('data-factor-id');
      const optId = input.getAttribute('data-option-id');
      const score = parseInt(input.value || '5', 10);
      const wt = factorWeights[fid] || 5;

      if (!optionSums[optId]) {
        optionSums[optId] = 0;
        optionCounts[optId] = 0;
      }
      optionSums[optId] += (score * wt);
      optionCounts[optId]++;
    });

    // Update displayed previews
    Object.keys(optionSums).forEach(optId => {
      const sum = optionSums[optId];
      const pct = maxScore > 0 ? ((sum / maxScore) * 100).toFixed(1) : 0;

      const previewVal = document.querySelector(`.live-score-val-${optId}`);
      if (previewVal) {
        previewVal.textContent = `${pct}%`;
      }
      const previewBar = document.querySelector(`.live-score-bar-${optId}`);
      if (previewBar) {
        previewBar.style.width = `${pct}%`;
      }
    });
  }

  scoreInputs.forEach(input => {
    input.addEventListener('input', recalculateLiveScores);
  });
});
