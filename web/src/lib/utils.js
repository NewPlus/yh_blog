// yh_blog/web/src/lib/utils.js
export async function fetchMarkdownPosts() {
  // Svelte 파일로 변환된 파일을 가져옵니다.
  const allPostFiles = import.meta.glob('/src/routes/blog/*.svelte');
  const iterablePostFiles = Object.entries(allPostFiles);

  const allPosts = await Promise.all(
    iterablePostFiles.map(async ([path, resolver]) => {
      const { metadata } = await resolver();
      const slug = path.split('/').pop().replace('.svelte', '');
      return { ...metadata, slug };
    })
  );

  return allPosts;
}