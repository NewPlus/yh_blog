<!-- yh_blog/web/src/routes/blog/+page.svelte -->
<script lang="ts">
  import { onMount } from 'svelte';
  import CategoryTree from './CategoryTree.svelte';

  type Post = {
    title: string;
    content: string;
    category: string;
  };

  let posts: Post[] = [];
  let paginatedPosts: Post[] = [];
  const postsPerPage = 10;
  let currentPage = 1;
  let totalPages = 1;
  const categories = ['dev', 'cs']; // 하위 폴더 이름

  async function fetchPosts(category: string) {
    const categoryPosts: Post[] = [];
    try {
      for (let i = 1; i <= 10; i++) {
        const response = await fetch(`/blog/${category}/post${i}.json`);
        if (response.ok) {
          const post = await response.json();
          categoryPosts.push({ ...post, category });
        } else {
          break;
        }
      }
    } catch (error) {
      console.error(`Error fetching posts from ${category}:`, error);
    }
    return categoryPosts;
  }

  function updatePaginatedPosts() {
    const start = (currentPage - 1) * postsPerPage;
    const end = start + postsPerPage;
    paginatedPosts = posts.slice(start, end);
  }

  function nextPage() {
    if (currentPage < totalPages) {
      currentPage += 1;
      updatePaginatedPosts();
    }
  }

  function prevPage() {
    if (currentPage > 1) {
      currentPage -= 1;
      updatePaginatedPosts();
    }
  }

  onMount(async () => {
    const allPosts = await Promise.all(categories.map(fetchPosts));
    posts = allPosts.flat();
    totalPages = Math.ceil(posts.length / postsPerPage);
    updatePaginatedPosts();
  });
</script>

<a href="/" class="blog-title">Yonghwan's Blog</a>

<!-- 카테고리 트리 컴포넌트 추가 -->
<CategoryTree {categories} />

<h1>모든 카테고리</h1>
<ul>
  {#each paginatedPosts as { title, content, category }}
    <li>
      <h2>{title}</h2>
      <p>{content.substring(0, 100)}...</p>
      <p><strong>카테고리:</strong> {category}</p>
    </li>
  {/each}
</ul>

<div class="pagination">
  <button on:click={prevPage} disabled={currentPage === 1}>이전</button>
  <span>페이지 {currentPage} / {totalPages}</span>
  <button on:click={nextPage} disabled={currentPage === totalPages}>다음</button>
</div>

<style>
  .blog-title {
    display: block;
    text-align: center;
    font-size: 2em;
    margin: 20px 0;
    text-decoration: none;
    color: inherit;
  }
  .pagination {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
  }
  button {
    margin: 0 10px;
  }
</style>