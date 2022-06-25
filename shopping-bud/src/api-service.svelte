<script context="module">
	const API_URL = 'http://localhost:8000/';

	export async function getShoppingList(type, filters) {
		return await fetch((API_URL + 'sample?type=' + type + "&filters=" + filters), {
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json'
			},
			method: 'GET'
		})
			.then((response) => response.json())
			.then((data) => {
				if (data) {
					return data;
				}
			});
	}

    export async function getSearchResults(query, category, allergens, labels, packaging, store, brand, nutriscore, nutriments, nutriments_op, nutriments_val) {
        return await fetch((API_URL + 'sample?query=' + query + "&category=" + category
            + "&allergens=" + allergens + "&labels=" + labels + "&packaging=" + packaging
            + "&store=" + store + "&brand=" + brand + "&nutriscore=" + nutriscore
            + "&nutriments=" + nutriments + "&nutriments_op=" + nutriments_op + "&nutriments_val=" + nutriments_val), {
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json'
            },
            method: 'GET'
        })
            .then((response) => response.json())
            .then((data) => {
                if (data) {
                    return data;
                }
            });
    }


</script>
