<script lang="ts">
  import { onMount } from 'svelte';

  type Post = {
    title: string;
    content: string;
  };

  let posts: Post[] = [];
  let category = 'dev';

  async function fetchAllPosts() {
    const categoryPosts: Post[] = [];
    try {
      // Assuming there are post1.json, post2.json, etc.
      for (let i = 1; i <= 10; i++) { // Adjust the range as needed
        const response = await fetch(`/blog/${category}/post${i}.json`);
        if (response.ok) {
          const post = await response.json();
          categoryPosts.push(post);
        } else {
          break; // Stop if no more posts are found
        }
      }
    } catch (error) {
      console.error('Error fetching posts:', error);
    }
    return categoryPosts;
  }

  onMount(async () => {
    posts = await fetchAllPosts();
  });
</script>

<a href="/" class="blog-title">Yonghwan's Blog</a>

<h1>{category.toUpperCase()} 카테고리</h1>
<ul>
  {#each posts as { title, content }}
    <li>
      <h2>{title}</h2>
      <p>{content.substring(0, 100)}...</p>
    </li>
  {/each}
</ul>

<style>
  .blog-title {
    display: block;
    text-align: center;
    font-size: 2em;
    margin: 20px 0;
    text-decoration: none;
    color: inherit;
  }
</style> 