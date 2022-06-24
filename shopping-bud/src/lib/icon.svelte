<script>
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
/* stroke-dark-500 fill-dark-500 stroke-blue-500 fill-blue-500 fill-white stroke-white fill-main stroke-main fill-dark stroke-dark fill-warning stroke-warning fill-secondary stroke-secondary* */
</script>
  
<svg
xmlns="http://www.w3.org/2000/svg"
{viewBox}
class={classdata}
{...$$restProps}
>
{@html elements}
</svg>