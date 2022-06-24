<script context="module">
	import { browser, dev } from '$app/env';

	// we don't need any JS on this page, though we'll load
	// it in dev so that we get hot module replacement...
	export const hydrate = dev;

	// ...but if the client-side router is already loaded
	// (i.e. we came here from elsewhere in the app), use it
	export const router = browser;

	// since there's no dynamic data here, we can prerender
	// it so that it gets served as a static asset in prod
	export const prerender = true;
</script>

<script>
import Filter from "$lib/filter.svelte";
import eatingHabitsIcon from "../lib/phosphoricons/fork-knife-fill.svg?raw";
import warningIcon from "../lib/phosphoricons/warning-circle-fill.svg?raw";

const eatingHabitOptions = [{label: "Vegetarian"}, {label: "Vegan"}, {label: "Halal"}];
const allergyOptions= [{label: "Nuts"}, {label: "Gluten"}, {label: "Lactose"}];
</script>

<svelte:head>
	<title>Filters</title>
	<meta name="description" content="Fixed filters" />
</svelte:head>

<div class="flex flex-col text-dark w-full">
	<div class="text-xl m-4 font-medium text-dark-grey"> Select filters</div>
	<Filter title="Eating Habits" icon={eatingHabitsIcon} options={eatingHabitOptions} />
	<Filter title="Allergies" icon={warningIcon} options={allergyOptions} />
</div>
