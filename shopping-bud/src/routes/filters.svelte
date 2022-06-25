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
import Preference from '$lib/preference.svelte';
import Prefrence from "$lib/preference.svelte";

import eatingHabitsIcon from "../lib/phosphoricons/fork-knife.svg?raw";
import warningIcon from "../lib/phosphoricons/warning-circle.svg?raw";
import globIcon from "../lib/phosphoricons/globe-hemisphere-east-light.svg?raw";
import moneyIcon from "../lib/phosphoricons/money.svg?raw";
import chartIcon from "../lib/phosphoricons/chart-pie-slice.svg?raw";
import filters from "../stores/filters";

// const eatingHabitOptions = [{label: "Vegetarian",checked:false}, {label: "Vegan",checked:false}, {label: "Halal",checked:false}];
// const allergyOptions= [{label: "Nuts",checked:false}, {label: "Gluten",checked:false}, {label: "Lactose",checked:false}];
// const neutOptions= [{label: "Fat",value:-1, color:"primary", min:0,max:100,steps:1, unit:"%"}, {label: "Protein",value:-1,color:
// "secondary",min:0,max:100,steps:1, unit:"%"}, {label: "Carbs",value:-1, color:"accent",min:0,max:100,steps:1, unit:"%"}];
// const moneyOptions= [{label: "Total Budget",value:-1, color:"accent",min:0,max:500,steps:0.5, unit:"€"}];
// const envOptions= [{label: "Total EF Score",value:-1, color:"primary",min:0,max:1,steps:0.1, unit:""}];


</script>

<svelte:head>
	<title>Filters</title>
	<meta name="description" content="Fixed filters" />
</svelte:head>

<div data-theme="cupcake" class="flex flex-col text-dark w-full font-nunito">
	<div class="text-xl m-3 text-center font-medium  badge-secondary gap-2" style="border-radius: 5px;"> Prefrences</div>
	<Preference title="Micro-nutrients" icon={chartIcon} options={$filters.neutriation} />
	<Preference title="Budget" icon={moneyIcon} options={$filters.budget} />
	<Preference title="Enviromental Footprint (EF)" icon={globIcon} options={$filters.enviroment} />
	<div class="divider"></div> 

	<div class="text-xl m-3 text-center font-medium  badge-secondary gap-2" style="border-radius: 5px;"> Filters</div>
	<Filter title="Eating Habits" icon={eatingHabitsIcon} options={$filters.eatingHabbit} />
	<Filter title="Allergies" icon={warningIcon} options={$filters.allergy} />
</div>



