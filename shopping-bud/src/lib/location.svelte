<script>

    import { location } from "../stores/location.js";

    let clicked = false;
    const confirmLocation = (newLocation) => {
		$location = newLocation;
        clicked = true;

	}
</script>
<div>
    <div class="flex items-center justify-center bg-dark rounded-full text-white font-medium text-center h-10 my-1 hover:bg-blue" on:click={() => confirmLocation("Kaufland Heidelberg-Weststadt")}>
        Kaufland Heidelberg-Weststadt
    </div>
    <div class="flex items-center justify-center bg-dark rounded-full text-white font-medium text-center h-10 my-1 hover:bg-blue" on:click={() => confirmLocation("Kaufland Heidelberg-Pfaffengrund")}>
        Kaufland Heidelberg-Pfaffengrund
    </div>
    <div class="flex items-center justify-center bg-dark rounded-full text-white font-medium text-center h-10 my-1 hover:bg-blue" on:click={() => confirmLocation("Kaufland Heidelberg-Rohrbach")}>
        Kaufland Heidelberg-Rohrbach
    </div>
</div>
