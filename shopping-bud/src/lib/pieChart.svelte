<script>
	import { onMount } from 'svelte';
	import Chart from 'chart.js';
	export let macros;

	let portfolio;
	const data_chart = {
		labels: ['Carbohydrates', 'Fat', 'Protein'],
		datasets: [
			{
				label: 'Macros',
				data: macros,
				backgroundColor: ['#7000e1', '#fc8800', '#00b0e8'],
				borderWidth: 0
			}
		]
	};
	const config = {
		type: 'pie',
		data: data_chart,
		options: {
			legend: {
				position: 'bottom',
				display: false
			}
		}
	};
	onMount(() => {
		const ctx = portfolio.getContext('2d');
		// Initialize chart using default config set
		var myChart = new Chart(ctx, config);
	});
</script>

<div>
	<canvas bind:this={portfolio} width={60} height={60} />
</div>
