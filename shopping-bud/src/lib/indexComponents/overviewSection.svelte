<script>
	export let data = [
		{
			title: 'Yoghurt',
			image: 'yoghurt.png',
			brand: 'Milram'
		}
	];
    export let title;
    import yogurtImage from "../../images/yoghurt.png";

    const handleClick = () => {
        console.log("clicked");
    };
</script>

<div>
	<div class="text-xl  m-4" on:click={handleClick}>{title}</div>
	<div class="flex overflow-x-scroll">
		{#each data as { ...item }, i}
			<div class="flex items-center mx-4 flex-none">
				<img src={yogurtImage} alt={item.title} class="w-24 h-24" />
				<div>
					<h3>{item.title}</h3>
					<p>{item.brand}</p>
				</div>
			</div>
		{/each}
        </div>
</div>
