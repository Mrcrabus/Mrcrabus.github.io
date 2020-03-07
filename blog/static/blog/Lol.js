const pop = document.querySelectorAll('.pop');
pop.forEach(function (post) {
    post.addEventListener('click', function () {
            location.href = `news/${post.id}`
        }
    );
});
