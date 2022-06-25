<script>
	import Icon from './icon.svelte';
	import downIcon from './phosphoricons/caret-down-fill.svg?raw';
    import {displayFullData, fullData, shoppingList} from "../stores/shopping-list-store.js";
	let bullets = [];
	let toBeAdded;

	const addItemToList = (item) => {
		bullets = [...bullets, item];
		toBeAdded = null;
	};
	const transformBulletList = (list) => {
		$shoppingList = $fullData;
        bullets = [];
	};
</script>

<div class="collapse">
	<input type="checkbox" class="peer" />
	<div
		class="collapse-title bg-white text-dark peer-checked:bg-white peer-checked:text-secondary-content flex items-center justify-between px-7"
	>
		Add items to your shopping list.
			<Icon data={downIcon} size="10" color="blue" padding="1" />
	</div>
	<div
		class="collapse-content bg-white text-dark peer-checked:bg-white peer-checked:text-secondary-content"
	>
		<div class="flex flex-col border-y-4 py-4 ">
			{#each bullets as bullet, i}
				<div class="text-dark text-xl ml-6">{bullet}</div>
			{/each}
			<div class="flex flex-row w-full justify-between focus:outline-blue  ">
				<input
					bind:value={toBeAdded}
					type="text"
					placeholder="type to add item"
					class="w-2/3 p-2 mx-4 h-auto rounded-full"
				/>
				<button
					class="rounded-full w-fit px-2 mx-2 bg-blue text-white disabled:bg-dark-grey cursor-pointer"
					on:click={() => addItemToList(toBeAdded)} disabled={!toBeAdded}>Add</button
				>
			</div>
			{#if bullets.length > 0}
				<button
					class="self-center rounded-full w-11/12 py-2  mt-4 bg-yellow text-white cursor-pointer"
					on:click={() => transformBulletList(bullets)}>Transform Bullet List</button
				>
			{/if}
		</div>
	</div>
</div>
