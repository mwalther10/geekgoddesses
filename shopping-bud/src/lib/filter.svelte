<script>
	import Icon from './icon.svelte';
	export let icon;
	export let title;
	export let options;
	// options = [{}]
</script>

<div class="flex flex-col items-center justify-center w-full">
	<div class="flex flex-row">
		<Icon data={icon} color={'dark'} size="8" padding="1" />
		<div class="text-l m-4">{title}</div>
	</div>
	<div class="grid grid-cols-3 ">
		{#each options as option, i}
		<div class="form-control flex justify-center items-center  p-4 mx-4 my-2 flex-none">
			<label class="label cursor-pointer">
			  <span class="label-text p-2">{option.label}</span>
			  <input type="checkbox" class="toggle toggle-primary " />
			</label>
		  </div>
		
			<!-- <div class="flex justify-center items-center p-4 mx-4 my-2 flex-none bg-light-grey rounded-lg text-blue font-bold"> -->
				<!-- {option.label}
			</div> -->
		{/each}
	</div>
</div>
