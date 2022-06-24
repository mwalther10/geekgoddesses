<script>
	export let color;
	export let size;

	function computeStyle() {
		return 'w-full border-' + color + ' border-' + size + ' rounded-lg';
	}
	/** border-dark border-red border-yellow border-blue border-light-grey border-dark-grey border-1 border-2 border-4 border-8*/
</script>

<hr class={computeStyle()} />
