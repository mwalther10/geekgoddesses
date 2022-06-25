<script>
	import Icon from './icon.svelte';
	import eurIcon from './phosphoricons/currency-eur-fill.svg?raw';

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

	import PieChart from './pieChart.svelte';
</script>

<div>
	<div class="flex ml-1 my-1 justify-between">
		<div class="flex flex-col justify-center items-center w-36">
			<div class="stat-figure text-secondary">
				<div class="avatar">
					<div class="w-16 rounded-full">
						<img src={item.image_url} alt={item.product_name} class="w-16 h-16" />
					</div>
				</div>
			</div>
			<div class="stat-title text-dark text-sm">{item.product_name}</div>
			<div class="stat-desc color-dark badge badge-accent badge-outline text-sm">
				{item.brands_tags}
			</div>
		</div>
		<div class="grid grid-cols-2 gap-y-0 gap-x-4 text-dark items-center justify-center  text-sm ">
			<div class="">Nutriscore</div>
			<div class="font-bold">{item.nutriscore_grade}</div>
			<div class="flex items-center"><Icon data={eurIcon} size="8" color="dark" padding="1" /></div>
			<div class="font-bold">
				{item.price}
			</div>
		</div>

		<PieChart macros={[item.carbohydrates_100g, item.fat_100g, item.protein_100g]} />
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
