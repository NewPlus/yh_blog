<script lang="ts">
  export let categories: string[] = [];
</script>

<ul class="category-tree">
  {#each categories as category}
    <li>
      <a href={`/blog/${category}`}>{category}</a>
    </li>
  {/each}
</ul>

<style>
  .category-tree {
    list-style: none;
    padding: 0;
  }
  .category-tree li {
    margin: 5px 0;
  }
  .category-tree a {
    text-decoration: none;
    color: inherit;
  }
</style> 