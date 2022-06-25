<script context="module">
	const API_URL = '';



	export async function getShoppingList(snapshot_id) {
		return await fetch((API_URL + 'snapshots/?snapshot_id=' + snapshot_id) as string, {
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
