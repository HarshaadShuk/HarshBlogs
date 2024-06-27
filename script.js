document.addEventListener('DOMContentLoaded', function() {
    const searchBar = document.getElementById('searchBar');
    const blogTiles = document.querySelectorAll('.blog-tile');
    const fullPost = document.getElementById('full-post');
    const postContent = document.getElementById('post-content');
    const closePostBtn = document.getElementById('close-post');

    // Function to handle showing full post content
    function showFullPost(content) {
        postContent.innerHTML = content;
        fullPost.style.display = 'block';
    }

    // Function to close full post
    function closeFullPost() {
        fullPost.style.display = 'none';
        postContent.innerHTML = '';
    }

    // Function to filter blog tiles based on search input
    function filterBlogTiles(searchText) {
        blogTiles.forEach(tile => {
            const title = tile.querySelector('h2').innerText.toLowerCase();
            const preview = tile.querySelector('.preview').innerText.toLowerCase();
            if (title.includes(searchText) || preview.includes(searchText)) {
                tile.style.display = 'block';
            } else {
                tile.style.display = 'none';
            }
        });
    }

    // Event listener for search bar input
    searchBar.addEventListener('input', function(event) {
        const searchText = event.target.value.toLowerCase();
        filterBlogTiles(searchText);
    });

    // Event listeners for read more buttons
    blogTiles.forEach(tile => {
        const readMoreBtn = tile.querySelector('.read-more');
        readMoreBtn.addEventListener('click', function(event) {
            event.preventDefault();
            const blogUrl = readMoreBtn.getAttribute('href');
            fetch(blogUrl)
                .then(response => response.text())
                .then(data => showFullPost(data))
                .catch(error => console.error('Error fetching blog content:', error));
        });
    });

    // Event listener for closing full post
    closePostBtn.addEventListener('click', closeFullPost);

    // Function to handle responsive adjustments (optional)
    function handleResponsive() {
        // Add any responsive adjustments here if needed
        // Example: Adjust grid layout for smaller screens
        if (window.innerWidth <= 768) {
            blogTiles.forEach(tile => {
                tile.style.width = '100%'; // Adjust tile width for smaller screens
            });
        } else {
            blogTiles.forEach(tile => {
                tile.style.width = 'auto'; // Reset tile width for larger screens
            });
        }
    }

    // Call handleResponsive initially and on window resize
    handleResponsive();
    window.addEventListener('resize', handleResponsive);
});
