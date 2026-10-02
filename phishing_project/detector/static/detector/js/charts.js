// detector/static/detector/js/charts.js

document.addEventListener('DOMContentLoaded', function () {
    const canvas = document.getElementById('performanceChart');
    if (!canvas) return; // Exit gracefully if not on the dashboard page

    const ctx = canvas.getContext('2d');
    
    // Setup Chart Layout Dimensions dynamically matching parent containers
    const dpr = window.devicePixelRatio || 1;
    canvas.width = canvas.parentElement.clientWidth * dpr;
    canvas.height = 240 * dpr;
    ctx.scale(dpr, dpr);

    // Performance Metrics Data Set Matrix Points
    const metrics = [
        { label: 'Accuracy', value: 96.2, color: '#3b82f6' },
        { label: 'Precision', value: 95.1, color: '#10b981' },
        { label: 'Recall', value: 93.7, color: '#f59e0b' },
        { label: 'F1-Score', value: 94.4, color: '#8b5cf6' }
    ];

    const chartWidth = canvas.width / dpr;
    const chartHeight = 200;
    const barWidth = 50;
    const spacing = (chartWidth - (barWidth * metrics.length)) / (metrics.length + 1);

    // Render Metric Bar Elements
    metrics.forEach((metric, index) => {
        const x = spacing + index * (barWidth + spacing);
        const barHeight = (metric.value / 100) * (chartHeight - 40);
        const y = chartHeight - barHeight - 20;

        // Draw Shadows/Glow Effect
        ctx.shadowBlur = 10;
        ctx.shadowColor = metric.color + '40';

        // Draw Metric Bar Column
        ctx.fillStyle = metric.color;
        ctx.beginPath();
        ctx.roundRect(x, y, barWidth, barHeight, [4, 4, 0, 0]);
        ctx.fill();

        // Reset shadow counters
        ctx.shadowBlur = 0;

        // Draw Value Percentage Labels Above Bars
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 12px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(`${metric.value}%`, x + (barWidth / 2), y - 8);

        // Draw Metrics Subtitle Labels Underneath Bars
        ctx.fillStyle = '#94a3b8';
        ctx.font = '11px sans-serif';
        ctx.fillText(metric.label, x + (barWidth / 2), chartHeight + 2);
    });
});
