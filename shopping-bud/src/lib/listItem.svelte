<script>
	import Icon from './icon.svelte';
	import eurIcon from './phosphoricons/currency-eur-fill.svg?raw';
	import packageIcone from './phosphoricons/trash.svg?raw';

	export let item = {
		EF_single_score: 0.03504003687783169,
		_id: '3478822005249',
		allergens_tags: [],
		brands_tags: ['jardin-bio'],
		carbohydrates_100g: 22,
		categories_tags: [
			'en:plant-based-foods-and-beverages',
			'en:plant-based-foods',
			'en:canned-foods',
			'en:fruits-and-vegetables-based-foods',
			'en:canned-plant-based-foods',
			'en:vegetables-based-foods',
			'en:canned-vegetables',
			'en:tomatoes-and-their-products',
			'en:sauces',
			'en:tomatoes',
			'en:canned-tomatoes',
			'en:tomato-sauces',
			'en:ketchup',
			'fr:epicerie'
		],
		'energy-kcal_100g': 102,
		fat_100g: 0.5,
		fibre_100g: 8.445312367504634,
		image_url:
			'https://images.openfoodfacts.org/images/products/347/882/200/5249/front_fr.49.400.jpg',
		labels_tags: [
			'en:organic',
			'en:eu-organic',
			'en:non-eu-agriculture',
			'en:1-for-the-planet',
			'en:eu-agriculture',
			'en:eu-non-eu-agriculture',
			'en:fr-bio-01',
			'en:no-additives',
			'en:no-flavors',
			'en:nutriscore',
			'en:pt-bio-02',
			'fr:ab-agriculture-biologique'
		],
		nutriscore_grade: 'd',
		packaging_tags: ['en:plastic', 'en:vial', 'fr:conteneur', 'fr:opercule-en-plastique'],
		price: 2,
		product_name: 'Ketchup',
		protein_100g: 16.55158983141465,
		stores_tags: ['magasins-u', 'carrefour-fr']
	};
	console.log(item)

	import PieChart from './pieChart.svelte';
</script>

<div>
	<div class="flex ml-1 my-1 justify-between">
		<div class="flex flex-col justify-center items-center w-36 border-r-2">
			<div class="stat-figure text-secondary">
				<div class="avatar">
					<div class="w-16 rounded-full ring ring-primary">
						<img src={item.image_url} alt={item.product_name} class="w-16 h-16" />
					</div>
				</div>
			</div>
			<div class="stat-title text-dark text-sm">{item.product_name}</div>
			<div class="stat-desc color-dark badge badge-accent badge-outline text-sm">
				{item.brands_tags}
			</div>
		</div>
		<div class="flex flex-col text-dark  justify-around  ">
			<div class="flex  items-center">
				<div class="pr-1 text-sm">Nutriscore</div>
				<div class="font-bold">{item.nutriscore_grade.toUpperCase()}</div>
			</div>
			<div class="flex  items-center">
				<div class="flex items-center">
					<div class="flex items-center">
						<Icon data={packageIcone} size="6" color="dark" padding="1" />
					</div><div class= "badge badge-secondary"> {item.packaging_tags[0].replace("en:","").replace("-packaging","")}</div>
				</div>
			</div>
			<div class="flex  items-center">
				<div class="flex items-center">
					<Icon data={eurIcon} size="6" color="dark" padding="1" />
				</div>
				<div class="font-bold text-sm">
					{item.price}
				</div>
			</div>
			<div class="flex items-center">
				<div class="flex items-center">
				{#if item.categories_tags.includes("en:plant-based-foods") && item.categories_tags.includes("en:vegetables-based-foods")}
				<div class="badge badge-primary">vegan</div>
				{:else if item.categories_tags.includes("en:vegetables-based-foods")}
				<div class="badge badge-primary">vegeterian</div>
				{/if}
				</div>
			</div>
			
		</div>
		<div class="flex justify-center items-center">
			<PieChart macros={[item.carbohydrates_100g, item.fat_100g, item.protein_100g]} />
		</div>
	</div>
	<div class="divider" />
</div>

<style>
	.color-dark {
		/* border:none;
        border-radius: 0;
        border-right: 1px solid #2C3763; */
		color: #2c3763;
		opacity: 1;
	}
</style>
