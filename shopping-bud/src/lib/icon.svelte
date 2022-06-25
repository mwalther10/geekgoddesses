<script>
// @ts-nocheck

    export let data = ''
    export let viewBox = '0 0 256 256' // default value
    
    export let size; // h-10 h-12 h-32 h-64 h-96 h-120 h-6 h-4 h-8|w-10 w-12 w-32 w-64 w-96 w-120 w-6 w-4 w-8
    export let color;
    export let padding; // p-1 p-2 p-3 p-4 p-5 p-6 p-7 p-8
    export let additionalStyle = ""; 
    $: classdata = "stroke-" + color + " fill-" + color + " w-" + size + " h-" + size + " p-" + padding + " " + additionalStyle
    $: elements = data
      .replace(/<svg ([^>]*)>/, '')
      .replace('</svg>', '')
/* fill-red stroke-red fill-blue stroke-blue fill-pink fill-light-blue  fill-dark stroke-dark fill-yellow stroke-yellow fill-white stroke-white fill-dark-grey fill-light-grey* */
</script>
  
<button class="btn btn-secondary  btn-circle "><svg
  xmlns="http://www.w3.org/2000/svg"
  {viewBox}
  class={classdata}
  {...$$restProps}
  >
  {@html elements}
  </svg></button>
